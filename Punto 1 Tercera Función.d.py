lista = []
for i in range(5):
    n = float(input("Insertar números reales: "))
    lista.append(n)

lista.sort()
potencia = lambda x, y: x ** y
resultado = potencia(lista[4], lista[0])
print("Potencia del mayor número elevado al menor número: " + str(resultado))
