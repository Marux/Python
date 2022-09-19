import alumno as a
import asignaturas as b

def listas ():
	print('..::.. Notas por asignaturas ..::..')
	print('Datos personales del Alumno:')
	print(a.alumno)
	print('Las notas de Matematica son: ',b.mate)
	print('Las notas de Lenguaje y Comunicacion son: ',b.lengu)
	print('Las notas de Historia y Geografia son: ',b.histo)
	return listas

def lista2():
	promedio = [[b.promeate],[b.promehis],[b.promelen]]
	menor = promedio[0]
	print('..::.. El promedio por asignatura ..::..')
	print('Matematicas: ',b.promeate)
	print('Lenguaje y Comunicacion: ',b.promelen)
	print('Historia y geografia: ',b.promehis)
	promedio.sort()
	menor = promedio[0]
	for n in promedio:
		print(n)
	print('El promedio de nota mas baja es: ', menor)
	return lista2

def lista3():
	if(b.promeate[0] >= 4):
		print('Felicitaciones! Aprobo Matematicas con promedio: ', b.promeate)
	if(b.promelen[0] >= 4):
		print('Felicitaciones! Aprobo Lenguaje con promedio:  ', b.promelen)
	if(b.promehis[0] >= 4):
		print('Felicitaciones! Aprobo Historia con promedio: ', b.promehis)

def borrar():
	a.alumno.clear()
	b.promeate.clear()
	b.promelen.clear()
	b.promehis.clear()
	b.mate.clear()
	b.lengu.clear()
	b.histo.clear()
	print('Se han vaciado todos los datos exitosamente.')
	return borrar
