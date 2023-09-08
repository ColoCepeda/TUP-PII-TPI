import cod_generator as cod_gen

# Crear un diccionario para cada libro
libro1 = {'cod': 'CRBJsAkS', 'cant_ej_ad': 3, 'cant_ej_pr': 1, "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez"}
libro2 = {'cod': 'QgfV4j3c', 'cant_ej_ad': 4, 'cant_ej_pr': 2, "titulo": "El principito", "autor": "Antoine de Saint-Exupéry"}
libro3 = {'cod': 'adOd09UE', 'cant_ej_ad': 1, 'cant_ej_pr': 0, "titulo": "El código Da Vinci", "autor": "Dan Brown"}

def nuevo_libro(titulo):                                # Función que recibe el título del nuevo libro luego de validar que no exista
    
    cod = generar_codigo()
    while True:
        try:
            cant_ej_ad = int(input("Ingrese la cantidad de ejemplares adquiridos: "))           # Usamos try-except para validar que las cantidades ingresadas sean numéricas 
        except ValueError:                                                                      # En caso de error, el bucle se reinicia, si no hay error, el bucle se rompe mediante el break
            print("Debe ingresar un valor numérico")
            continue
        try:
            cant_ej_pr = int(input("Ingrese la cantidad de ejemplares prestados: "))
        except ValueError:
            print("Debe ingresar un valor numérico")
            continue
        if cant_ej_ad < cant_ej_pr:
            print("La cantidad de unidades prestadas no puede ser mayor a los ejemplares adquiridos, intente nuevamente")       # Validamos que la cantidad prestada no sea mayor a la adquirida
        else:
            break    
    autor = input("Ingrese el autor del libro: ")
    print("El libro a agregar se titula " + titulo + ", del autor " + autor + ", el código es " + cod + ". hay " + str(cant_ej_ad) + " ejemplares disponibles y " + str(cant_ej_pr) + " ejemplares prestados")
    print()
    print("--------------------------------------------------------")
    print()
    confirmacion = input(f"¿Desea confirmar el registro? (S/N): ").strip().upper()
    if confirmacion == 'S':
        libro = {'cod': cod, 'cant_ej_ad': cant_ej_ad, 'cant_ej_pr': cant_ej_pr, "titulo": titulo, "autor": autor }
        print("Operación realizada exitosamente.")
        return libro                                            # Devolvemos el libro a agregar a la lista
    else:
        print("La operación ha sido cancelada")                
        return None                                             # Devolvemos None si se cancela la operación
    
def generar_codigo():
    
    return cod_gen.generar()
