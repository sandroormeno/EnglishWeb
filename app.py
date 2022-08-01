from flask import Flask, render_template, request, flash
from mydata import Myquestions, bigData, answers_test2, answers, Mydata
from mydata2 import questions2, qtwo
import random
import copy

app = Flask(__name__)
app.secret_key = "HOLLAsasds"
global contador
contador = 0
# https://www.youtube.com/watch?v=CHRikEvvcUc&t=50s

@app.route("/hello")
def index():
	#flash("What's your name?")
	return render_template("index.html")
@app.route("/greet", methods=['POST', 'GET'])
def greeter():
	print(str(request.form['name_input']))
	flash("Hi " + str(request.form['name_input']) + ", great to see you!")
	return render_template("index.html")

# https://entrellaves.com/javascript/cambiar-css-con-javascript/
@app.route("/test")
def transactions():
    return render_template("test.html", data=Mydata , respuestas = answers)

@app.route("/test2")
def lolo():
    return render_template("test2.html")

qthree = [
	[ # 1 entrada
	[ #   https://ttsmp3.com/ 
	("Renzo", "Rénzo", "/static/audio/words/renzo.mp3"), # botones para elegir
	("do", "", "/static/audio/words/do.mp3"),
	("not", "no", "/static/audio/words/not.mp3"),
	("need", "necesita", "/static/audio/words/need.mp3"),
	("a", "un", "/static/audio/words/a.mp3"),
	("lot", "mucho", "/static/audio/words/lot.mp3"),
	("of", "de", "/static/audio/words/of.mp3"),
	("money", "dinero", "/static/audio/words/money.mp3"),

	],[
	("Renzo", "Rénzo"), # No estoy usando x ahora
	("do not", "no"),
	("need", "necesita"),
	("a lot of", "mucho"),
	("money", "dinero"),
	],[
	"renzo do not need a lot of money" # opciones de respuesta
	],[
	("audio", "/static/audio/renzo_do_not_need_alotof_money.mp3"), # audio normal
	("audioSlow", "/static/audio/renzo__do__not__need__alotof__money.mp3") #audio lento
	# pregunta en español,  num respuesta correcta , nivel de avance , imegen de ilustración
	# https://materializecss.com/icons.html
	# https://www.svgrepo.com/
	],["Rénzo no necesita mucho dinero", 15, "/static/images/bar_2.svg", "https://www.svgrepo.com/show/125433/student.svg"]
	],[ # 2 entrada
	[ #   https://ttsmp3.com/ 
	("What", "Cuál", "/static/audio/words/what.mp3"), # botones para elegir
	("is", "es", "/static/audio/words/is.mp3"),
	("your", "tu", "/static/audio/words/your.mp3"),
	("name?", "nombre?", "/static/audio/words/name.mp3"),
	],[
	("What", "Cuál"), # No estoy usando x ahora
	("is", "es"),
	("your", "tu"),
	("name?", "nombre?"),
	],[
	"What is your name?" # opciones de respuesta
	],[
	("audio", "/static/audio/renzo_do_not_need_alotof_money.mp3"), # audio normal
	("audioSlow", "/static/audio/renzo__do__not__need__alotof__money.mp3") #audio lento
	# pregunta en español,  num respuesta correcta , nivel de avance , imegen de ilustración
	# https://materializecss.com/icons.html
	# https://www.svgrepo.com/
	],["Cuál es tu nombre?", 15, "/static/images/bar_4.svg", "https://www.svgrepo.com/show/230766/customer-service-question.svg"]
	],
	[ # 3 entrada
	[ #   https://ttsmp3.com/ 
	("Where", "Dónde", "/static/audio/words/where.mp3"), # botones para elegir
	("are", "eres", "/static/audio/words/are.mp3"),
	("you", "tú", "/static/audio/words/You.mp3"),
	("from?", "de?", "/static/audio/words/from.mp3"),
	],[
	("Where...from?", "De dónde"), # No estoy usando x ahora
	("are you", "eres?"),

	],[
	"Where are you from?" # opciones de respuesta
	],[
	("audio", "/static/audio/renzo_do_not_need_alotof_money.mp3"), # audio normal
	("audioSlow", "/static/audio/renzo__do__not__need__alotof__money.mp3") #audio lento
	# pregunta en español,  num respuesta correcta , nivel de avance , imegen de ilustración
	# https://materializecss.com/icons.html
	# https://www.svgrepo.com/
	],["De dónde eres?", 15, "/static/images/bar_6.svg", "https://www.svgrepo.com/show/230783/world.svg"]
	],[ # 4 entrada
	[ #   https://ttsmp3.com/ 
	("I", "Yo", "/static/audio/words/I.mp3"), # botones para elegir
	("want", "quero", "/static/audio/words/want.mp3"),
	("an", "una", "/static/audio/words/an.mp3"),
	("orange", "naranja", "/static/audio/words/orange.mp3"),
	("jacket", "chaqueta", "/static/audio/words/jacket.mp3"),
	],[
	("I", "Yo"), # No estoy usando x ahora
	("want", "quiero"),
	("an", "una"),
	("orange jacket", "chaqueta naranja"),
	],[
	"I want an orange jacket" # opciones de respuesta
	],[
	("audio", "/static/audio/renzo_do_not_need_alotof_money.mp3"), # audio normal
	("audioSlow", "/static/audio/renzo__do__not__need__alotof__money.mp3") #audio lento
	# pregunta en español,  num respuesta correcta , nivel de avance , imegen de ilustración
	# https://materializecss.com/icons.html
	# https://www.svgrepo.com/
	],["De dónde eres?", 15, "/static/images/bar_8.svg", "https://www.svgrepo.com/show/131688/jacket.svg"]
	],
	[ # 5 entrada
	[ #   https://ttsmp3.com/ 
	("Renzo", "Rénzo", "/static/audio/words/renzo.mp3"), # botones para elegir
	("has", "tiene", "/static/audio/words/has.mp3"),
	("a", "un", "/static/audio/words/a.mp3"),
	("small", "pequeño", "/static/audio/words/small.mp3"),
	("sandwich", "sándwich", "/static/audio/words/sandwich.mp3"),
	],[
	("Renzo", "Rénzo"), # No estoy usando x ahora
	("has", "tiene"),
	("a", "un"),
	("small snadwich", "sándwich pequeño"),
	],[
	"Renzo has a small sandwich" # opciones de respuesta
	],[
	("audio", "/static/audio/renzo_do_not_need_alotof_money.mp3"), # audio normal
	("audioSlow", "/static/audio/renzo__do__not__need__alotof__money.mp3") #audio lento
	# pregunta en español,  num respuesta correcta , nivel de avance , imegen de ilustración
	# https://materializecss.com/icons.html
	# https://www.svgrepo.com/
	],["De dónde eres?", 15, "/static/images/bar_10.svg", "https://www.svgrepo.com/show/356615/sandwich-02.svg"]
	],[ # 6 entrada
	[ #   https://ttsmp3.com/ 
	("Where", "Dónde", "/static/audio/words/where.mp3"), # botones para elegir
	("is", "está", "/static/audio/words/is.mp3"),
	("the", "el", "/static/audio/words/the.mp3"),
	("airport?", "aeropuerto?", "/static/audio/words/airport.mp3"),
	],[
	("Where", "Dónde"), # No estoy usando x ahora
	("is", "está"),
	("the", "el"),
	("airport?", "aeropuerto?"),
	],[
	"Where is the airport?" # opciones de respuesta
	],[
	("audio", "/static/audio/renzo_do_not_need_alotof_money.mp3"), # audio normal
	("audioSlow", "/static/audio/renzo__do__not__need__alotof__money.mp3") #audio lento
	# pregunta en español,  num respuesta correcta , nivel de avance , imegen de ilustración
	# https://materializecss.com/icons.html
	# https://www.svgrepo.com/
	],["De dónde eres?", 15, "/static/images/bar_12.svg", "https://www.svgrepo.com/show/234749/departure-airport.svg"]
	],[ # 7 entrada
	[ #   https://ttsmp3.com/ 
	("This", "Este", "/static/audio/words/This.mp3"), # botones para elegir
	("is", "es", "/static/audio/words/is.mp3"),
	("your", "tu", "/static/audio/words/your.mp3"),
	("large", "grande", "/static/audio/words/large.mp3"),
	("salad", "ensalada", "/static/audio/words/salad.mp3"),
	],[
	("This", "Esta"), # No estoy usando x ahora
	("is", "es"),
	("your", "tu"),
	("large salad", "ensalada grande"),
	],[
	"This is your large salad" # opciones de respuesta
	],[
	("audio", "/static/audio/renzo_do_not_need_alotof_money.mp3"), # audio normal
	("audioSlow", "/static/audio/renzo__do__not__need__alotof__money.mp3") #audio lento
	# pregunta en español,  num respuesta correcta , nivel de avance , imegen de ilustración
	# https://materializecss.com/icons.html
	# https://www.svgrepo.com/
	],["De dónde eres?", 15, "/static/images/bar_14.svg", "https://www.svgrepo.com/show/405754/green-salad.svg"]
	],[ # 8 entrada
	[ #   https://ttsmp3.com/ 
	("You", "Tú", "/static/audio/words/You.mp3"), # botones para elegir
	("have", "tienes", "/static/audio/words/have.mp3"),
	("an", "un", "/static/audio/words/an.mp3"),
	("expensive", "caro", "/static/audio/words/expensive.mp3"),
	("car", "carro", "/static/audio/words/car.mp3"),
	],[
	("You", "Tú"), # No estoy usando x ahora
	("have", "tienes"),
	("an", "un"),
	("expensive car", "auto costoso"),
	],[
	"You have an expesive car" # opciones de respuesta
	],[
	("audio", "/static/audio/renzo_do_not_need_alotof_money.mp3"), # audio normal
	("audioSlow", "/static/audio/renzo__do__not__need__alotof__money.mp3") #audio lento
	# pregunta en español,  num respuesta correcta , nivel de avance , imegen de ilustración
	# https://materializecss.com/icons.html
	# https://www.svgrepo.com/
	],["De dónde eres?", 15, "/static/images/bar_16.svg", "https://www.svgrepo.com/show/398386/sport-utility-vehicle.svg"]
	],[ # 9 entrada
	[ #   https://ttsmp3.com/ 
	("Here", "Aquí", "/static/audio/words/here.mp3"), # botones para elegir
	("is", "está", "/static/audio/words/is.mp3"),
	("your", "su", "/static/audio/words/your.mp3"),
	("delicious", "delicioso", "/static/audio/words/delicious.mp3"),
	("soda", "refresco", "/static/audio/words/soda.mp3"),
	],[
	("Here", "Aquí"), # No estoy usando x ahora
	("is", "está"),
	("your", "su"),
	("delicious soda", "refresco delicioso"),
	],[
	"Here is your delicious soda" # opciones de respuesta
	],[
	("audio", "/static/audio/renzo_do_not_need_alotof_money.mp3"), # audio normal
	("audioSlow", "/static/audio/renzo__do__not__need__alotof__money.mp3") #audio lento
	# pregunta en español,  num respuesta correcta , nivel de avance , imegen de ilustración
	# https://materializecss.com/icons.html
	# https://www.svgrepo.com/
	],["De dónde eres?", 15, "/static/images/bar_18.svg", "https://www.svgrepo.com/show/187148/drink-soda.svg"]
	],[ # 10 entrada
	[ #   https://ttsmp3.com/ 
	("This", "Este", "/static/audio/words/this.mp3"), # botones para elegir
	("is", "es", "/static/audio/words/is.mp3"),
	("my", "mi", "/static/audio/words/my.mp3"),
	("coffee", "café", "/static/audio/words/coffee.mp3"),
	("and", "y", "/static/audio/words/and.mp3"),
	("a", "un", "/static/audio/words/a.mp3"),
	("delicious", "delicioso", "/static/audio/words/delicious.mp3"),
	("sandwich", "sándwich", "/static/audio/words/sandwich.mp3"),
	],[
	("This", "Este"), # No estoy usando x ahora
	("is", "es"),
	("my", "mi"),
	("coffee", "café"),
	("and", "y"),
	("a", "un"),
	("delicious sandwich", "sándwich delicioso"),
	],[
	"This is my coffe and a delicious sandwich" # opciones de respuesta
	],[
	("audio", "/static/audio/renzo_do_not_need_alotof_money.mp3"), # audio normal
	("audioSlow", "/static/audio/renzo__do__not__need__alotof__money.mp3") #audio lento
	# pregunta en español,  num respuesta correcta , nivel de avance , imegen de ilustración
	# https://materializecss.com/icons.html
	# https://www.svgrepo.com/
	],["De dónde eres?", 15, "/static/images/bar_20.svg", "https://www.svgrepo.com/show/288060/breakfast-sandwich.svg"]
	],
]

