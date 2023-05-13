# De los retos anteriores seleciones 3 funciones y escribalas con argumentos no definidos (*args).

#Diseñar una función que permita calcular una aproximación de la función exponencial alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. nota: use math para traer la función exponencial y mostrar la diferencia entre el valor real y la aproximación.

import math
def exponential_function (*args) -> float:
    summation = 0
    for i in range (n):
       summation += math.pow(x, i) / math.factorial(i)
    return summation


if __name__ == "__main__":
  n = (int(input(" Number of the term of Maclaurin series: ")))
  x = (float(input("Real value to calculate the approximation of the exponential fucntion around 0: ")))
  
print("Result using created funtion:"+ str(exponential_function (x, n)))
print("Result using function imported from math:"+ str(math.exp(x))) 
difference = math.exp(x) - exponential_function (x, n)
print("The difference between the actual value and the approximation is: " + str(difference))
