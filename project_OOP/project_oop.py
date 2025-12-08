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
    
    def __init__(self, pathology_database, exercice_database):
        self.database = pathology_database  # On stocke la référence à PathologyDatabase
        self.exercice_database = exercice_database
        
        self.figlet = Figlet()
        self.figlet.setFont(font="big")

    def run(self):
            """Lance le menu principal (ancien main())"""
            print(self.figlet.renderText("Welcome"))
            print("1. All Pathologies.".title())
            print("2. Search by Name.".title())
            print("3. Sort by Body Part.".title())
            print("4. Show Exercice Programs.".title())
            
            while True:
                try:
                    choice = int(input("Choice: "))
                    if not (1 <= choice <= 4):
                        print("Please enter a number (1 to 4)!")
                        continue
                except ValueError:
                    print("Please enter a number (1 to 4)")
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
                elif choice == 4:
                    self.handle_show_exercise_programs()
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

    def handle_show_exercise_programs(self):
            """Option 4: Affiche les programmes d'exercices et permet d'en choisir un"""
            print()
            print("Available exercise programs:\n")

            # Liste tous les protocoles avec leur slug et leur nom
            protocols = self.exercice_database.get_all_protocols()
            if not protocols:
                print("No exercise programs found.")
                return
            
            for protocol in protocols:
                print(f" - {protocol['slug']}: {protocol['name']}")

            slug_choice = input("\nEnter the slug of the program you want to view: ").strip()
            print()

            protocol = self.exercice_database.get_protocol_by_slug(slug_choice)
            if not protocol:
                print("Exercise program not found.")
                return

            # Affichage des informations du protocole
            print(self.figlet.renderText(protocol["name"]))
            print(f"Body part: {protocol['body_part']}")
            print(f"Goal: {protocol['goal']}\n")
            print(f"Duration / Frequency: {protocol['duration_frequency']}\n")
            print("General tips:")
            print(f"  - {protocol['general_tips']}\n")

            print("Key points:")
            for kp in protocol["key_points"]:
                print(f"  - {kp}")
            print()

            print("Exercises:\n")
            for ex in protocol["exercises"]:
                # Chaque ex est un objet Exercise, on utilise son __str__()
                print(ex)
                print("-" * 40)
        

class Exercise:
    def __init__(self, slug, name, video_url, sets, repetitions, description, 
                 tips, progression, duration=None, rest=None, equipment=None):
        self.slug = slug
        self.name = name
        self.video_url = video_url
        self.sets = sets
        self.repetitions = repetitions
        self.duration = duration
        self.rest = rest
        self.equipment = equipment
        self.description = description
        self.tips = tips
        self.progression = progression
    
    def __str__(self):
        """Affichage formaté pour le terminal"""
        result = f"## {self.name}\n"
        result += f"Video: {self.video_url}\n\n"
        result += f"Sets: {self.sets}\n"
        result += f"Repetitions: {self.repetitions}\n"
        
        if self.duration:
            result += f"Duration: {self.duration}\n"
        if self.rest:
            result += f"Rest: {self.rest}\n"
        if self.equipment:
            result += f"Equipment: {self.equipment}\n"
        
        result += f"\nDescription: {self.description}\n"
        result += f"\nTips: {self.tips}\n"
        result += f"\nProgression: {self.progression}\n"
        
        return result
    
    def __repr__(self):
        return f"Exercise(name='{self.name}', slug='{self.slug}')"


class ExerciseDatabase:
    def __init__(self):
        self.protocols = []  # Liste de dictionnaires {protocol_info, exercises}
    
    def load_from_json(self, file_path):
        """Charge les protocoles d'exercices depuis le JSON"""
        with open(file_path) as f:
            data = json.load(f)
        
        for protocol_data in data:
            # Créer les objets Exercise pour ce protocole
            exercises = []
            for ex_item in protocol_data["exercises"]:
                exercise = Exercise(
                    slug=ex_item["slug"],
                    name=ex_item["name"],
                    video_url=ex_item["video_url"],
                    sets=ex_item["sets"],
                    repetitions=ex_item["repetitions"],
                    description=ex_item["description"],
                    tips=ex_item["tips"],
                    progression=ex_item["progression"],
                    duration=ex_item.get("duration"),
                    rest=ex_item.get("rest"),
                    equipment=ex_item.get("equipment")
                )
                exercises.append(exercise)
            
            # Stocker le protocole avec ses métadonnées
            protocol = {
                "slug": protocol_data["slug"],
                "pathology_slug": protocol_data["pathology_slug"],
                "name": protocol_data["name"],
                "body_part": protocol_data["body_part"],
                "goal": protocol_data["goal"],
                "duration_frequency": protocol_data["duration_frequency"],
                "general_tips": protocol_data["general_tips"],
                "key_points": protocol_data["key_points"],
                "exercises": exercises
            }
            self.protocols.append(protocol)
    
    def get_protocols_for_pathology(self, pathology_slug):
        """Retourne tous les protocoles liés à une pathologie"""
        slug_lower = pathology_slug.lower()
        return [
            p for p in self.protocols
            if p["pathology_slug"].lower() == slug_lower
        ]
    
    def get_protocol_by_slug(self, slug):
        """Retourne un protocole complet par son slug"""
        slug_lower = slug.lower()
        for protocol in self.protocols:
            if protocol["slug"].lower() == slug_lower:
                return protocol
        return None
    
    def get_protocol_by_body_part(self, body_part):
        """Retourne tous les protocoles pour une partie du corps"""
        body_part_lower = body_part.lower()
        return [p for p in self.protocols 
                if body_part_lower in p["body_part"].lower()]
    
    def get_all_protocols(self):
        """Retourne tous les protocoles"""
        return self.protocols
    
    def list_protocol_names(self):
        """Retourne la liste des noms de protocoles"""
        return [p["name"] for p in self.protocols]


def main():
    # 1. Créer la base de données
    pathology_db = PathologyDatabase()
    pathology_db.load_from_json("pathologies_data.json")
    
    # Charger les exercices
    exercice_db = ExerciseDatabase()
    exercice_db.load_from_json("exercises_data.json")

    # 2. Créer le menu EN LUI PASSANT les database
    menu = PathologyMenu(pathology_db, exercice_db)
    
    # 3. Lancer le menu
    menu.run()


if __name__ == "__main__":
    main()


