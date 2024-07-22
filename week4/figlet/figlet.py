import random
import sys
import pyfiglet
from pyfiglet import Figlet

def check_font(figlet, text):
    try:
        text = pyfiglet.figlet_format(text, font=sys.argv[2])
    except:
        print("Invalid usage")
        exit(-1)
    return text

def error_args():
    if len(sys.argv) != 1 and len(sys.argv) != 3:
        print("Invalid usage")
        exit(-1)
    if len(sys.argv) == 3:
        if sys.argv[1] != "-f" and sys.argv[1] != "--font":
            print("Invalid usage")
            exit(-1)
        try:
            pyfiglet.figlet_format("test", font=sys.argv[2])
        except:
            print("Invalid usage")
            exit(-1)

def main():
    error_args()
    text = str(input("Input: "))
    figlet = Figlet()
    figfonts = figlet.getFonts()
    if len(sys.argv) == 1:
        ascii_art = pyfiglet.figlet_format(text, font=random.choice(figfonts))
    if len(sys.argv) == 3:
        ascii_art = check_font(figlet, text)
    print(ascii_art)

if __name__ == "__main__":
    main()