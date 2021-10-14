from Plugins.CoinexPlugin import CoinexPlugin
from Plugins.BinancePlugin import BinancePlugin
from Plugins.PluginInterface import PluginInterface


class PluginRegister:
    _plugins = {
        'binance': BinancePlugin,
        'coinex': CoinexPlugin
    }

    def get_register(self, ref: str) -> PluginInterface:
        return self._plugins[ref]()
