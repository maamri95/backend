import json

from api_vigenere_hill.vigenere_hill.hill import inv
from .vigenere_hill import VigenereHill

from flask import Flask, request

app = Flask(__name__)
app.config.from_object('config')


@app.route('/encrypt', methods=['POST'])
def encrypt():
    """
    returne le msg intermidaire et chiffre
    """
    try:
        vigenere_hill = parametre(request)
    except ArithmeticError:
        return render("matrice impossible a inverse", 404)
    text_clair = request.json.get("text_clair")
    text_interm, text_crypt = vigenere_hill.crypt(text_clair)
    return render(
        {
            "text_interm": text_interm,
            "text_crypt": text_crypt,
        },
        200
    )


@app.route('/decrypt', methods=['POST'])
def decrypt():
    """
    returne le msg intermidaire et claire et l'inverse,
    k, comatrice et la transpose de la comatrice
    :return: http response
    """
    try:
        vigenere_hill = parametre(request)
    except ArithmeticError:
        return render("matrice impossible a inverse", 404)
    text_crypt = request.json.get("text_crypt")
    text_interm, text_clair = vigenere_hill.decrypt(text_crypt)
    return render(
        {
            "text_interm": text_interm,
            "text_clair": text_clair,
            "inverse": vigenere_hill.hill.tinv,
            "k": vigenere_hill.hill.k,
            "com": vigenere_hill.hill.comMatrice,
            "com_t": vigenere_hill.hill.comMatriceT
        },
        200
    )


@app.route("/inversible", methods=["POST"])
def inversible():
    """
    returne 200 si la matrice est inversible sinon 404
    :return:
    """
    cleHill = request.json.get("cleHill")
    try:
        inv(cleHill)
        render("cette matrice a un inverse", 200)
    except ArithmeticError:
        return render("impossible d'inverse cette matrice", 404)


def render(context, status, mimetype="application/json"):
    """
    perime de render de json
    :param context: contexte a serialize
    :param status: statute a rendre
    :param mimetype: header
    :return: http  response
    """
    return app.response_class(
        response=json.dumps(context),
        status=status,
        mimetype=mimetype
    )


def parametre(requestparam):
    """
    recupre les cles dechifferement
    :param requestparam:
    :return:
    """
    cleHill: list = requestparam.json.get("cleHill")
    cleVigenere: str = requestparam.json.get("cleVigenere")
    for c in cleVigenere:
        if not c.isalpha():
            return render("erreur cle de vigenere incorrecte elle dois etre alphabetique", 404)
    for line in cleHill:
        for num in line:
            if not isinstance(num, int):
                return render("la matrice dois contenir des entier", 404)
    return VigenereHill(cleHill, cleVigenere)
