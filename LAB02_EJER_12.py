#Programa: LAB02_EJER_12.py
#Grupo: 1
#Autores: Elmer Montoya, Elvis Aguilar, Rafael Argüello, Joseph Avilez
#Fecha de Modificación: 23/09/2024
#Versión de Python: 3.12
#IDE Usada: Visual Studio Code
#Propósito: Crear una función que doble los valores de una lista de números.
def doblar_valores(numeros):
    for i, n in enumerate(numeros):
        numeros[i] *= 2

n = [5, 10, 15, 20]
doblar_valores(n)

print(n)