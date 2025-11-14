# input user item, case insensit
# until ctrl d
# output list sorted alphabet and all uppercase
# + prefixe item with number of time that item was input
#  keys are items and the values are counts.

def main():
    # Il est préférable de définir le dic à l'intérieur de la fonction où il est utilisé.
    counts = {}

    while True:
        try:

            item = input().upper()

            # 2. Met à jour le compteur pour l'article.
            #    .get(item, 0) récupère la valeur actuelle de 'item'. Si 'item' n'existe pas, il retourne 0.
            #    Ensuite, on ajoute 1 à cette valeur et on met à jour le dictionnaire.
            counts[item] = counts.get(item, 0) + 1     # 0 : La valeur par défaut à retourner si la clé item n'est pas trouvée

        # 3. Ce bloc s'exécute lorsque l'utilisateur appuie sur Ctrl-D (signal de fin de fichier).
        except EOFError:
            # Appelle la fonction 'alphabetic_order' pour obtenir une version triée du dictionnaire 'counts'.
            # Cette fonction est censée retourner un dictionnaire avec les clés triées alphabétiquement.
            sorted_counts = alphabetic_order(counts)
            # Étant donné que 'sorted_counts' est censé avoir ses clés déjà triées,
            # cette boucle itérera sur les articles dans l'ordre alphabétique.
            for i in sorted_counts:
                # Affiche la quantité de l'article (la valeur associée à la clé 'i' dans 'sorted_counts')
                # suivie du nom de l'article lui-même ('i').
                print(sorted_counts[i], i)
            break


# Définit une fonction nommée 'alphabetic_order' qui prend un dictionnaire 'counts' en argument.
# Le but de cette fonction est de retourner un nouveau dictionnaire dont les clés sont triées alphabétiquement.
def alphabetic_order(counts):
    # 1. `counts.items()`: Retourne une vue des paires (clé, valeur) du dictionnaire.
    # 2. `sorted(...)`: Trie cette liste de paires. Par défaut, le tri se fait sur le premier élément de chaque paire (la clé).
    # 3. `dict(...)`: Convertit la liste de paires triées en un nouveau dictionnaire.
    sorted_count = dict(sorted(counts.items()))
    return sorted_count

main()
