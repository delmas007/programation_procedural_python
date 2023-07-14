-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : ven. 23 juin 2023 à 09:17
-- Version du serveur : 5.7.36
-- Version de PHP : 7.4.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `biblio_bd`
--

-- --------------------------------------------------------

--
-- Structure de la table `livre`
--

DROP TABLE IF EXISTS `livre`;
CREATE TABLE IF NOT EXISTS `livre` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ref_livre` varchar(36) DEFAULT NULL,
  `libelle` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `auteur` varchar(255) DEFAULT NULL,
  `date_parution` varchar(255) DEFAULT NULL,
  `maison_edition` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ref_livre` (`ref_livre`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `livre`
--

INSERT INTO `livre` (`id`, `ref_livre`, `libelle`, `description`, `auteur`, `date_parution`, `maison_edition`) VALUES
(5, '13257', 'harry potter', 'magie', 'J. K. Rowling', '16/11/2001', 'Bloomsbury Publishing'),
(6, '32456', 'alice au pays des merveilles', 'fantastique', 'Lewis Carroll', '5/03/2010', 'Macmillan and Co');

-- --------------------------------------------------------

--
-- Structure de la table `personne`
--

DROP TABLE IF EXISTS `personne`;
CREATE TABLE IF NOT EXISTS `personne` (
  `id_per` int(11) NOT NULL AUTO_INCREMENT,
  `nom` varchar(255) DEFAULT NULL,
  `prenom` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_per`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `personne`
--

INSERT INTO `personne` (`id_per`, `nom`, `prenom`) VALUES
(1, 'Kouame', 'Aya'),
(2, 'Diallo', 'Samba'),
(3, 'Diop', 'Aissatou'),
(4, 'Sow', 'Ousmane'),
(5, 'Keita', 'Mariam');

-- --------------------------------------------------------

--
-- Structure de la table `pret`
--

DROP TABLE IF EXISTS `pret`;
CREATE TABLE IF NOT EXISTS `pret` (
  `id_pret` int(11) NOT NULL AUTO_INCREMENT,
  `date_pret` date DEFAULT NULL,
  `date_retour` date DEFAULT NULL,
  `rendu` tinyint(1) NOT NULL,
  `id_Livre` int(11) DEFAULT NULL,
  `id_per_Personne` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_pret`),
  KEY `FK_Pret_id_Livre` (`id_Livre`),
  KEY `FK_Pret_id_per_Personne` (`id_per_Personne`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `pret`
--

INSERT INTO `pret` (`id_pret`, `date_pret`, `date_retour`, `rendu`, `id_Livre`, `id_per_Personne`) VALUES
(1, '2023-06-01', '2023-06-10', 1, 5, 1),
(2, '2023-05-15', '2023-05-23', 0, 6, 2),
(3, '2023-06-16', '2023-06-30', 1, 6, 4),
(4, '2023-06-16', '2023-06-20', 0, 5, 1),
(5, '2023-06-16', '2023-06-25', 0, 5, 2);

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `pret`
--
ALTER TABLE `pret`
  ADD CONSTRAINT `FK_Pret_id_Livre` FOREIGN KEY (`id_Livre`) REFERENCES `livre` (`id`),
  ADD CONSTRAINT `FK_Pret_id_per_Personne` FOREIGN KEY (`id_per_Personne`) REFERENCES `personne` (`id_per`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
