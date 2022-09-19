alumno = []
def alumnos ():
	print('[:::: Registro de Alumno ::::]')
	#CURSO
	curso = input('Ingrese letra del curso: ')
	alumno.append('Curso: '+ curso)
	#RUT
	rut = input('Ingrese RUT del alumno: ')
	alumno.append('RUT: ' + rut)
	#Nombre
	nombre = input('Ingrese nombre del alumno: ')
	alumno.append('Nombre: ' + nombre)
	#Apellido Paterno
	apellido = input('Ingrese apellido paterno del alumno: ')
	alumno.append('Apellido Paterno: ' + apellido)
	#Apellido materno
	apellidom = input('Ingrese apellido materno del alumno: ')
	alumno.append('Apellido Materno: ' + apellidom)
	#Datos a mostrar
	print('[:::: Se a registrado a siguente alumno :::::]')
	print(alumno)
	return alumnos
