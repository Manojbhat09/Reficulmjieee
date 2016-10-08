from flask import Flask
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,scoped_session
app = Flask(__name__,instance_relative_config=True)
app.config.from_pyfile("config.py")
admin = Admin(app, name='IEEE Portal', template_mode='bootstrap3')
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'],echo=True)
db_session = scoped_session(sessionmaker(autocommit=False,autoflush=False))
db_session.configure(bind=engine)
from models import Answer,Question,User
from app import views