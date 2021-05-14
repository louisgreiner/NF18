DROP TABLE IF EXISTS association;
CREATE TABLE IF NOT EXISTS association (
  nom varchar(50) NOT NULL,
  description text NOT NULL,
  categorie varchar(50) NOT NULL,
  email varchar(100) NOT NULL,
  dateCreation date NOT NULL,
  siteWeb text,
  PRIMARY KEY (nom),
  UNIQUE(email)
) ;

--
-- Déchargement des données de la table association
--

INSERT INTO association (nom, description, categorie, email, dateCreation, siteWeb) VALUES
('test', 'test test', 'catest', 'test@test', '2010-05-05', 'test.com');

-- --------------------------------------------------------

--
-- Structure de la table batiment
--

DROP TABLE IF EXISTS batiment;
CREATE TABLE IF NOT EXISTS batiment (
  numBat int NOT NULL,
  PRIMARY KEY (numBat)
) ;

-- --------------------------------------------------------

--
-- Structure de la table billet
--

DROP TABLE IF EXISTS billet;
CREATE TABLE IF NOT EXISTS billet (
  idBillet SERIAL,
  categorie varchar(50) DEFAULT NULL,
  dateCreation date NOT NULL,
  tarif decimal(10,0) DEFAULT NULL,
  idSeance int DEFAULT NULL,
  idAcheteur int DEFAULT NULL,
  PRIMARY KEY (idBillet)
) ;

-- --------------------------------------------------------

--
-- Structure de la table categorie
--

DROP TABLE IF EXISTS categorie;
CREATE TABLE IF NOT EXISTS categorie (
  idSeance int NOT NULL,
  idBillet int NOT NULL,
  PRIMARY KEY (idSeance,idBillet),
  UNIQUE(idBillet)
) ;

-- --------------------------------------------------------

--
-- Structure de la table compose
--

DROP TABLE IF EXISTS compose;
CREATE TABLE IF NOT EXISTS compose (
  idEtudiant int NOT NULL,
  nomAsso varchar(100) NOT NULL,
  statut varchar(50) NOT NULL,
  PRIMARY KEY (idEtudiant,nomAsso),
  UNIQUE(nomAsso)
) ;

-- --------------------------------------------------------

--
-- Structure de la table concert
--

DROP TABLE IF EXISTS concert;
CREATE TABLE IF NOT EXISTS concert (
  idConcert int NOT NULL,
  compositeur varchar(100) NOT NULL,
  genre varchar(50) DEFAULT NULL,
  anneeParution date DEFAULT NULL,
  PRIMARY KEY (idConcert),
  UNIQUE(genre)
) ;

-- --------------------------------------------------------

--
-- Structure de la table etudiant
--

DROP TABLE IF EXISTS etudiant CASCADE;
CREATE TABLE IF NOT EXISTS etudiant (
  idPersonne int NOT NULL,
  numeroCIN int NOT NULL,
  PRIMARY KEY (idPersonne),
  UNIQUE(numeroCIN)
) ;

-- --------------------------------------------------------

--
-- Structure de la table exterieur
--

DROP TABLE IF EXISTS exterieur;
CREATE TABLE IF NOT EXISTS exterieur (
  idPersonne int NOT NULL,
  organisme varchar(50) NOT NULL,
  contact varchar(10) NOT NULL,
  PRIMARY KEY (idPersonne)
) ;

-- --------------------------------------------------------

--
-- Structure de la table genreconcert
--

DROP TABLE IF EXISTS genreconcert;
CREATE TABLE IF NOT EXISTS genreconcert (
  genreConcert varchar(50) NOT NULL,
  PRIMARY KEY (genreConcert)
) ;

-- --------------------------------------------------------

--
-- Structure de la table genrestandup
--

DROP TABLE IF EXISTS genrestandup;
CREATE TABLE IF NOT EXISTS genrestandup (
  genreStandUp varchar(50) NOT NULL,
  PRIMARY KEY (genreStandUp)
) ;

-- --------------------------------------------------------

--
-- Structure de la table genretheatre
--

DROP TABLE IF EXISTS genretheatre;
CREATE TABLE IF NOT EXISTS genretheatre (
  genreTheatre varchar(50) NOT NULL,
  PRIMARY KEY (genreTheatre)
) ;

-- --------------------------------------------------------

--
-- Structure de la table participeetudiant
--

DROP TABLE IF EXISTS participeetudiant;
CREATE TABLE IF NOT EXISTS participeetudiant (
  idEtudiant int NOT NULL,
  idSpectacle int NOT NULL,
  role varchar(50) NOT NULL,
  PRIMARY KEY (idEtudiant,idSpectacle),
  UNIQUE(idSpectacle)
) ;

