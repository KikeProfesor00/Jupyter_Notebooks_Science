elementos={"C":12,"H":1,"O":16,"N":14}
print ("El diccionario es: ",elementos,"\n")
for elemento in elementos:
	print("El elemento "+elemento,"tiene como masa atomica:",elementos[elemento])
while True:
	elem=input("\nDe que elemento deseas saber su masa atomica (Fin para acabar)? ")
	if elem == "fin":
		print("\n\nHasta la proxima")
		exit()
	try:
		print("\nLa masa atomica del",elem, "es", elementos[elem])
	except KeyError:  #  identificamos el error especifico
		print("\nLo tecleado es incorrecto")