from functools import wraps
from flask import session, redirect, url_for


def usuario_logado():
    return "usuario_email" in session


def login_obrigatorio(funcao):
    """Protege uma rota: quem não fez login volta para a página inicial."""
    @wraps(funcao)
    def verificar(*args, **kwargs):
        if not usuario_logado():
            return redirect(url_for("main.index"))
        return funcao(*args, **kwargs)
    return verificar