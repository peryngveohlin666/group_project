-- MySQL dump 10.13  Distrib 8.0.19, for macos10.15 (x86_64)
--
-- Host: 127.0.0.1    Database: ATS
-- ------------------------------------------------------
-- Server version	8.0.19

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
-- Table structure for table `Blank`
--

DROP TABLE IF EXISTS `Blank`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Blank` (
  `number` int NOT NULL AUTO_INCREMENT,
  `type` int NOT NULL,
  `is_sold` bit(1) NOT NULL,
  `is_refunded` bit(1) NOT NULL,
  `Customerid` int NOT NULL,
  `date` date NOT NULL,
  `User_Blank_AssignmentUserid` int NOT NULL,
  `User_Blank_AssignmentBlanknumber` int NOT NULL,
  PRIMARY KEY (`number`),
  UNIQUE KEY `number` (`number`),
  KEY `FKBlank371617` (`Customerid`),
  KEY `FKBlank490598` (`User_Blank_AssignmentUserid`,`User_Blank_AssignmentBlanknumber`),
  CONSTRAINT `FKBlank371617` FOREIGN KEY (`Customerid`) REFERENCES `Customer` (`id`),
  CONSTRAINT `FKBlank490598` FOREIGN KEY (`User_Blank_AssignmentUserid`, `User_Blank_AssignmentBlanknumber`) REFERENCES `User_Blank_Assignment` (`Userid`, `Blanknumber`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Card_Informatin`
--

