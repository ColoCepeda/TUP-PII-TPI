import cod_generator as cod_gen

# Crear un diccionario para cada libro
libro1 = {'cod': 'CRBJsAkS', 'cant_ej_ad': 3, 'cant_ej_pr': 1, "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez"}
libro2 = {'cod': 'QgfV4j3c', 'cant_ej_ad': 4, 'cant_ej_pr': 2, "titulo": "El principito", "autor": "Antoine de Saint-Exupéry"}
libro3 = {'cod': 'adOd09UE', 'cant_ej_ad': 1, 'cant_ej_pr': 0, "titulo": "El código Da Vinci", "autor": "Dan Brown"}

def nuevo_libro():
    cod = generar_codigo()
    cant_ej_ad = int(input("Ingrese la cantidad de ejemplares disponibles: "))
    cant_ej_pr = int(input("Ingrese la cantidad de ejemplares prestados: "))
    titulo = input("Ingrese el título del libro :")
    autor = input("Ingrese el autor del libro: ")
    print("El libro que desea agregar se titula " + titulo + ", del autor " + autor + ", el código es " + cod)
    confirmacion = input(f"¿Desea confirmar el registro? (S/N): ").strip().upper()
    if confirmacion == 'S':
        libro = {'cod': cod, 'cant_ej_ad': cant_ej_ad, 'cant_ej_pr': cant_ej_pr, "titulo": titulo, "autor": autor }
        print("Operación realizada exitosamente.")
        return libro
    else:
        print("La operación ha sido cancelada")
        return None

def generar_codigo():
    
    return cod_gen.generar()
