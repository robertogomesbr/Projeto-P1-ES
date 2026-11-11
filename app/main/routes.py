from flask import Blueprint, flash, request, redirect, url_for, render_template
from app.services.usuario_service import *

main = Blueprint('main', __name__)

@main.route('/')
def index():
    
    return render_template('index.html')

@main.route('/cadastro', methods=['POST'])
def cadastro():
    nome = request.form.get('nome', '')
    email = request.form.get('email', '')
    senha = request.form.get('senha', '')
    confirma_senha = request.form.get('confirma_senha', '')
    
    erros = []
    
    if not validar_nome(nome):
        erros.append('O nome deve ter no mínimo 3 e no máximo 20 caracteres.')
        
    if not validar_email(email):
        erros.append('O email deve conter @ para ser válido.')
        
    if not validar_senha(senha):
        erros.append('A senha deve ter no mínimo 6 caracteres, 1 número, 1 letra maiúscula e 1 letra minúscula.')
    
    if senha != confirma_senha:
        erros.append('A senha e a confirmação de senha devem ser iguais.')
        
    if erros:
        for erro in erros:
            flash(erro, 'cadastro')
        return redirect(url_for('main.index'))
    else:
        
        # Armazenar dos dados em csv
        flash('Conta criada com sucesso!', 'sucesso')
    
    return redirect(url_for('main.index'))