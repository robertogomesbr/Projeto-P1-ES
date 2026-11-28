from flask import (
    abort,
    Blueprint,
    render_template,
    redirect,
    url_for,
    request,
    session,
    flash
)

from app.usuario.auth import login_obrigatorio
from app.services.objeto_service import CATEGORIAS, criar_objeto


objeto = Blueprint('objeto', __name__)


@objeto.route('/objetos/cadastrar', methods=['GET', 'POST'])
@login_obrigatorio
def cadastrar():
    if request.method == 'POST':
        nome = request.form.get('nome', '')
        descricao = request.form.get('descricao', '')
        local = request.form.get('local', '')
        categoria = request.form.get('categoria', '')
        data = request.form.get('data', '')

        sucesso, resultado = criar_objeto(
            nome,
            descricao,
            local,
            categoria,
            data,
            session['usuario_email']
        )

        if not sucesso:
            return render_template(
                'cadastrar_objeto.html',
                categorias=CATEGORIAS,
                erro=resultado,
                form=request.form
            )

        flash('Objeto cadastrado com sucesso!', 'sucesso')
        return redirect(url_for('objeto.cadastrar'))

    return render_template(
        'cadastrar_objeto.html',
        categorias=CATEGORIAS,
        form=request.form
    )

@objeto.route('/detalhes-objeto/<int:id>')
def detalhes(id):
    objeto = listar_objeto_id(id)
    
    if objeto is None:
        abort(404)
    
    return render_template('detalhes_objeto.html', objeto=objeto)