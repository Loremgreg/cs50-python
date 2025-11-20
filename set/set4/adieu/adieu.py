import inflect

p = inflect.engine()
names_list = []

while True:
    try:
        name_input = input()
    except EOFError:
        break
    else:
        names_list.append(name_input)

print(f"Adieu, adieu, to {p.join(names_list)}")
