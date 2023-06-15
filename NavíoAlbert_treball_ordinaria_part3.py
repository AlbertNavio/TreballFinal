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

    # Si el registre a procesar es el primer, cream el diccionari amb les dades d'aquest registre
    # Si el registre no es el primer, afegim les noves dades al diccionari
    if registre == 0:
        diccionari = {nom: mitjana}
    else:
        diccionari[nom] = mitjana

    registre += 1

# Bucle FOR sobre el diccionari de notes per convertir la mitjana en nivells qualitatius
for clau in diccionari:
    valor = diccionari[clau]
    if valor <= 2.49:
        diccionari[clau] = "Novell"
    elif 2.5 <= valor <= 6.24:
        diccionari[clau] = "Aprenent"
    elif 6.25 <= valor <= 8.74:
        diccionari[clau] = "Avançat"
    else: 
        diccionari[clau] = "Expert"
 
# Mostram el contingut del diccionari    
print(diccionari)

# Tancam la conexio amb la BD
connexio.close()
