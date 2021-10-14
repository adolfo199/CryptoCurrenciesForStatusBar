import json
import os

from Helpers.PluginRegister import PluginRegister
from Utils.CryptoFormater import CryptoFormater


def loadCurrencies():
    home_directory = os.path.expanduser('~')
    f = open(f'{home_directory}/.config/CryptoBarModule/config.json')
    data = json.load(f)
    return data["currencies"]


def main():
    currencies = loadCurrencies()
    out = ""
    totalBalance = 0
    for currency in currencies:
        plugin = PluginRegister().get_register(currency[2])
        response = plugin.GETCurrency(currency)
        totalBalance += response[1]
        out += response[0]+" | "
    if(totalBalance > 0):
        out += f'T:${CryptoFormater.format2(totalBalance)}'
    print(out)


main()
