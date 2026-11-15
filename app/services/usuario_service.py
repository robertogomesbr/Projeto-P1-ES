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