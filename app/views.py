from flask import render_template,redirect,flash,request,jsonify,session
import random
from flask_admin.contrib.sqla import ModelView
from  sqlalchemy.sql.expression import func
from app import admin
from app import app,User,Answer,Question,db_session
admin.add_view(ModelView(Answer, db_session))
admin.add_view(ModelView(Question, db_session))
@app.errorhandler("404")
def error404():
	return "<h1>Page Not Found</h1>"
@app.teardown_appcontext
def close_db(exception):
	print("Closing DB")
	db_session.close()
@app.route("/questionmaker",methods=['GET','POST'])
def questionmaker():
	if (session['level'] == 2):
		q={}
		q = Question.query.filter(Question.level == session['level']).order_by(func.random()).first()
		some={}
		a = Answer.query.filter(Answer.q_id == q.q_id).all()
		ans=[]
		for i in a:
			ans.append(i.answer)
		some['q_id'] = q.q_id
		some['ques'] = q.question
		some['ans'] = ans
		session['marks'] = q.marks
		return render_template("round2.html",obj=some)
	elif(session['level'] == 1):
		q={}
		q = Question.query.filter(Question.level == session['level']).order_by(func.random()).first()
		some={}
		some['q_id'] = q.q_id
		some['ques'] = q.question
		session['marks'] = q.marks
		return render_template("round1.html",obj=some)
	elif(session.get('level') == None):
		return redirect("/")
@app.route("/login",methods=['GET','POST'])
def login():
	if 'username' in session and session['username']!=None:
		return redirect("/")
	else:
		error=""
		if request.method == "POST":
			email = request.form['email']
			password = request.form['password']
			u = User.query.filter(User.email == email).first()
			if u:
				if u.check_pass(password):
					session['level'] = u.level
					session['username'] = u.username
					return redirect("/")
				else:
					error = "Wrong Username or Password"
				return render_template("login.html",error=error)
			else:
				error="Wrong Username or Password"
		return render_template("login.html",error=error)

@app.route("/register",methods=['GET','POST'])
def register():
	if session.get('username') ==None:
		error=""
		if request.method == "POST":
			username = request.form['username']
			password = request.form['password']
			email = request.form['email']
			users = User.query.filter(User.username == username and User.email == email).count()
			if users > 0 :
				error = "User already exists"
			else:	
				u = User(username,password,email)
				db_session.add(u)
				db_session.commit()
				error = "Successfully registered user"
		return render_template("register.html")
	else:
		return redirect("/")

@app.route("/logout",methods=['GET','POST'])
def logout():
	if 'username' in session:
		session.pop('username')
		session.pop('level')
	return redirect("/login")

@app.route("/",methods=['GET','POST'])
def index():
	if session.get('username') == None:
		return redirect("/login")
	if session['level'] == 1:
		return render_template("index.html")
	elif session['level'] ==2:
		return render_template("index1.html")

@app.route("/post",methods=['GET','POST'])
def checkr():
	if request.method == "POST":
		if (session['level']==2):
			print request.form['answer']
			ans = Answer.query.filter(Answer.answer == request.form['answer'].replace("_"," ",10) and Answer.q_id == request.form['q_id']).first()
			print ans.is_correct
			if ans.is_correct:
				user = User.query.filter(User.username == session['username']).first()
				user.q_solved = user.q_solved+1
				session['q_solved']=user.q_solved
				user.marks  =user.marks+ session['marks']
				session.pop('marks')
				db_session.add(user)
				db_session.commit()
				return jsonify(color="green")
			else:
				session.pop('marks')
				return jsonify(color="red")
		elif(session['level']==1):
			ans = Answer.query.filter(Answer.answer == request.form['answer'] and Answer.q_id == request.form['q_id']).first()
			if ans.is_correct:
				user = User.query.filter(User.username == session['username']).first()
				user.q_solved = user.q_solved+1
				session['q_solved']=user.q_solved
				user.marks  =user.marks+ session['marks']
				if user.marks > 15:
					user.level=user.level+1
					session['level'] = user.level
				session.pop('marks')
				db_session.add(user)
				db_session.commit()
				return jsonify(color="green")
			else:
				session.pop('marks')
				return jsonify(color="red")			
# @app.route("/question",methods=['GET','POST'])
# def question():
# 	if request.method == "POST":
# 		q = Question(request.form['question'],request.form['marks'],request.form['level'])
# 		db_session.add(q)
# 		db_session.commit()
# 		return q.q_id

# @app.route("/user",methods=['GET','POST'])
# def user():
# 	if request.method == "POST":
# 		u = User(request.form['username'])
# 		db_session.add(u)
# 		db_session.commit()
# @app.route("/answer",methods=['GET','POST'])
# def answer():
# 	if request.method == "POST":
# 		ans = Answer(request.form['answer'],request.form['q_id'],True if request.form['is_correct'] == "True" else False)
# 		db_session.add(ans)
# 		db_session.commit()