import json
from pyfiglet import Figlet

figlet = Figlet()
figlet.setFont(font="big")


def main():
# gère le menu, les input(), les print()
    print(figlet.renderText("Welcome"))
    print("1. All Pathologies.")
    print("2. Search by Name.")
    
    while True:
        try:
            choice = int(input("Choice: "))
            1 <= choice <= 3
        except ValueError:
            print("Please enter a number (1 to 3)")
            continue

        if choice == 1:
            list_all_pathologies()
            name_choice = input("Select a pathology: ")
            print()
            get_pathology_by_name(name_choice)
            break

        elif choice == 2:
            name_choice = input("Name: ")
            print()
            get_pathology_by_name(name_choice)
            break
        else:
            print("Please enter a number (1 to 3)!")
            continue


def list_all_pathologies():
        # ensuite selectionnée une patho et afficher result 
        with open("pathologies_data.json") as data_file:
            parsed_json = json.load(data_file)

        list_of_patho = []
        for pathology in parsed_json:
            if pathology["name"]:
                list_of_patho.append(pathology["name"])
        
        print("List of pathologies:\n")
        for patho in list_of_patho:
            print(f" - {patho}")

        return list_of_patho
    

# def get_pathology_by_query():
# Recherche simple par mot clé (ou partie du nom) 

def get_pathology_by_name(name_choice):
    name_choice = name_choice.lower()
    with open("pathologies_data.json") as data_file:
        parsed_json = json.load(data_file)
        
        for pathology in parsed_json:
            # parsed_json.values(slug)
            if pathology["name"].lower() == name_choice:
                print(f"{pathology['name']}: \n")
                print(f"Typical duration (weeks): {pathology['typical_duration_weeks']}\n")

                print("Phases:")
                for phase in pathology["phases"]:
                    print(f"  - {phase}")
                print()

                print("Prognosis:")
                print(f"  - {pathology["prognosis"]}")
                print()

                print("Red flags:")
                for flag in pathology["red_flags"]:
                    print(f"  - {flag}")
                print()

                print("Key Points:")
                for key in pathology["key_points"]:
                    print(f"  - {key}")
                print()
                return pathology


# def normalize_name():
# insensible aux majuscules/minuscules, espaces   

# def search_pathologies_by_body_part():
# 4. filtrer selon MS, MI, Dos, Traumatologie (fracture, elongation): search_pathologies_by_body_part: 

# def exercices():
#fonction qui genere des exercices en selectionnant des exos random dans une liste 


if __name__ == "__main__":
    main()


# Si tape :
# 1. liste toutes les patho
# 2. filtrer selon partie du corps: search_pathologies_by_body_part: 
# 3. Recherche par nom (par slug) : get_pathology_by_slug()
# 4. Recherche par mot clé:  search_pathologies_by_query()
# 5. quitter 

# print 
# le menu interractif 
# → plusieurs actions
# → saisie utilisateur
# → affichage formaté
# → moteur de recherche simple
 
