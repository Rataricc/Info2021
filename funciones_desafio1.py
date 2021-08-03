"""
Desafio 1: Funciones: 
		150 años es el tiempo que tarda una bolsa de plastico comun en degradarse y una botella de PET
		puede tardar 1.000 años en desaparecer.

		Por otro lado los Envases de tetabrik pueden tardar hasta 30 años en degradarse. 

		Un trozo de chicle tarda 5 años en degradarse.

		Se solicita una funcion para que dado el ingreso de un elemento, se solicite tipo: Bolsa 
		de plastico, botella PET, envase tetabrik o chicle, e imprima la cantidad de años que tarda en
		degradarse.
"""




import time
def degradacion(elemento):
	if elemento == 1: 
		return 150
	elif elemento == 2: 
		return 1000
	elif elemento == 3: 
		return 30 
	elif elemento == 4: 
		return 5

def menu():
	print("") 
	print("                                  ¡Salvemos nuetro planeta!.\n")
	print("¿Quiere saber cuales son los objetos que mas tardan de degradarse una ves que los desechamos\n" + 
		"a la via publica?...\n")
	print("Mira nuetro menu, elige una opcion y fijate la informacion que hay.\n")
	for x in ["Menu: ", "1 - Bolsa de Plastico.", "2 - Envase de PET.","3 - Botella de Tetabrik.", "4 - Chicle.",
		"0 - Salir."]:
		time.sleep(1.5)
		print(x)
	return input()

es_valido = False
salio = False 

while not es_valido and not salio: 
	opcion = menu()
	if not opcion.isdigit(): 
		opcion = menu()
		continue
	opcion = int(opcion)
	if opcion == 0: 
		salio = True
	elif opcion >= 5: 
		continue
	else: 
		es_valido = True

if es_valido and not salio: 
	obtener_degradacion = degradacion(opcion)
	print("")
	print("El Material ingresado demora %s años en degradarse." % (obtener_degradacion))