class CryptoFormater:
    def format2(value):
        if value == 0:
            return 0
        if value < 0.01:
            return "{:.2e}".format(value)
        return "{:.2f}".format(value)
