from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    request,
    session,
    flash
)

from app.services.usuario_service import (
    validar_nome,
    validar_email,
    validar_senha,
    criar_usuario,
    validar_login
)


usuario = Blueprint('usuario', __name__)


@usuario.route('/cadastro', methods=['POST'])
def cadastro():
    nome = request.form.get('nome', '')
    email = request.form.get('email', '')
    senha = request.form.get('senha', '')
    confirmar_senha = request.form.get('confirmar_senha', '')
    
    nome = request.form.get('nome', '')
    email = request.form.get('email', '')
    senha = request.form.get('senha', '')
    confirmar_senha = request.form.get('confirmar_senha', '')

    print('NOME:', nome)
    print('EMAIL:', email)
    print('SENHA PREENCHIDA:', bool(senha))
    print('CONFIRMAÇÃO PREENCHIDA:', bool(confirmar_senha))

    erros = []

    if not validar_nome(nome):
        erros.append('O nome deve ter no mínimo 3 e no máximo 20 caracteres.')

    if not validar_email(email):
        erros.append('Digite um e-mail válido.')

    if not validar_senha(senha):
        erros.append(
            'A senha deve ter no mínimo 6 caracteres, '
            '1 número, 1 letra maiúscula e 1 letra minúscula.'
        )

    if senha != confirmar_senha:
        erros.append('A senha e a confirmação de senha devem ser iguais.')

    if erros:
        print('ERROS DE VALIDAÇÃO:', erros)
        for erro in erros:
            flash(erro, 'cadastro')

        return redirect(url_for('main.index'))

    sucesso, resultado = criar_usuario(nome, email, senha)

    if not sucesso:
        flash(resultado, 'cadastro')
        return redirect(url_for('main.index'))

    session['usuario_id'] = resultado['id']
    session['usuario_nome'] = resultado['nome']
    session['usuario_email'] = resultado['email']

    flash('Conta criada com sucesso!', 'sucesso')

    return redirect(url_for('main.index'))


@usuario.route('/login', methods=['POST'])
def login():
    email = request.form.get('email', '')
    senha = request.form.get('senha', '')

    dados, erro = validar_login(email, senha)

    if erro:
        return render_template(
            'index.html',
            erro_login=erro,
            email_digitado=email,
            abrir_modal=True
        )

    session['usuario_id'] = dados['id']
    session['usuario_nome'] = dados['nome']
    session['usuario_email'] = dados['email']

    return redirect(url_for('main.index'))


@usuario.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('main.index'))