DROP TABLE IF EXISTS `Card_Informatin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Card_Informatin` (
  `name` varchar(255) NOT NULL,
  `surname` varchar(255) NOT NULL,
  `no` int NOT NULL AUTO_INCREMENT,
  `cvv` int NOT NULL,
  `password` int NOT NULL,
  `card_type` varchar(255) NOT NULL,
  `Customerid` int NOT NULL,
  PRIMARY KEY (`no`),
  KEY `FKCard_Infor761361` (`Customerid`),
  CONSTRAINT `FKCard_Infor761361` FOREIGN KEY (`Customerid`) REFERENCES `Customer` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Currency`
--

DROP TABLE IF EXISTS `Currency`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Currency` (
  `type` int NOT NULL AUTO_INCREMENT,
  `rate` int NOT NULL,
  PRIMARY KEY (`type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Customer`
--

DROP TABLE IF EXISTS `Customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Customer` (
  `id` int NOT NULL AUTO_INCREMENT,
  `is_regular` bit(1) NOT NULL,
  `is_valued` bit(1) NOT NULL,
  `name` varchar(255) NOT NULL,
  `surname` varchar(255) NOT NULL,
  `address` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Discount`
--

DROP TABLE IF EXISTS `Discount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Discount` (
  `type` bit(1) NOT NULL,
  `rate` int DEFAULT NULL,
  PRIMARY KEY (`type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Domestic_Sales_Report`
--

DROP TABLE IF EXISTS `Domestic_Sales_Report`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Domestic_Sales_Report` (
  `Reportid` int NOT NULL,
  `fare_base_ngl` int NOT NULL,
  `fare_base_usd` int NOT NULL,
  `cash_local` int NOT NULL,
  `cheque_local` int NOT NULL,
  `invoice_local` int NOT NULL,
  `credit_usd` int NOT NULL,
  `taxes` int NOT NULL,
  `total_amount_paid` int NOT NULL,
  `commissions_assessable_amount` int NOT NULL,
  `commission_rate` int NOT NULL,
  `notes` varchar(255) DEFAULT NULL,
  `total_net_amount_airvia` int NOT NULL,
  `total_commission_amount` int NOT NULL,
  `net_amounts_for_agent_debit` int NOT NULL,
  PRIMARY KEY (`Reportid`),
  CONSTRAINT `FKDomestic_S819725` FOREIGN KEY (`Reportid`) REFERENCES `Report` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Global_Domestic_Sales`
--

DROP TABLE IF EXISTS `Global_Domestic_Sales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Global_Domestic_Sales` (
  `Domestic_Sales_ReportReportid` int NOT NULL,
  `agent_id` int NOT NULL,
  `ttl_ttk_reported_num` int NOT NULL,
  PRIMARY KEY (`Domestic_Sales_ReportReportid`),
  CONSTRAINT `FKGlobal_Dom370294` FOREIGN KEY (`Domestic_Sales_ReportReportid`) REFERENCES `Domestic_Sales_Report` (`Reportid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Global_Interline_Sales_Report`
--

DROP TABLE IF EXISTS `Global_Interline_Sales_Report`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Global_Interline_Sales_Report` (
  `Interline_Sales_ReportReportid` int NOT NULL,
  `advisor_no` int NOT NULL,
  `doc_no_acpns` int NOT NULL,
  `fare_amount` int NOT NULL,
  `airvia_docs` int NOT NULL,
  `airvia_fcpns` int NOT NULL,
  `airvia_prorate_amounts` int NOT NULL,
  `other_airline_docs` int NOT NULL,
  `other_airline_fcpns` int NOT NULL,
  `other_airline_prorate_amounts` int NOT NULL,
  PRIMARY KEY (`Interline_Sales_ReportReportid`),
  CONSTRAINT `FKGlobal_Int467036` FOREIGN KEY (`Interline_Sales_ReportReportid`) REFERENCES `Interline_Sales_Report` (`Reportid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Group`
--

DROP TABLE IF EXISTS `Group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Group_Permissions`
--

DROP TABLE IF EXISTS `Group_Permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Group_Permissions` (
  `Groupid` int NOT NULL,
  `Permissionid` int NOT NULL,
  PRIMARY KEY (`Groupid`,`Permissionid`),
  UNIQUE KEY `Groupid` (`Groupid`),
  KEY `FKGroup_Perm527187` (`Permissionid`),
  CONSTRAINT `FKGroup_Perm423461` FOREIGN KEY (`Groupid`) REFERENCES `Group` (`id`),
  CONSTRAINT `FKGroup_Perm527187` FOREIGN KEY (`Permissionid`) REFERENCES `Permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Individual_Domestic_Sales_Report`
--

DROP TABLE IF EXISTS `Individual_Domestic_Sales_Report`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Individual_Domestic_Sales_Report` (
  `Domestic_Sales_ReportReportid` int NOT NULL,
  `num_of_tickets` int NOT NULL,
  `original_issued_num` int NOT NULL,
  `other_details` varchar(255) DEFAULT NULL,
  `airvia_n` int NOT NULL,
  `airvia_amount` int NOT NULL,
  `airvia_bank_acc` int NOT NULL,
  `airvia_doc_no` int NOT NULL,
  `airvia_date` date NOT NULL,
  PRIMARY KEY (`Domestic_Sales_ReportReportid`),
  CONSTRAINT `FKIndividual345877` FOREIGN KEY (`Domestic_Sales_ReportReportid`) REFERENCES `Domestic_Sales_Report` (`Reportid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Individual_Interline_Sales_Report`
--

DROP TABLE IF EXISTS `Individual_Interline_Sales_Report`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Individual_Interline_Sales_Report` (
  `Interline_Sales_ReportReportid` int NOT NULL,
  `number_of_tickets` int NOT NULL,
  `original_issue_no` int NOT NULL,
  `fa_usd` int DEFAULT NULL,
  `fa_usd_local` int DEFAULT NULL,
  `airline_docs_no` int NOT NULL,
  `airline_fc` int NOT NULL,
  `airline_pror_amnt` int NOT NULL,
  `airline_cd` int NOT NULL,
  PRIMARY KEY (`Interline_Sales_ReportReportid`),
  CONSTRAINT `FKIndividual995737` FOREIGN KEY (`Interline_Sales_ReportReportid`) REFERENCES `Interline_Sales_Report` (`Reportid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Interline_Sales_Report`
--

DROP TABLE IF EXISTS `Interline_Sales_Report`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Interline_Sales_Report` (
  `Reportid` int NOT NULL,
  `taxes_LZ` int NOT NULL,
  `taxes_OTHS` int NOT NULL,
  `commission_rate` int NOT NULL,
  `cash` int NOT NULL,
  `credit_lc` int NOT NULL,
  `credit_usd` int NOT NULL,
  `credit_local` int NOT NULL,
  `non_assess_amount` int NOT NULL,
  `total_net_to_airvia` int NOT NULL,
  `airvia_n` int NOT NULL,
  `airvia_amount` int NOT NULL,
  `airvia_bank_acc_no` int NOT NULL,
  `airvia_doc_no` int NOT NULL,
  `airvia_date` date NOT NULL,
  PRIMARY KEY (`Reportid`),
  CONSTRAINT `FKInterline_761250` FOREIGN KEY (`Reportid`) REFERENCES `Report` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Payment`
--

DROP TABLE IF EXISTS `Payment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Payment` (
  `Blanknumber` int NOT NULL,
  `amount` int NOT NULL,
  `type` bit(1) NOT NULL,
  `is_valid` bit(1) NOT NULL,
  `is_regular` bit(1) NOT NULL,
  `Currencytype` int NOT NULL,
  `Discounttype` bit(1) DEFAULT NULL,
  PRIMARY KEY (`Blanknumber`),
  KEY `FKPayment811398` (`Currencytype`),
  KEY `FKPayment232106` (`Discounttype`),
  CONSTRAINT `FKPayment232106` FOREIGN KEY (`Discounttype`) REFERENCES `Discount` (`type`),
  CONSTRAINT `FKPayment811398` FOREIGN KEY (`Currencytype`) REFERENCES `Currency` (`type`),
  CONSTRAINT `FKPayment981424` FOREIGN KEY (`Blanknumber`) REFERENCES `Blank` (`number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Permission`
--

DROP TABLE IF EXISTS `Permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `codename` varchar(10) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `codename` (`codename`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Report`
--

DROP TABLE IF EXISTS `Report`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Report` (
  `id` int NOT NULL AUTO_INCREMENT,
  `period_from` date NOT NULL,
  `period_to` date NOT NULL,
  `created_on` date NOT NULL,
  `is_global` bit(1) NOT NULL,
  `number` int NOT NULL,
  `sales_office_place` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Report_Blank_Inclusion`
--

DROP TABLE IF EXISTS `Report_Blank_Inclusion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Report_Blank_Inclusion` (
  `Reportid` int NOT NULL,
  `Blanknumber` int NOT NULL,
  PRIMARY KEY (`Reportid`,`Blanknumber`),
  KEY `FKReport_Bla496473` (`Blanknumber`),
  CONSTRAINT `FKReport_Bla496473` FOREIGN KEY (`Blanknumber`) REFERENCES `Blank` (`number`),
  CONSTRAINT `FKReport_Bla560650` FOREIGN KEY (`Reportid`) REFERENCES `Report` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Report_User`
--

DROP TABLE IF EXISTS `Report_User`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Report_User` (
  `Reportid` int NOT NULL,
  `Userid` int NOT NULL,
  `relationship_type` int NOT NULL,
  PRIMARY KEY (`Reportid`,`Userid`),
  KEY `FKReport_Use116167` (`Userid`),
  CONSTRAINT `FKReport_Use116167` FOREIGN KEY (`Userid`) REFERENCES `User` (`id`),
  CONSTRAINT `FKReport_Use649540` FOREIGN KEY (`Reportid`) REFERENCES `Report` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Ticket_Stock_Turnover_Report`
--

DROP TABLE IF EXISTS `Ticket_Stock_Turnover_Report`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Ticket_Stock_Turnover_Report` (
  `Reportid` int NOT NULL,
  `agent_received_blank_from` int NOT NULL,
  `agent_received_blank_to` int NOT NULL,
  `agent_used_from` int NOT NULL,
  `agent_used_to` int NOT NULL,
  `sub_agent_from` int NOT NULL,
  `sub_agent_to` int NOT NULL,
  PRIMARY KEY (`Reportid`),
  CONSTRAINT `FKTicket_Sto281292` FOREIGN KEY (`Reportid`) REFERENCES `Report` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `User`
--

DROP TABLE IF EXISTS `User`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `User` (
  `id` int NOT NULL AUTO_INCREMENT,
  `staff_code` int NOT NULL,
  `password` int NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `surname` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `agency` varchar(255) NOT NULL,
  `Groupid` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `staff_code` (`staff_code`),
  KEY `FKUser810444` (`Groupid`),
  CONSTRAINT `FKUser810444` FOREIGN KEY (`Groupid`) REFERENCES `Group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `User_Blank_Assignment`
--

DROP TABLE IF EXISTS `User_Blank_Assignment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `User_Blank_Assignment` (
  `Userid` int NOT NULL,
  `Blanknumber` int NOT NULL,
  `comission_rate` int NOT NULL,
  PRIMARY KEY (`Userid`,`Blanknumber`),
  CONSTRAINT `FKUser_Blank506842` FOREIGN KEY (`Userid`) REFERENCES `User` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-02-21 21:03:58
