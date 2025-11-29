import re
import sys

# ip = sys.argv[1]

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # REGEX pour valider le format IPv4 basique :
    # ^               → début de la chaîne
    # (?!0\d)         → empêche des nombres avec un zéro non nécessaire (ex: 01, 002)
    # (\d+)           → capture 1 ou plusieurs chiffres = premier octet
    # \.              → un point littéral
    # (?!0\d)(\d+)    → deuxième octet
    # \.
    # (?!0\d)(\d+)    → troisième octet
    # \.
    # (?!0\d)(\d+)    → quatrième octet
    # $               → fin de la chaîne
    pattern = r"^(?!0\d)(\d+)\.(?!0\d)(\d+)\.(?!0\d)(\d+)\.(?!0\d)(\d+)$"

    # re.search essaie de trouver un match complet avec la regex
    match = re.search(pattern, ip)

    # Si aucun match, ce n'est pas une IPv4 valide
    if not match:
        return False

    # match.groups() renvoie un tuple contenant les 4 octets capturés
    subgroup = match.groups()

    # On vérifie maintenant que chaque numéro est entre 0 et 255
    for group in subgroup:
        # Si un octet dépasse 255, l'adresse est invalide
        if int(group) > 255:
            return False

    # Si tout est bon, IPv4 valide
    return True


if __name__ == "__main__":
    main()