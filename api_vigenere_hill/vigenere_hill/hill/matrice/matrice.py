def reduire(mat, n, m):
    """
        return la matrice moi la ligne n et la collenne m
    :param m: collenne
    :param n: ligne
    :param mat: matrice
    :type n: int
    :type m: int
    :type mat: list[list[int]]
    """
    res = []
    for i in range(len(mat)):
        if i != n:
            lin = []
            for j in range(len(mat[i])):
                if j != m:
                    lin += [mat[i][j]]

            res += [lin]
    if len(res) == 1:
        return res[0][0]
    return res


def det(mat):
    if type(mat) == int:
        return mat
    if len(mat) == 1:
        return mat[0]
    if len(mat) == 2:
        return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
    determinant: int = 0
    for i in range(len(mat[0])):
        determinant += (mat[0][i] * (-1) ** (2 + i)) * det(reduire(mat, 0, i))
    return determinant


def com(mat):
    """

    :rtype: list[list[int]]
    """
    res = []
    for i in range(len(mat)):
        lin = []
        for j in range(len(mat[i])):
            lin += [det(reduire(mat, i, j)) * (-1) ** (2 + i + j)]
        res += [lin]
    return res


def transpose(mat):
    """

    :rtype: list[list[int]]
    """
    res = []
    for i in range(len(mat[0])):
        lin = []
        for j in range(len(mat)):
            lin += [mat[j][i]]
        res += [lin]
    return res


def compliment(determinant, coef=29):
    """

    :rtype: int
    """
    for i in range(coef):
        if (determinant * i) % coef == 1:
            return i


def inv(mat, coef=29):
    """

    :param mat: matrice a inverse
    :type mat: list[list[int]]
    :param coef: coef de modole
    :type coef: int
    :return: inverse
    :rtype: list[list[int]]
    :raise: ArithmeticError
    """
    d = det(mat)
    if d == 0:
        raise ArithmeticError("inversion impossible")
    k = compliment(d)
    com_matrice = com(mat)
    com_matrice_t = transpose(com_matrice)
    return (
        [
            [
                (k * com_matrice_t[i][j]) % coef
                for j in range(len(com_matrice_t[i]))
            ]
            for i in range(len(com_matrice_t))
        ],
        com_matrice,
        com_matrice_t,
        k
    )


def prod(cle, mat, coef=29):
    res = []
    for i in range(len(cle)):
        lin = []
        for j in range(len(mat[i])):
            x = 0
            for k in range(len(cle[i])):
                x += cle[i][k] * mat[k][j]
            lin += [x % coef]
        res += [lin]
    return res
