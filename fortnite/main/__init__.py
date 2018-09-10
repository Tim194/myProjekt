from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config["SECRET_KEY"] = "rqmbPdMMcIndTLsjmfUZNFX3jNk77UQIRM3ML4g6qLTiMZsuShz89KoF4Pzlj1kEpLiKtIo4kfgi"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
Login_Manager = LoginManager(app)

from main import routes