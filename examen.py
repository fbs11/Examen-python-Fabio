from libro import *


f = open("fichero.txt", mode="wt", encoding="utf-8")
palabras = ["boca", "pelo", "gracias", "nariz", "pez"]
f.write("hola soy Fabio encantado")
f.close()

fr = open("fichero.txt", mode="rt", encoding="utf-8")


def get_list(fr):
    texto = fr.read()
    separado = texto.split()
    if separado == None:
        raise ValueError("EL fichero no tiene palabras")
    print(separado)
    dic_palabras = {}
    valores = []
    for i in separado:
        dic_palabras[len(i)] = i

    print(dic_palabras)


f.close()
l1 = Libro(autor="Juan", titulo="enfermedades", anyo="1970")
l2 = Libro(autor="Salvador", titulo="cocina", anyo="1980")
l3 = Libro(autor="Susana", titulo="fantasias", anyo="1990")
libros = [l1, l2, l3]


def mas_antiguos


""" MAIN """

get_list(fr)
