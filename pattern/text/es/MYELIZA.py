# -*- coding: utf-8 -*-
import random
import re
from __init__ import *
from corrector import *

"""
reflections = {
  "i am"       : "you are",
  "i was"      : "you were",
  "i"          : "you",
  "i'm"        : "you are",
  "i'd"        : "you would",
  "i've"       : "you have",
  "i'll"       : "you will",
  "my"         : "your",
  "you are"    : "I am",
  "you were"   : "I was",
  "you've"     : "I have",
  "you'll"     : "I will",
  "your"       : "my",
  "yours"      : "mine",
  "you"        : "me",
  "me"         : "you"
}

"""
reflections={
	"yo soy" 		: "eres",
	"yo era" 		: "tu eras",
	"yo" 		    : "tu",
	"estoy" 		: "usted esta",
	"lo hare" 		: "lo haras",
	"tengo" 		: "tienes",
	"lo hare" 		: "Vas a",
	"mio"			: "tuyo",
	"usted esta" 	: "Yo soy",
	"estabas" 		: "Yo era",
	"tienes" 		: "Yo tengo",
	"Usted"			: "yo",
	"tu" 			: "mi",
	"tuya" 			: "mia",
	"tu" 			: "yo",
	"yo" 			: "tu"
}

psique = [
    [r'necesito (.*)',
    ["Por que lo necesitas {0}?",
    "realmente ayudara a conseguir {0}?",
    "Estas seguro que lo necesitas{0}?"]],

    [r'puedes (.*)',
    ["De verdad crees que no {0}?",
    "Tal vez con el tiempo lo hare {0}.",
    "De verdad quieres que {0}?"]],

    [r'por que no puedo ([^\?]*)\??',
    ["Usted cree que deberia ser capaz de {0}?",
    "Si se pudiera {0}, que harias?",
    "No se - Por que no puedes {0}?",
    "Usted realmente lo ha intentado?"]],

    [r'no puedo (.*)',
    ["como sabe que no se puede {0}?",
    "Tal vez podria {0} si se trato.",
    "Que haria falta para que usted pueda {0}?"]],

    [r'yo soy (.*)',
    ["Has venido a mi porque usted es {0}?",
    "Cuanto tiempo ha sido {0}?",
    "como se siente ser {0}?"]],

    [r'estoy (.*)',
    [" {0} ?, como te hace sentir eso?",
    "Le gusta estar {0}?",
    "Por que me dices que eres {0}?",
    "Por que crees que estas {0}?"]],

    [r'eres tu ([^\?]*)\??',
    ["Por que es importante que sea {0}?",
    "Quieres que preferiria que no fuera {0}?",
    "Tal vez creo que soy {0}.",
    "Puedo ser {0} -- Que piensas?"]],

    [r'que (.*)',
    ["Por que lo preguntas?",
    "como seria una respuesta a esa ayudarle?",
    "Que piensas?"]],

    [r'como (.*)',
    ["como cree?",
    "Tal vez usted puede responder a su propia pregunta.",
    "Que es lo que estas pidiendo realmente?"]],

    [r'porque (.*)',
    ["Esa es la verdadera razon?",
    "Que otras razones vienen a la mente?",
    "Eso se aplica a cualquier otra cosa?",
    "Si {0}, lo demas debe ser cierto?"]],

    [r'(.*) lo siento (.*)',
    ["Hay muchos momentos en los que no es necesaria ninguna disculpa.",
    "Que sensaciones tienes cuando te disculpas?"]],

    [r'hola(.*)',
    ["Hola ... Me alegro de que puedo verlo hoy.",
    "Hola, como estas hoy?",
    "Hola, como te sientes hoy?"]],

    [r'creo (.*)',
    ["Dudas {0}?",
    "De verdad piensas eso?",
    "Pero no esta seguro de {0}?"]],


    [r'(.*) amigo (.*)',
    ["Dime mas sobre sus amigos.",
    "Cuando se piensa en un amigo, que le viene a la mente?",
    "Por que no me cuentas de un amigo de la infancia?"]],

    [r'si',
    ["Usted parece muy seguro.",
    "Esta bien, pero se puede elaborar un poco?"]],

    [r'(.*) computadora (.*)',
    ["Esta realmente hablando de mi?",
    "Le parece extraño hablar a un ordenador?",
    "como las computadoras hacen sentir?",
    "Se siente amenazado por las computadoras?"]],

    [r'lo es (.*)',
    ["Cree que es {0}?",
    "Quizas es {0} - que te parece?",
    "Si se tratara de {0}, que haria?",
    "Bien podria ser que {0}."]],

    [r'esto es (.*)',
    ["Usted parece muy seguro.",
    "Si te dijera que probablemente no es {0}, que sentiria?"]],

    [r'tu puedes ([^\?]*)\??',
    ["Que te hace pensar que no puedo {0}?",
    "Si pudiera {0}, entonces, que?",
    "Por que preguntas si puedo {0}?"]],

    [r'yo puedo ([^\?]*)\??',
    ["Tal vez usted no quiere {0}.",
    "Quieres ser capaz de {0}?",
    "Si pudiera {0}, verdad?"]],

    [r'usted esta(.*)',
    ["Por que cree que estoy {0}?",
    "por favor, piense que estoy {0}?",
    "Tal vez le gustaria que yo sea {0}.",
    "Tal vez usted esta realmente hablando de si mismo?"]],

    [r'eres(.*)',
    ["Por que dices que soy {0}?",
    "Por que cree que estoy {0}?",
    "Estamos hablando de usted, o de mi?"]],

    [r'yo no (.*)',
    ["usted en verdad no {0}?",
    "Por que no {0}?",
    "Quieres {0}?"]],

    [r'siento (.*)',
    ["Bueno, dime mas acerca de estos sentimientos.",
    "A menudo se siente {0}?",
    "Cuando sueles sentir {0}?",
    "Cuando se sienta {0}, que haces?"]],

    [r'yo tengo (.*)',
    ["Por que me dices que tienes {0}?",
    "Tiene usted realmente {0}?",
    "Ahora que tiene {0}, que vas a hacer ahora?"]],

    [r'me gustaria (.*)',
    ["Podria explicar por que lo haria {0}?",
    "Por que {0}?",
    "Quien mas sabe que lo haria {0}?"]],

    [r'esta ahi (.*)',
    ["Cree que existe {0}?",
    "Es probable que exista {0}.",
    "Le gustaria que exista {0}?"]],

    [r'mi (.*)',
    ["Veo, su {0}.",
    "Por que dice que su {0}?",
    "Cuando su {0}, como se siente?"]],

    [r'tu (.*)',
    ["Deberiamos estar hablando de usted, no de mi.",
    "Por que dice eso de mi?",
    "Por que te importa si yo {0}?"]],

    [r'por que (.*)',
    ["Por que no me dice la razon por la que {0}?",
    "Por que cree {0}?"]],

    [r'yo quiero (.*)',
    ["Que significaria para usted si usted tiene {0}?",
    "Por que quiere {0}?",
    "Que haria usted si usted tiene {0}?",
    "Si usted tiene {0}, entonces, que harias?"]],

    [r'(.*) madre (.*)',
    ["Dime mas acerca de su madre.",
    "Cual era su relacion con su madre?",
    "como se siente acerca de su madre?",
    "como se relaciona esto con sus sentimientos hoy?",
    "Las buenas relaciones familiares son importantes."]],

    [r'(.*) padre (.*)',
    ["Dime mas acerca de su padre.",
    "como fue tu padre te hace sentir?",
    "como se siente acerca de su padre?",
    "Su relacion con su padre se relacionan con sus sentimientos hoy?",
    "Tiene problemas para mostrar afecto con su familia?"]],

    [r'(.*) niño (.*)',
    ["Tenia amigos cercanos cuando era un niño?",
    "Cual es tu recuerdo favorito de la infancia?",
    "Recuerda algun sueño o pesadillas de la infancia?",
    "Los otros niños a veces se burlan de ti?",
    "como cree que sus experiencias de la infancia se relacionan con sus sentimientos hoy?"]],


    [r'(.*)\?',
    ["Porque preguntas eso?",
    "Por favor, considere si puede responder a su propia pregunta.",
    "Quizas la respuesta esta dentro de ti mismo?",
    "Por que no me lo dijiste?"]],

    [r'adios',
    ["Gracias por hablar conmigo.",
    "Adios.",
    "Gracias, son $ 150. que tenga un buen dia!"]],

    [r'(.*)',
    ["Por favor, cuentame mas.",
    "Vamos a cambiar centrarse un poco ... Hableme de su familia.",
    "Puedes profundizar sobre eso?",
    "Por que dice que {0}?",
    "Ya veo.",
    "Muy interesante.",
    "{0}.",
    "Ya veo. Y que te dice eso?",
    "como te hace sentir eso?",
    "como se siente cuando usted dice eso?"]]
]

