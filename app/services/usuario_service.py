def validar_nome(nome):
    # Verifica tamanho do nome
    return len(nome) >= 3 and len(nome) <= 20

def validar_email(email):
    # Verifica se contém @ no email
    return '@' in email

def validar_senha(senha):
    # Verifica tamanho e composição da senha
    if len(senha) >= 6:
        
        qtd_num_senha = 0
        qtd_maius_senha = 0
        qtd_minus_senha = 0
                
        for simbolo in senha:
            if simbolo >= '0' and simbolo <= '9':
                qtd_num_senha += 1
            elif simbolo >= 'A' and simbolo <= 'Z':
                qtd_maius_senha += 1
            elif simbolo >= 'a' and simbolo <= 'z':
                qtd_minus_senha += 1
                
        if qtd_num_senha < 1:
            return False
        if qtd_maius_senha < 1:
            return False
        if qtd_minus_senha < 1:
            return False
        
        return True
    else:
        return False