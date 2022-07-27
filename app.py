from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "HOLLAsasds"
global contador
contador = 0
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
answers_test2 = [
	("My name is Rosa"),
	("Nice to meet you"),
	("How are you?")
]

bigData = [
	[ #primera entrada
	[
	("What", "Cuál"),
	("is", "es"),
	("your", "tu"),
	("name?", "nombre?")
	],[
	("Me llano Rosa"),
	("Encantado de conocerte"),
	("Cómo estás?")
	],[
	("My name is Rosa"),
	("Nice to meet you"),
	("How are you?")
	],[
	("audio", "/static/audio/what_is_your_name.mp3"),
	("audioSlow", "/static/audio/want__is__your__name.mp3")
	],["Reponde a la pregunta: ", 0, "/static/images/bar1.svg"]
	],
	[  #segunda entrada
	[
	("How", "Cómo"),
	("are", "estás"),
	("you", "tú"),
	],[
	("Cómo estás?"),
	("Encantado de conocerte"),
	("De dóde eres?")
	],[
	("How are you?"),
	("Nice to meet you"),
	("Where are you from?")
	],[
	("audio", "/static/audio/how_are_you.mp3"),
	("audioSlow", "/static/audio/how__are__you.mp3")
	],["Contesta a la pregunta siguiente: ", 1, "/static/images/bar2.svg"]
	],
	[  #tercera entrada
	[ 
	("I", "Yp"),
	("...", "..."),
	("at", "en"),
	("the", "el"),
	("airport", "aeropuesto"),
	],[
	("quiero"),
	("tengo"),
	("estoy")
	],[
	("want"),
	("have"),
	("am")
	],[
	("audio", "/static/audio/how_are_you.mp3"),
	("audioSlow", "/static/audio/how__are__you.mp3")
	],["Contesta a la pregunta siguiente: ", 2, "/static/images/bar2.svg"]
	]
]