reglas=[
{
	"verbo":r'(vigilar|cuidar)',
	"hora": r'([0-9]+)(am|pm)(a|.*)([0-9]+)(am|pm)',
	"lugar": r'el([a-z]+)',
	"respuesta": "ok, vigilando"
}
]


def verbo(texto):
	for i in texto:
		#print i
		if i[1]== 'VB':
			return (conjugate(i[0], INFINITIVE))
	return " "

def reflect(fragment):
    tokens = fragment.lower().split()
    for i, token in enumerate(tokens):
        if token in reflections:
            tokens[i] = reflections[token]
    return ' '.join(tokens)


def analisis1(sentencia):
    for pattern, responses in psique:
        match = re.match(pattern, sentencia.rstrip(".!"))
        if match:
            response = random.choice(responses)
            return response.format(*[reflect(g) for g in match.groups()])

def analisis2(sentencia):
	correccion= corregir_texto(sentencia)
	#print ("palabra corregida:>",correccion)
	s = parse(correccion).split()
	#print ("POSTTAGER: >", s)
	for data in reglas:
		
		match1 = re.match(r'(vigilar|cuidar)', verbo(s[0]))
		if match1:
			print "\t\tidentifico intencion: vigilar"
			match2 = re.findall(data["hora"], correccion.replace(" ",""))
			try:
				if len(match2[0])>1:
					print "\t\tidentifico una hora ",list(match2[0])
			except Exception, e:
				continue
			if(match1):
				print data["respuesta"]
		else:
			print analisis1(correccion)



def main():
    print "Hola. Soy Aurora. En que te puedo ayudar"

    while True:
        sentencia = raw_input("> ")
        if sentencia == "adios":
        	print analisis1(sentencia)
        	break
        else:
        	analisis2(sentencia)


if __name__ == "__main__":
    main()
