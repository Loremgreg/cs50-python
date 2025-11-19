from pyfiglet import Figlet
import sys
from random import choice

figlet = Figlet()

if len(sys.argv) == 1:
    # 1. Bringing the list of the font from figlet
    # 2. use random to choose a font
    # 3. put the random font in variable name
    font_list = figlet.getFonts()

    random_font = choice(font_list)

    font = figlet.setFont(font=random_font)
    input = input("Input: ")
    print(figlet.renderText(input))


elif len(sys.argv) > 2:
    if "-f" != sys.argv[1] and "--font" != sys.argv[1]:
        sys.exit("Invalid usage")

    font_list = figlet.getFonts()
    if sys.argv[2] not in font_list:
        sys.exit("Invalid usage")

    font = figlet.setFont(font=sys.argv[2])
    input = input("Input: ")
    print(figlet.renderText(input))

else:
    sys.exit("Invalid usage")


