#!/usr/bin/env python
# coding: utf-8

# # Identifiants

# In[ ]:


import psycopg2
import re


# In[ ]:


# Benjamin
arguments = "dbname='benji' user='benji' host='localhost' password=''"


# In[ ]:


# Léna
arguments = "dbname='léna' user='benji' host='localhost' password=''"


# In[ ]:


# Louis
arguments = "dbname='nf18' user='root' host='localhost' password=''"


# In[ ]:


# Rodolphe
arguments = "dbname='rodolpheolommer' user='rodolpheolommer' host='localhost' password='' port=5433"


# # I. Le code

# In[ ]:


def run(sql,args):
    conn = psycopg2.connect(arguments)
    cur = conn.cursor()
    cur.execute(sql,args)

    if cur.description: # Si la requête renvoie des informations (e.g. SELECT)
        results = cur.fetchall()
    else:
        results = False

    conn.commit()
    cur.close()
    conn.close()
    return results


# ### 1. Ajout d'une association 

# In[ ]:


# PROGRAMME PYTHON TYPE CREER ASSOCIATION (à dériver sous toutes ses formes pour faire les autres fonctions)

def addAssociation():
    
    # Renseignement du nom
    nom = input('Nom de l\'association : ')
    
    # Vérification du nom
    foundAsso = run('SELECT * FROM association WHERE nom=%s',(nom,))
    
    while foundAsso:
        print(f'Le nom \'{nom}\' est déjà pris...\n')
        nom = input('Nom de l\'association : ')
        foundAsso = run('SELECT * FROM association WHERE nom=%s',(nom,))
    
    # Renseignement des autres champs
    description = input('Description : ')
    categorie = input('Catégorie : ')
    email = input('Adresse email : ')
    dateCreation = input('Date de création (DD/MM/YYYY) : ')
    
    while not re.match("[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]", dateCreation):
        dateCreation = input('Veuillez saisir une date au format DD/MM/YYYY...\n\nDate de création (DD/MM/YYYY) : ')

    site = input('Site web (ENTRÉE si aucun) : ')
    site = None if site == '' else site
    
    insert = 'INSERT INTO association VALUES (%s, %s, %s, %s, TO_DATE(%s, \'DD/MM/YYYY\'), %s)'
    run(insert,(nom,description,categorie,email,dateCreation,site))
    print(f'\nL\'association {nom} a été ajoutée avec succès')
    return 

addAssociation()


# ### 2. Ajout d'une personne 

# In[ ]:


def addPersonne():
    
    # choix personnel, etu, autre
    print('Choisissez le type de personne à ajouter :\n  1: Étudiant\n  2: Personnel\n  3: Extérieur\n  4: Retour au menu\n\n')
    
    choix = input('Votre choix : ')
        
    if choix == '1': # Etudiant
        print('addEtudiant()')
    elif choix == '2': # Personnel
        print('addPersonnel()')
    elif choix == '3': # Exterieur
        print('addExterieur()')
    elif choix != '4': # Retour
        print('Veuillez saisir un nombre entre 1 et 4.')
        addPersonne()

    return

addPersonne()


# In[ ]:


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

addEtudiant()


# In[ ]:


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

    statut_dic = {'1' : 'Enseignant', '2' : 'Personnel Administratif', '3' : 'Personnel Technique'}
    
    while True: 
        
        # Affichage des statuts disponibles
        print('Statut : ')
        for key in statut_dic:
            print(f'  {key}: {statut_dic[key]}')

        # Choix d'un statut
        choix = input('\nVotre choix : ')
        
        # Si le choix est valide, on sort
        if choix in statut_dic.keys():
            break
            
        print('Veuillez saisir un numéro entre 1 et 3...')
    
    statut = statut_dic[choix]
    
    # Ajout du personnel
    idPersonne = run('INSERT INTO personne (nom, prenom) VALUES (%s,%s) RETURNING idPersonne', (nom, prenom))[0][0]
    run('INSERT INTO personnel VALUES (%s,%s,%s)',(idPersonne, numCIN,statut))
    print(f'Le personnel suivant a bien été ajouté :\nID : {idPersonne}\n{prenom} {nom}\nCIN : {numCIN}\nStatut : {statut}')
    
    return

addPersonnel()


# In[ ]:


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

addExterieur()


# ### 3. Ajout d'un spectacle 

# In[ ]:


