from estudiantes import Estudiante

estudiantes = []

for i in range(1, 5):
    estudiantes.append(Estudiante(i))
    estudiantes[i-1].start()