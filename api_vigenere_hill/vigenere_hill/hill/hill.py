import string

from .matrice import prod, transpose, inv


class Hill:
    """
        classe qui defini le cryptage de hill

    """

    def __init__(self, t, m, add_alph=",!?", alphavoid="x"):
        """
            classe qui defini le cryptage de hill
                :param t: matrice de codage
                :type t: list[list[int]]
                :param m: taille de bloc
                :type m: int
                :param add_alph: caractaires a rajoute a l'alphabe latin
                :type add_alph: str
                :param alphavoid: caractaire de remplacement
                :type alphavoid: str
        """
        self.alpha = string.ascii_lowercase + add_alph
        self.alphavoid = alphavoid
        (self.tinv, self.comMatrice, self.comMatriceT, self.k) = inv(t)
        self.t = t
        self.m = m

    def numbloc(self, msg):
        """
        devise le msg en bloc de self.m lettre
        :param msg: le texte a devise
        :type msg : str
        :return: une matrice
        :rtype: list[list[int]]
        """
        msg = msg.lower()
        if len(msg) % self.m != 0:
            msg += self.alphavoid * (self.m - (len(msg) % self.m))
        return transpose([
            [
                self.alpha.index(j)
                for j in msg[i:i + self.m]
            ]
            for i, c in enumerate(msg) if i % self.m == 0
        ])

    def msg(self, tab):
        """
        transforme la matrice en texte
        :param tab: matrice
        :type tab: list[list[int]]
        :return: texte contenu dans la matrice
        :rtype: str
        """
        m = ""
        tab = transpose(tab)
        for i in range(len(tab)):
            for j in range(len(tab[i])):
                m += self.alpha[tab[i][j]]
        return m

    def crypto(self, text_clair: str):
        """
        crypte le texte entre
        :param text_clair: texte a crypte
        :type text_clair: str
        :return: texte crypte
        :rtype: str
        """
        text_clair = text_clair.lower()
        text_clair = text_clair.replace(" ", "")
        mat = self.numbloc(text_clair)
        mat_res = prod(self.t, mat)
        return self.msg(mat_res).upper()

    def decrypto(self, text_crypt):
        """
        decrypte le texte d'entre
        :param text_crypt: texte a decrypte
        :type text_crypt: str
        :return: texte decrypte
        :rtype: str
        """
        text_crypt = text_crypt.replace(" ", "").lower()
        mat = self.numbloc(text_crypt)
        matres = prod(self.tinv, mat)
        return self.msg(matres)
