from pathlib import Path
from werkzeug.security import generate_password_hash
from app.services.csv_service import (
    ler_csv,
    adicionar_linha,
    gerar_id
)

# Caminho do arquivo de usuários
PASTA_PROJETO = Path(__file__).resolve().parents[2]
ARQUIVO_USUARIOS = str(PASTA_PROJETO / 'data' / 'usuarios.csv')

COLUNAS_USUARIOS = ['id', 'nome', 'email', 'senha_hash']

def validar_nome(nome):
    # Verifica tamanho do nome
    return len(nome) >= 3 and len(nome) <= 20

def validar_email(email):
    # Verifica se contém @ no email
    return '@' in email

def validar_senha(senha):
    # Verifica tamanho e composição da senha
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

    if qtd_num_senha < 1:
        return False

    if qtd_maius_senha < 1:
        return False

    if qtd_minus_senha < 1:
        return False

    return True

def criar_usuario(nome, email, senha):
    # Normaliza os dados recebidos
    nome = nome.strip()
    email = email.strip().casefold()

    # Lê os usuários já cadastrados
    usuarios = ler_csv(ARQUIVO_USUARIOS)

    # Verifica se o email já está cadastrado
    for usuario in usuarios:
        if usuario['email'].strip().casefold() == email:
            return False, 'Este email já está cadastrado.'

    # Gera o hash da senha
    senha_hash = generate_password_hash(senha)

    # Monta os dados do novo usuário
    novo_usuario = {
        'id': gerar_id(ARQUIVO_USUARIOS),
        'nome': nome,
        'email': email,
        'senha_hash': senha_hash
    }

    # Armazena o usuário no CSV
    adicionar_linha(
        ARQUIVO_USUARIOS,
        COLUNAS_USUARIOS,
        novo_usuario
    )

    return True, novo_usuario
