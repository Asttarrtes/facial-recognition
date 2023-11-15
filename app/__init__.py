from flask import Flask

def create_app():
    app = Flask(__name__)

    from app import routes
    # Puedes agregar más configuraciones aquí si es necesario

    return app