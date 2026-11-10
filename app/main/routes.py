from flask import Blueprint, flash, request, redirect, url_for, render_template

main = Blueprint('main', __name__)

@main.route('/')
def index():
    
    return render_template('index.html')

@main.route('/cadastro', methods=['POST'])
def cadastro():
    nome = request.form.get('nome')
    email = request.form.get('email')
    senha = request.form.get('senha')
    
    erros = []
    
    # Aqui vai entrar as chamadas de validação
    # Armazenar dos dados em csv
    
    flash('Conta criada com sucesso!', 'sucesso')
    
    return redirect(url_for('main.index'))