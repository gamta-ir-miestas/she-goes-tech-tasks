-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Apr 23, 2023 at 05:46 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `homework`
--

-- --------------------------------------------------------

--
-- Table structure for table `Customer`
--

CREATE TABLE `Customer` (
  `ID` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `surname` varchar(255) NOT NULL,
  `phone_number` varchar(15) NOT NULL,
  `cust_email` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `Customer`
--

INSERT INTO `Customer` (`ID`, `name`, `surname`, `phone_number`, `cust_email`) VALUES
(1, 'Patrizia Emilia', 'Hellowa', '+3725566778', 'pehellowa@gmaill.com'),
(2, 'Jane Maria Julie', 'Barbadosa Martinez', '+37244998877', 'jmjbm@gmaill.com'),
(3, 'Joshua', 'Ausho', '+37211223344', 'jushua.joshua@hottmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `Customer_orders`
--

CREATE TABLE `Customer_orders` (
  `ID` int(11) NOT NULL,
  `ProductID` int(11) NOT NULL,
  `CustomerID` int(11) NOT NULL,
  `Order_statusID` int(11) NOT NULL,
  `product_amount` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `Customer_orders`
--

INSERT INTO `Customer_orders` (`ID`, `ProductID`, `CustomerID`, `Order_statusID`, `product_amount`) VALUES
(1, 1, 3, 1, 2),
(2, 2, 1, 4, 3),
(3, 3, 2, 3, 1);

-- --------------------------------------------------------

--
-- Table structure for table `Order_status`
--

CREATE TABLE `Order_status` (
  `ID` int(11) NOT NULL,
  `status` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `Order_status`
--

INSERT INTO `Order_status` (`ID`, `status`) VALUES
(1, 'entered'),
(2, 'in process'),
(3, 'cancelled'),
(4, 'completed');

-- --------------------------------------------------------

--
-- Table structure for table `Product`
--

CREATE TABLE `Product` (
  `ID` int(11) NOT NULL,
  `prod_name` varchar(255) NOT NULL,
  `description` varchar(5000) NOT NULL,
  `warranty_period` int(11) NOT NULL,
  `price_eur` int(11) NOT NULL,
  `category` varchar(255) NOT NULL,
  `SupplierID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `Product`
--

INSERT INTO `Product` (`ID`, `prod_name`, `description`, `warranty_period`, `price_eur`, `category`, `SupplierID`) VALUES
(1, 'Blue Pen', 'Pen with gel ink that writes everything in blue', 1, 1, 'stationery', 1),
(2, 'Computer ABC', 'Very powerful computer, best choice ever', 24, 1300, 'electronics', 2),
(3, 'Computer DEF', 'Cheapest computer ever, perfect for people with no money. The computer is slow tho', 15, 350, 'electronics', 2),
(4, 'Binbobs 95', 'Newest operating system with a blast to the past. the system is powerful and has all of the newest features, but the design scream 90s', 0, 100, 'software', 3);

-- --------------------------------------------------------

--
-- Table structure for table `Supplier`
--

CREATE TABLE `Supplier` (
  `ID` int(11) NOT NULL,
  `sup_name` varchar(255) NOT NULL,
  `contact` varchar(255) NOT NULL,
  `phone_no` varchar(20) NOT NULL,
  `email` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `Supplier`
--

INSERT INTO `Supplier` (`ID`, `sup_name`, `contact`, `phone_no`, `email`) VALUES
(1, 'Pens for everyone', 'Jane Doe', '+123456789', 'jane.doe@pfe.com'),
(2, 'Computer World', 'Josh Josh', '010-1234-5678', 'josh.josh@cw.xyz'),
(3, 'Binbobs Enterprise', 'Wi TooLo', '+4823546798445', 'wi.toolo@binbobs.hello');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Customer`
--
ALTER TABLE `Customer`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `Customer_orders`
--
ALTER TABLE `Customer_orders`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `one` (`CustomerID`),
  ADD KEY `two` (`ProductID`),
  ADD KEY `three` (`Order_statusID`);

--
-- Indexes for table `Order_status`
--
ALTER TABLE `Order_status`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `Product`
--
ALTER TABLE `Product`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `kk` (`SupplierID`);

--
-- Indexes for table `Supplier`
--
ALTER TABLE `Supplier`
  ADD PRIMARY KEY (`ID`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `Customer_orders`
--
ALTER TABLE `Customer_orders`
  ADD CONSTRAINT `one` FOREIGN KEY (`CustomerID`) REFERENCES `Customer` (`ID`),
  ADD CONSTRAINT `three` FOREIGN KEY (`Order_statusID`) REFERENCES `Order_status` (`ID`),
  ADD CONSTRAINT `two` FOREIGN KEY (`ProductID`) REFERENCES `Product` (`ID`);

--
-- Constraints for table `Product`
--
ALTER TABLE `Product`
  ADD CONSTRAINT `kk` FOREIGN KEY (`SupplierID`) REFERENCES `Supplier` (`ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
