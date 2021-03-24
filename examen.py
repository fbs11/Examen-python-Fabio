import unittest
from libro import *
from autor import *


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
l1 = Libro(autor="Juan", titulo="enfermedades", anyo=1970)
l2 = Libro(autor="Salvador", titulo="cocina", anyo=1980)
l3 = Libro(autor="Susana", titulo="fantasias", anyo=1990)
libros = [l1, l2, l3]


def mas_antiguos(lista_libros, tiempo):
    res = []

    for i in libros:
        if i.get_anyo() <= tiempo:
            res.append(i.get_titulo())
        elif tiempo < 1900 or tiempo > 2021:
            raise ValueError("El año no es valido")

    print(res)
    return res


""" TESTS """


class Pruebas(unittest.TestCase):
    def test_muestra_todos(self):
        l1 = Libro(autor="Juan", titulo="enfermedades", anyo=1970)
        l2 = Libro(autor="Salvador", titulo="cocina", anyo=1980)
        l3 = Libro(autor="Susana", titulo="fantasias", anyo=1990)
        libros = [l1, l2, l3]

        self.assertEqual(mas_antiguos(libros, 2000), "se añaden los 3")

    def test_muestra_elmasantiguo(self):
        l1 = Libro(autor="Juan", titulo="enfermedades", anyo=1970)
        l2 = Libro(autor="Salvador", titulo="cocina", anyo=1980)
        l3 = Libro(autor="Susana", titulo="fantasias", anyo=1990)
        libros = [l1, l2, l3]

        self.assertEqual(mas_antiguos(libros, 1970),
                         "se añade el primero solo")

    def test_muestra_nada(self):
        l1 = Libro(autor="Juan", titulo="enfermedades", anyo=1970)
        l2 = Libro(autor="Salvador", titulo="cocina", anyo=1980)
        l3 = Libro(autor="Susana", titulo="fantasias", anyo=1990)
        libros = [l1, l2, l3]

        self.assertEqual(mas_antiguos(libros, 1930),
                         "no muestra ninguno")


class Suite(unittest.TestSuite):
    def __init__(self):
        super(Suite, self).__init__()
        self.addTest(Pruebas('test_muestra_todos'))
        self.addTest(Pruebas('test_muestra_elmasantiguo'))
        self.addTest(Pruebas('test_muestra_nada'))


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    my_suite = Suite()
    runner.run(my_suite)

""" MAIN """

get_list(fr)
mas_antiguos(libros, 1990)
