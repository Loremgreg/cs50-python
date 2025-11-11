def main():
    question_time = input("What time is it? ")

    # Convertit la chaîne de caractères entrée en un nombre décimal représentant l'heure en format 24h
    time = convert(question_time)

    if 7 <= time <= 8:
        print ("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time") 

def convert(time):
    # Sépare la chaîne de caractères en deux parties : heures et minutes, en utilisant ":" comme séparateur
    h, m = time.split(":")
    # Convertit la partie heures en nombre décimal (float)
    h_conv = float(h)
    # Convertit la partie minutes en fraction d'heure 
    m_conv = float(m) / 60
    h_m_conv = h_conv + m_conv
    return h_m_conv

# Point d'entrée du programme : si ce fichier est exécuté directement, lance la fonction main()
if __name__ == "__main__":
    main()


# output : breakfast time, lunch time, or dinner time. If it’s not time for a meal, don’t output anything
# formatted in 24-hour time as #:## or ##:##