def addSpectacle():
    
    # choix concert, théâtre, stand-up
    print('Choisissez le type de spectacle à créer :\n  1: Concert\n  2: Théâtre\n  3: Stand-Up\n  4: Retour au menu\n\n')
    
    choix = input('Votre choix : ')
        
    if choix == '1': # Concert
        addConcert()
    elif choix == '2': # Théâtre
        addTheatre()
    elif choix == '3': # Stand-Up
        addStandUp()
    elif choix != '4': # Retour
        print('Veuillez saisir un nombre entre 1 et 4.')
        addSpectacle()

    return

addSpectacle()


# In[ ]:


def addConcert():

    # Vérification des associations
    foundAsso = run('SELECT * FROM association',())
    
    if not foundAsso:
        print('Vous n\'avez créé aucune association...')
        return
    
    # Renseignement des champs
    compositeur = input('Compositeur : ') 
    genre = input('Genre : ') 
    duree = input('Durée (ex 1:30) : ') 
    
    while not re.match('[0-9][0-9]?:[0-9][0-9]', duree):
        duree = input('Veuillez saisir une durée au format HH:MM...\n\nDurée (ex 1:30) : ')
    
    anneeParution = input('Année de parution : ')
    
    # Choix d'une association
    assos_dict = {}
    print('Association en charge :')
    for cpt, asso in enumerate(foundAsso):
        print(f'  {cpt+1}: {asso[0]}')
        assos_dict[cpt+1] = asso[0]
    
    choix = int(input('\nVotre choix : '))
    while choix > cpt+1 or choix < 1:
        choix = int(input(f'\nVeuillez saisir un nombre entre 1 et {cpt+1}... \n\nVotre choix : '))
    
    association = assos_dict[choix]
    
    # Ajout du concert
    idSpectacle = run('INSERT INTO spectacle (duree, nomAsso) VALUES (TO_TIMESTAMP(%s, \'HH24:MI\'),%s) RETURNING idSpectacle', (duree, association))[0][0]
    run('INSERT INTO concert VALUES (%s,%s,%s,TO_TIMESTAMP(%s, \'YYYY\'))',(idSpectacle, compositeur, genre, anneeParution))
    print(f'Le concert suivant a bien été ajouté :\nID : {idSpectacle}\nCompositeur : {compositeur}\nGenre : {genre}\nDurée : {duree}\nAnnée de parution : {anneeParution}')
    
    return

addConcert()


# In[ ]:


def addTheatre():

    # Vérification des associations
    foundAsso = run('SELECT * FROM association',())
    
    if not foundAsso:
        print('Vous n\'avez créé aucune association...')
        return
    
    # Renseignement des champs
    auteur = input('Auteur : ') 
    genre = input('Genre : ') 
    duree = input('Durée (ex 1:30) : ') 
    
    while not re.match('[0-9][0-9]?:[0-9][0-9]', duree):
        duree = input('Veuillez saisir une durée au format HH:MM...\n\nDurée (ex 1:30) : ')
    
    anneeParution = input('Année de parution : ')
    
    # Choix d'une association
    assos_dict = {}
    print('Association en charge :')
    for cpt, asso in enumerate(foundAsso):
        print(f'  {cpt+1}: {asso[0]}')
        assos_dict[cpt+1] = asso[0]
    
    choix = int(input('\nVotre choix : '))
    while choix > cpt+1 or choix < 1:
        choix = int(input(f'\nVeuillez saisir un nombre entre 1 et {cpt+1}... \n\nVotre choix : '))
    
    association = assos_dict[choix]
    
    # Ajout de la pièce
    idSpectacle = run('INSERT INTO spectacle (duree, nomAsso) VALUES (TO_TIMESTAMP(%s, \'HH24:MI\'),%s) RETURNING idSpectacle', (duree, association))[0][0]
    run('INSERT INTO theatre VALUES (%s,%s,TO_TIMESTAMP(%s, \'YYYY\'),%s)',(idSpectacle, auteur, anneeParution, genre))
    print(f'La pièce de théâtre suivante a bien été ajoutée :\nID : {idSpectacle}\nAuteur : {auteur}\nGenre : {genre}\nDurée : {duree}\nAnnée de parution : {anneeParution}')
    
    return

addTheatre()


# In[ ]:


