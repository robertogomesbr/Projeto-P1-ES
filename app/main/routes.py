from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def index():
    
    return render_template('index.html')

@main.route('/objetos')
def pg_principal():
    return render_template('pg-principal.html', objetos=[])