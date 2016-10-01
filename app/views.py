from flask import render_template,redirect,flash,request
import random
from app import app,Answer,Question,db_session
def questionmaker():
	q={}
	while not isinstance(q,Question):
		rand=random.randrange(0,db_session.query(Question).count())
		q = Question.query.all()[rand]
	return q
@app.errorhandler("404")
def error404():
	return "<h1>Page Not Found</h1>"
@app.teardown_appcontext
def close_db(exception):
	print("Closing DB")
	db_session.close()
@app.route("/question",methods=['GET','POST'])
def question():
	if request.method == "POST":
		q = Question(request.form['question'],request.form['marks'])
		db_session.add(q)
		db_session.commit()
		return q.q_id

@app.route("/answer",methods=['GET','POST'])
def answer():
	if request.method == "POST":
		ans = Answer(request.form['answer'],request.form['q_id'],True if request.form['is_correct'] == "True" else False)
		db_session.add(ans)
		db_session.commit()

@app.route("/",methods=['GET','POST'])
def index():
	some={}
	q = questionmaker()
	a = Answer.query.filter(Answer.q_id == q.q_id).all()
	ans=[]
	for i in a:
		ans.append(i.answer)
	some['q_id'] = q.q_id
	some['ques'] = q.question
	some['ans'] = ans
	return render_template("index.html",obj = some)

@app.route("/post",methods=['GET','POST'])
def checkr():
	if request.method == "POST":
		ans = Answer.query.filter(Answer.answer == request.form['Answer'].replace("_"," ",10) and Answer.q_id == request.form['Question']).first()
		if ans.is_correct:
			flash("Correct")
			return redirect("/")
		else:
			flash("Incorrect")
			return redirect("/")
		return redirect("/")
	else:
		return redirect("/")