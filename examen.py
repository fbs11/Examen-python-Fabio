from libro import *


f = open("fichero.txt", mode="rt", encoding="utf-8")
palabras = ["boca", "pelo", "gracias", "nariz", "pez"]
f.write("hola")
f.write("gente")
texto = f.read()
print(texto)
f.close()


with open('fichero.txt', 'r') as palabras:
    lineas = [linea.strip() for linea in palabras]

for linea in lineas:
    print(linea)
