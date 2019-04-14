from flask import Flask
from .config import app_config
from .models import bcrypt, db
from .models import user
from .views.user_view import user_api
import os
def create_app(env_name):
    '''
    Create Application
    '''
    app = Flask(__name__)
    config_name = os.getenv('FLASK_ENV')
    app.config.from_object(app_config[config_name])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.register_blueprint(user_api, url_prefix='/api/v1/users')
    bcrypt.init_app(app)
    db.init_app(app)
    @app.route('/')
    def index():
        return 'This is the index route'

    return app