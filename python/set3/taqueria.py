taqueria_price = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    while True:
        try:
            item = input("Item: ")
            prix = check_item(taqueria_price[item])
            print(f"${prix}")
        except EOFError:
            return

def check_item(item):
    list_items = []
    for item in taqueria_price:
        list_items += item
    return list_items

def total_cost(list_items):
    pass


main()

    # demander au user to place an order - stop quand "ctrl-d"
    # display total cost of all items a 2 decimale
    # input user est case insensitively
    # ignorer (continue) quand ce nest pas un item de la liste

    # Plan:
    # main() : va prompter le user avec un try except error
    # total_cost() : va additionner le montant des items et retourner une valeur
    # check_item() : va utiliser get(key, default=None, /) pour looper dans le dic. Return le prix de l'item

