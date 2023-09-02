import libro as l

# Crear una lista vacía para almacenar los libros
libros = []

# Añadir los diccionarios a la lista
libros.append(l.libro1)
libros.append(l.libro2)
libros.append(l.libro3)

def ejemplares_prestados():
    # completar
    return None

def registrar_nuevo_libro():
    nuevo_libro = l.nuevo_libro()
    libros.append(nuevo_libro)
    print(libros)
    print(nuevo_libro)   
    return None

def eliminar_ejemplar_libro():
    #completar
    return None

def prestar_ejemplar_libro():
    libro_a_prestar = input("Ingrese el nombre del libro que quiere sacar a prestamo: ")
    for libro in libros:
        if libro["titulo"] == libro_a_prestar:
            print("El libro existe")
            if libro['cant_ej_pr'] < libro['cant_ej_ad']:
                libro['cant_ej_pr'] += 1
                print("Se realizo el prestamo de con éxito.")
                return None
            else:
                print("El libro no tiene ejemplares disponibles para prestar. ")
                return None
    print("El libro no existe en la biblioteca. ")
    return None

def devolver_ejemplar_libro():
    libro_a_devolver = input("Ingrese el nombre del libro que quiere devolver: ")
    for libro in libros:
        if libro["titulo"] == libro_a_devolver:
            if libro["cant_ej_pr"] > 0:
                print("Se ha gestionado la devolución correctamente.")
                libro["cant_ej_pr"] -= 1
                return None
            else:
                print("No existen ejemplares prestados para el libro ingresado.")
                return None
    print("El libro no existe en la biblioteca")
    return None

def nuevo_libro():
    #completar
    return None