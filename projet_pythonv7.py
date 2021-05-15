##### A CHANGER  #####

arguments = "dbname='dbnf18p073' user='nf18p073' host='tuxa.sme.utc' password='96ScTkSo'"

######################

import psycopg2
import re
from datetime import date

def run(sql,args):
    conn = psycopg2.connect(arguments)
    cur = conn.cursor()
    try:
        pass
    except Exception as e:
        raise
    cur.execute(sql,args)

    if cur.description: # Si la requête renvoie des informations (e.g. SELECT)
        results = cur.fetchall()
    else:
        results = False

    conn.commit()
    cur.close()
    conn.close()
    return results


def isDate(str):
    return (re.match('[0-9]{2}/[0-9]{2}/[0-9]{4}', str) and int(str[0:2]) <= 31 and int(str[3:5]) <= 12)


def isTime(str):
    if re.match('[0-9][0-9]?:[0-9][0-9]', str) :
        if str[1] == ':' and int(str[0:1]) <= 23 and int(str[2:4]) <= 59 :
            return True
        elif str[1] != ':' and int(str[0:2]) <= 23 and int(str[3:5]) <= 59 :
            return True
        else:
            return False


def isYear(str):
    return (re.match('[0-9]{4}', str))


def isPrice(str):
    return re.match('[0-9]{1,3}(\.[0-9])?[0-9]?', str)


def inputDate(inputMessage):
    dateInput = input(inputMessage)

    while not isDate(dateInput):
        dateInput = input('Veuillez saisir une date au format DD/MM/YYYY...\n\n' + inputMessage)

    return dateInput


def inputTime(inputMessage):
    timeInput = input(inputMessage)

    while not isTime(timeInput):
        timeInput = input('Veuillez saisir un horaire au format HH:MM...\n\n' + inputMessage)

    return timeInput


def inputYear(inputMessage):
    yearInput = input(inputMessage)

    while not isYear(yearInput):
        yearInput = input('Veuillez saisir une année au format YYYY...\n\n' + inputMessage)

    return yearInput


def inputFromDict(dict):

    while True:

        # Affichage des choix disponibles
        for key in dict:
            print(f'  {key}: {dict[key]}')

        # Input d'un choix
        choix = input('\nVotre choix : ')

        # Si le choix est valide, on sort
        if choix in dict.keys():
            return dict[choix]

        print('Numéro choisi incorrect...\n')


def inputPrice(inputMessage):
    priceInput = input(inputMessage)

    while not isPrice(priceInput):
        priceInput = input('Saisie Invalide ...\n\n' + inputMessage)

    return priceInput


def printTable(table, header_list, width_list, length):

    # Affichage du header
    for i in range(len(header_list)):
        print(f'| {str(header_list[i]):{width_list[i]}}', end = " ")
    print('|')
    
    # Ligne de séparation
    for _ in range(length):
        print('-', end='')
    print()

    # Affichage du corps
    id_list = []
    for row in table:
        for i in range(len(row)):
            print(f'| {str(row[i]):{width_list[i]}}', end = " ")
        print('|')
        
        id_list.append(str(row[0]))
    
    return id_list


def chooseSpectacle():
    
    # Vérification qu'il existe un spectacle
    listSpect = run('SELECT * FROM spectacle_medium ORDER BY ID',())
    if not listSpect:
        print('Vous n\'avez créé aucun spectacle...')
        return

    print('Choisissez le spectacle :\n')
    
    # Affichage des spectacles
    header_list = ['ID', 'Organisateur', 'Durée', 'Genre', 'Catégorie']
    width_list = [4, 15, 8, 12, 9]
    length = 64
    id_list = printTable(listSpect, header_list, width_list, length)
    
    # Choix du spectacle
    idSpectacle = input('\nID du spectacle : ')
    while idSpectacle not in id_list:
        idSpectacle = input('Veuillez saisir un des IDs de la première colonne... \n\nVotre choix : ')

    return int(idSpectacle)


