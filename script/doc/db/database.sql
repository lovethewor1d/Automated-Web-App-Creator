-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 29, 2023 at 12:17 AM
-- Server version: 10.4.6-MariaDB
-- PHP Version: 7.1.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `php_docker`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id` int(100) NOT NULL,
  `username` varchar(255) COLLATE utf8_bin NOT NULL,
  `password` varchar(100) COLLATE utf8_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `username`, `password`) VALUES
(1, 'admin', 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `comments`
--
-- Error reading structure for table database.comments: #1932 - Table 'database.comments' doesn't exist in engine
-- Error reading data for table database.comments: #1064 - You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'FROM `database`.`comments`' at line 1

-- --------------------------------------------------------

--
-- Table structure for table `commentsnew`
--

CREATE TABLE `commentsnew` (
  `name` varchar(255) NOT NULL,
  `comment` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `commentsnew`
--

INSERT INTO `commentsnew` (`name`, `comment`) VALUES
('love', 'test'),
('love', 'test'),
('love', '<script>alert(1)</script>'),
('\"><svg/onload=prompt(String.fromCharCode(88,83,83))>', '\"><svg/onload=prompt(String.fromCharCode(88,83,83))>'),
('\"><img src=x onerror=(document.cookie)>', '\"><img src=x onerror=(document.cookie)>'),
('\"><img src=x onerror=(document.cookie)>', '\"><img src=x onerror=(document.cookie)>'),
('love', '\"><img src=x onerror=(99)>');

-- --------------------------------------------------------

--
-- Table structure for table `image`
--

CREATE TABLE `image` (
  `images` longblob NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Dumping data for table `image`
--

INSERT INTO `image` (`images`) VALUES
(0x646f63756d656e74732f6267332e6a7067),
(0x646f63756d656e74732f75706c6f61647368656c6c2e706870),
(0x646f63756d656e74732f7368656c6c2e706870),
(0x646f63756d656e74732f),
(0x646f63756d656e74732f7368656c6c2e706870),
(0x646f63756d656e74732f),
(0x646f63756d656e74732f636d642e706870),
(0x646f63756d656e74732f),
(0x646f63756d656e74732f39613562613537352e30),
(0x646f63756d656e74732f39613562613537352e30),
(0x646f63756d656e74732f7061726b2e747874),
(0x646f63756d656e74732f75706c6f61647368656c6c2e706870),
(0x646f63756d656e74732f),
(0x646f63756d656e74732f);

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `id` int(100) NOT NULL,
  `type` varchar(100) CHARACTER SET latin1 COLLATE latin1_spanish_ci NOT NULL,
  `name` varchar(255) CHARACTER SET latin1 COLLATE latin1_spanish_ci NOT NULL,
  `price` varchar(255) CHARACTER SET latin1 COLLATE latin1_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`id`, `type`, `name`, `price`) VALUES
(1, 'cars', 'alfa-romero', '13495'),
(1, 'cars', 'audi', '13950'),
(1, 'cars', 'bmw', '16430'),
(1, 'cars', 'chevrolet', '5151'),
(1, 'cars', 'dodge', '5572'),
(1, 'cars', 'honda', '6479'),
(1, 'cars', 'isuzu', '6785'),
(1, 'cars', 'jaguar', '32250'),
(1, 'cars', 'mazda', '5195'),
(1, 'cars', 'mercedes-benz', '25552'),
(1, 'cars', 'mercury', '16503'),
(1, 'cars', 'mitsubishi', '5389'),
(1, 'cars', 'nissan', '5499'),
(1, 'cars', 'peugot', '11900'),
(1, 'cars', 'plymouth', '5572'),
(1, 'cars', 'porsche', '22018'),
(1, 'cars', 'renault', '9295'),
(1, 'cars', 'saab', '11850'),
(1, 'cars', 'subaru', '5118'),
(1, 'cars', 'toyota', '5348'),
(1, 'cars', 'volkswagen', '7775'),
(1, 'cars', 'volvo', '12940'),
(2, 'bikes', 'Royal Enfield Classic 350', '175000'),
(2, 'bikes', 'Honda Dio', '45000'),
(2, 'bikes', 'Royal Enfield Classic Gunmetal Grey', '150000'),
(2, 'bikes', 'Yamaha Fazer FI V 2.0 [2016-2018]', '65000'),
(2, 'bikes', 'Yamaha SZ [2013-2014]', '20000'),
(2, 'bikes', 'Honda CB Twister', '18000'),
(2, 'bikes', 'Honda CB Hornet 160R', '78500'),
(2, 'bikes', 'Royal Enfield Bullet 350 [2007-2011]', '180000'),
(2, 'bikes', 'Hero Honda CBZ extreme', '30000'),
(2, 'bikes', 'Bajaj Discover 125', '50000'),
(2, 'bikes', 'Yamaha FZ16', '35000'),
(2, 'bikes', 'Honda Navi', '28000'),
(2, 'bikes', 'Bajaj Avenger Street 220', '80000'),
(2, 'bikes', 'Yamaha YZF R3', '365000'),
(2, 'bikes', 'Jawa 42', '185000'),
(2, 'bikes', 'Suzuki Access 125 [2007-2016]', '25000'),
(2, 'bikes', 'Hero Honda Glamour', '25000'),
(2, 'bikes', 'Yamaha YZF R15 S', '40000'),
(2, 'bikes', 'Royal Enfield Classic Gunmetal Grey', '150000'),
(2, 'bikes', 'Yamaha FZ25', '120000'),
(2, 'bikes', 'Hero Passion Pro 110', '15000'),
(2, 'bikes', 'Honda Navi [2016-2017]', '26000'),
(3, 'planes', 'EMBRAER:EMB-145XR', '98313'),
(3, 'planes', 'AIRBUS INDUSTRIE:A320-214', '1831398'),
(3, 'planes', 'EMBRAER:EMB-145LR', '398139'),
(3, 'planes', 'BOEING:737-824', '193813'),
(3, 'planes', 'BOEING:767-332', '8241391'),
(3, 'planes', 'BOEING:757-224', '17331'),
(3, 'planes', 'AIRBUS:A320-214', '294729'),
(3, 'planes', 'BOMBARDIER INC:CL-600-2D24', '394819'),
(3, 'planes', 'BOEING:737-724', '913197'),
(3, 'planes', 'BOEING:737-524', '931743'),
(3, 'planes', 'BOEING:767-3P6', '91373'),
(3, 'planes', 'AIRBUS:A321-211', '931743'),
(3, 'planes', 'AIRBUS INDUSTRIE:A321-211', '137931'),
(3, 'planes', 'BOEING:737-76N', '29472'),
(3, 'planes', 'EMBRAER	ERJ:190-100 IGW', '937391'),
(3, 'planes', 'BOEING:737-7H4', '293742'),
(3, 'planes', 'CESSNA:150', '23947'),
(3, 'planes', 'CESSNA:421C', '20374'),
(3, 'planes', 'BOEING:777-222', '294723'),
(3, 'planes', 'BOEING:787-8', '723972'),
(3, 'planes', 'BOEING:767-201', '297429'),
(3, 'planes', 'GULFSTREAM AEROSPACE:G-IV', '23729'),
(4, 'laptop', 'Apple MacBook Pro', '1339.69'),
(4, 'laptop', 'Apple Macbook Air', '898.94'),
(4, 'laptop', 'HP 250 G6', '575'),
(4, 'laptop', 'Acer Aspire 3', '2537.45'),
(4, 'laptop', 'Asus ZenBook UX430UN', '1803.6'),
(4, 'laptop', 'Acer Swift 3', '400'),
(4, 'laptop', 'Dell Inspiron 3567', '2139.97'),
(4, 'laptop', 'Apple MacBook 12', '1158.7'),
(4, 'laptop', 'Lenovo IdeaPad 320-15IKB', '1495'),
(4, 'laptop', 'Dell XPS 13', '770'),
(4, 'laptop', 'Asus Vivobook E200HA', '393.9'),
(4, 'laptop', 'Lenovo Legion Y520-15IKBN', '344.99'),
(4, 'laptop', 'HP 255 G6', '2439.97'),
(4, 'laptop', 'Dell Inspiron 5379', '498.9'),
(4, 'laptop', 'HP 15-BS101nv', '1262.4'),
(4, 'laptop', 'Dell Inspiron 5570', '1518.55'),
(4, 'laptop', 'Dell Latitude 5590', '745'),
(4, 'laptop', 'HP ProBook 470', '2858'),
(4, 'laptop', 'Chuwi LapBook 15.6', '499'),
(4, 'laptop', 'Asus E402WA-GA010T', '979'),
(4, 'laptop', 'HP 17-ak001nv', '191.9'),
(4, 'laptop', 'Lenovo IdeaPad 120S-14IAP', '999'),
(5, 'headphones', 'Apple Earbuds', '323'),
(5, 'headphones', 'Bose QuietComfort 35', '313'),
(5, 'headphones', 'Bose QuietComfort 20', '1901'),
(5, 'headphones', 'Sony MDR-7506', '329'),
(5, 'headphones', 'Shure SE215', '129'),
(5, 'headphones', 'August EP650', '299'),
(5, 'headphones', 'Bose QuietComfort 25', '420'),
(5, 'headphones', 'Bose SoundTrue', '301'),
(5, 'headphones', 'AKG K550', '482'),
(5, 'headphones', 'Apple Airpods', '493'),
(5, 'headphones', 'Audio Technica ATH-D40fs', '301'),
(5, 'headphones', 'Audio Technica ATH-M40X', '430'),
(5, 'headphones', 'Beoplay H6', '491'),
(5, 'headphones', 'Bose QuietComfort 15', '120'),
(5, 'headphones', 'FIDUE A83', '321'),
(5, 'headphones', 'Koss Portapros', '326'),
(5, 'headphones', 'Logitech G930', '659'),
(5, 'headphones', 'Mono Price Hi-Fi Light Weight Over-the-Ear Headphones', '356'),
(5, 'headphones', 'Panasonic RP-HT161', '342'),
(5, 'headphones', 'Panatronic BackBeat Pro', '546'),
(5, 'headphones', 'Sennheiser HD 280', '349'),
(5, 'headphones', 'Audio Technica ATH-M50X', '319');

-- --------------------------------------------------------

--
-- Table structure for table `types`
--

CREATE TABLE `types` (
  `id` varchar(2000) NOT NULL,
  `name` varchar(2000) NOT NULL,
  `description` varchar(2000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `types`
--

INSERT INTO `types` (`id`, `name`, `description`) VALUES
('1', '<p>Web pentesting</p>', '<p>Web is fun</p>'),
('2', '<p>Network pentesting</p>', '<p>Network is fun</p>'),
('3', '<p>Mobile pentesting</p>', '<p>Mobile is fun</p>');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(100) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `password`) VALUES
(1, 'love', 'love'),
(2, 'test', 'rest'),
(3, 'new', 'new'),
(4, 'love', 'Zxc123!@#'),
(5, 'love', 'love'),
(7, 'love', 'love'),
(8, 'love', 'Zxc123!@#');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
