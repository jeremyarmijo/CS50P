import sys
import requests
import json

def transform_value(nb):
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
        Final_result = float(response['bpi']["USD"]["rate"].replace(",", ""))
        return Final_result * nb
    except requests.RequestException:
        print("Request failure") 

def main():
    try:
        if len(sys.argv) != 2:
            sys.exit("Missing command-line argument")
        nb = float(sys.argv[1])
        nb = transform_value(nb)
        print(f"${nb:,.4f}")
    except ValueError:
        sys.exit("Command-line argument is not a number")

if __name__ == "__main__":
    main()