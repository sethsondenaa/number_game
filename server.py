from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "janjasdlfnalsjdnflkoaowpe5joi"
import random

@app.route("/")
def index():
	if "answer" not in session:
		session["count"] = 0
		session["answer"] = random.randrange(0, 101)
		session["guess"] = ""
	return render_template("index.html")

@app.route("/pick", methods=["POST"])
def pick():
	session["guess"] = int(request.form["guess"])
	session["count"] += 1;
	return redirect("/")

@app.route("/reset")
def reset():
	session.pop("answer")
	session.pop("guess")
	session.pop("count")
	return redirect("/")


app.run(debug=True)