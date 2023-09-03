import cod_generator as cod_gen

# Crear un diccionario para cada libro
libro1 = {'cod': 'CRBJsAkS', 'cant_ej_ad': 3, 'cant_ej_pr': 1, "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez"}
libro2 = {'cod': 'QgfV4j3c', 'cant_ej_ad': 4, 'cant_ej_pr': 2, "titulo": "El principito", "autor": "Antoine de Saint-Exupéry"}
libro3 = {'cod': 'adOd09UE', 'cant_ej_ad': 1, 'cant_ej_pr': 0, "titulo": "El código Da Vinci", "autor": "Dan Brown"}

def nuevo_libro():
    cod = generar_codigo()
    while True:
        cant_ej_ad = int(input("Ingrese la cantidad de ejemplares adquiridos: "))
        cant_ej_pr = int(input("Ingrese la cantidad de ejemplares prestados: "))
        if cant_ej_ad < cant_ej_pr:
            print("La cantidad de unidades prestadas no puede ser mayor a los ejemplares adquiridos, intente nuevamente")
        else:
            break
    titulo = input("Ingrese el título del libro :")
    autor = input("Ingrese el autor del libro: ")
    print("El libro agregado se titula " + titulo + ", del autor " + autor + ", el código es " + cod + ". hay " + str(cant_ej_ad) + " ejemplares disponibles y " + str(cant_ej_pr) + " ejemplares prestados")
    print()
    print("--------------------------------------------------------")
    print()
    libro = {'cod': cod, 'cant_ej_ad': cant_ej_ad, 'cant_ej_pr': cant_ej_pr, "titulo": titulo, "autor": autor }
    return libro

def generar_codigo():
    
    return cod_gen.generar()