def printSpectacle():
    
    # Vérification qu'il existe un spectacle
    listSpect = run('SELECT * FROM spectacle_medium ORDER BY ID',())
    if not listSpect:
        print('Vous n\'avez créé aucun spectacle...')
        return
    
    # Affichage des spectacles
    header_list = ['ID', 'Organisateur', 'Durée', 'Genre', 'Catégorie']
    width_list = [4, 15, 8, 12, 9]
    length = 64
    id_list = printTable(listSpect, header_list, width_list, length)
    
    return


def chooseAssociation():
    
    # Vérification qu'il existe une association
    listAsso = run('SELECT nom, description FROM association ORDER BY nom',())
    if not listAsso:
        print('Vous n\'avez créé aucune association...')
        return

    print('Choisissez l\'association :\n')
    
    # Affichage des associations
    header_list = ['Nom', 'Description']
    width_list = [15, 50]
    length = 72
    id_list = printTable(listAsso, header_list, width_list, length)
    
    # Choix de l'association
    nomAsso = input('\nNom : ')
    while nomAsso not in id_list:
        nomAsso = input('Veuillez saisir un des noms de la première colonne... \n\nVotre choix : ')

    return nomAsso


def printAssociation():
    
    # Vérification qu'il existe une association
    listAsso = run('SELECT nom, description, categorie FROM association ORDER BY nom',())
    if not listAsso:
        print('Vous n\'avez créé aucune association...')
        return
    
    # Affichage des associations
    header_list = ['Nom', 'Description','Catégorie']
    width_list = [15, 50,15]
    length = 90
    id_list = printTable(listAsso, header_list, width_list, length)
    
    return 


def chooseSalle():
    
    # Vérification qu'il existe un batiment
    listBat = run('SELECT * FROM batiment ORDER BY numBat',())
    if not listBat:
        print('Vous n\'avez créé aucun batiment...')
        return
    
    print('Choisissez le bâtiment :\n')
    
    # Affichage des batiments
    header_list = ['Numéro']
    width_list = [8]
    length = 12
    id_list = printTable(listBat, header_list, width_list, length)
        
    # Choix du batiment
    numBat = input('\nNuméro : ')
    while numBat not in id_list:
        numBat = input('Veuillez saisir un numéro valide... \n\nVotre choix : ')

    # Vérification qu'il existe une salle
    listSalle = run('SELECT numsalle, libelletype FROM typesalle WHERE numBat=%s ORDER BY numSalle',(numBat))
    if not listSalle:
        print('Il n\'existe aucune salle dans ce batiment...')
        return
    
    print('Choisissez la salle dans ce bâtiment :\n')

    # Affichage des salles
    header_list = ['Numéro', 'Type']
    width_list = [8, 11]
    length = 26
    id_list = printTable(listSalle, header_list, width_list, length)    
    
    # Choix de la salle
    numSalle = input('\nNuméro : ')
    while numSalle not in id_list:
        numSalle = input('Veuillez saisir un numéro valide... \n\nVotre choix : ')

    return int(numBat), int(numSalle)


def printSalle():
    
    # Vérification qu'il existe un batiment
    listSalle = run('SELECT * FROM typesalle ORDER BY numBat',())
    if not listSalle:
        print('Vous n\'avez créé aucune salle...')
        return

    # Affichage des salles
    header_list = ['Bâtiment', 'Numéro', 'Type']
    width_list = [8, 8, 11]
    length = 37
    id_list = printTable(listSalle, header_list, width_list, length)    
    
    return


def choosePersonne():
    
    # Vérification qu'il existe une personne
    listPers = run('SELECT * FROM personne ORDER BY idPersonne',())
    if not listPers:
        print('Il n\'existe aucun utilisateur dans la base...')
        return

    print('Choisissez le propriétaire du billet :\n')
    
    # Affichage des personnes
    header_list = ['ID', 'Nom', 'Prénom']
    width_list = [4, 16, 16]
    length = 46
    id_list = printTable(listPers, header_list, width_list, length)
    
    # Choix de la personne
    idPers = input('\nID de la personne : ')
    while idPers not in id_list:
        idPers = input('Veuillez saisir un des IDs de la première colonne... \n\nVotre choix : ')

    return int(idPers)

