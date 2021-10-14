import json
from Plugins.PluginInterface import PluginInterface
from Utils.CryptoFormater import CryptoFormater


class CoinexPlugin(PluginInterface):
    def __init__(self) -> None:
        super().__init__('https://api.coinex.com/v1/market/ticker?')

    def create_output(self, data: object, currency):
        price = float(data["data"]["ticker"]["last"])
        balance = float(currency[1]) * price
        return ["{} ${} {}".format(currency[0],
                                   CryptoFormater.format2(price),
                                   CryptoFormater.format2(balance)), balance]

    def GETCurrency(self, currency) -> str:
        session = super().create_session({
            'Accepts': 'application/json'
        })
        parameters = {
            'market': f'{currency[0]}USDT'
        }
        response = session.get(self.URL, params=parameters)
        data = json.loads(response.text)
        return self.create_output(data, currency)
