from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config.from_object('config')
db = SQLAlchemy(app)

# from config import SQLALCHEMY_DATABASE_URI
# # print SQLALCHEMY_DATABASE_URI
# from config import BASE_INFO_FILE

# from config import BASE_DIR



from app import views,models