@app.route("/questionsthree", methods=['POST', 'GET'])
def questionsThree():
	valor = 0
	wrong = 0
	if request.method == 'POST':
		wrong = int(request.form['malo'])
		valor = int(request.form['numero'])
		print(" Errores : " + str(request.form['malo']))
	if valor < len(qthree):
		# Necesito unva versión de la lsita sin shuffle
		sinshuffle = copy.copy(qthree[valor][0]) 
		# estA PARTE es el barajado
		mylist = qthree[valor][0]
		myshuffle ="" # este es un string 
		myArray = [] # este es un arreglo
		# shuffle python : https://www.w3schools.com/python/trypython.asp?filename=demo_ref_random_shuffle
		random.shuffle(mylist) # el barajado
		for i in mylist:
			#myshuffle.append(i[0]) 
			myshuffle += i[0] + " " # el resultado lo pongo en un string
		myArray.append(myshuffle) # luego en un arreglo para enviar e jscript

		return render_template("q3.html",
			val =  valor,
			error =  wrong,
			res_ok = qthree[valor][2] ,
			respuestas = myArray,
			botones= mylist,   
			myAudios = qthree[valor][3],
			question = qthree[valor][4],
			MyEsQuestion = qthree[valor][1]
			)
	else:
		errores = wrong
		valor = 0
		wrong = 0
		return render_template("fin.html", bad = errores, total = len(qthree))

