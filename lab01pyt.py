#"Codigo Realizado Por Rolando Alvarado para el curso de Analisis de datos en ADA SCHOOL"
'''
Define una variable de cada tipo de primitivo
Concatena a la cadena las otras variables aplicando la conversión correcta para funcionar, guarda el resultado en una 
variable
Investiga sobre el límite de los enteros y los flotantes en python y anotar sus descubrimientos como comentarios en el archivo
Aplica la fórmula de la suma de los primeros n números pares (investigar), tomando como n la variable de tipo entero y almacenar el resultado en una variable
Imprimir los resultados de las tareas anteriores
Envía el link del archivo en el repositorio con las respuesta
'''
# Variables de diferentes tipos
cadena = "Hola, mi nombre es Rolando Alvarado "
entero = 15
flotante = 3.1416
booleano = True
# Concatenación de variables
resultado_concatenacion = cadena + " " + str(entero) + " " + str(flotante) + " " + str(booleano)
print(resultado_concatenacion)
# Límite de enteros
limite_enteros = "El límite de los enteros en Python es " + str(pow(2, 31) - 1)  # Para plataformas de 32 bits
print("El limite de un numero entero en python es:", limite_enteros)
#Pow sirve para elevar un numero a una potencia 
# Límite de flotantes
#Los float a diferencia de los int tienen unos valores mínimo y máximos que pueden representar.
# La mínima precisión es 2.2250738585072014e-308 y la máxima 1.7976931348623157e+308
import sys
print("El limite minimo de un numero flotante es",sys.float_info.min) #2.2250738585072014e-308
print("El limite maximo de un numero flotante es",sys.float_info.max) #1.7976931348623157e+308

# Define la variable n
n = int(input("Escribe un número: "))

# Inicializa la variable suma con 0(variable auxiliar para la suma)
suma = 0

# Itera desde 2 hasta n, sumando cada número par a la variable suma
for i in range(2, n + 1, 2):
  suma += i

# Imprime el resultado
print("La suma de los primeros", n, "números pares es", suma)
