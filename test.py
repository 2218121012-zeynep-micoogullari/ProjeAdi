import unittest
from main import toplama, cikarma, carpma, bolme

class TestCalculator(unittest.TestCase):

    def test_toplama(self):
        self.assertEqual(toplama(5, 3), 8)  # 5 + 3 = 8
        self.assertEqual(toplama(-1, 1), 0)  # -1 + 1 = 0

    def test_cikarma(self):
        self.assertEqual(cikarma(5, 3), 2)  # 5 - 3 = 2
        self.assertEqual(cikarma(5, 8), -3)  # 5 - 8 = -3

    def test_carpma(self):
        self.assertEqual(carpma(5, 3), 15)  # 5 * 3 = 15
        self.assertEqual(carpma(0, 3), 0)  # 0 * 3 = 0
        self.assertEqual(carpma(-5, 3), -15)  # -5 * 3 = -15

    def test_bolme(self):
        self.assertEqual(bolme(6, 3), 2)  # 6 / 3 = 2
        self.assertEqual(bolme(5, 0), "Bir sayı sıfıra bölünemez!")  # Bölme hatası
        self.assertEqual(bolme(9, 3), 3)  # 9 / 3 = 3

if __name__ == '__main__':
    unittest.main()