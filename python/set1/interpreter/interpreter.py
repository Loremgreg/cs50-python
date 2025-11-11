def main():
    # On demande l'expression et on sépare en 3 parties
    x, y, z = input("Expression: ").split(" ")

    # On convertit x et z en nombres
    x = float(x)
    z = float(z)

    # On appelle la fonction interpreter
    result = interpreter(x, y, z)

    # On affiche le résultat avec 1 décimale
    print(f"{result:.1f}")


def interpreter(x, y, z):
    if y == "/":
        return x / z
    elif y == "+":
        return x + z
    elif y == "-":
        return x - z
    else:
        return x * z


main()