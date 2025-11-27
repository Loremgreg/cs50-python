import sys
from PIL import Image, ImageOps
import os


def main():
    # Valide les arguments et récupère les infos utiles
    input_img, output_img, input_ext, output_ext = validate_args()

    # Traite l’image (ouvre, redimensionne, colle le t-shirt, sauvegarde)
    process_image(input_img, output_img, input_ext, output_ext)


def validate_args():
    """
    Vérifie le nombre d'arguments et prépare les noms + extensions.
    """
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_img = sys.argv[1]
    output_img = sys.argv[2]

    input_root, input_ext = os.path.splitext(input_img)
    output_root, output_ext = os.path.splitext(output_img)

    return input_img, output_img, input_ext, output_ext


def process_image(input_img, output_img, input_ext, output_ext):
    """
    Vérifie les extensions et applique le t-shirt sur la photo.
    """
    if len(sys.argv) == 3:
        # Vérifie que les fichiers ont des extensions d’image valides
        if not input_img.lower().endswith(('.jpg', 'jpeg', '.png')) or not output_img.lower().endswith(('.jpg', 'jpeg', '.png')):
            sys.exit("Invalid output")

        # Vérifie que les extensions sont identiques
        if input_ext.lower() != output_ext.lower():
            sys.exit("Input and output have different extensions")

        # Tente d’ouvrir l’image d’entrée
        try:
            photo = Image.open(input_img)
        except FileNotFoundError:
            sys.exit("Input does not exist")

        # Fichier du t-shirt (toujours le même)
        shirt_img = "shirt.png"
        shirt = Image.open(shirt_img)

        # Adapter la taille de la photo à celle du t-shirt
        size = shirt.size
        photo = ImageOps.fit(photo, size)

        # Coller le t-shirt sur la photo
        photo.paste(shirt, shirt)

        # Sauvegarder l’image finale
        photo.save(output_img)


if __name__ == "__main__":
    main()