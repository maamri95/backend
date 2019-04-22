from unittest import TestCase

from .matrice import inv, compliment, com, det, prod, transpose


class TestMatrice(TestCase):
    def setUp(self):
        self.t = [[11, 13], [5, 6]]
        self.t3 = [[1, 2, 3], [0, 1, 2], [-1, -4, -1]]

    def test_com_3(self):
        self.assertEqual(com(self.t3), [[7, -2, 1], [-10, 2, 2], [1, -2, 1]])

    def test_com_2(self):
        self.assertEqual(com(self.t), [[6, -5], [-13, 11]])

    def test_transpose(self):
        mat2 = [[15, 18, 4, 4, 14, 18], [0, 3, 17, 15, 13, 4]]
        rep = [[15, 0], [18, 3], [4, 17], [4, 15], [14, 13], [18, 4]]
        self.assertEqual(transpose(mat2), rep)

    def test_compliment(self):
        self.assertEqual(compliment(3), 10)

    def test_inv(self):
        self.assertEqual(inv(self.t),
                         ([
                              [6, 16],
                              [24, 11]
                          ],
                          com(self.t),
                          transpose(com(self.t)),
                          compliment(det(self.t)),
                         ))

    def test_produit(self):
        mat1 = [[11, 13], [5, 6]]
        mat2 = [[15, 18, 4, 4, 14, 18], [0, 3, 17, 15, 13, 4]]
        res = [[20, 5, 4, 7, 4, 18], [17, 21, 6, 23, 3, 27]]
        self.assertEqual(prod(mat1, mat2), res)

    def test_inv_raise(self):
        with self.assertRaises(ArithmeticError):
            inv([[11, 6], [11, 6]])

    def test_det_3(self):
        self.assertEqual(det([
            [7, 9, 2],
            [5, 6, 8],
            [3, 4, 1]
        ]), -7)

    def test_det_2(self):
        self.assertEqual(det(self.t), 1)
