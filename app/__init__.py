import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv()

def cria_app():
    
    app = Flask(__name__)
    
    # Configura a chave secreta através do ambiente
    secret_key = os.environ.get('SECRET_KEY')
    
    if not secret_key:
        raise RuntimeError('A varável SECRET_KEY não foi configurada.')
    
    app.config['SECRET_KEY'] = secret_key
    
    from app.main.routes import main
    from app.usuario.routes import usuario
    
    app.register_blueprint(main)
    app.register_blueprint(usuario)
    
    return app