def printPersonne():
    
    # Vérification qu'il existe une personne
    listPers = run('SELECT * FROM personne_medium ORDER BY id',())
    if not listPers:
        print('Il n\'existe aucun utilisateur dans la base...')
        return
    
    # Affichage des personnes
    header_list = ['ID', 'Nom', 'Prénom', 'Catégorie']
    width_list = [4, 16, 16,10]
    length = 59
    printTable(listPers, header_list, width_list, length)
    
    return


def chooseEtudiant():
    
    # Vérification qu'il existe une personne
    listPers = run('SELECT p.idPersonne, p.nom, p.prenom FROM personne p, etudiant e where e.idPersonne = p.idPersonne ORDER BY idPersonne',())
    if not listPers:
        print('Il n\'existe aucun étudiant dans la base...')
        return

    print('Choisissez l\'étudiant :\n')
    
    # Affichage des personnes
    header_list = ['ID', 'Nom', 'Prénom']
    width_list = [4, 16, 16]
    length = 46
    id_list = printTable(listPers, header_list, width_list, length)
    
    # Choix de la personne
    idPers = input('\nID de l\'étufiant : ')
    while idPers not in id_list:
        idPers = input('Veuillez saisir un des IDs de la première colonne... \n\nVotre choix : ')

    return int(idPers)


def choosePersonnel():
    
    # Vérification qu'il existe un personnel
    listPers = run('SELECT p.idPersonne, p.nom, p.prenom FROM personne p, personnel where personnel.idPersonne = p.idPersonne ORDER BY idPersonne',())
    if not listPers:
        print('Il n\'existe aucun personnel dans la base...')
        return

    print('Choisissez le personnel :\n')
    
    # Affichage des personnes
    header_list = ['ID', 'Nom', 'Prénom']
    width_list = [4, 16, 16]
    length = 46
    id_list = printTable(listPers, header_list, width_list, length)
    
    # Choix de la personne
    idPers = input('\nID du personnel : ')
    while idPers not in id_list:
        idPers = input('Veuillez saisir un des IDs de la première colonne... \n\nVotre choix : ')

    return int(idPers)


def chooseSeance():
    
    # Vérification qu'il existe une séance
    listSeance = run('select idseance, date, horaireDebut, numBat, numSalle, categorie from seance se, spectacle_medium sp where id = idSpectacle;',())

    if not listSeance:
        print('Il n\'existe aucune séance...')
        return

    print('Choisissez la séance :\n')
    
    # Affichage des séances
    header_list = ['ID', 'Date', 'Heure', 'Salle', 'Bâtiment', 'Catégorie']
    width_list = [3, 10, 8, 6, 8, 12]
    length = 66
    id_list = printTable(listSeance, header_list, width_list, length)
    
    # Choix de la séance
    idSeance = input('\nID de la séance : ')
    while idSeance not in id_list:
        idSeance = input('Veuillez saisir un des IDs de la première colonne... \n\nVotre choix : ')

    return int(idSeance)


def chooseGenreConcert():
    
    # Vérification qu'il existe un genre
    listgenre = run('SELECT * FROM genreconcert',())
    if not listgenre:
        print('Il n\'y a aucun genre de concert prédéfini...')
        return

    print('Choisissez le genre :\n')
    
    # Affichage des genres
    header_list = ['Nom']
    width_list = [14]
    length = 18
    id_list = printTable(listgenre, header_list, width_list, length)
    
    # Choix du genre
    nomGenre = input('\nNom du genre : ')
    while nomGenre not in id_list:
        nomGenre = input('Veuillez saisir un des noms de la première colonne... \n\nVotre choix : ')

    return nomGenre


def chooseGenreTheatre():
    
    # Vérification qu'il existe un genre
    listgenre = run('SELECT * FROM genretheatre',())
    if not listgenre:
        print('Il n\'y a aucun genre prédéfini pour les pièces de théâtre ...')
        return

    print('Choisissez le genre :\n')
    
    # Affichage des genres
    header_list = ['Nom']
    width_list = [14]
    length = 18
    id_list = printTable(listgenre, header_list, width_list, length)
    
    # Choix du genre
    nomGenre = input('\nNom du genre : ')
    while nomGenre not in id_list:
        nomGenre = input('Veuillez saisir un des noms de la première colonne... \n\nVotre choix : ')

    return nomGenre


