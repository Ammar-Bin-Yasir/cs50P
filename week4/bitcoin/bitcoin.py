# Program that dynamically shows the price in USD of a bitcoin
import json
import requests
import sys

# Prompt user for the number of Bitcoins in float as command line argument
if len(sys.argv) != 2:
    print("Missing command-line argument")
    sys.exit(1)
elif len(sys.argv) == 2:
    try:
        coin = float(sys.argv[1])
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)
    else:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

        o = response.json()

        rate = o["bpi"]["USD"]["rate_float"]

        amount = rate * coin

        print(f"${amount:,.4f}")
# 
