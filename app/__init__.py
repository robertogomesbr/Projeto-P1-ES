from flask import Flask

def cria_app():
    
    app = Flask(__name__)
    app.secret_key = "chave-de-desenvolvimento"   # <- nova
    
    from app.main.routes import main
    from app.usuario.routes import usuario
    
    app.register_blueprint(main)
    app.register_blueprint(usuario)
    
    return app