def chooseGenreStandUp():
    
    # Vérification qu'il existe un genre
    listgenre = run('SELECT * FROM genrestandup',())
    if not listgenre:
        print('Il n\'y a aucun genre prédéfini pour le Stand-Up ...')
        return

    print('Choisissez le genre :\n')
    
    # Affichage des genres
    header_list = ['Nom']
    width_list = [14]
    length = 18
    id_list = printTable(listgenre, header_list, width_list, length)
    
    # Choix du genre
    nomGenre = input('\nNom du genre : ')
    while nomGenre not in id_list:
        nomGenre = input('Veuillez saisir un des noms de la première colonne... \n\nVotre choix : ')

    return nomGenre


def chooseCategorie():
    
    # Vérification qu'il existe une catégorie
    listCat = run('SELECT * FROM categorie',())
    if not listCat:
        print('Il n\'y a aucune catégorie de billet prédéfinie dans la base...')
        return

    print('Choisissez la catégorie :\n')
    
    # Affichage des catégories
    header_list = ['Nom']
    width_list = [18]
    length = 22
    id_list = printTable(listCat, header_list, width_list, length)
    
    # Choix du genre
    nomCat = input('\nNom de la catégorie : ')
    while nomCat not in id_list:
        nomCat = input('Veuillez saisir un des noms de la première colonne... \n\nVotre choix : ')

    return nomCat



# ### 1. Ajout d'une association

def addAssociation():

    # Renseignement du nom
    nom = input('Nom de l\'association : ')

    # Vérification du nom
    foundAsso = run('SELECT * FROM association WHERE nom=%s',(nom,))

    while foundAsso:
        print(f'Le nom \'{nom}\' est déjà pris...\n')
        nom = input('Nom de l\'association : ')
        foundAsso = run('SELECT * FROM association WHERE nom=%s',(nom,))

    print('Qui sera président de cette association ?')
    idPresident = chooseEtudiant()

    print('Qui sera trésorier de cette association ?')
    idTresorier = chooseEtudiant()

    # Renseignement des autres champs
    description = input('Description l\'association : ')
    categorie = input('Catégorie : ')
    email = input('Adresse email : ')
    dateCreation = inputDate('Date de création (DD/MM/YYYY) : ')

    site = input('Site web (ENTRÉE si aucun) : ')
    site = None if site == '' else site

    insert = 'INSERT INTO association VALUES (%s, %s, %s, %s, TO_DATE(%s, \'DD/MM/YYYY\'), %s)'
    run(insert,(nom,description,categorie,email,dateCreation,site))
    run('insert into compose values (%s, %s, %s)', (idPresident, nom, 'Président'))
    run('insert into compose values (%s, %s, %s)', (idTresorier, nom, 'Trésorier'))

    print(f'\nL\'association {nom} a été ajoutée avec succès')
    
    return


# ### 2. Ajout d'une personne

def addPersonne():

    # choix personnel, etu, autre
    print('Choisissez le type de personne à ajouter :\n  1: Étudiant\n  2: Personnel\n  3: Extérieur\n  4: Retour au menu\n\n')

    choix = input('Votre choix : ')

    if choix == '1': # Etudiant
        print('\nAjout d\'un etudiant :')
        addEtudiant()
        
    elif choix == '2': # Personnel
        print('\nAjout d\'un membre du personnel :')
        addPersonnel()
    elif choix == '3': # Exterieur
        print('\nAjout d\'un membre extérieur :')
        addExterieur()
    elif choix != '4': # Retour
        print('Veuillez saisir un nombre entre 1 et 4.')
        addPersonne()

    return


