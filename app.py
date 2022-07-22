from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "HOLLAsasds"
# https://www.youtube.com/watch?v=CHRikEvvcUc&t=50s
Mydata = [
	("What", "Cuál"),
	("is", "es"),
	("your", "tu"),
	("name?", "nombre?")
]
answers = [
	("Cómo estás?"),
	("De dónde eres?"),
	("Cuál es tu nombre?")
]


@app.route("/hello")
def index():
	#flash("What's your name?")
	return render_template("index.html")
@app.route("/greet", methods=['POST', 'GET'])
def greeter():
	flash("Hi " + str(request.form['name_input']) + ", great to see you!")
	return render_template("index.html")

# https://entrellaves.com/javascript/cambiar-css-con-javascript/
@app.route("/test")
def transactions():
    return render_template("test.html", data=Mydata , respuestas = answers)

@app.route("/test2")
def lolo():
    return render_template("test2.html")

@app.route("/test3")
def test3():
    return render_template("test3.html" , data=Mydata )