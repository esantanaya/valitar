class Tarjeta:
    _TIPOS = ('INVALID', 'AMEX', 'MASTERCARD', 'VISA')
    _VALIDACIONES = {
        'AMEX': {'len': 15, 'starts': ('34', '37')},
        'MASTERCARD': {'len': 16, 'starts': ('51', '52', '53', '54', '55')},
        'VISA': {'len': '13|16', 'starts': ('4')},
    }

    def __init__(self, numero):
        self.numero = numero
        self.tipo = 0

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, numero):
        self._numero = numero

    @property
    def tipo(self):
        return self._TIPOS[self._tipo]

    @tipo.setter
    def tipo(self, tipo):
        if 0 < tipo < len(self._TIPOS):
            self._tipo = tipo
        else:
            self._tipo = 0

    def _valida_luhn(self):
        lista_numeros = [int(x) for x in self.numero]
        pares = [sum(divmod(x * 2, 10)) for x in lista_numeros][-2::-2][::-1]
        nones = [x for x in lista_numeros][-3::-2][::-1]
        suma_total = sum(pares + nones)
        digito_ver = 10 - (suma_total % 10)
        return digito_ver == lista_numeros[-1]

    def valida_tarjeta(self):
        if 
