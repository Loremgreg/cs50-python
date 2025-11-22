from random import randint


def main():
    # 1) Demande un niveau de difficulté (1, 2 ou 3)
    level = get_level()

    score = 0  # compteur de bonnes réponses

    # 2) Génère 10 problèmes
    for _ in range(10):
        # Génère deux nombres adaptés au niveau choisi
        x = generate_integer(level)
        y = generate_integer(level)

        correct_answer = x + y
        tries = 0  # nombre d'essais pour cette question

        # 3 essais maximum
        while tries < 3:
            try:
                # Demande à l'utilisateur de résoudre l'opération
                calculus = int(input(f"{x} + {y} = "))

                # Réponse correcte
                if calculus == correct_answer:
                    score += 1
                    break  # sortir de la boucle "tries"
            except ValueError:
                # Si l'utilisateur entre autre chose qu'un nombre
                pass

            # Si mauvaise réponse ou erreur → affiche "EEE"
            print("EEE")
            tries += 1

        # Après 3 erreurs → afficher la solution
        if tries == 3:
            print(f"{x} + {y} = {correct_answer}")

    # Affiche le score final sur 10
    print(f"Score: {score}")


def get_level():
    # Fonction qui demande un niveau valide : 1, 2 ou 3
    while True:
        try:
            get_level = int(input("Level: "))
            if get_level in [1, 2, 3]:
                return get_level
        except ValueError:
            # Si l'utilisateur tape autre chose → recommence
            pass


def generate_integer(level):
    """
    Retourne un entier aléatoire avec 'level' chiffres :
    - level 1 → entre 0 et 9
    - level 2 → entre 10 et 99
    - level 3 → entre 100 et 999
    """
    if level == 1:
        return randint(0, 9)
    elif level == 2:
        return randint(10, 99)
    elif level == 3:
        return randint(100, 999)
    else:
        raise ValueError  # ne devrait jamais arriver


# Lance le programme
if __name__ == "__main__":
    main()