mate = []
promeate = []
def matematicas ():
	print('[:::: INGRESO DE NOTAS MATEMATICAS ::::]')
	suma = 0
	for contador in range(3):
		print('ingrese notas del alumno: ', contador+1)
		nota=int(input())
		mate.append(nota)
		suma+=nota
	promedio = suma / 3
	promeate.append(promedio)
	print('Notas ingresadas en Matematicas son: ')
	print('Nota 1: ', mate[0])
	print('Nota 2: ', mate[1])
	print('Nota 3: ', mate[2])
	print('______________________________________________')
	print('El promedio de la Asignatura: ', promeate)
	return mate

lengu = []
promelen = []
def lenguaje ():
	print('[:::: INGRESO DE NOTAS LENGUAJE Y COMUNICACION ::::]')
	suma = 0
	for contador in range(3):
		print('ingrese notas del alumno: ', contador+1)
		nota=int(input())
		lengu.append(nota)
		suma+=nota
	promedio = suma / 3
	promelen.append(promedio)
	print('Notas ingresadas en Lenguaje y Comunicacion son: ')
	print('Nota 1: ', lengu[0])
	print('Nota 2: ', lengu[1])
	print('Nota 3: ', lengu[2])
	print('______________________________________________')
	print('El promedio de la Asignatura: ', promelen)
	return lenguaje


histo = []
promehis = []
def historia():
	print('[:::: INGRESO DE NOTAS HISTORIA Y GEOGRAFIA ::::]')
	suma = 0
	for contador in range(3):
		print('ingrese notas del alumno: ', contador+1)
		nota=int(input())
		histo.append(nota)
		suma+=nota
	promedio = suma / 3
	promehis.append(promedio)
	print('Notas ingresadas en Historia y Geografia son: ')
	print('Nota 1: ', histo[0])
	print('Nota 2: ', histo[1])
	print('Nota 3: ', histo[2])
	print('______________________________________________')
	print('El promedio de la Asignatura: ', promehis)
	return historia
