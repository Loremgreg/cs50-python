import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = r"""
    <iframe[^>]*               # <iframe suivi de n'importe quels caractères SAUF '>' (attributs divers)
    src="                      # On cherche ensuite l'attribut src="
    https?://                  # http ou https : le s après un caractère → le rend optionnel
    (?:www\.)?                 # www. optionnel (group non capturant car commence par ?:)
    youtube\.com/embed/        # domaine + chemin embed/
    ([^"]+)                    # capture l'ID vidéo (groupe capturant "1")
    "                          # fin de l'attribut src
"""

    match = re.search(pattern, s)

    if not match:
       return False

    match = match.group(1)
    return f"https://youtu.be/{match}"


...


if __name__ == "__main__":
    main()