-- --------------------------------------------------------

--
-- Structure de la table participepersonnel
--

DROP TABLE IF EXISTS participepersonnel;
CREATE TABLE IF NOT EXISTS participepersonnel (
  idPersonnel int NOT NULL,
  idSpectacle int NOT NULL,
  role varchar(50) NOT NULL,
  PRIMARY KEY (idPersonnel,idSpectacle),
  UNIQUE(idSpectacle)
) ;

-- --------------------------------------------------------

--
-- Structure de la table personne
--

DROP TABLE IF EXISTS personne;
CREATE TABLE IF NOT EXISTS personne (
  idPersonne SERIAL,
  nom varchar(50) NOT NULL,
  prenom varchar(50) NOT NULL,
  PRIMARY KEY (idPersonne)
) ;

-- --------------------------------------------------------

--
-- Structure de la table personnel
--

DROP TABLE IF EXISTS personnel;
CREATE TABLE IF NOT EXISTS personnel (
  idPersonne int NOT NULL,
  numeroCIN int NOT NULL,
  statut varchar(150) NOT NULL,
  PRIMARY KEY (idPersonne),
  UNIQUE(numeroCIN)
) ;

-- --------------------------------------------------------

--
-- Structure de la table reservation
--

DROP TABLE IF EXISTS reservation;
CREATE TABLE IF NOT EXISTS reservation (
  nom varchar(50) NOT NULL,
  numSalle int NOT NULL,
  numBat int NOT NULL,
  date date NOT NULL,
  heure time NOT NULL,
  PRIMARY KEY (nom,numSalle,numBat),
  UNIQUE(numSalle),
  UNIQUE(numBat)
) ;

-- --------------------------------------------------------

--
-- Structure de la table salle
--

DROP TABLE IF EXISTS salle;
CREATE TABLE IF NOT EXISTS salle (
  numSalle int NOT NULL,
  capacite int NOT NULL,
  PRIMARY KEY (numSalle)
) ;

-- --------------------------------------------------------

--
-- Structure de la table seance
--

DROP TABLE IF EXISTS seance;
CREATE TABLE IF NOT EXISTS seance (
  idSeance SERIAL,
  date date NOT NULL,
  horaireDebut time NOT NULL,
  idSpectacle int DEFAULT NULL,
  numBat int DEFAULT NULL,
  numSalle int DEFAULT NULL,
  PRIMARY KEY (idSeance)
) ;

-- --------------------------------------------------------

--
-- Structure de la table spectacle
--

DROP TABLE IF EXISTS spectacle;
CREATE TABLE IF NOT EXISTS spectacle (
  idSpectacle SERIAL,
  duree time NOT NULL,
  nomAsso varchar(100) DEFAULT NULL,
  PRIMARY KEY (idSpectacle)
) ;

-- --------------------------------------------------------

--
-- Structure de la table standup
--

DROP TABLE IF EXISTS standup;
CREATE TABLE IF NOT EXISTS standup (
  idStandUp int NOT NULL,
  genre varchar(50) DEFAULT NULL,
  PRIMARY KEY (idStandUp),
  UNIQUE(genre)
) ;

-- --------------------------------------------------------

--
-- Structure de la table theatre
--

DROP TABLE IF EXISTS theatre;
CREATE TABLE IF NOT EXISTS theatre (
  idTheatre int NOT NULL,
  auteur varchar(100) NOT NULL,
  anneeParution date NOT NULL,
  genre varchar(50) DEFAULT NULL,
  PRIMARY KEY (idTheatre),
  UNIQUE(genre)
) ;

-- --------------------------------------------------------

--
-- Structure de la table typesalle
--

DROP TABLE IF EXISTS typesalle;
CREATE TABLE IF NOT EXISTS typesalle (
  numBat int NOT NULL,
  numSalle int NOT NULL,
  libelleType varchar(50) NOT NULL,
  PRIMARY KEY (numBat,numSalle)
) ;

-- Ajout de vues

create view spectacle_small as select idtheatre as ID, genre, 'Théâtre' as categorie from theatre                                                                                                                                  union select idconcert as ID, genre, 'Concert' as categorie from concert                                                                                                                                    union select idstandup as ID, genre, 'Stand-Up' as categorie from standup;

create view spectacle_medium as select id, nomAsso as organisateur, duree, genre, categorie from spectacle_small v, spectacle s where idspectacle=id;

