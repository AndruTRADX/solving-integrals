import numpy as np

def f(x):
    """
    Definición de la función f(x) para la cual se desea calcular la integral.
    """
    return 1 / np.sqrt(1 + x)

def regla_simpson(a, b, n):
    """
    Aproxima el valor de la integral definida de f(x) entre a y b utilizando la Regla de Simpson.

    Parámetros:
        a (float): Límite inferior del intervalo de integración.
        b (float): Límite superior del intervalo de integración.
        n (int): Número de subintervalos.

    Retorna:
        float: Aproximación del valor de la integral definida.
    """
    # Calcula el ancho de cada subintervalo
    delta_x = (b - a) / n
    # print("\nPaso 1: Ancho de cada subintervalo (ΔX) =", delta_x)
    
    # Inicializa la suma de las áreas de los subintervalos
    area = 0
    
    # Itera sobre los subintervalos utilizando la Regla de Simpson
    for i in range(n):
        # Calcula los límites del subintervalo
        x0 = a + i * delta_x
        x1 = a + (i + 1) * delta_x
        xm = (x0 + x1) / 2
        

        # Calcula el área bajo la parábola utilizando la Regla de Simpson
        # print("\nárea de la parabola ≈ DeltaX / 6 (f(x0) + 4 * f(xm) + f(x1)) ≈ {delta_x} / 6 (f({x0}) + 4 * f({xm}) + f({x1}))")
        area += delta_x / 6 * (f(x0) + 4 * f(xm) + f(x1))

    
    return area

# Límites del intervalo de integración
a = 0
b = 2

# Número de subintervalos
n = 12

# Calcula la aproximación de la integral utilizando la Regla de Simpson
aproximacion_integral = regla_simpson(a, b, n)
print("\nAproximación de la integral definida ≈ ", aproximacion_integral)
