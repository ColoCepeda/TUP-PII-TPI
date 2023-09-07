import libro as l
import msvcrt

# Crear una lista vacía para almacenar los libros
libros = []

# Añadir los diccionarios a la lista
libros.append(l.libro1)
libros.append(l.libro2)
libros.append(l.libro3)

#Poner un limpiar pantalla y poner los disponibles
def mostrar_libros():
    print("Lista de libros")
    for libro in libros:
        print("Titulo: " + libro['titulo'] + " - Disponibles: " + str(libro["cant_ej_ad"] - libro["cant_ej_pr"]) + ".")
    return None

def ejemplares_prestados():
    print("Ejemplares prestados de cada libro: ")
    for libro in libros:
        if libro['cant_ej_pr'] > 0:
            print("La cantidad de ejemplares prestados del libro: " + libro['titulo'] + ", es de " + str(libro["cant_ej_pr"])+".")
        else:
            print("El libro " + libro['titulo'] + " no tiene ejemplares prestados.")
    return None

def registrar_nuevo_libro():
    titulo = input("Ingrese el título del libro :")
    for libro in libros:
        if libro["titulo"] == titulo:
            print("El libro ya existe")
            return None

    nuevo_libro = l.nuevo_libro(titulo)
    if nuevo_libro != None:libros.append(nuevo_libro)
    return None

def eliminar_ejemplar_libro():#corrobora que si tiene ejemplares disp y no es igual que los prestados lo elimina
    titulo_a_eliminar = input("Ingrese el título del libro del cual desea eliminar un ejemplar: ") 
    for libro in libros:
        if libro["titulo"] == titulo_a_eliminar:
            confirmacion = input(f"¿Está seguro que desea eliminar un ejemplar de '{titulo_a_eliminar}'? (S/N): ").strip().upper()
            
            if confirmacion == 'S':
                if libro['cant_ej_ad'] > 0 and libro['cant_ej_ad'] != libro['cant_ej_pr']:
                    libro['cant_ej_ad'] -= 1  
                    print(f"Se eliminó un ejemplar de '{titulo_a_eliminar}' con éxito.")
                else:
                    print(f"No hay ejemplares disponibles de '{titulo_a_eliminar}' para eliminar.")
                return None
            else:
                print("Eliminación de ejemplar cancelada.")
                return None
    
    print(f"El libro '{titulo_a_eliminar}' no existe en la biblioteca.")
    return None

def agregar_ejemplar():
    titulo_a_agregar = input("Ingrese el título del libro del cual desea agregar un ejemplar: ") 
    for libro in libros:
        if libro["titulo"] == titulo_a_agregar:
            confirmacion = input(f"¿Está seguro que desea agregar un ejemplar de '{titulo_a_agregar}'? (S/N): ").strip().upper()
            
            if confirmacion == 'S':
                libro['cant_ej_ad'] += 1  
                print(f"Se agregó un ejemplar de '{titulo_a_agregar}' con éxito.")
            return None
        else:
            print("Agregar ejemplar cancelado.")
            return None
        
    print(f"El libro '{titulo_a_agregar}' no existe en la biblioteca.")
    return None

def prestar_ejemplar_libro():
    libro_a_prestar = input("Ingrese el nombre del libro que quiere sacar a préstamo: ")
    libro_existe = False  
    
    for libro in libros:
        if libro["titulo"] == libro_a_prestar:
            #print("El libro existe")
            libro_existe = True  
            if libro['cant_ej_pr'] < libro['cant_ej_ad']:
                libro['cant_ej_pr'] += 1
                print("Se realizó el préstamo con éxito.")
                return None
            else:
                print("El libro no tiene ejemplares disponibles para prestar.")
                return None

    if not libro_existe:
        while True: 
            confirmacion = input("El libro no existe en la biblioteca. ¿Desea agregarlo? (S/N)").strip().upper()
            if confirmacion == 'S':
                nuevo_libro = l.nuevo_libro(libro_a_prestar)
                if nuevo_libro != None:libros.append(nuevo_libro)
                break
            elif confirmacion == 'N':
                print()
                break
            else: 
                print("Ingrese una opción válida")
                
    return None

def devolver_ejemplar_libro():
    libro_a_devolver = input("Ingrese el nombre del libro que quiere devolver: ")
    libro_existe = False
    for libro in libros:
        if libro["titulo"] == libro_a_devolver:
            libro_existe = True
            if libro["cant_ej_pr"] > 0:
                print("Se ha gestionado la devolución correctamente.")
                libro["cant_ej_pr"] -= 1
                return None
            else:
                print("No existen ejemplares prestados para el libro ingresado.")
                return None

    if not libro_existe:
        while True: 
            confirmacion = input("El libro no existe en la biblioteca. ¿Desea agregarlo? (S/N)").strip().upper()
            if confirmacion == 'S':
                nuevo_libro = l.nuevo_libro(libro_a_devolver)
                if nuevo_libro != None:libros.append(nuevo_libro)
                break
            elif confirmacion == 'N':
                print()
                break
            else: 
                print("Ingrese una opción válida")
                
    return None
# Espera hasta que se presione cualquier tecla
def pause():
    print("Presione cualquier tecla para continuar...")
    msvcrt.getch().strip()