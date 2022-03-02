# Funciones [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.2

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con funciones

# --------------------------------
# Aquí dentro definir la función que solicitará
# el nombre de tres invitados
# def generar_invitados():

from re import I


def cantidad_invitados():
    invitados_cantidad = int(input("¿Cuántos invitados desea ingresar?:\n"))
    return invitados_cantidad


def generar_invitados(invitados):
    input('EMPECEMOS')
    lista_invitados =[] #lista para almacenar invitados empieza vacia
    for i in range(invitados):
        nombre = input(f'Nombre del invitado, {i + 1}:\n')
        lista_invitados.append(nombre)
    return lista_invitados
# --------------------------------


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python\n")
    print('Hola, vamos a crear una lista de invitados\n')
    # Alumno: Crear la función "generar_invitados"
    
    # Dentro de esa función el sistema deberá solicitar
    # al usuario por consola que ingrese tres nombres de 
    # tres invitados.
    # IMPORTANTE: Utilizar un "input" por cada invitado
    # que se solicite ingresar
    
    # Los tres nombres ingresados se deberán guardar en
    # una lista

    # La función generar_invitados deberá retornar
    # la lista de invitados generados

    # NOTA: Recomendamos utilizar bucles para no repetir código
    # y solicitar los 3 invitiados, uno en cada iteración del bucle

    # Luego de crear la función invocarla en este lugar:
    invitados = cantidad_invitados()
    print(f'Ingresaremos {invitados} invitados.')
    
    lista_completa = generar_invitados(invitados)
    
    # Imprimir en pantalla "lista_invitados":

    print(f'Su lista de invitados {lista_completa}\n')
    
    print("terminamos")
