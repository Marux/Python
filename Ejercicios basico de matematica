print('  ________      .__             .___          _____  .__                       .__  __                        ')
print(' /  _____/ __ __|__|____      __| _/____     /  _  \ |  |    ____   ___________|__|/  |_  _____   ____  ______')
print('/   \  ___|  |  \  \__  \    / __ |/ __ \   /  /_\  \|  |   / ___\ /  _ \_  __ \  \   __\/     \ /  _ \/  ___/')
print('\    \_\  \  |  /  |/ __ \_ / /_/ \  ___/  /    |    \  |__/ /_/  >  <_> )  | \/  ||  | |  Y Y  (  <_> )___ \ ')
print(' \______  /____/|__(____  / \____ |\___  > \____|__  /____/\___  / \____/|__|  |__||__| |__|_|  /\____/____  >')
print('        \/              \/       \/    \/          \/     /_____/                             \/           \/ ')

def menu ():
	print('(1) Sacar promedio de 3 notas')
	print('(2) Compara tres valores y determinar cual es el mayor')
	print('(3) Suma de enteros entre el 0 al 10')
	print('(4) Determine si un numero ingresado es par o impar')
	print('(5) Compara dos numeros para saber el mayor o menor')
	print('(6) Transformar KM/s a MT/s')
	print('(7) Promediar cierta cantidad de notas, este se detendra en si digita 0')
	print('(0) precione 0 para salir')

menu ()
options = int(input('Ingrese la opcion a ejecutar: '))

while options!=0:
	if options == 1:
		
		print('ingrese nota 1: ')
		n1 = int(input())

		print('ingrese nota 2 : ')
		n2 = int(input())

		print('ingrese nota 3 : ')
		n3 = int(input())

		suma = float(n1 + n2 + n3)

		promedio = suma / 3

		print('El promedio de las 3 notas es: ', promedio)

		if(promedio >= 4): 
			print('Aprobo')
			if(promedio >= 5.5):
				print('Se exime de la prueba')
		else:
			print('Reprobo')
			
	if options == 2:
		
		print('Ingrese Valor A')
		A = int(input())

		print('Ingrese Valor B')
		B = int(input())

		print('Ingrese Valor C')
		C = int(input())

		if(A==B or A==C or B==C):
			print('ingrese valores distintos')
		if A!=B and A!=C and B!=C:
			if(A>B):
				if(A>C):
					print('el numero mayor a imprimir es: ', A)
			elif(B>C):
				print('el numero mayor a imprimir es: ', B)
			else: 
				print('el numero mayor a imprimir es: ', C)

	if options == 3:
		
		suma = 0

		for i in range (10):
			suma = suma + i+1
		print('La suma de de los numeros enteros entre el 1 al 10 son: ', suma)

	if options == 4:
		
		print('Determine si el numero ingresado es par o impar')
		n1 = int(input())

		resultado = n1 % 2

		if resultado == 1:
			print('El numero ingresado es numero impar')
		else:
			print('El numero ingresado es numero par')

	if options == 5:
		
		print('Ingrese dos numero distintos para determinar cual es el mayor:')
		n1 = int(input())
		n2 = int(input())

		i = n1==n2

		if i:
			print('No ingreso dos numeros distintos.')
		if n1!=n2:
			if(n1>n2):
				print('El numero mayor es: ', n1 , ' El numero menos es: ' , n2)
			else:
				print('El numero mayor es: ', n2 , 'El numero menor es: ', n1 )
				
	if options == 6:
				
		print('Transformar Km/h a Mt/s')
		print('Ingrese Km/h:')
		kh = int(input())

		if kh > 0:
			ms = kh / 3.6
			print('La cantidad de km/h a m/s es: ', ms)
		else:
			print('Favor reingresar numero enteros')
	
	if options == 7:
		print('Ingrese notas a promediar')
		print('Este Finalizara cuando digite 0:')
		suma = 0
		contador = 0
		ev = True
		while(ev):
			numero = int(input())
			
			if(numero !=0):
				suma = float (suma + numero)
				contador = contador + 1
				
			else:
				ev = False
		if(suma == 0):
			print('No ingreso numeros')
		else:
			promedio = suma / contador
			print('El promedio es: ', promedio)	


	"""print de abajo para separa"""
	print()
	menu()
	print('Ingrese opcion a ejecutar: ')
	options = int(input())
print('________________________________________')
print('Gracias por preferir mi programa')
print('________________________________________')
print('Victor Trimpai')
print('Analista Programador -  Vespertino')
print('IP Santo Tomas - Sede San joaquin')
print('________________________________________')
