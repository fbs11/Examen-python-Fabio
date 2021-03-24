from libro import *


f = open("fichero.txt", mode="wt", encoding="utf-8")
palabras = ["boca", "pelo", "gracias", "nariz", "pez"]
f.write("hola me llamo Fabio")
f.close()

fr = open("fichero.txt", mode="rt", encoding="utf-8")


def get_list(fr):
    texto = fr.read()
    separado = texto.split()
    print(separado)
    dic_palabras = {}
    for i in separado:
        len(i).append(dic_palabras)
    print(dic_palabras)


f.close()
get_list(fr)
