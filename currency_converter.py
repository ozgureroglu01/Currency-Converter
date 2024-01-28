import requests
from countryinfo import CountryInfo

def main():
    while True:
        try:
            currency_convert_from = get_convert_from()
            currency_convert_to = get_convert_to()
            break
        except KeyError:
            print("İnvalid country name try again")
    amount = input("Enter amount: ")
    print(convert(currency_convert_from,currency_convert_to,amount))
  
def supported_counrties():
    url = "https://currency-converter18.p.rapidapi.com/api/v1/supportedCurrencies"

    headers = {
        "X-RapidAPI-Key": "e7939e3929msh39a6e7067aca73cp11e489jsn76676d6ab054",
        "X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    return response.json()


def get_convert_from():
    convert_from = input("Enter country name to convert from: ").title()
    country = CountryInfo(convert_from)
    currency_info = country.currencies()
    if len(currency_info) > 1:
        if currency_info[0] != supported_counrties()[0]["symbol"]:
            for i in range(len(currency_info)):
                new_currency_info=currency_info[i]
            return new_currency_info
    return currency_info[0]

def get_convert_to():
    convert_to = input("Enter country name to convert to: ").title()
    country = CountryInfo(convert_to)
    currency_info = country.currencies()
    if len(currency_info) > 1:
        if currency_info[0] != supported_counrties()[0]["symbol"]:
            for i in range(len(currency_info)):
                new_currency_info=currency_info[i]
            return new_currency_info
    return currency_info[0]


def convert(currency_convert_from,currency_convert_to,amount):
    url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

    querystring = {"from":currency_convert_from,"to":currency_convert_to,"amount":amount}

    headers = {
        "X-RapidAPI-Key": "e7939e3929msh39a6e7067aca73cp11e489jsn76676d6ab054",
        "X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    return "{:.2f}".format(response.json()["result"]["convertedAmount"])

if __name__ == "__main__":
    main()

