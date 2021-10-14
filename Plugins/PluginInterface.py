from requests.sessions import Session


class PluginInterface:
    def __init__(self, url: str) -> None:
        self.URL = url

    def create_output(self, data: object, currency: str):
        raise NotImplementedError("Output method not implemented")

    def create_session(self, headers) -> Session:
        session = Session()
        session.headers.update(headers)
        return session

    def GETCurrency(currency) -> str:
        raise NotImplementedError(f"{currency[0]} get data method not defined")
