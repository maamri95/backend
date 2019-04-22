from .hill import Hill
from .vigenere import Vigenere


class VigenereHill:
    """
    class de bicryptage vigenere et hill

    """

    def __init__(self, t, cle, m=3):
        """
        classe de bicryptage vigenere et hill

        :param t: cle matricielle de hill
        :type t : list[list[int]]
        :param cle: mot cle de vigenere
        :type cle: str
        :param m: taille des bloc pour hill
        ;:type m: int
        """
        self.hill = Hill(t, m)
        self.vigenere = Vigenere(cle)

    def crypt(self, text_clair):
        """
        crypte le texte donne en param

        :param text_clair: texte a crypte
        :type text_clair: str
        :returns: text_interm, text_crypt
        :return text_interm: texte intermidaire
        :return text_crypt: texte crypte final
        :rtype: str
        """
        text_interm = self.vigenere.crypto(text_clair)
        return text_interm, self.hill.crypto(text_interm.lower())

    def decrypt(self, text_crypt):
        """
        decrypte le texte donne en param

        :param text_crypt: texte a decrypte
        :type text_crypt: str
        :returns: text_interm, text_clair
        :return text_interm: texte intermidaire
        :return text_clair: texte claire
        :rtype: str
        """
        text_interm = self.hill.decrypto(text_crypt)
        while text_interm[-1] == "x":
            text_interm = text_interm[0:-1]
        return text_interm, self.vigenere.decrypto(text_interm)
