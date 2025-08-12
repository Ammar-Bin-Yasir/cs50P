# Show the txt of the user in the form of ASCII art
import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
figlet_list = figlet.getFonts()

if len(sys.argv) == 2 and (sys.argv[1] == "-f" or sys.argv[1] == "--font") and (sys.argv[2] in figlet_list):

    # txt = input("Input: ")

    figlet.setFont(font=sys.argv[2])

    print(f"Output {figlet.renderText(input("Input: "))}")

elif len(sys.argv) == 1:
    # txt  = input("Input: ")

    figlet.setFont(font=random.choice(figlet_list))

    print(f"Output {figlet.renderText(input("Input: "))}")
else:
    sys.exit(1)












