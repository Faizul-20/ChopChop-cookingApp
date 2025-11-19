from flask import Flask

### Import Module
from app.routes import main

def create_app():
    
    app = Flask(__name__)
    
    app.register_blueprint(main)
    
    return app
