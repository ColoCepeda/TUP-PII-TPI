# Trabajo Práctico I - Programación II
import os
import bibloteca as biblio

print("Bienvenido!")
respuesta = ''

def menu():
    print("1 - Mostrar libros")
    print("2 - Gestionar Prestamo")
    print("3 - Gestionar Devolucion")
    print("4 - Registrar nuevo libro")
    print("5 - Eliminar ejemplar")
    print("6 - Mostrar ejemplares prestados")
    print("7 - Salir")

while respuesta != "salir":
    menu()
    opt = input("\n Ingrese la opción de menú: ")
    os.system ("cls") #Limpiar pantalla
    if opt.isnumeric():
        if int(opt) == 1:
            biblio.mostrar_libros()
            print()
        elif int(opt) == 2:
            biblio.prestar_ejemplar_libro()
            print()
        elif int(opt) == 3:
            biblio.devolver_ejemplar_libro()
            print()
        elif int(opt) == 4:
            biblio.registrar_nuevo_libro()
            print()
        elif int(opt) == 5:
            biblio.eliminar_ejemplar_libro() #agregar funcion de agregar ejemplares?
            print()
        elif int(opt) == 6:
            biblio.ejemplares_prestados()
            print()
        elif int(opt) == 7:
            respuesta = "salir"
        else: print("Ingrese una opción válida")
    else: 
        print("Ingrese una opción numérica")
    
    biblio.pause()

print("Hasta luego!.")