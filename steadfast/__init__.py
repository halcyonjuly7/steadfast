
### Standard Library Imports ###
import os
################################

### 3rd Party Imports ###
from flask import Flask
from flask_mail import Mail
from flask.ext.pymongo import PyMongo
from flask.ext.bootstrap import Bootstrap
from flask.ext.login import LoginManager
#################################

### Local Imports ###

#################################


bootstrap = Bootstrap()
mail = Mail()
mongo = PyMongo()
lm = LoginManager()
lm.login_view = "/"


def create_app(config_name):
    app = Flask(__name__)
    cfg = os.path.join(os.getcwd(), "config", config_name + ".py")
    app.config.from_pyfile(cfg)
    bootstrap.init_app(app)
    mail.init_app(app)
    mongo.init_app(app)
    lm.init_app(app)
    from .apps.services import services
    from .apps.main import main
    from .apps.careers import careers
    app.register_blueprint(services, url_prefix='/services')
    app.register_blueprint(main)
    app.register_blueprint(careers, url_prefix = '/careers')
    return app