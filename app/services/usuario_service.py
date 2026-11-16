from pathlib import Path
from werkzeug.security import generate_password_hash, check_password_hash

from app.services.csv_service import (
    ler_csv,
    adicionar_linha,
    gerar_id
)


PASTA_PROJETO = Path(__file__).resolve().parents[2]
ARQUIVO_USUARIOS = str(PASTA_PROJETO / 'data' / 'usuarios.csv')

COLUNAS_USUARIOS = ['id', 'nome', 'email', 'senha_hash']


def validar_nome(nome):
    nome = nome.strip()
    return 3 <= len(nome) <= 20


def validar_email(email):
    email = email.strip()

    return (
        '@' in email
        and '.' in email.split('@')[-1]
        and ' ' not in email
    )


def validar_senha(senha):
    if len(senha) < 6:
        return False

    qtd_num_senha = 0
    qtd_maius_senha = 0
    qtd_minus_senha = 0

    for simbolo in senha:
        if simbolo.isdigit():
            qtd_num_senha += 1
        elif simbolo.isupper():
            qtd_maius_senha += 1
        elif simbolo.islower():
            qtd_minus_senha += 1

    return (
        qtd_num_senha >= 1
        and qtd_maius_senha >= 1
        and qtd_minus_senha >= 1
    )


def criar_usuario(nome, email, senha):
    nome = nome.strip()
    email = email.strip().casefold()

    usuarios = ler_csv(ARQUIVO_USUARIOS)

    for usuario in usuarios:
        if usuario['email'].strip().casefold() == email:
            return False, 'Este e-mail já está cadastrado.'

    senha_hash = generate_password_hash(senha)

    novo_usuario = {
        'id': gerar_id(ARQUIVO_USUARIOS),
        'nome': nome,
        'email': email,
        'senha_hash': senha_hash
    }

    adicionar_linha(
        ARQUIVO_USUARIOS,
        COLUNAS_USUARIOS,
        novo_usuario
    )

    return True, novo_usuario


def validar_login(email, senha):
    email = email.strip().casefold()

    if email == '' or senha == '':
        return None, 'Preencha o e-mail e a senha.'

    usuarios = ler_csv(ARQUIVO_USUARIOS)

    for usuario in usuarios:
        if usuario['email'].strip().casefold() == email:
            if check_password_hash(usuario['senha_hash'], senha):
                return usuario, None

            return None, 'Senha incorreta.'

    return None, 'E-mail não cadastrado.'