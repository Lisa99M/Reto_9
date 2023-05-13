if __name__ == "__main__":
  list = []
  for i in range (5):
    n = int(input("Insertar numeros para calcular promedio: "))
    list.append(n)
promedio = (lambda n: sum(list)/5)(n)
print("El promedio de los números ingresados es: " + str(promedio))