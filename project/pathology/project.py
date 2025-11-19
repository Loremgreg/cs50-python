import json
from pyfiglet import Figlet

figlet = Figlet()
figlet.setFont(font="big")


def main():
# gère le menu, les input(), les print()
    print(figlet.renderText("1. Search by slug."))
    print("2. list_all_pathologies.")
    choice = input("Choice: ")
    
    # if choice < 1 and choice > 4:
        # afficher message d'erreur et reprompter 
    if choice == "1":
        slug_choice = input("Slug: ")
        print(get_pathology_by_slug(slug_choice))
    else:
        pass

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
 

# def list_all_pathologies():
        

# def get_pathology_by_query():
# Recherche simple par mot clé (ou partie du nom) 

def get_pathology_by_slug(slug_choice):
    with open("pathologies_data.json") as data_file:
        parsed_json = json.load(data_file)

        for slug in parsed_json:
            # parsed_json.values(slug)
            if slug == slug_choice:
                return slug["typical_duration_weeks"]

# def normalize_name():
# insensible aux majuscules/minuscules, espaces   

# def search_pathologies_by_body_part():
# 4. filtrer selon MS, MI, Dos, Traumatologie (fracture, elongation): search_pathologies_by_body_part: 

main()



