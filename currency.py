from requests import get
from dotenv import load_dotenv
import os

BASE_URL = "https://v6.exchangerate-api.com/"

load_dotenv()
API_KEY = os.getenv("API_KEY")


def get_currencies():
    endpoint = f"v6/{API_KEY}/latest/USD"
    url = BASE_URL + endpoint
    data = get(url).json()
    data = data.get("conversion_rates")
    #print(data)  #this line is commented out but retained for use when gathering data for the pytest
    for currency in data:
        print(f"{currency}: {data[currency]}")

    return data


def exchange_rate(currency1, currency2):
    endpoint = f"v6/{API_KEY}/pair/{currency1}/{currency2}"
    url = BASE_URL + endpoint
    response = get(url)

    data = response.json()
    
    rate = data.get("conversion_rate")

    if rate is None:
        print("Invalid input.")
        return "Invalid input."

    else:
        print(f"{currency1} to {currency2} = {rate}")
        return rate
    
def convert(currency1, currency2, amount):
    rate = exchange_rate(currency1, currency2)
    if rate == "Invalid input.":
        return "Invalid input."
    
    try:
        amount = float(amount)
    except:
        print("Invalid input.")
        

    rate = float(rate)

    converted_amount = rate * amount
    print(f"{amount} {currency1} is equal to {converted_amount} {currency2}.")
    return converted_amount

def main():

    print("$$$Currency converter! Use commands listed below.$$$")
    print("List - lists all available currencies.")
    print("Convert - converts an amount from one currency to another.")
    print("Rate - shows the exchange rate between two currencies.")
    print("Q - quits the program.")
    print()

    while True:
        command = input("Enter a command: ").lower()

        if command == "list":
            get_currencies()
            
        elif command == "convert":
            currency1 = input("Enter the source currency (e.g. USD): ").upper()
            currency2 = input("Enter the target currency (e.g. EUR): ").upper()
            amount = input("Enter the amount to convert: ")
            convert(currency1, currency2, amount)
        elif command == "rate":
            currency1 = input("Enter the first currency (e.g. USD): ").upper()
            currency2 = input("Enter the second currency (e.g. EUR): ").upper()
            exchange_rate(currency1, currency2)
        elif command == "q":
            print("Finished.")
            break
        else:
            print("Invalid command. Use commands listed below.")
            print("List - lists all available currencies.")
            print("Convert - converts an amount from one currency to another.")
            print("Rate - shows the exchange rate between two currencies.")
            print("Q - quits the program.")

if __name__ == "__main__":
    main()