def addStandUp():

    # Vérification des associations
    foundAsso = run('SELECT * FROM association',())
    
    if not foundAsso:
        print('Vous n\'avez créé aucune association...')
        return
    
    # Renseignement des champs
    genre = input('Genre : ') 
    duree = input('Durée (ex 1:30) : ') 
    
    while not re.match('[0-9][0-9]?:[0-9][0-9]', duree):
        duree = input('Veuillez saisir une durée au format HH:MM...\n\nDurée (ex 1:30) : ')
        
    # Choix d'une association
    assos_dict = {}
    print('Association en charge :')
    for cpt, asso in enumerate(foundAsso):
        print(f'  {cpt+1}: {asso[0]}')
        assos_dict[cpt+1] = asso[0]
    
    choix = int(input('\nVotre choix : '))
    while choix > cpt+1 or choix < 1:
        choix = int(input(f'\nVeuillez saisir un nombre entre 1 et {cpt+1}... \n\nVotre choix : '))
    
    association = assos_dict[choix]
    
    # Ajout du stand-up
    idSpectacle = run('INSERT INTO spectacle (duree, nomAsso) VALUES (TO_TIMESTAMP(%s, \'HH24:MI\'),%s) RETURNING idSpectacle', (duree, association))[0][0]
    run('INSERT INTO standup VALUES (%s,%s)',(idSpectacle, genre))
    print(f'Le stand-up suivant a bien été ajouté :\nID : {idSpectacle}\nGenre : {genre}\nDurée : {duree}')
    
    return

addStandUp()


# ### 4. Ajout d'une salle 

# In[ ]:


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
    types_dic = {'1' : 'Cours', '2' : 'Amphitéâtre', '3' : 'Bureau'}
    while True: 
        
        # Affichage des types disponibles
        print('Type de la salle : ')
        for key in types_dic:
            print(f'  {key}: {types_dic[key]}')

        # Choix d'un statut
        choix = input('\nVotre choix : ')
        
        # Si le choix est valide, on sort
        if choix in types_dic.keys():
            break
            
        print('Veuillez saisir un numéro entre 1 et 3...')
    
    libelleType = types_dic[choix]
    
    run('insert into salle values (%s,%s)', (numSalle,capacite))
    run('insert into batiment values (%s)', (numBat))
    run('insert into typeSalle values (%s,%s,%s)', (numBat, numSalle, libelleType))
    
    print(f'La salle suivante a bien été ajoutée :\nNuméro : {numSalle}\nBâtiment : {numBat}\nCapacité : {capacite}\nType : {libelleType}')

    return

addSalle()


# ### 5. Ajout d'une séance 

# In[ ]:


def addSeance():
    
    # Vérification qu'il existe spectacle
    listSpect = run('SELECT * FROM spectacle_medium ORDER BY ID',())
    if not listSpect:
        print('Vous n\'avez créé aucun spectacle...')
        return
    
    # Choix de la date
    date = input("Date de la séance (ex 30/06/2021) : ")
        
    while not re.match("[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]", date):
        date = input('Veuillez saisir une date au format DD/MM/YYYY...\n\nDate de la séance (ex 30/06/2021) : ')
    
    # Choix de l'horaire
    horaireDebut = input('Horaire de début (ex 20:45) : ')   
        
    while not re.match('[0-9][0-9]?:[0-9][0-9]', horaireDebut):
        horaireDebut = input('Veuillez saisir un horaire au format HH:MM...\n\nHoraire du début (ex 20:45) : ')
    
    # Choix du spectacle
    print('Spectacle représenté :\n\n\tID\tOrganisateur\tduree\tgenre\tspectacle\t')    
    id_list = []
    for spectacle in listSpect:
        print(f'\t{spectacle[0]}\t{spectacle[1]}\t{spectacle[2]}\t{spectacle[3]}\t{spectacle[4]}\t')
        id_list.append(spectacle[0])
    
    idSpectacle = int(input('\nID du spectacle : '))
    while idSpectacle not in id_list:
        idSpectacle = int(input(f'\nVeuillez saisir un des IDs de la première colonne... \n\nVotre choix : '))
    
    # Choix de la salle
    listSalle = run('select * from typesalle',())
    
    print('Choix de la salle :\n\n\tBatiment\tSalle\tType\t')    
    bat_list = []
    salle_list = []
    
    # Affichage des salles disponibles
    for salle in listSalle:
        print(f'\t{salle[0]}\t{salle[1]}\t{salle[2]}\t')
        bat_list.append(str(salle[0]))
        salle_list.append(str(salle[1]))
    
    while True:
        
        # Choix du batiment
        numBat = input('Numéro du bâtiment : ')
        if numBat not in bat_list:
            print('Veuillez saisir le numéro d\'un des bâtiments de la liste...')
            continue
            
         # Choix du numéro de salle
        numSalle = input('Numéro de la salle : ')
        if numSalle not in salle_list:
            print('Veuillez choisit un numéro de salle valide...')
            continue
        else:
            break
    
    idSeance = run('insert into seance(date, horairedebut, idspectacle, numbat, numsalle) values (TO_DATE(%s,\'DD/MM/YYYY\'), TO_TIMESTAMP(%s, \'HH24:MI\'), %s,%s,%s) returning idSeance', (date, horaireDebut, idSpectacle, numBat, numSalle))[0][0]
    
    print(f'La séance suivante a bien été ajoutée :\ID : {idSeance}\nDate : {date}\nHoraire : {horaireDebut}\nSpectacle : {idSpectacle}\nSalle {numSalle}, bâtiment {numBat}')

    return

