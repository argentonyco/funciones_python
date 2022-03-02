# Funciones [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.2

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con funciones

    # La función promedio recibe como parámetro una
    # lista de números. Con ella calcule el promedio como:

    # promedio = sumatoria_numeros / cantidad_numeros

    # Resuelva la sumatoria y la cantidad con las herramientas
    # que desee, recomendamos usar las funciones disponibles
    # de Python para ello:    
    # sum --> obtener la sumatoria de números
    # len --> obtener la cantidad de números

    # La función debe retornar (return) el promedio calculado
    # La función debe contemplar si se le pasa una lista vacia
    # (es decir, de "0" elementos)

def promedio(numeros):
    print("Funcion promedio")

    # nuevo_promedio = 0
    
    if len(numeros) == 0:
        return 'Lista vacia'
    else:
        promedio = sum(numeros) / len(numeros) 
        return promedio    
          
if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    numeros = []

    # Alumno: Complete la función "promedio"

    # Llamar a la función en este lugar y capturar el valor del retorno
    
    #promedio(numeros)

    # Luego imprimir en pantalla el valor resultante:
    
    nuevo_promedio = promedio(numeros)
    print(f'El valor resultante es: {nuevo_promedio}')
        
    print("terminamos")


