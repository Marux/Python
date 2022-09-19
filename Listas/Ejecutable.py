"""
Se necesita de un sistema que pueda ingresar las notas de un estudiante de un curso a sus respectivas asignaturas.
"""
print('______________________________________________________________')
print('   ________  __   ______  ____  ______')
print('  / __/ __ \/ /  / __/  |/  / |/ / __/')
print(' _\ \/ /_/ / /__/ _// /|_/ /    / _/  ')
print('/___/\____/____/___/_/  /_/_/|_/___/  ')
print('                                      ')
print('______________________________________________________________')
print('Estructuras De Datos Y Algoritmos')
print('Profesor:')
print('Juan Rodrigo Cabello Silva <jcabello2@santotomas.cl>')
print('______________________________________________________________')

import menu as m
import alumno as a
import asignaturas as b
import firma as f
import listas as l


op = True
while (op != 0):
	op = m.menu()
	
	if (op == 1):
		print('______________________________________________')
		a.alumnos()
		print('______________________________________________')
	elif (op == 2):
		print('______________________________________________')
		op2 = True
		while (op2 !=0):
			op2 = m.submenu()
			if (op2 ==1):
				print('______________________________________________')
				b.matematicas()
				print('______________________________________________')
			elif (op2 == 2):
				print('______________________________________________')
				b.lenguaje()
				print('______________________________________________')
			elif (op2 == 3):
				print('______________________________________________')
				b.historia()
				print('______________________________________________')
			else:
				print('______________________________________________')
	elif (op == 3):
		print('______________________________________________')
		l.listas()
		print('______________________________________________')
	elif (op == 4):
		print('______________________________________________')
		l.lista2()
		print('______________________________________________')
	elif (op == 5):
		print('______________________________________________')
		l.lista3()
		print('______________________________________________')
	elif (op == 9):
		print('______________________________________________')
		l.borrar()
		print('______________________________________________')	
	elif (op == 0):
		print('______________________________________________')
		print('A finalizado el programa')
		f.firma()
		print('______________________________________________')
	else:
		print('______________________________________________')
		print('Ingrese opcion valida.')
		print('______________________________________________')
