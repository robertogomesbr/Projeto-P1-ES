import csv
import os


def ler_csv(arquivo):
    if not os.path.exists(arquivo):
        return []

    with open(arquivo, 'r', newline='', encoding='utf-8') as arquivo_csv:
        leitor = csv.DictReader(arquivo_csv)
        return list(leitor)


def escrever_csv(arquivo, colunas, dados):
    pasta = os.path.dirname(arquivo)

    if pasta:
        os.makedirs(pasta, exist_ok=True)

    with open(arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
        escritor = csv.DictWriter(arquivo_csv, fieldnames=colunas)

        escritor.writeheader()
        escritor.writerows(dados)


def adicionar_linha(arquivo, colunas, linha):
    pasta = os.path.dirname(arquivo)

    if pasta:
        os.makedirs(pasta, exist_ok=True)

    precisa_cabecalho = (
        not os.path.exists(arquivo)
        or os.path.getsize(arquivo) == 0
    )

    with open(arquivo, 'a', newline='', encoding='utf-8') as arquivo_csv:
        escritor = csv.DictWriter(arquivo_csv, fieldnames=colunas)

        if precisa_cabecalho:
            escritor.writeheader()

        escritor.writerow(linha)


def gerar_id(arquivo):
    dados = ler_csv(arquivo)

    ids = [
        int(linha['id'])
        for linha in dados
        if linha.get('id', '').isdigit()
    ]

    return str(max(ids, default=0) + 1)