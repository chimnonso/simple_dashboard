import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)
login_manager = LoginManager()
basedir = os.path.abspath(os.path.dirname(__file__))
secret_key = os.urandom(16)

app.config['SECRET_KEY'] = secret_key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'dashboard.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
Migrate(app,db)
login_manager.init_app(app)
login_manager.login_view = "accounts.login"
login_manager.login_message = "What are you trying to access? You better login and retry. Nonsense"
login_manager.login_message_category = 'danger'



from project.accounts.views import accounts_bp
from project.articles.views import articles_bp
app.register_blueprint(accounts_bp, url_prefix='/accounts')
app.register_blueprint(articles_bp, url_prefix='/articles')