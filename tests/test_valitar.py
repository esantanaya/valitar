from valitar import __version__
from valitar.credit import Tarjeta


def test_version():
    assert __version__ == '0.1.0'

def test_AMEX_1():
    t = Tarjeta('378282246310005')
    t.valida_tarjeta()
    assert t.tipo == 'AMEX'

def test_AMEX_2():
    t = Tarjeta('371449635398431')
    t.valida_tarjeta()
    assert t.tipo == 'AMEX'

def test_AMEX_CORP():
    t = Tarjeta('378734493671000')
    t.valida_tarjeta()
    assert t.tipo == 'AMEX'

def test_Diners():
    t = Tarjeta('30569309025904')
    t.valida_tarjeta()
    assert t.tipo == 'INVALID'

def test_Discover_1():
    t = Tarjeta('6011111111111117')
    t.valida_tarjeta()
    assert t.tipo == 'INVALID'

def test_Discover_2():
    t = Tarjeta('6011000990139424')
    t.valida_tarjeta()
    assert t.tipo == 'INVALID'

def test_JCB_1():
    t = Tarjeta('3530111333300000')
    t.valida_tarjeta()
    assert t.tipo == 'INVALID'

def test_JCB_2():
    t = Tarjeta('3566002020360505')
    t.valida_tarjeta()
    assert t.tipo == 'INVALID'

def test_MASTERCARD_1():
    t = Tarjeta('5555555555554444')
    t.valida_tarjeta()
    assert t.tipo == 'MASTERCARD'

def test_MASTERCARD_2():
    t = Tarjeta('5105105105105100')
    t.valida_tarjeta()
    assert t.tipo == 'MASTERCARD'

def test_Visa_1():
    t = Tarjeta('4111111111111111')
    t.valida_tarjeta()
    assert t.tipo == 'VISA'

def test_Visa_2():
    t = Tarjeta('4012888888881881')
    t.valida_tarjeta()
    assert t.tipo == 'VISA'

def test_Visa_3():
    t = Tarjeta('4222222222222')
    t.valida_tarjeta()
    assert t.tipo == 'VISA'
