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
	("I", "I", "Yo", "/static/audio/words/I.mp3"), # pregunta
	("want","want", "quiero", "/static/audio/words/want.mp3"),
	("to","to", "comprar", "/static/audio/words/to.mp3"),
	("buy","buy", "comprar", "/static/audio/words/buy.mp3"),
	("a", "a", "una", "/static/audio/words/a.mp3"),
	("house", "house", "casa", "/static/audio/words/house.mp3"),
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
	],["Escucha y selecciona:", 15, "/static/images/bar_2.svg", "/static/images/friend.svg"]
	],
]

# estA PARTE es el barajado
# 
mylist = qtwo[contador][0]
myshuffle ="" # este es un string 
myArray = [] # este es un arreglo
random.shuffle(mylist) # el barajado
for i in mylist:
	#myshuffle.append(i[0]) 
	myshuffle += i[0] + " " # el resultado lo pongo en un string
myArray.append(myshuffle) # luego en un arreglo para enviar e jscript
#print(myArray)

@app.route("/questionstwo", methods=['POST', 'GET'])
def questionsTwo():
    return render_template("q2.html",
		res_ok = qtwo[contador][2] ,
		respuestas = myArray,
		botones= mylist,   # shuffle python : https://www.w3schools.com/python/trypython.asp?filename=demo_ref_random_shuffle
		myAudios = qtwo[contador][3],
		question = qtwo[contador][4]
		)

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