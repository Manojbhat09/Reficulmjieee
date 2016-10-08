from sqlalchemy import Column, Integer, Boolean,String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from werkzeug.security import generate_password_hash,check_password_hash
from sqlalchemy.orm import relationship
from random import choice
from app import db_session
base=declarative_base()
class User(base):
	__tablename__ = 'user'
	query=db_session.query_property()
	id = Column(Integer(10),primary_key=True,nullable=False,unique=True)
	username = Column(String(128),nullable=False)
	password = Column(String(128),nullable=False)
	email = Column(String(256),nullable=False,unique=True)
	level = Column(Integer(2))
	marks = Column(Integer(5))

	def __init__(self,username=None,password=None,email=None):
		self.id = ''.join(choice('0123456789') for i in range(10))
		self.username = username
		self.salt_pass(password)
		self.email = email
		self.level = 1
		self.marks = 0
		self.q_solved = 0
	def salt_pass(self,password):
		self.password = generate_password_hash(password)
	def check_pass(self,password):
		return check_password_hash(self.password, password)
	def __repr__(self):
		return "<User(Username:%s)>"%(self.username)

class Question(base):
    __tablename__ = 'question'
    query = db_session.query_property()
    q_id = Column(String(16),unique = True, primary_key=True,nullable=False)
    question = Column(String(500))
    marks = Column(Integer(5))
    level = Column(Integer(2))
    answer = relationship("Answer")

    def __init__(self, question=None,marks=None,level = None):
    	self.q_id = ''.join(choice('0123456789ABCDEF') for i in range(16))
    	self.question = question
    	self.marks = marks
    	self.level = level
    def __repr__(self):
       return "<Question(question='%s')>" % (self.question)


class Answer(base):
	__tablename__ = 'answer'
	query = db_session.query_property()
	a_id=Column(String(16),unique=True,primary_key=True,nullable=False)
	q_id = Column(String(16),ForeignKey('question.q_id'))
	answer = Column(String(500))
	is_correct = Column(Boolean)

	def __init__(self,answer=None,q_id=None,is_correct=None):
		self.a_id = ''.join(choice('0123456789ABCDEF') for i in range(16))
		self.answer = answer
		self.is_correct=is_correct
		self.q_id = q_id
	def __repr__(self):
		return "<Answer(answer='%s')>" % (self.answer)