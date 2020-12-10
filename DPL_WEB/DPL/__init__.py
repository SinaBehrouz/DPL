import os
import secrets
import stripe
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

secret_key = secrets.token_hex(16)

app = Flask(__name__)
mail = Mail(app)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = "parcelsolution440@gmail.com"
app.config['MAIL_PASSWORD'] = "parcel440"
mail = Mail(app)

stripe_keys = {
  'secret_key': "pk_test_51HAlzwJxCod5ibwz1qoTHZ6sNfXWBsKtjFwLgxsc0U5UUZmMUMmz8MsUM8ksbA8n57qVLLHlJKd4McTTh3fU4FLP00FnJrzKTr",
  'publishable_key': "sk_test_51HAlzwJxCod5ibwzuOmzGJwQ4AjYksOWNCVqlC9fLAvU2v0WuVm6Rv6Yxf0G2oMGFSqniqZ7ElblIq243kMbcO1l00TrMS8g62"
}
stripe.api_key = stripe_keys['secret_key']

from DPL import routes
