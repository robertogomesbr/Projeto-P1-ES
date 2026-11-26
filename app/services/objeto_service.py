from datetime import date
from pathlib import Path

from app.services.csv_service import ler_csv, adicionar_linha, gerar_id


PASTA_PROJETO = Path(__file__).resolve().parents[2]
ARQUIVO_OBJETOS = str(PASTA_PROJETO / 'data' / 'objetos.csv')

COLUNAS_OBJETOS = [
    'id', 'nome', 'descricao', 'local',
    'categoria', 'data', 'cadastrado_por'
]

CATEGORIAS = [
    'Documentos', 'Eletrônicos', 'Roupas e acessórios',
    'Material escolar', 'Chaves', 'Outros'
]


def validar_nome(nome):
    nome = nome.strip()
    return 3 <= len(nome) <= 50


def validar_local(local):
    local = local.strip()
    return 3 <= len(local) <= 60


def validar_descricao(descricao):
    return len(descricao.strip()) <= 200


def validar_categoria(categoria):
    return categoria in CATEGORIAS


def validar_data(data):
    # O campo type="date" envia no formato AAAA-MM-DD
    try:
        data_objeto = date.fromisoformat(data)
    except ValueError:
        return False

    return data_objeto <= date.today()


def listar_objetos():
    return ler_csv(ARQUIVO_OBJETOS)


def criar_objeto(nome, descricao, local, categoria, data, cadastrado_por):
    if not validar_nome(nome):
        return False, 'O nome deve ter entre 3 e 50 caracteres.'
    elif not validar_local(local):
        return False, 'O local deve ter entre 3 e 60 caracteres.'
    elif not validar_categoria(categoria):
        return False, 'Escolha uma categoria válida.'
    elif not validar_data(data):
        return False, 'Informe uma data válida, que não seja no futuro.'
    elif not validar_descricao(descricao):
        return False, 'A descrição pode ter no máximo 200 caracteres.'

    novo_objeto = {
        'id': gerar_id(ARQUIVO_OBJETOS),
        'nome': nome.strip(),
        'descricao': descricao.strip(),
        'local': local.strip(),
        'categoria': categoria,
        'data': data,
        'cadastrado_por': cadastrado_por
    }

    adicionar_linha(ARQUIVO_OBJETOS, COLUNAS_OBJETOS, novo_objeto)

    return True, novo_objeto