addSeance()


# ### 6. Ajout d'un billet 

# In[ ]:


def addBillet():
    
    # Vérification qu'il existe au moins un utilisateur et une séance
    listPers = run('SELECT * FROM personne ORDER BY idPersonne',())
    listSeance = run('select idseance, date, horaireDebut, numBat, numSalle, categorie from seance se, spectacle_medium sp where id = idSpectacle;',())

    if not listPers:
        print('Veuillez d\'abord ajouter un utilisateur...')
        return
    
    if not listSeance:
        print('Veuillez d\'abord ajouter une séance...')
        return
    
    # Choix de l'acheteur
    print('ID de l\'acheteur :\n\tID\tNom\tPrénom\t')

    id_list = []
    for personne in listPers:
        print(f'\t{personne[0]}\t{personne[1]}\t{personne[2]}\t')
        id_list.append(personne[0])
    
    idPersonne = int(input('\nID choisi : '))
    while idPersonne not in id_list:
        idPersonne = int(input(f'Veuillez saisir un des IDs de la première colonne... \n\nID choisi : '))
 
    # Choix de la séance
    print('ID de la séance :\n\tID\tDate\tHeure\tSalle\tBâtiment\tCatégorie\t')

    id_list = []
    for seance in listSeance:
        print(f'\t{seance[0]}\t{seance[1]}\t{seance[2]}\t{seance[3]}\t{seance[4]}\t{seance[5]}\t')
        id_list.append(seance[0])
    
    idSeance = int(input('\nID choisi : '))
    while idSeance not in id_list:
        idSeance = int(input(f'Veuillez saisir un des IDs de la première colonne... \n\nID choisi : '))
 
    # Choix de la catégorie
    categorie_dic = {'1' : 'Invitation', '2' : 'Billet Étudiant', '3' : 'Billet Personnel', '4' : 'Billet Extérieur'}

    while True: 
        
        # Affichage des statuts disponibles
        print('Catégories :')
        for key in categorie_dic:
            print(f'  {key}: {categorie_dic[key]}')

        # Choix d'une catégorie
        choix = input('\nVotre choix : ')
        
        # Si le choix est valide, on sort
        if choix in categorie_dic.keys():
            break
            
        print('Numéro choisi incorrect...\n')
    
    categorie = categorie_dic[choix]

    # Choix du tarif
    tarif = input('\nTarif (ex 25.3 pour 25€30, 22 pour 22€00) : ' )

    while not re.match('[0-9][0-9]?[0-9]?([.][0-9][0-9]?)?', tarif):
        tarif = input('Saisie non reconnue...\n\nTarif (ex 25.3 pour 25€30, 22 pour 22€00) : ')
    
    dateCreation = date.today().strftime("%d/%m/%Y")
    
    # Ajout du billet
    idBillet = run('insert into billet(categorie, dateCreation, tarif, idSeance, idAcheteur) values (%s, TO_DATE(%s,\'DD/MM/YYYY\'), %s,%s,%s) returning idBillet', (categorie, dateCreation, tarif, idSeance, idPersonne))[0][0]
    
    print(f'Le billet suivant a bien été créé :\ID : {idBillet}\nDate de Création : {dateCreation}\nTarif : {tarif}€\nSéance : {idSeance}\nAcheteur {idPersonne}')

    return

addBillet()

