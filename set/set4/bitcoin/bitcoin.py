import requests
import json
import sys

def main():
    # On tente d'appeler l'API CoinCap (fetch des données Bitcoin)
    try:
        response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=b39cc01b59728e2f26a01342c7e8c1a00f9da171687938441ce9c1ea359d5ab1")
        print(response)                 # Affiche le status HTTP (200, 403, etc.)
        response.raise_for_status()     # Génère une erreur si le status n'est pas 200

    # Si un problème réseau/API survient → on sort proprement du programme
    except requests.RequestException:
        print("REQUEST ERROR")
        return


    # Deuxième bloc try/except DÉDIÉ au traitement des arguments depuis la ligne de commande
    # Pourquoi un second try ? Parce que les erreurs ici n'ont rien à voir avec l'API.
    try:
        n = float(sys.argv[1])          # On essaie de convertir l’argument en float (quantité de Bitcoin)
    
    # Si aucun argument n'a été fourni → sys.argv[1] n'existe pas
    except IndexError:
        sys.exit("Missing command-line argument")

    # Si un argument a été fourni mais n'est PAS un nombre ("abc", etc.)
    except ValueError:
        sys.exit("Command-line argument is not a number")


    # On parse le JSON de la réponse API
    content = response.json()

    # L'API renvoie un prix sous forme de string → on convertit en float
    price_one_bitcoin = float(content["data"]["priceUsd"])

    # On calcule combien vaut n Bitcoin
    convertion = price_one_bitcoin * n

    # Formatage esthétique : séparateur de milliers, 4 décimales
    print(f"${convertion:,.4f}")


main()