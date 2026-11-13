import csv
import os
from werkzeug.security import check_password_hash

PASTA_RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CAMINHO_CSV = os.path.join(PASTA_RAIZ, "data", "usuarios.csv")


def ler_usuarios():
    usuarios = []
    if not os.path.exists(CAMINHO_CSV):
        return usuarios
    with open(CAMINHO_CSV, newline="", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            usuarios.append(linha)
    return usuarios


def validar_login(email, senha):
    """Devolve (usuario, None) se der certo, ou (None, mensagem) se der erro."""
    email = email.strip().lower()

    if email == "" or senha == "":
        return None, "Preencha o e-mail e a senha."
    elif "@" not in email:
        return None, "Digite um e-mail válido."

    for usuario in ler_usuarios():
        if usuario["email"].strip().lower() == email:
            if check_password_hash(usuario["senha"], senha):
                return usuario, None
            return None, "Senha incorreta."

    return None, "E-mail não cadastrado."