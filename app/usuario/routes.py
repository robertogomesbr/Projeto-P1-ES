from flask import Blueprint, render_template, redirect, url_for

usuario = Blueprint('usuario', __name__)

@usuario.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@usuario.route('/login', methods=['POST'])
def login():
    return redirect(url_for('main.index'))