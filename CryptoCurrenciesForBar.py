from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import os
API_KEY = ''


def join_items(f, arr):
    return ','.join(list(map(f, arr)))


def format2(value):
    if value < 0.01:
        return "{:.2e}".format(value)
    return "{:.2f}".format(value)


def get_price(coin):
    return coin["quote"]["USD"]["price"]


def create_session():
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': API_KEY,
    }
    session = Session()
    session.headers.update(headers)
    return session


def get_output(data, currencies):
    out = ""
    totalBalance = 0
    for currency in currencies:

        price = get_price(data[currency[0]])
        balance_calc = format2(price*currency[1])
        totalBalance += float(balance_calc)
        balance = ""
        if currency[1] > 0:
            balance = "${}".format(balance_calc)
        out += "{} ${} {}% {} | ".format(currency[0],
                                         format2(price), "{:.2f}".format(data[currency[0]]["quote"]["USD"]["percent_change_24h"]), balance)
    if totalBalance > 0:
        out += "T:{}".format(format2(totalBalance))
    return out


def loadCurrencies():
    home_directory = os.path.expanduser('~')
    f = open(f'{home_directory}/.config/CryptoBarModule/config.json')
    data = json.load(f)
    return data


def main():
    crypto_currencies = loadCurrencies()["currencies"]
    currencies_names = join_items(lambda x: x[0], crypto_currencies)
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = {
        'symbol': currencies_names,
        'convert': 'USD'
    }
    session = create_session()
    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        out = get_output(data["data"], crypto_currencies)
        print(out)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)


main()
