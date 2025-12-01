from datetime import date
import sys
import inflect


def main():
    # Demander la date de naissance
    date_user_input = input("Date of Birth: ")
    
    # Convertir la date
    birth_date = parse_date(date_user_input)
    
    # Calculer et afficher les minutes
    minutes = calculate_minutes(birth_date)
    print(convert_to_words(minutes))


def parse_date(date_string):
    """
    Parse une date au format YYYY-MM-DD et retourne un objet date.
    Sort du programme si le format est invalide.
    """
    try:
        # La méthode fromisoformat attend exactement le format YYYY-MM-DD
        birth_date = date.fromisoformat(date_string)
        return birth_date
    except ValueError:
        sys.exit("Invalid date")


def calculate_minutes(birth_date):
    """
    Calcule le nombre de minutes entre la date de naissance et aujourd'hui.
    """
    today = date.today()
    
    # Soustraire les deux dates pour obtenir un timedelta
    difference = today - birth_date
    
    # Convertir en minutes (timedelta.days donne le nombre de jours)
    minutes = difference.days * 24 * 60
    
    return minutes


def convert_to_words(number):
    """
    Convertit un nombre en mots anglais en utilisant inflect.
    """
    p = inflect.engine()
    words = p.number_to_words(number, andword="")
    
    # Capitaliser la première lettre et ajouter " minutes"
    return words.capitalize() + " minutes"


if __name__ == "__main__":
    main()