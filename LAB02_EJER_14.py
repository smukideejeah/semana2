#Programa: LAB02_EJER_14.py
#Grupo: 1
#Autores: Elmer Montoya, Elvis Aguilar, Rafael Argüello, Joseph Avilez
#Fecha de Modificación: 23/09/2024
#Versión de Python: 3.12
#IDE Usada: Visual Studio Code
#Propósito: Crear un programa que convierta entre kilogramos y libras, y entre kilómetros y millas.

class conversor:
    def fromKgToLb(kg):
        return kg * 2.2
    
    def fromLbToKg(lb):
        return lb / 2.2
    
    def fromKmToMi(km):
        return km * 0.6
    
    def fromMiToKm(mi):
        return mi / 0.6

def convert(number, fromTo):
    match fromTo:
        case "1":
            return conversor.fromKgToLb(number)
        case "2":
            return conversor.fromLbToKg(number)
        case "3":
            return conversor.fromKmToMi(number)
        case "4":
            return conversor.fromMiToKm(number)
        case _:
            convert(number, input("Opción inválida. Ingrese una opción válida: "))
        
print("Seleccione la conversión que desea realizar:")
print("1. Kilogramos a Libras")
print("2. Libras a Kilogramos")
print("3. Kilómetros a Millas")
print("4. Millas a Kilómetros")
fromTo = input("Ingrese una opción: ")
number = float(input("Ingrese el número a convertir: "))
print("Resultado: ", convert(number, fromTo));