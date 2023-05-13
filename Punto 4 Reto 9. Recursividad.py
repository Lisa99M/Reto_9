def potencia_recursiva(n : int , x: int)-> float:
  
  # Caso base 
  if n == 1 and x == 0: 
    result = 1
    return result
  elif x == 1:
    result = n
    return result
  elif x < 0: 
    result = 1/n*potencia_recursiva(n,x-1)
  else:
    return n*potencia_recursiva(n,x-1)

if __name__ == "__main__":
  n = int(input("Ingrese numero para la base: "))
  x = int(input("Ingrese número para el exponente: "))
  print(str(n) + " elevado a la " + str(x) + " es: " + str(potencia_recursiva(n,x)))


 