def addEtudiant():

    # Renseignement du numéro CIN
    numCIN = input('Numéro CIN : ')

    # Vérification du numero CIN
    foundCIN = run('SELECT numeroCIN FROM etudiant WHERE numeroCIN=%s UNION SELECT numeroCIN FROM personnel WHERE numeroCIN=%s',(numCIN,numCIN))

    while foundCIN:
        print(f'Le numéro CIN \'{numCIN}\' est déjà pris...\n')
        numCIN = input('Numéro CIN : ')
        foundCIN = run('SELECT numeroCIN FROM etudiant WHERE numeroCIN=%s UNION SELECT numeroCIN FROM personnel WHERE numeroCIN=%s',(numCIN,numCIN))

    # Renseignement des autres champs
    nom = input('Nom : ')
    prenom = input('Prénom : ')

    # Ajout de l'étudiant
    idPersonne = run('INSERT INTO personne (nom, prenom) VALUES (%s,%s) RETURNING idPersonne', (nom, prenom))[0][0]
    run('INSERT INTO etudiant VALUES (%s,%s)',(idPersonne, numCIN))
    print(f'L\'étudiant suivant a bien été ajouté :\nID : {idPersonne}\n{prenom} {nom}\nCIN : {numCIN}')

    return


def addPersonnel():

    # Renseignement du numéro CIN
    numCIN = input('Numéro CIN : ')

    # Vérification du numero CIN
    foundCIN = run('SELECT numeroCIN FROM etudiant WHERE numeroCIN=%s UNION SELECT numeroCIN FROM personnel WHERE numeroCIN=%s',(numCIN,numCIN))

    while foundCIN:
        print(f'Le numéro CIN \'{numCIN}\' est déjà pris...\n')
        numCIN = input('Numéro CIN : ')
        foundCIN = run('SELECT numeroCIN FROM etudiant WHERE numeroCIN=%s UNION SELECT numeroCIN FROM personnel WHERE numeroCIN=%s',(numCIN,numCIN))

    # Renseignement des autres champs
    nom = input('Nom : ')
    prenom = input('Prénom : ')

    print('Statut : ')
    statut_dic = {'1' : 'Enseignant', '2' : 'Personnel Administratif', '3' : 'Personnel Technique'}
    statut = inputFromDict(statut_dic)

    # Ajout du personnel
    idPersonne = run('INSERT INTO personne (nom, prenom) VALUES (%s,%s) RETURNING idPersonne', (nom, prenom))[0][0]
    run('INSERT INTO personnel VALUES (%s,%s,%s)',(idPersonne, numCIN,statut))
    print(f'Le personnel suivant a bien été ajouté :\nID : {idPersonne}\n{prenom} {nom}\nCIN : {numCIN}\nStatut : {statut}')

    return


def addExterieur():

    # Renseignement du contact
    contact = input('Numéro de téléphone : ')

    # Vérification du contact
    foundExt = run('SELECT * FROM exterieur WHERE contact=%s',(contact,))

    while foundExt:
        print(f'Le numéro \'{contact}\' existe déjà...\n')
        contact = input('Numéro de téléphone : ')
        foundExt = run('SELECT * FROM exterieur WHERE contact=%s',(contact,))

    # Renseignement des autres champs
    nom = input('Nom : ')
    prenom = input('Prénom : ')
    organisme = input('Organisme de la personne exterieure : ')

    # Ajout de la personne extérieure
    idPersonne = run('INSERT INTO personne (nom, prenom) VALUES (%s,%s) RETURNING idPersonne', (nom, prenom))[0][0]
    run('INSERT INTO exterieur VALUES (%s,%s,%s)',(idPersonne, organisme, contact))
    print(f'La personne suivante a bien été ajoutée :\nID : {idPersonne}\n{prenom} {nom}\n{organisme}\n{contact}')

    return


# ### 3. Ajout d'un spectacle


def addSpectacle():
    association = chooseAssociation()

    while True:

        # choix concert, théâtre, stand-up
        print('Choisissez le type de spectacle à créer :\n  1: Concert\n  2: Théâtre\n  3: Stand-Up\n  4: Retour au menu\n')

        choix = input('Votre choix : ')

        if choix == '1': # Concert
            print('\nAjout d\'un concert :')
            addConcert(association)
            return
        elif choix == '2': # Théâtre
            print('\nAjout d\'une pièce de théâtre :')
            addTheatre(association)
            return
        elif choix == '3': # Stand-Up
            print('\nAjout d\'un Stand-Up :')
            addStandUp(association)
            return
        elif choix == '4': # Retour
            return
        else:
            print('Veuillez saisir un nombre entre 1 et 4.')


