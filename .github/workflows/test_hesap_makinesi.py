import pytest
from hesap_makinesi import toplama, cikarma, carpma, bolme

def test_toplama():
    assert toplama(2, 3) == 5

def test_cikarma():
    assert cikarma(5, 3) == 2

def test_carpma():
    assert carpma(2, 3) == 6

def test_bolme():
    assert bolme(6, 2) == 3
    assert bolme(6, 0) == "Bir sayı sıfıra bölünemez!"
