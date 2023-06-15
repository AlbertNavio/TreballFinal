import sqlite3

# Conexión a la base de datos
conn = sqlite3.connect("Notes.db")
cursor = conn.cursor()

# Consulta para obtener la lista de alumnos
cursor.execute("SELECT * FROM Notes")
alumnos = cursor.fetchall()
# Cálculo de la media de las notas de cada alumno
registre = 0
while registre < len(alumnos):
    alumno = alumnos[registre]
    nombre = alumno[1]
    curso = alumno[2]
    notas = alumno[3:]

    cont = 0
    suma_notas = 0
    while cont < len(notas):
        suma_notas += notas[cont]
        cont += 1

    media = suma_notas / len(notas)

    # Imprimir la media de cada alumno
    if registre == 0:
        diccionari = {nombre: media}
    else:
        diccionari[nombre] = media
    #print(f"Mitjana {nombre} de {curso}: {media}")

    registre += 1
    
print(diccionari)
# Cerrar la conexión a la base de datos
conn.close()
