from unittest import TestCase

from .hill import Hill


class TestHill(TestCase):
    def setUp(self):
        self.t = [[11, 13], [5, 6]]
        self.t3 = [[11, 13, 7], [5, 6, 3], [1, 8, 4]]
        self.m = 2
        self.hill = Hill(self.t, self.m)
        self.x = [[15, 18, 4, 4, 14, 18], [0, 3, 17, 15, 13, 4]]

    def test_crypto(self):
        self.assertEqual(self.hill.crypto("pas de reponse"), "URFVEGHXEDS!")

    def test_crypto_3(self):
        hill = Hill([
            [7, 9, 2],
            [5, 6, 8],
            [3, 4, 1]
        ], 3)
        self.assertEqual(hill.crypto("pas de reponse"), "ZQFEBNRT?AC?")

    def test_decrypto(self):
        self.assertEqual(self.hill.decrypto("URFVEGHXEDS!"), "pasdereponse")

    def test_decrypto_3(self):
        hill = Hill([
            [7, 9, 2],
            [5, 6, 8],
            [3, 4, 1]
        ], 3)
        self.assertEqual(hill.decrypto(hill.crypto("pas de reponse")), "pasdereponse")

    def test_numbloc(self):
        self.assertEqual(self.hill.numbloc("pasdereponse"), self.x)

    def test_msg(self):
        self.assertEqual(self.hill.msg(self.x), "pasdereponse")

    def test_init_raise(self):
        with self.assertRaises(ArithmeticError):
            Hill([[11, 6], [11, 6]], self.m)
