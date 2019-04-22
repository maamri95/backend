import string


class Vigenere:
    """
        classe qui defini le cryptage de vigenere
    """
    alph = string.ascii_lowercase

    def __init__(self, cle):
        """
            classe qui defini le cryptage de vigenere
            :param cle: cle de chifferement
            :type cle: str
        """
        self.cle = cle

    def crypto(self, text_clair: str):
        """
        crypte le text_clair en un code vigenere en utilisant l'atrubut self.cle
        :type text_clair: str
        :return text_crypt: str
        """
        text_clair = text_clair.lower().replace(" ", "")
        text_crypt = ""
        for i, c in enumerate(text_clair):
            index = self.alph.index(c)
            pos = (index + self.alph.index(self.cle[i % len(self.cle)])) % len(self.alph)
            text_crypt += self.alph[pos]
        return text_crypt.upper()

    def decrypto(self, text_crypt: str):
        text_crypt = text_crypt.lower().replace(" ", "")
        text_clair = ""
        for i, c in enumerate(text_crypt):
            index = self.alph.index(c)
            pos = (index - self.alph.index(self.cle[i % len(self.cle)])) % len(self.alph)
            text_clair += self.alph[pos]
        return text_clair