def addConcert(association):

    # Renseignement des champs
    compositeur = input('Compositeur : ')
    genre = chooseGenreConcert()
    duree = inputTime('Durée (ex 1:30) : ')
    anneeParution = inputYear('Année de parution : ')

    # Ajout du concert
    idSpectacle = run('INSERT INTO spectacle (duree, nomAsso) VALUES (TO_TIMESTAMP(%s, \'HH24:MI\'),%s) RETURNING idSpectacle', (duree, association))[0][0]
    run('INSERT INTO concert VALUES (%s,%s,%s,TO_TIMESTAMP(%s, \'YYYY\'))',(idSpectacle, compositeur, genre, anneeParution))
    print(f'Le concert suivant a bien été ajouté :\nID : {idSpectacle}\nCompositeur : {compositeur}\nGenre : {genre}\nDurée : {duree}\nAnnée de parution : {anneeParution}')

    return


def addTheatre(association):

    # Renseignement des champs
    auteur = input('Auteur : ')
    genre = chooseGenreTheatre()
    duree = inputTime('Durée (ex 1:30) : ')
    anneeParution = inputYear('Année de parution : ')

    # Ajout de la pièce
    idSpectacle = run('INSERT INTO spectacle (duree, nomAsso) VALUES (TO_TIMESTAMP(%s, \'HH24:MI\'),%s) RETURNING idSpectacle', (duree, association))[0][0]
    run('INSERT INTO theatre VALUES (%s,%s,TO_TIMESTAMP(%s, \'YYYY\'),%s)',(idSpectacle, auteur, anneeParution, genre))
    print(f'La pièce de théâtre suivante a bien été ajoutée :\nID : {idSpectacle}\nAuteur : {auteur}\nGenre : {genre}\nDurée : {duree}\nAnnée de parution : {anneeParution}')

    return


def addStandUp(association):

    # Renseignement des champs
    genre = chooseGenreStandUp()
    duree = inputTime('Durée (ex 1:30) : ')

    # Ajout du stand-up
    idSpectacle = run('INSERT INTO spectacle (duree, nomAsso) VALUES (TO_TIMESTAMP(%s, \'HH24:MI\'),%s) RETURNING idSpectacle', (duree, association))[0][0]
    run('INSERT INTO standup VALUES (%s,%s)',(idSpectacle, genre))
    print(f'Le stand-up suivant a bien été ajouté :\nID : {idSpectacle}\nGenre : {genre}\nDurée : {duree}')

    return


# ### 4. Ajout d'une salle

def addSalle():

    # Renseignement des champs
    numSalle = input('Numero de la Salle : ')
    capacite = input('Capacité : ')
    numBat = input('Numéro du batiment : ')

    # Vérification de la salle
    foundSalle = run('SELECT * FROM typesalle where numBat=%s AND numSalle=%s',(numBat, numSalle))

    if foundSalle:
        print(f'La salle \'{numSalle}\' existe déjà dans le bâtiment {numBat}')
        return

    # Renseignement du type
    print('Type de la salle : ')
    types_dic = {'1' : 'Cours', '2' : 'Amphitéâtre', '3' : 'Bureau'}
    libelleType = inputFromDict(types_dic)

    # Création de la salle
    run('insert into salle values (%s,%s)', (numSalle,capacite))
    run('insert into batiment values (%s)', (numBat))
    run('insert into typeSalle values (%s,%s,%s)', (numBat, numSalle, libelleType))

    print(f'La salle suivante a bien été ajoutée :\nNuméro : {numSalle}\nBâtiment : {numBat}\nCapacité : {capacite}\nType : {libelleType}')

    return


# ### 5. Ajout d'une séance

def addSeance():

    idSpectacle = chooseSpectacle()
    numBat, numSalle = chooseSalle()
    date = inputDate("Date de la séance (ex 30/06/2021) : ")
    horaireDebut = inputTime('Horaire de début (ex 20:45) : ')
    idSeance = run('insert into seance(date, horairedebut, idspectacle, numbat, numsalle) values (TO_DATE(%s,\'DD/MM/YYYY\'), TO_TIMESTAMP(%s, \'HH24:MI\'), %s,%s,%s) returning idSeance', (date, horaireDebut, idSpectacle, numBat, numSalle))[0][0]

    print(f'La séance suivante a bien été ajoutée :\nID : {idSeance}\nDate : {date}\nHoraire : {horaireDebut}\nSpectacle : {idSpectacle}\nSalle {numSalle}, bâtiment {numBat}')

    return


