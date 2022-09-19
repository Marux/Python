def menu():
	print('______________________________________________')
	print('.::.::. MENU PRINCIPAL .::.::.')
	print('1- Registro datos del alumno.')
	print('2- Ingreso de notas del alumno.')
	print('______________________________________________')
	print('3- Lista de notas del alumno por asignatura.')
	print('4- Agignatura con promedio de nota mas baja.')
	print('5- Promedios con nota igual o mayor a 4.')
	print('9- Digite 9 para borrar los datos del alumno.')
	print('0- Digite 0 para salir del programa.')
	print('______________________________________________')
	op = int(input())
	return op
	
def submenu():
	print('______________________________________________')
	print('.:::. ELIGA UNA ASIGNATURA .:::.')
	print('1- Matematicas.')
	print('2- Lenguaje y comunicacion.')
	print('3- Historia y Geografia.')
	print('0- Para volver a menu principal digite 0.')
	print('______________________________________________')
	op2 = int(input())
	return op2
