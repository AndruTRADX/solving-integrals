# Ejemplo de uso:
import math

"""
    Calcula una aproximación del área bajo la curva de la función dada utilizando la regla del trapecio.

    Args:
    funcion: La función de la que se desea aproximar el área bajo la curva.
    a: El límite inferior del intervalo.
    b: El límite superior del intervalo.
    n: El número de subintervalos a utilizar.

    Returns:
    La aproximación del área bajo la curva.
    """
def regla_del_trapecio(funcion, a, b, n):
    delta_x = (b - a) / n
    # print("Delta de x = {}".format(delta_x))
    suma_trapecios = 0.0
    counter = 1

    for i in range(n):
        

        x0 = a + i * delta_x
        x1 = a + (i + 1) * delta_x
        area_trapecio = delta_x * (funcion(x0) + funcion(x1)) / 2

        # print("T{} = f({}) + f({}) / 2 = {}".format(counter, x0, x1, area_trapecio))

        counter += 1
        suma_trapecios += area_trapecio
    return suma_trapecios

# Definición de la función 
def funcion_integral(x):
    return 1 / math.sqrt(1 + x)

# Intervalo [a, b]
a = 0
b = 2

# Número de subintervalos
n = 12

# Aproximación del área bajo la curva de la función_ejemplo en el intervalo [a, b]
area_aproximada = regla_del_trapecio(funcion_integral, a, b, n)
print("Aproximación del área bajo la curva:", area_aproximada)