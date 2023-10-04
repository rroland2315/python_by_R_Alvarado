from math import sqrt

def std(values: str) -> float:
    # Convertir la cadena de números a una lista de enteros
    numbers = [int(num) for num in values.split()]

    # Calcular la media
    mean = sum(numbers) / len(numbers)

    # Calcular la suma de los cuadrados de las diferencias con la media
    squared_diff = sum((num - mean)**2 for num in numbers)

    # Calcular la varianza
    variance = squared_diff / len(numbers)

    # Calcular la desviación estándar
    std_deviation = sqrt(variance)

    # Redondear a un decimal con un margen de error de ±0.1
    rounded_std_deviation = round(std_deviation, 1)

    return rounded_std_deviation

# Ejemplo de uso
input_values = "10 40 30 50 20"
result = std(input_values)
print(result)
