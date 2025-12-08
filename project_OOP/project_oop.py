import json
from pyfiglet import Figlet
from fpdf import FPDF


figlet = Figlet()
figlet.setFont(font="big")

class Pathology:
    def __init__(self, name, body_part, typical_duration_weeks, phases, prognosis, red_flags, key_points):
        self.name = name
        self.body_part = body_part
        self.typical_duration_weeks = typical_duration_weeks
        self.phases = phases
        self.prognosis = prognosis
        self.red_flags = red_flags
        self.key_points = key_points
    

    def __str__(self):
        
        result = f"{self.name}:\n\n"
        result += f"Typical duration (weeks): {self.typical_duration_weeks}\n\n"
        
        result += "Phases:\n"
        for phase in self.phases:
            result += f"  - {phase}\n"
        result += "\n"
        
        result += "Prognosis:\n"
        result += f"  - {self.prognosis}\n\n"
        
        result += "Red flags:\n"
        for flag in self.red_flags:
            result += f"  - {flag}\n"
        result += "\n"
        
        result += "Key Points:\n"
        for key in self.key_points:
            result += f"  - {key}\n"
        
        return result  # RETURN, pas print!


class PathologyDatabase:
    
    def __init__(self):
        self.pathologies = []

    def load_from_json(self, file_path): 
        with open (file_path) as data_file:
            parsed_json = json.load(data_file)

        for item in parsed_json:
            pathology = Pathology(
                name=item["name"],
                typical_duration_weeks=item["typical_duration_weeks"],
                phases=item["phases"],
                prognosis=item["prognosis"],
                red_flags=item["red_flags"],
                key_points=item["key_points"],
                body_part=item["body_part"]
            )
            self.pathologies.append(pathology)

    def get_all(self):
            """Retourne toutes les pathologies"""
            return self.pathologies
    
    def list_names(self):
        """Retourne la liste des noms de pathologies"""
        return [p.name for p in self.pathologies]
    
    def get_by_name(self, name):
        """Cherche une pathologie par nom (insensible à la casse)"""
        name_lower = name.lower()
        for pathology in self.pathologies:
            if pathology.name.lower() == name_lower:
                return pathology  # Retourne l'objet Pathology trouvé
        return None  

    def get_sorted_by_body_part(self):
        return sorted(self.pathologies, key=lambda p: p.body_part)
    
class PathologyMenu:
    
    def __init__(self, database):
        self.database = database  # On stocke la référence à PathologyDatabase
        self.figlet = Figlet()
        self.figlet.setFont(font="big")

    def run(self):
            """Lance le menu principal (ancien main())"""
            print(self.figlet.renderText("Welcome"))
            print("1. All Pathologies.".title())
            print("2. Search by Name.".title())
            print("3. Sort by Body Part.".title())
            
            while True:
                try:
                    choice = int(input("Choice: "))
                    if not (1 <= choice <= 3):
                        print("Please enter a number (1 to 3)!")
                        continue
                except ValueError:
                    print("Please enter a number (1 to 3)")
                    continue

                if choice == 1:
                    self.handle_list_all()
                    break
                elif choice == 2:
                    self.handle_search_by_name()
                    break
                elif choice == 3:
                    self.handle_sort_by_body_part()
                    break

    def handle_list_all(self):
        """Option 1: Liste toutes les pathologies puis permet d'en sélectionner une"""
        # Je vais devoir créer database.get_all() et database.list_names()
        names = self.database.list_names()
        
        print("\nList of pathologies:\n")
        for name in names:
            print(f" - {name}")
        
        name_choice = input("\nSelect a pathology: ")
        print()
        pathology = self.database.get_by_name(name_choice)
        
        if pathology:
            print(pathology)
        else:
            print("Pathology not found")
    
    def handle_search_by_name(self):
        name = input("Name: ")
        pathology = self.database.get_by_name(name)
        
        if pathology:
            print(pathology)  # Appelle automatiquement __str__()
        else:
            print("Pathology not found")

    def handle_sort_by_body_part(self):
        """Option 3: Affiche triées par partie du corps"""
        print()
        print("List sorted by body part:".title())
        # Tu vas devoir créer database.get_sorted_by_body_part()
        sorted_pathologies = self.database.get_sorted_by_body_part()
        
        for pathology in sorted_pathologies:
            print(f"{pathology.body_part}: {pathology.name}")

def main():
    # 1. Créer la base de données
    database = PathologyDatabase()
    database.load_from_json("pathologies_data.json")
    
    # 2. Créer le menu EN LUI PASSANT la database
    menu = PathologyMenu(database)
    
    # 3. Lancer le menu
    menu.run()


if __name__ == "__main__":
    main()