Myquestions = [
	[ #primera entrada
	[
	("I", "Yo"),
	("...", "..."),
	("Rosa Elena", "ROsa Elena")
	],[
	("Want\nQuerer"),
	("Have\nTener"),
	("I am Rosa Elena\nYo soy Rosa Elena")
	],[
	("want"),
	("have"),
	("am")
	],[
	("audio", "/static/audio/i_am_rosa_elena.mp3"),
	("audioSlow", "/static/audio/i__am__rosa__elena.mp3")
	],["Cuál es el verbo que falta: ", 2, "/static/images/bar_1.svg", "/static/images/i_am_rosa.svg"]
	],
	[ # 2 entrada
	[
	("You", "tü"),
	("___", "___"),
	("from", "de"),
	("Mexico", "México"),
	],[
	("You are from Mexico\nTú eres de México"),
	("Is\nEs"),
	("Am\nSoy")
	],[
	("are"),
	("is"),
	("am")
	],[
	("audio", "/static/audio/You_are_from_mexico.mp3"),
	("audioSlow", "/static/audio/You__are__from__mexico.mp3")
	],["Cuál es el verbo que falta: ", 0, "/static/images/bar_2.svg", "/static/images/mexico.svg"]
	],
	[ # 3 entrada
	[
	("I", "Yo"),
	("___", "___"),
	("in", "en"),
	("the", "el"),
	("airport", "aeropuerto"),
	],[
	("estoy"),
	("estas"),
	("quiero")
	],[
	("am"),
	("are"),
	("want")
	],[
	("audio", "/static/audio/I_am_in_the_airport.mp3"),
	("audioSlow", "/static/audio/I__am__in__the__airport.mp3")
	],["Cuál es el verbo que falta: ", 0, "/static/images/bar_3.svg", "/static/images/airport.svg"]
	],[ # 4 entrada
	[
	("This", "Este"),
	("___", "___"),
	("my", "mi"),
	("friend", "amigo"),
	],[
	("eres"),
	("is"),
	("tener")
	],[
	("are"),
	("is"),
	("have")
	],[
	("audio", "/static/audio/this_is_my_friend.mp3"),
	("audioSlow", "/static/audio/this__is__my__friend..mp3")
	],["Cuál es el verbo que falta: ", 1, "/static/images/bar_4.svg", "/static/images/friend.svg"]
	],[ # 5 entrada
	[
	("Malena", "Malena"),
	("___", "___"),
	("at", "en"),
	("a", "un"),
	("restaurant", "restaurante"),
	],[
	("está"),
	("estas"),
	("tienes")
	],[
	("is"),
	("are"),
	("have")
	],[
	("audio", "/static/audio/Malena_is_at_a_restaurant.mp3"),
	("audioSlow", "/static/audio/Malena__is__at__a__restaurant.mp3")
	],["Cuál es el verbo que falta: ", 0, "/static/images/bar_5.svg", "/static/images/restaurant.svg"]
	],[ # 6 entrada
	[
	("I", "Yo"),
	("___", "___"),
	("a", "una"),
	("small apple", "manzana pequeña"),
	],[
	("eres"),
	("es"),
	("quiero")
	],[
	("are"),
	("is"),
	("want")
	],[
	("audio", "/static/audio/I_want_a_small_apple.mp3"),
	("audioSlow", "/static/audio/I__want__a__small__apple.mp3")
	],["Cuál es el verbo que falta: ", 2, "/static/images/bar_6.svg", "/static/images/apple.svg"]
	],[ # 7 entrada
	[
	("You", "Tú"),
	("___", "___"),
	("a", "una"),
	("large salad", "ensalada grande"),
	],[
	("quiero"),
	("eres"),
	("soy")
	],[
	("want"),
	("are"),
	("am")
	],[
	("audio", "/static/audio/you_want_a_small_salad.mp3"),
	("audioSlow", "/static/audio/you__want__a__small__salad.mp3")
	],["Cuál es el verbo: ", 0, "/static/images/bar_7.svg", "/static/images/salad.svg"]
	],[ # 8 entrada
	[
	("I", "Yo"),
	("___", "___"),
	("to buy", "comprar"),
	("a", "una"),
	("house", "casa"),
	],[
	("eres"),
	("quiero"),
	("soy")
	],[
	("are"),
	("want"),
	("am")
	],[
	("audio", "/static/audio/I_want_to_buy_a_house.mp3"),
	("audioSlow", "/static/audio/I__want__to__buy__a__house.mp3")
	],["Cuál es el verbo: ", 1, "/static/images/bar_8.svg", "/static/images/house.svg"]
	],[ # 9 entrada
	[
	("You", "Tú"),
	("___", "___"),
	("an", "una"),
	("orange jacket", "chaqueta naranja"),
	],[
	("soy"),
	("estoy"),
	("quiero")
	],[
	("am"),
	("are"),
	("want")
	],[
	("audio", "/static/audio/i_want_an_orange_jacket.mp3"),
	("audioSlow", "/static/audio/i__want__an__orange__jacket.mp3")
	],["Cuál es el verbo: ", 2, "/static/images/bar_9.svg", "/static/images/orange.svg"]
	],[ # 10 entrada
	[
	("Rosa", "Rosa"),
	("___", "___"),
	("to buy", "compara"),
	("a", "un"),
	("ticket", "boleto"),
	],[
	("quiere"),
	("ir"),
	("tener")
	],[
	("wants"),
	("go"),
	("have")
	],[
	("audio", "/static/audio/rosa_want_to_buy_a_ticket.mp3"),
	("audioSlow", "/static/audio/rosa__want__to__buy__a__ticket.mp3")
	],["Cuál es el verbo: ", 0, "/static/images/bar_10.svg", "/static/images/ticket.svg"]
	],[ # 11 entrada
	[
	("I", "Yo"),
	("___", "___"),
	("some", "un poco de"),
	("bread", "pan"),
	],[
	("necesito"),
	("estoy"),
	("soy")
	],[
	("need"),
	("are"),
	("is")
	],[
	("audio", "/static/audio/i_need_some_bread.mp3"),
	("audioSlow", "/static/audio/i__need__some__bread.mp3")
	],["Cuál es el verbo: ", 0, "/static/images/bar_11.svg", "/static/images/bread.svg"]
	],[ # 12 entrada
	[
	("You", "Tú"),
	("___", "___"),
	("a", "un"),
	("bithday cake", "pastel de cumpleaños"),
	],[
	("soy"),
	("estoy"),
	("necesito")
	],[
	("am"),
	("are"),
	("need")
	],[
	("audio", "/static/audio/you_need_a_bithday_cake.mp3"),
	("audioSlow", "/static/audio/you__need__a__bithday__cake.mp3")
	],["Cuál es el verbo: ", 2, "/static/images/bar_12.svg", "/static/images/cake.svg"]
	],[ # 13 entrada
	[
	("I", "Yo"),
	("___", "___"),
	("a lot of", "mucho"),
	("money", "dinero"),
	],[
	("ir"),
	("necesito"),
	("estoy")
	],[
	("go"),
	("need"),
	("am")
	],[
	("audio", "/static/audio/i_need_a_lot_of_money.mp3"),
	("audioSlow", "/static/audio/i__need__a__lot__of__money.mp3")
	],["Cuál es el verbo: ", 1, "/static/images/bar_13.svg", "/static/images/money.svg"]
	],[ # 14 entrada
	[
	("Do", "..."),
	("you", "tú"),
	("___", "____"),
	("some", "un poco de"),
	("money?", "dinero?"),
	],[
	("estás"),
	("necesito"),
	("es")
	],[
	("are"),
	("need"),
	("is")
	],[
	("audio", "/static/audio/do_you_need_some_money.mp3"),
	("audioSlow", "/static/audio/do__you__need__some__money.mp3")
	],["Cuál es el verbo: ", 1, "/static/images/bar_14.svg", "/static/images/money2.svg"]
	],[ # 15 entrada
	[
	("Renzo", "..."),
	("do not", "no"),
	("___", "____"),
	("a lot of", "mucho"),
	("money", "dinero"),
	],[
	("come"),
	("va"),
	("necesita")
	],[
	("eat"),
	("go"),
	("need")
	],[
	("audio", "/static/audio/renzo_do_not_need_alotof_money.mp3"),
	("audioSlow", "/static/audio/renzo__do__not__need__alotof__money.mp3")
	],["Cuál es el verbo: ", 2, "/static/images/bar_15.svg", "/static/images/money.svg"]
	],[ # 16 entrada
	[
	("I", "Yo"),
	("___", "___"),
	("a", "un"),
	("red car", "carro rojo"),
	],[
	("tengo"),
	("correr"),
	("estoy")
	],[
	("have"),
	("run"),
	("are")
	],[
	("audio", "/static/audio/i_have_a_red_car.mp3"),
	("audioSlow", "/static/audio/i__have__a__red__car.mp3")
	],["Cuál es el verbo: ", 0, "/static/images/bar_16.svg", "/static/images/car.svg"]
	],[ # 17 entrada
	[
	("You", "Tú"),
	("___", "___"),
	("a", "una"),
	("big bag", "maleta grande"),
	],[
	("quiere"),
	("tienes"),
	("estás")
	],[
	("wants"),
	("have"),
	("are")
	],[
	("audio", "/static/audio/you_have_a_big_bag.mp3"),
	("audioSlow", "/static/audio/you__have__a__big__bag.mp3")
	],["Cuál es el verbo: ", 1, "/static/images/bar_17.svg", "/static/images/bag.svg"]
	],[ # 18 entrada
	[
	("Do you", "Tú"),
	("__", "___"),
	("a", "una"),
	("ticket", "boleto"),
	],[
	("tienes"),
	("estás"),
	("es")
	],[
	("have"),
	("are"),
	("is")
	],[
	("audio", "/static/audio/Do_you_have_a_ticket.mp3"),
	("audioSlow", "/static/audio/Do__you__have__a__ticket.mp3")
	],["Cuál es el verbo: ", 0, "/static/images/bar_18.svg", "/static/images/ticket.svg"]
	],[ # 19 entrada
	[
	("Renzo", "Rénzo"),
	("__", "___"),
	("a", "una"),
	("beautiful", "hermosa"),
	("house", "casa"),
	],[
	("tiene"),
	("ir"),
	("estás")
	],[
	("has"),
	("go"),
	("are")
	],[
	("audio", "/static/audio/Renzo_has_a_beautiful_house.mp3"),
	("audioSlow", "/static/audio/Renzo__has__a__beautiful__house.mp3")
	],["Cuál es el verbo: ", 0, "/static/images/bar_19.svg", "/static/images/house2.svg"]
	],[ # 20 entrada
	[
	("Rosa", "Rosa"),
	("__", "___"),
	("a", "una"),
	("small pet", "mascota pequeña"),
	],[
	("tiene"),
	("tienes"),
	("es")
	],[
	("has"),
	("have"),
	("is")
	],[
	("audio", "/static/audio/Rosa_has_a_small_pet.mp3"),
	("audioSlow", "/static/audio/Rosa__has__a__small__pet.mp3")
	],["Cuál es el verbo: ", 0, "/static/images/bar_20.svg", "/static/images/pet.svg"]
	]
]

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
	if request.method == 'POST':
		if 	str(request.form['midata']) == "EXITO":
			global contador
			contador += 1
			#print(str(contador))
	if contador < len(Myquestions):
		return render_template("questions.html" , 
			data= Myquestions[contador][0] , 
			correcion = Myquestions[contador][1] ,
			respuestas = Myquestions[contador][2] ,
			myAudios = Myquestions[contador][3],
			question = Myquestions[contador][4]
			)
	else:
		contador = 0
		return render_template("fin.html")

#@app.route("/rest", methods=['POST', 'GET'])
#def intex():
#	print("estoy en rest")
#	if request.method == 'POST':	
#		print(str(request.form['midata']))
#	return render_template("test3.html" , data= bigData[0] , correcion = bigData[1] , respuestas = bigData[2])

if __name__ == '__main__':
    app.run(debug=True)