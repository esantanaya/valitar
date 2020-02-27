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
        if suma_total % 10 == 0:
            digito_ver = 0
        return digito_ver == lista_numeros[-1]

    def _valida_longitud(self, longitud):
        if isinstance(longitud, int):
            return len(self.numero) == longitud
        if isinstance(longitud, str):
            return len(self.numero) in [int(x) for x in longitud.split('|')]

    def _valida_comienzo(self, opciones):
        return any([self.numero.startswith(x) for x in opciones])

    def valida_tarjeta(self):
        for tipo, validacion in self._VALIDACIONES.items():
            if (self._valida_longitud(validacion.get('len')) and
                self._valida_comienzo(validacion.get('starts')) and
                self._valida_luhn()):
                self.tipo = self._TIPOS.index(tipo)


if __name__ == '__main__':
    t = Tarjeta(input('Number: '))
    t.valida_tarjeta()
    print(t.tipo)
    print()