# ### 6. Ajout d'un billet

def addBillet():

    # Choix de la personne
    idPersonne = choosePersonne()

    # Choix de la séance
    idSeance = chooseSeance()

    # Choix de la catégorie
    categorie = chooseCategorie()

    # Choix du tarif
    tarif = inputPrice('\nTarif (ex 25.3 pour 25€30, 22 pour 22€00) : ' )
    dateCreation = date.today().strftime("%d/%m/%Y")

    # Ajout du billet
    idBillet = run('insert into billet(categorie, dateCreation, tarif, idSeance, idAcheteur) values (%s, TO_DATE(%s,\'DD/MM/YYYY\'), %s,%s,%s) returning idBillet', (categorie, dateCreation, tarif, idSeance, idPersonne))[0][0]

    print(f'Le billet suivant a bien été créé :\nID : {idBillet}\nDate de Création : {dateCreation}\nTarif : {tarif}€\nSéance : {idSeance}\nAcheteur {idPersonne}')

    return

def addReservation():

    # Renseignement des différents champs
    association = chooseAssociation()
    numBat, numSalle = chooseSalle()
    date = inputDate("Date de la réservation (ex 30/06/2021) : ")

    foundReservation = run('SELECT * FROM reservation WHERE numBat=%s AND numSalle=%s AND date=TO_DATE(%s,\'DD/MM/YYYY\') ',(numBat, numSalle, date))

    if foundReservation:
        print(f'Désolé, cette salle est déjà le soir du {date}')
        return 

    # Ajout de la réservation
    run('insert into reservation values (%s, %s, %s, TO_DATE(%s,\'DD/MM/YYYY\'))', (association, numSalle, numBat, date))

    print(f'La salle {numSalle}, Bâtiment {numBat} a bien été réservée')

    return

def addCompose():

    # Renseignement des différents champs
    association = chooseAssociation()
    idEtudiant = chooseEtudiant()

    foundEtu = run('SELECT * FROM compose WHERE idEtudiant=%s AND nomAsso=%s',(idEtudiant, association))

    if foundEtu:
        print(f'Cet étudiant est déjà inscrit à {association}')
        return 

    # Ajout de l'étudiant
    run('insert into compose values (%s, %s, %s)', (idEtudiant, association, 'Membre'))

    print(f'L\'étudiant {idEtudiant} a bien été inscrit à {association}')

    return

def addParticipeEtudiant():

    # Renseignement des différents champs
    idEtudiant = chooseEtudiant()
    idSpectacle = chooseSpectacle()

    role = input('Rôle de l\'étudiant dans le spectacle : ')

    foundEtu = run('SELECT * FROM participeetudiant WHERE idEtudiant=%s AND idSpectacle=%s',(idEtudiant, idSpectacle))

    if foundEtu:
        print(f'Cet étudiant participe déjà au spectacle n°{idSpectacle}')
        return 

    # Ajout de l'étudiant
    run('insert into participeetudiant values (%s, %s, %s)', (idEtudiant, idSpectacle, role))

    print(f'L\'étudiant {idEtudiant} a bien été inscrit au spectacle n°{idSpectacle}')

    return

def addParticipePersonnel():

    # Renseignement des différents champs
    idPersonnel = choosePersonnel()
    idSpectacle = chooseSpectacle()

    role = input('Rôle du personnel dans le spectacle : ')

    foundPers = run('SELECT * FROM participepersonnel WHERE idPersonnel=%s AND idSpectacle=%s',(idPersonnel, idSpectacle))

    if foundPers:
        print(f'Ce membre du personnel participe déjà au spectacle n°{idSpectacle}')
        return 

    # Ajout du personnel
    run('insert into participepersonnel values (%s, %s, %s)', (idPersonnel, idSpectacle, role))

    print(f'Le personnel n°{idPersonnel} a bien été inscrit au spectacle n°{idSpectacle}')

    return


