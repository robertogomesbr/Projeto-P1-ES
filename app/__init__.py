from flask import Flask

def cria_app():
    
    app = Flask(__name__)
    
    from app.main.routes import main
    
    app.register_blueprint(main)
    
    return app