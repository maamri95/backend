from unittest import TestCase

from .vigenere import Vigenere


class TestVigenere(TestCase):
    def setUp(self):
        self.v = Vigenere("permute")

    def test_crypto(self):
        self.assertEqual(self.v.crypto("securite"), "HITGLBXT")

    def test_decrypto(self):
        self.assertEqual(self.v.decrypto("HITGLBXT"), "securite")