@app.route("/questionstwo", methods=['POST', 'GET'])
def questionsTwo():
	valor = 0
	wrong = 0
	if request.method == 'POST':
		wrong = int(request.form['malo'])
		valor = int(request.form['numero'])
		print(" Errores : " + str(request.form['malo']))
	if valor < len(qtwo):
		# estA PARTE es el barajado
		mylist = qtwo[valor][0]
		myshuffle ="" # este es un string 
		myArray = [] # este es un arreglo
		# shuffle python : https://www.w3schools.com/python/trypython.asp?filename=demo_ref_random_shuffle
		random.shuffle(mylist) # el barajado
		for i in mylist:
			#myshuffle.append(i[0]) 
			myshuffle += i[0] + " " # el resultado lo pongo en un string
		myArray.append(myshuffle) # luego en un arreglo para enviar e jscript

		return render_template("q2.html",
			val =  valor,
			error =  wrong,
			res_ok = qtwo[valor][2] ,
			respuestas = myArray,
			botones= mylist,   
			myAudios = qtwo[valor][3],
			question = qtwo[valor][4]
			)
	else:
		errores = wrong
		valor = 0
		wrong = 0
		return render_template("fin.html", bad = errores, total = len(qtwo))

@app.route("/test3", methods=['POST', 'GET'])
def test3():	
	if request.method == 'POST':
		if 	str(request.form['midata']) == "EXITO":
			global contador
			contador += 1
			#print(str(contador))
	if contador < len(bigData):
		return render_template("test3.html" , 
			data= bigData[contador][0] , 
			correcion = bigData[contador][1] ,
			respuestas = bigData[contador][2] ,
			myAudios = bigData[contador][3],
			question = bigData[contador][4]
			)
	else:
		return render_template("fin.html")

@app.route("/questions", methods=['POST', 'GET'])
def questions():
	# https://youtu.be/CEyymB-vta8
	valor = 0
	wrong = 0
	if request.method == 'POST':
		wrong = int(request.form['malo'])
		valor = int(request.form['numero'])
		print(" Errores : " + str(request.form['malo']))
	if valor < len(questions2):
		return render_template("questions.html" ,
			val =  valor,
			error =  wrong,
			data= questions2[valor][0] , 
			correcion = questions2[valor][1] ,
			respuestas = questions2[valor][2] ,
			myAudios = questions2[valor][3],
			question = questions2[valor][4]
			)
	else:
		errores = wrong
		valor = 0
		wrong = 0
		return render_template("fin.html", bad = errores, total = len(questions2))

if __name__ == '__main__':
    app.run(debug=True)