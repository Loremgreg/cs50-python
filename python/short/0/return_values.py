def area(lenght, width):
    print(f"{lenght * width} square metter")
    return lenght * width


def main():
    house = area(10, 12)
    garden = area(20, 9)
    tot = house + garden
    print(f"{tot} total square met")
main()
