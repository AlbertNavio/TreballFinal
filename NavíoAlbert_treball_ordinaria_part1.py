import sqlite3

# Cream la connexio i el cursor per llegir la base de dades
connexio = sqlite3.connect("Notes.db")
cursor = connexio.cursor()

# Obtenim la llista de alumnes
cursor.execute("SELECT * FROM Notes")
alumnes = cursor.fetchall()

# Variable per procesar cada fila o registre de la BD
registre = 0

# Bucle per obtenir les dades de cada registre 
while registre < len(alumnes):
    alumne = alumnes[registre]
    nom = alumne[1]
    curs = alumne[2]
    notes = alumne[3:]

    # Variables per procesar totes les notes d'un mateix alumne
    cont = 0
    suma_notes = 0

    # Bucle per sumar totes les notes d'un mateix alumne
    while cont < len(notes):
        suma_notes += notes[cont]
        cont += 1

    # Calcul de la mitjana de notes
    mitjana = suma_notes / len(notes)

    # Mostram el nom de l'alumne, el seu curs i la seva mitjana de notes
    print("Mitjana "+str(nom)+" de "+str(curs)+" "+str(mitjana))

    registre += 1

# Tancam la conexio amb la BD
connexio.close()
