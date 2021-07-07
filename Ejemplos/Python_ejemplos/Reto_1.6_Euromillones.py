#  Reto de Tema 6 del Curso de Python de Afredo Sanchez Sanchez
import random
def sorteo():
	numeros=[]
	num_max=50
	for n in range(5+2):  #incluye las dos estrellas
		# añadiendo numeros premiados
		# NO tiene que estar en la lista actual
		# generamos numero
		numero=random.randint(1,num_max)
		# generamos nuevo numero mientra este en la lisna numeros
		while numero in numeros:
			numero=random.randint(1,num_max)
		# si he llegado aqui es que no esta
		numeros.append(numero)
		if n<5:
			numeros.sort()
	return(numeros)

print("Bienvenido a tu eleccion de numeros para Euromillones\n\n")
while True:
	combinaciones=input("¿Cuantas combinaciones quieres generar? ")
	try:
		combinaciones=int(combinaciones)
		break
	except ValueError:  # Identificamos el error de NO numero
		print("Por favor, indica un valor posible.\n")

print("\nGenerando", combinaciones,"combinaciones")
for n in range(combinaciones):
	print("Combinacion",n+1,"\n")
	numeros_premiados=sorteo()
	# Control print(numeros_premiados)
	print("Numeros premiados:", numeros_premiados[:5])
	print("Estrellas", numeros_premiados[5:7],"\n")