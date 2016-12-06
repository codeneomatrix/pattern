import re
from collections import Counter

def palabras(text): return re.findall(r'\w+', text.lower())

#def tokens(text): return (text.lower()).split() 

conjunto_palabras = Counter(palabras(open('texto2.txt').read()))

def P(palabra, N=sum(conjunto_palabras.values())): 
    "probabilidad de la `palabra`."
    return conjunto_palabras[palabra] / N

def combinacion1(palabra):
    "Todas las versiones  de  una  `palabra`."
    letras         = 'abcdefghijklmnopqrstuvwxyz'
    separadores    = [(palabra[:i], palabra[i:])    for i in range(len(palabra) + 1)]
    eliminaciones  = [L + R[1:]               for L, R in separadores if R]
    trasposisiones = [L + R[1] + R[0] + R[2:] for L, R in separadores if len(R)>1]
    remplazos      = [L + c + R[1:]           for L, R in separadores if R for c in letras]
    inserciones    = [L + c + R               for L, R in separadores for c in letras]
    return set(eliminaciones + trasposisiones + remplazos + inserciones)

def combinacion2(palabra): 
    "Todas las versiones  de  una  `palabra`."
    return (e2 for e1 in combinacion1(palabra) for e2 in combinacion1(e1))

def buscar(palabras): 
    "El subconjunto de `palabras` que aparecen en el diccionario de PALABRAS."
    return set(w for w in palabras if w in conjunto_palabras)

def candidatos(palabra): 
    "Generar posibles correcciones ortograficas para la palabra."
    return (buscar([palabra]) or buscar(combinacion1(palabra)) or buscar(combinacion2(palabra)) or [palabra])

def candidatos2(palabra): 
    "Generar posibles correcciones ortograficas para la palabra."
    return (buscar([palabra]) or buscar(combinacion1(palabra)) or [palabra])    

def correccion(palabra): 
    "Correccion ortografica mas probable por palabra."
    return max(candidatos2(palabra), key=P)

def formato(text):
    "Devuelve la funcion de caso apropiada para el texto: minuscula,mayuscula, titulo o simplemente texto."
    return (str.upper if text.isupper() else
            str.lower if text.islower() else
            str.title if text.istitle() else
            str)

def corregir_coincidencia(match):
    "Correccion ortografica de la palabra en coincidencia, y preservar el formato minusculas/mayusculas/titulo."
    word = match.group()
    return formato(word)(correccion(word.lower()))

def corregir_texto(texto):
    return re.sub('[a-zA-Z]+', corregir_coincidencia, texto)


#corregir_texto('sirve que checas el cpu')