from flask import Blueprint, render_template, redirect, url_for, request, session
from app.usuario.validacao import validar_login

usuario = Blueprint('usuario', __name__)


@usuario.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')


@usuario.route('/login', methods=['POST'])
def login():
    email = request.form.get('email', '')
    senha = request.form.get('senha', '')

    dados, erro = validar_login(email, senha)

    if erro:
        # Mostra a página de novo, com o modal aberto e a mensagem de erro
        return render_template('index.html', erro_login=erro,
                               email_digitado=email, abrir_modal=True)

    session['usuario_nome'] = dados['nome']
    session['usuario_email'] = dados['email']
    return redirect(url_for('main.index'))