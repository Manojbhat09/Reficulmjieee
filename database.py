from sqlalchemy.orm import sessionmaker,scoped_session,mapper,relationship
from sqlalchemy import MetaData,create_engine
from sqlalchemy.ext.declarative import declarative_base
from app import app
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'],echo=True,convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,autoflush=False))
db_session.configure(bind=engine)
metadata = MetaData(bind=engine)
from app.models import Question,Answer,base
def init_db():
	base.metadata.drop_all(bind=engine,checkfirst=True)
	base.metadata.create_all(bind=engine)