-- MySQL dump 10.17  Distrib 10.3.17-MariaDB, for debian-linux-gnueabihf (armv7l)
--
-- Host: localhost    Database: users
-- ------------------------------------------------------
-- Server version	10.3.17-MariaDB-0+deb10u1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;



--
-- Table structure for table `Vorlesung`
--

DROP TABLE IF EXISTS `Vorlesung`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Vorlesung` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `startDatum` datetime NOT NULL DEFAULT current_timestamp(),
  `profID` int(11) NOT NULL,
  `raum` varchar(255) NOT NULL,
  `endDatum` datetime NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `profKey` (`profID`),
  CONSTRAINT `profKey` FOREIGN KEY (`profID`) REFERENCES `Vorlesung` (`id`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Vorlesung`
--

LOCK TABLES `Vorlesung` WRITE;
/*!40000 ALTER TABLE `Vorlesung` DISABLE KEYS */;
INSERT INTO `Vorlesung` VALUES (1,'Internet der Dinge','2020-01-14 00:00:00',1,'','0000-00-00 00:00:00'),(2,'Internet der Dinge dinge','2020-01-14 09:00:00',1,'','0000-00-00 00:00:00');
/*!40000 ALTER TABLE `Vorlesung` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `pw` varchar(255) DEFAULT NULL,
  `mail` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'Lukas','1234','1234@1234.com');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-01-25 10:55:46


--
-- Table structure for table `Bewertung`
--

DROP TABLE IF EXISTS `Bewertung`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Bewertung` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `wert` int(11) DEFAULT NULL,
  `datum` datetime NOT NULL DEFAULT current_timestamp(),
  `vorlesungsID` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `vorlesungsID` (`vorlesungsID`),
  CONSTRAINT `vorlesungsID` FOREIGN KEY (`vorlesungsID`) REFERENCES `Vorlesung` (`id`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Bewertung`
--

LOCK TABLES `Bewertung` WRITE;
/*!40000 ALTER TABLE `Bewertung` DISABLE KEYS */;
INSERT INTO `Bewertung` VALUES (1,1,'2020-01-14 00:00:00',1),(2,1,'2020-01-14 08:00:00',1);
/*!40000 ALTER TABLE `Bewertung` ENABLE KEYS */;
UNLOCK TABLES;