def menuPrincipal():

    print('Bienvenue cher utilisateur !\n')
    while True :
        print('Que souhaitez vous faire ?')

        choix = input('  1: Gérer les utilisateurs\n  2: Gérer les spectacles\n  3: Gérer les salles\n  4: Gérer les associations\n  5: Quitter\n\nVotre choix : ')

        if choix == '1': # utilisateur
            print('Bienvenue dans la gestion des utilisateurs ! \n\nQue souhaitez-vous faire ?')

            while True:
                choixUser = input('  1: Ajouter un utilisateur\n  2: Afficher les utilisateurs\n  3: Retour\n\nVotre choix : ')

                if choixUser == '1':
                    print('\n*** Ajout d\'un utilisateur ***')
                    addPersonne()
                    break
                elif choixUser == '2':
                    print('\n*** Affichage des utilisateurs ***')
                    printPersonne()
                    break
                elif choixUser == '3':
                    break
                else:
                    print('Saisie non reconnue...')

        elif choix == '2': # spectacle
            
            print('Bienvenue dans la gestion des spectacles ! \n\nQue souhaitez-vous faire ?')

            while True:
                choixSpec = input('  1: Ajouter un spectacle\n  2: Afficher les spectacles\n  3: Ajouter une séance à un spectacle\n  4: Faire participer un étudiant à un spectacle\n  5: Faire participer un membre du personnel à un spectacle\n  6: Acheter un billet pour un spectacle\n  7: Retour\n\nVotre choix : ')

                if choixSpec == '1':
                    print('\n*** Ajout d\'un spectacle ***')
                    addSpectacle()
                    break
                elif choixSpec == '2':
                    print('\n*** Affichage des spectacles ***')
                    printSpectacle()
                    break
                elif choixSpec == '3':
                    print('\n*** Ajout d\'une séance ***')
                    addSeance()
                    break
                elif choixSpec == '4':
                    print('\n*** Ajout d\'un participant étudiant ***')
                    addParticipeEtudiant()
                    break
                elif choixSpec == '5':
                    print('\n*** Ajout d\'un participant du personnel ***')
                    addParticipePersonnel()
                    break
                elif choixSpec == '6':
                    print('\n*** Création d\'un billet ***')
                    addBillet()
                    break
                elif choixSpec == '7':
                    break
                else:
                    print('Saisie non reconnue...')

        elif choix == '3': # salle
            print('Bienvenue dans la gestion des salles ! \n\nQue souhaitez-vous faire ?')

            while True:
                choixSalle = input('  1: Ajouter une salle\n  2: Afficher la liste des salles\n  3: Réserver une salle\n  4: Retour\n\nVotre choix : ')

                if choixSalle == '1':
                    print('\n*** Ajout d\'une salle ***')
                    addSalle()
                    break
                elif choixSalle == '2':
                    print('\n*** Affichage salles ***')
                    printSalle()
                    break

                elif choixSalle == '3':
                    print('\n*** Réservation d\'une salle ***')
                    addReservation()
                    break
                elif choixSalle == '4':
                    break
                else:
                    print('Saisie non reconnue...')

        elif choix == '4': # association
            print('Bienvenue dans la gestion des associations ! \n\nQue souhaitez-vous faire ?')

            while True:
                choixAsso = input('  1: Ajouter une association\n  2: Afficher les associations\n  3: Inscrire un étudiant à une association\n  4: Retour\n\nVotre choix : ')

                if choixAsso == '1':
                    print('\n*** Ajout d\'une association ***')
                    addAssociation()
                    break
                elif choixAsso == '2':
                    print('\n*** Affichage des associations ***')
                    printAssociation()
                    break
                elif choixAsso == '3':
                    print('\n*** Inscription d\'un étudiant ***')
                    addCompose()
                    break
                elif choixAsso == '4':
                    break
                else:
                    print('Saisie non reconnue...')

        elif choix == '5': # Retour
            print('A bientôt :)')
            break
        else:
            print('Saisie non reconnue...')
        print('\n*** Menu Principal ***')

menuPrincipal()
