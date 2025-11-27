import sys
from PIL import Image, ImageOps
import os

# Vérifie qu’il y a AU MOINS 2 arguments (script + input + output)
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

# Vérifie qu’il n’y a PAS PLUS de 3 arguments (script + 2 fichiers)
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

# On récupère les noms des fichiers d’entrée et de sortie
# Exemple : python shirt.py input.jpg output.jpg
input_img = sys.argv[1]
output_img = sys.argv[2]

# On sépare le nom du fichier et son extension
# splitext("photo.jpg") → ("photo", ".jpg")
input_root, input_ext = os.path.splitext(input_img)
output_root, output_ext = os.path.splitext(output_img)

# Vérification des extensions
if len(sys.argv) == 3:

    # Vérifie que les fichiers se terminent par .jpg, .jpeg ou .png (insensible à la casse)
    if not input_img.lower().endswith(('.jpg', 'jpeg', '.png')) or not output_img.lower().endswith(('.jpg', 'jpeg', '.png')):
        sys.exit("Invalid output")

    # Vérifie que l’extension d'entrée et celle de sortie sont identiques
    # Exemple valide : input.png → output.png
    # Exemple invalide : input.jpg → output.png
    if input_ext.lower() != output_ext.lower():
        sys.exit("Input and output have different extensions")

    # On tente d’ouvrir l’image d’entrée
    try:
        photo = Image.open(input_img)
    except FileNotFoundError:
        sys.exit("Input does not exist")

    # ----------- AVOID HARDCODING -----------
    # Au lieu de mettre "shirt.png" en dur, on le met dans une variable
    # Cela rend le code plus flexible si tu veux changer l'image du t-shirt.
    shirt_img = "shirt.png"
    # ----------------------------------------

    # On ouvre l’image du t-shirt avec fond transparent
    shirt = Image.open(shirt_img)

    # On récupère la taille du t-shirt (largeur, hauteur)
    size = shirt.size

    # On redimensionne + recadre la photo d'entrée pour qu’elle ait la même taille que le t-shirt
    # ImageOps.fit ajuste l’image tout en conservant le ratio puis centre l’image
    photo = ImageOps.fit(photo, size)

    # On colle le t-shirt sur la photo
    # Le 2e argument (shirt) sert de masque pour respecter la transparence
    photo.paste(shirt, shirt)

    # On sauvegarde l'image finale
    photo.save(output_img)