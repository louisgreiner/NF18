-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : mar. 04 mai 2021 à 15:57
-- Version du serveur :  5.7.31
-- Version de PHP : 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `nf18`
--

-- --------------------------------------------------------

--
-- Structure de la table `association`
--

DROP TABLE IF EXISTS `association`;
CREATE TABLE IF NOT EXISTS `association` (
  `nom` varchar(50) NOT NULL,
  `description` text NOT NULL,
  `categorie` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `dateCreation` date NOT NULL,
  `siteWeb` text,
  PRIMARY KEY (`nom`),
  UNIQUE KEY `email` (`email`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `association`
--

INSERT INTO `association` (`nom`, `description`, `categorie`, `email`, `dateCreation`, `siteWeb`) VALUES
('test', 'test test', 'catest', 'test@test', '2010-05-05', 'test.com');

-- --------------------------------------------------------

--
-- Structure de la table `batiment`
--

DROP TABLE IF EXISTS `batiment`;
CREATE TABLE IF NOT EXISTS `batiment` (
  `numBat` int(11) NOT NULL,
  PRIMARY KEY (`numBat`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `billet`
--

DROP TABLE IF EXISTS `billet`;
CREATE TABLE IF NOT EXISTS `billet` (
  `idBillet` int(11) NOT NULL AUTO_INCREMENT,
  `categorie` varchar(50) DEFAULT NULL,
  `dateCreation` date NOT NULL,
  `tarif` decimal(10,0) DEFAULT NULL,
  `idSeance` int(11) DEFAULT NULL,
  `idAcheteur` int(11) DEFAULT NULL,
  PRIMARY KEY (`idBillet`),
  KEY `idSeance` (`idSeance`),
  KEY `idAcheteur` (`idAcheteur`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `categorie`
--

DROP TABLE IF EXISTS `categorie`;
CREATE TABLE IF NOT EXISTS `categorie` (
  `idSeance` int(11) NOT NULL,
  `idBillet` int(11) NOT NULL,
  PRIMARY KEY (`idSeance`,`idBillet`),
  KEY `idBillet` (`idBillet`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `compose`
--

DROP TABLE IF EXISTS `compose`;
CREATE TABLE IF NOT EXISTS `compose` (
  `idEtudiant` int(11) NOT NULL,
  `nomAsso` varchar(100) NOT NULL,
  `statut` varchar(50) NOT NULL,
  PRIMARY KEY (`idEtudiant`,`nomAsso`),
  KEY `nomAsso` (`nomAsso`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `concert`
--

DROP TABLE IF EXISTS `concert`;
CREATE TABLE IF NOT EXISTS `concert` (
  `idConcert` int(11) NOT NULL,
  `compositeur` varchar(100) NOT NULL,
  `genre` varchar(50) DEFAULT NULL,
  `anneeParution` date DEFAULT NULL,
  PRIMARY KEY (`idConcert`),
  KEY `genre` (`genre`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `etudiant`
--

DROP TABLE IF EXISTS `etudiant`;
CREATE TABLE IF NOT EXISTS `etudiant` (
  `idPersonne` int(11) NOT NULL,
  `numeroCIN` int(11) NOT NULL,
  PRIMARY KEY (`idPersonne`),
  UNIQUE KEY `numeroCIN` (`numeroCIN`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `exterieur`
--

DROP TABLE IF EXISTS `exterieur`;
CREATE TABLE IF NOT EXISTS `exterieur` (
  `idPersonne` int(11) NOT NULL,
  `organisme` varchar(50) NOT NULL,
  `contact` varchar(10) NOT NULL,
  PRIMARY KEY (`idPersonne`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `genreconcert`
--

DROP TABLE IF EXISTS `genreconcert`;
CREATE TABLE IF NOT EXISTS `genreconcert` (
  `genreConcert` varchar(50) NOT NULL,
  PRIMARY KEY (`genreConcert`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `genrestandup`
--

DROP TABLE IF EXISTS `genrestandup`;
CREATE TABLE IF NOT EXISTS `genrestandup` (
  `genreStandUp` varchar(50) NOT NULL,
  PRIMARY KEY (`genreStandUp`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `genretheatre`
--

DROP TABLE IF EXISTS `genretheatre`;
CREATE TABLE IF NOT EXISTS `genretheatre` (
  `genreTheatre` varchar(50) NOT NULL,
  PRIMARY KEY (`genreTheatre`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `participeetudiant`
--

DROP TABLE IF EXISTS `participeetudiant`;
CREATE TABLE IF NOT EXISTS `participeetudiant` (
  `idEtudiant` int(11) NOT NULL,
  `idSpectacle` int(11) NOT NULL,
  `role` varchar(50) NOT NULL,
  PRIMARY KEY (`idEtudiant`,`idSpectacle`),
  KEY `idSpectacle` (`idSpectacle`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `participepersonnel`
--

DROP TABLE IF EXISTS `participepersonnel`;
CREATE TABLE IF NOT EXISTS `participepersonnel` (
  `idPersonnel` int(11) NOT NULL,
  `idSpectacle` int(11) NOT NULL,
  `role` varchar(50) NOT NULL,
  PRIMARY KEY (`idPersonnel`,`idSpectacle`),
  KEY `idSpectacle` (`idSpectacle`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `personne`
--

DROP TABLE IF EXISTS `personne`;
CREATE TABLE IF NOT EXISTS `personne` (
  `idPersonne` int(11) NOT NULL AUTO_INCREMENT,
  `nom` varchar(50) NOT NULL,
  `prenom` varchar(50) NOT NULL,
  PRIMARY KEY (`idPersonne`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `personnel`
--

DROP TABLE IF EXISTS `personnel`;
CREATE TABLE IF NOT EXISTS `personnel` (
  `idPersonne` int(11) NOT NULL,
  `numeroCIN` int(11) NOT NULL,
  `statut` varchar(150) NOT NULL,
  PRIMARY KEY (`idPersonne`),
  UNIQUE KEY `numeroCIN` (`numeroCIN`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `reservation`
--

DROP TABLE IF EXISTS `reservation`;
CREATE TABLE IF NOT EXISTS `reservation` (
  `nom` varchar(50) NOT NULL,
  `numSalle` int(11) NOT NULL,
  `numBat` int(11) NOT NULL,
  `date` date NOT NULL,
  `heure` time NOT NULL,
  PRIMARY KEY (`nom`,`numSalle`,`numBat`),
  KEY `numSalle` (`numSalle`),
  KEY `numBat` (`numBat`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `salle`
--

DROP TABLE IF EXISTS `salle`;
CREATE TABLE IF NOT EXISTS `salle` (
  `numSalle` int(11) NOT NULL,
  `capacite` int(11) NOT NULL,
  PRIMARY KEY (`numSalle`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `seance`
--

DROP TABLE IF EXISTS `seance`;
CREATE TABLE IF NOT EXISTS `seance` (
  `idSeance` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `horaireDebut` time NOT NULL,
  `idSpectacle` int(11) DEFAULT NULL,
  `numBat` int(11) DEFAULT NULL,
  `numSalle` int(11) DEFAULT NULL,
  PRIMARY KEY (`idSeance`),
  KEY `idSpectacle` (`idSpectacle`),
  KEY `numBat` (`numBat`),
  KEY `numSalle` (`numSalle`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `spectacle`
--

DROP TABLE IF EXISTS `spectacle`;
CREATE TABLE IF NOT EXISTS `spectacle` (
  `idSpectacle` int(11) NOT NULL AUTO_INCREMENT,
  `duree` time NOT NULL,
  `nomAsso` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`idSpectacle`),
  KEY `nomAsso` (`nomAsso`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `standup`
--

DROP TABLE IF EXISTS `standup`;
CREATE TABLE IF NOT EXISTS `standup` (
  `idStandUp` int(11) NOT NULL,
  `genre` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`idStandUp`),
  KEY `genre` (`genre`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `theatre`
--

DROP TABLE IF EXISTS `theatre`;
CREATE TABLE IF NOT EXISTS `theatre` (
  `idTheatre` int(11) NOT NULL,
  `auteur` varchar(100) NOT NULL,
  `anneeParution` date NOT NULL,
  `genre` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`idTheatre`),
  KEY `genre` (`genre`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `typesalle`
--

DROP TABLE IF EXISTS `typesalle`;
CREATE TABLE IF NOT EXISTS `typesalle` (
  `numBat` int(11) NOT NULL,
  `numSalle` int(11) NOT NULL,
  `libelleType` varchar(50) NOT NULL,
  PRIMARY KEY (`numBat`,`numSalle`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
