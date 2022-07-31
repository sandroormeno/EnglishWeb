from flask import Flask, render_template, request, flash
from mydata import Myquestions, bigData, answers_test2, answers, Mydata
from mydata2 import questions2
import random

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

qtwo = [
	[ #primera entrada
	[
	("I", "Yo", "/static/audio/words/I.mp3"), # pregunta
	("want", "quiero", "/static/audio/words/want.mp3"),
	("to", "comprar", "/static/audio/words/to.mp3"),
	("buy", "comprar", "/static/audio/words/buy.mp3"),
	("a", "una", "/static/audio/words/a.mp3"),
	("house", "casa", "/static/audio/words/house.mp3"),
	],[
	("Hello\nHola - es un saludo formal"), # comentario de respuesta
	("See you later\nNos vemos luego"),
	("Bye\nAdios - se usa para despedirce")
	],[
	"I want to buy a house" # opciones de respuesta
	],[
	("audio", "/static/audio/I_want_to_buy_a_house.mp3"), # audio normal
	("audioSlow", "/static/audio/I__want__to__buy__a__house.mp3") #audio lento
	# pregunta ,  num respuesta correcta , nivel de avance , imegen de ilustración
	# https://materializecss.com/icons.html
	# https://www.svgrepo.com/
	],["Escucha y selecciona:", 15, "/static/images/bar_2.svg", "https://www.svgrepo.com/show/415757/building-home-house.svg"]
	],[ # 2 entrada
	[
	("You", "Tú", "/static/audio/words/You.mp3"), # pregunta
	("need", "necesitas", "/static/audio/words/need.mp3"),
	("a", "un", "/static/audio/words/a.mp3"),
	("birthday", "cumpleaños", "/static/audio/words/birthday.mp3"),
	("cake", "pastel", "/static/audio/words/cake.mp3"),
	],[
	("Hello\nHola - es un saludo formal"), # comentario de respuesta
	("See you later\nNos vemos luego"),
	("Bye\nAdios - se usa para despedirce")
	],[
	"You need a birthday cake" # opciones de respuesta
	],[
	("audio", "/static/audio/You_need_a_birthday_cake.mp3"), # audio normal
	("audioSlow", "/static/audio/You__need__a__birthday__cake.mp3") #audio lento
	# pregunta ,  num respuesta correcta , nivel de avance , imegen de ilustración
	# https://materializecss.com/icons.html
	# https://www.svgrepo.com/
	],["Escucha y selecciona:", 15, "/static/images/bar_4.svg", "https://www.svgrepo.com/show/288801/birthday-cake-cake.svg"]
	],[ # 3 entrada
	[
	("Where", "Dónde", "/static/audio/words/where.mp3"), # pregunta
	("are", "eres", "/static/audio/words/are.mp3"),
	("you", "tú", "/static/audio/words/you.mp3"),
	("from?", "de", "/static/audio/words/from.mp3"),

	],[
	("Hello\nHola - es un saludo formal"), # comentario de respuesta
	("See you later\nNos vemos luego"),
	("Bye\nAdios - se usa para despedirce")
	],[
	"Where are you from?" # opciones de respuesta
	],[
	("audio", "/static/audio/where_are_you_from.mp3"), # audio normal
	("audioSlow", "/static/audio/where__are__you__from.mp3") #audio lento
	# pregunta ,  num respuesta correcta , nivel de avance , imegen de ilustración
	# https://materializecss.com/icons.html
	# https://www.svgrepo.com/
	],["Escucha y selecciona:", 15, "/static/images/bar_6.svg", "https://www.svgrepo.com/show/244916/internet-world.svg"]
	],
	[ # 4 entrada
	[
	("You", "Tú", "/static/audio/words/you.mp3"), # pregunta
	("want", "quieres", "/static/audio/words/want.mp3"),
	("a", "una", "/static/audio/words/a.mp3"),
	("small", "pequeña", "/static/audio/words/small.mp3"),
	("salad", "ensalada", "/static/audio/words/salad.mp3"),
	],[
	("Hello\nHola - es un saludo formal"), # comentario de respuesta
	("See you later\nNos vemos luego"),
	("Bye\nAdios - se usa para despedirce")
	],[
	"you want a small salad" # opciones de respuesta
	],[
	("audio", "/static/audio/you_want_a_small_salad.mp3"), # audio normal
	("audioSlow", "/static/audio/you__want__a__small__salad.mp3") #audio lento
	# pregunta ,  num respuesta correcta , nivel de avance , imegen de ilustración
	# https://materializecss.com/icons.html
	# https://www.svgrepo.com/
	],["Escucha y selecciona:", 15, "/static/images/bar_8.svg", "https://www.svgrepo.com/show/15590/salad.svg"]
	],[ # 5 entrada
	[
	("Do", "_", "/static/audio/words/Do.mp3"), # pregunta
	("you", "tú", "/static/audio/words/you.mp3"),
	("have", "quieres", "/static/audio/words/have.mp3"),
	("a", "un", "/static/audio/words/a.mp3"),
	("ticket?", "boleto", "/static/audio/words/ticket.mp3"),
	],[
	("Hello\nHola - es un saludo formal"), # comentario de respuesta
	("See you later\nNos vemos luego"),
	("Bye\nAdios - se usa para despedirce")
	],[
	"Do you have a ticket?" # opciones de respuesta
	],[
	("audio", "/static/audio/Do_you_have_a_ticket.mp3"), # audio normal
	("audioSlow", "/static/audio/Do__you__have__a__ticket.mp3") #audio lento
	# pregunta ,  num respuesta correcta , nivel de avance , imegen de ilustración
	# https://materializecss.com/icons.html
	# https://www.svgrepo.com/
	],["Escucha y selecciona:", 15, "/static/images/bar_10.svg", "https://www.svgrepo.com/show/275144/plane-ticket-travel.svg"]
	],[ # 6 entrada
	[
	("You", "Tú", "/static/audio/words/you.mp3"), # pregunta
	("are", "eres", "/static/audio/words/are.mp3"),
	("from", "de", "/static/audio/words/from.mp3"),
	("Mexico", "México", "/static/audio/words/mexico.mp3"),
	],[
	("Hello\nHola - es un saludo formal"), # comentario de respuesta
	("See you later\nNos vemos luego"),
	("Bye\nAdios - se usa para despedirce")
	],[
	"You are from Mexico" # opciones de respuesta
	],[
	("audio", "/static/audio/You_are_from_mexico.mp3"), # audio normal
	("audioSlow", "/static/audio/You__are__from__mexico.mp3") #audio lento
	# pregunta ,  num respuesta correcta , nivel de avance , imegen de ilustración
	# https://materializecss.com/icons.html
	# https://www.svgrepo.com/
	],["Escucha y selecciona:", 15, "/static/images/bar_12.svg", "https://www.svgrepo.com/show/405549/flag-for-flag-mexico.svg"]
	]
]
"""
# estA PARTE es el barajado
# 
mylist = qtwo[contador][0]
myshuffle ="" # este es un string 
myArray = [] # este es un arreglo
# shuffle python : https://www.w3schools.com/python/trypython.asp?filename=demo_ref_random_shuffle
random.shuffle(mylist) # el barajado
for i in mylist:
	#myshuffle.append(i[0]) 
	myshuffle += i[0] + " " # el resultado lo pongo en un string
myArray.append(myshuffle) # luego en un arreglo para enviar e jscript
#print(myArray)
"""
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