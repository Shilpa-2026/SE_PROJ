-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: localhost    Database: accounts
-- ------------------------------------------------------
-- Server version	8.0.27

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `pnl`
--

DROP TABLE IF EXISTS `pnl`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pnl` (
  `product_sales` varchar(45) DEFAULT NULL,
  `service_sales` varchar(45) DEFAULT NULL,
  `manufacturing_e` varchar(45) DEFAULT NULL,
  `sales_e` varchar(45) DEFAULT NULL,
  `administrative_e` varchar(45) DEFAULT NULL,
  `depreciation` varchar(45) DEFAULT NULL,
  `rate` varchar(45) DEFAULT NULL,
  `tax_rate` varchar(45) DEFAULT NULL,
  `year` varchar(4) NOT NULL,
  `contact_number` varchar(10) NOT NULL,
  `loan_amount` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`year`,`contact_number`),
  KEY `contact4_idx` (`contact_number`),
  CONSTRAINT `contact4` FOREIGN KEY (`contact_number`) REFERENCES `create_account` (`contact_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pnl`
--

LOCK TABLES `pnl` WRITE;
/*!40000 ALTER TABLE `pnl` DISABLE KEYS */;
INSERT INTO `pnl` VALUES ('6000000','1000000','1800000','300000','120000','800000','NULL','40','2019','1234567890','NULL'),('NULL','NULL','NULL','NULL','9000','NULL','NULL','40','2022','1234567890','NULL');
/*!40000 ALTER TABLE `pnl` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-11 13:07:03
