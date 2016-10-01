from sqlalchemy import Column, Integer, Boolean,String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from random import choice
from app import db_session
base=declarative_base()
class Question(base):
    __tablename__ = 'question'
    query = db_session.query_property()
    q_id = Column(String(16),unique = True, primary_key=True,nullable=False)
    question = Column(String(500))
    marks = Column(Integer)
    answer = relationship("Answer")

    def __init__(self, question=None,marks=None):
    	self.q_id = ''.join(choice('0123456789ABCDEF') for i in range(16))
    	self.question = question
    	self.marks = marks
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