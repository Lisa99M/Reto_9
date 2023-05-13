#plantilla de code para contar el tiempo
import time

start_time = time.time()
def fibo(n : int )-> int:
  i : int = 1
  # caso base
  n1 : int = 0
  n2 : int = 1
  while(i <= n):
    # Condicion
    sumFibo = n1 + n2
    print(sumFibo)
    # Actualizacion
    n1 = n2
    n2 = sumFibo
    i += 1
  return sumFibo

if __name__ == "__main__":
  num = int(input("Ingrese numero: "))
  serieFibo = fibo(num)
  print("La serie de Fibonacci hasta " + str(num) + " es " + str(serieFibo))
# instrucciones sobre las cuales se quiere medir tiempo de ejecución
end_time = time.time()

timer1 = end_time - start_time
print("Tiempo: " + str(timer1))


start_time = time.time()
# instrucciones sobre las cuales se quiere medir tiempo de ejecución
def fiboRecursivo(n : int )-> int:
  if n <=1:
    # caso base
    return 1
  else:
    # condicion
    return fiboRecursivo(n-1)+fiboRecursivo(n-2)  

if __name__ == "__main__":
  num = int(input("Ingrese numero: "))
  serieFibo = fiboRecursivo(num)
  print("La serie de Fibonacci hasta " + str(num) + " es " + str(serieFibo))
end_time = time.time()

timer2 = end_time - start_time
print("Tiempo: " + str(timer2))

if timer2 - timer1 > 0.1:
  print("La diferencia entre iteración y recursión es significativa para " + str(num))
else:
  print("La diferencia entre iteración y recursión no es significativa para " + str(num))
