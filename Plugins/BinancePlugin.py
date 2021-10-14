import json
from Plugins.PluginInterface import PluginInterface
from Utils.CryptoFormater import CryptoFormater


class BinancePlugin(PluginInterface):
    def __init__(self) -> None:
        super().__init__('https://api.binance.com/api/v3/ticker/24hr?')

    def create_output(self, data: object, currency):
        price = float(data["lastPrice"])
        balance = float(currency[1]) * price
        return ["{} ${} {}% {}".format(currency[0],
                                       CryptoFormater.format2(price),
                                       "{:.2f}".format(
            float(data["priceChangePercent"])),
            CryptoFormater.format2(balance)), balance]

    def GETCurrency(self, currency) -> str:
        session = super().create_session({
            'Accepts': 'application/json'
        })
        parameters = {
            'symbol': f'{currency[0]}USDT'
        }
        response = session.get(self.URL, params=parameters)
        data = json.loads(response.text)
        return self.create_output(data, currency)
