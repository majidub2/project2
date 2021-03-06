from flask import Flask
from os import getenv
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://root:{getenv('MYSQL_ROOT_PASSWORD')}@db:3306/prizes_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from application import routes

  