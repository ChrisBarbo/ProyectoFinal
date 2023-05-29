-- phpMyAdmin SQL Dump
-- version 4.7.7
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 05-12-2019 a las 16:08:11
-- Versión del servidor: 5.7.21-log
-- Versión de PHP: 7.2.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `proyecto`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cliente`
--

CREATE TABLE `cliente` (
  `idcliente` int(11) NOT NULL,
  `Usuario` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish_ci NOT NULL,
  `nombrec` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  `correoc` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `direccion` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `telefonoc` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `clave` varchar(100) COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `cliente`
--

INSERT INTO `cliente` (`idcliente`, `Usuario`, `nombrec`, `correoc`, `direccion`, `telefonoc`, `clave`) VALUES
(14, 'LiliBM', 'Liliana Barbosa Mederos', 'li.li100@hotmail.com', 'Av. Torremolinos', '3265412487', '$2b$12$wkpBmbLRpF/cFfq9996dBuydJYDc7OV0jlBwAZsO3jo44FzSlcuGO'),
(15, 'Luisgr', 'Luis Jose Garcia Robles', 'luisgr@hotmail.com', 'Fracc. 18 de Marzo', '2335565943', '$2b$12$B7sNGwONyTjuuQ3RAL5wl.YLsMPb7ITye54Z5Gm3IGPfrnkNLboyO'),
(16, 'BrendaBM', 'Brenda Barbosa Mederos', 'brendabarmed@gmail', 'Fracc. 18 de Marzo', '3315264584', '$2b$12$QuszhH7cWjPBqYdBZPygEeY/.VHUXPPYzLgSXy2sF5FfFsZteS4Mu'),
(17, 'Tati11', 'Santiago Garcia Barbosa', 'santi@gmail.com', 'Av. 145 de abc', '5568731154', '$2b$12$JUmusQDDWoSiykRqUkJUdeeQrjRI9qy8jpEkF/rqn7RdXm.lyYk62'),
(20, 'Chris2019', 'Christian Garcia Barbosa', 'chrisgb2000@outlook.com', 'Av. De la Mancha 22569', '3314458962', '$2b$12$uH45XpfUceBfEvgUc//sCOwz0jvimFEi2g5guwcnHPOjrrByn3bpe'),
(21, 'Administrador', 'Administrador', 'prueba1@hotmail.com', 'Av. prueba123', '3326598', '$2b$12$TF2phe5Iq5L6Y4vPfwPf.uBorg61vxYPG4RmBGL8Drhgp8x.rIQ86'),
(23, 'Luisa1', 'Luis Angel Hernandez', '123@ooo.com', 'Av. Federalismo', '3366372612', '$2b$12$nIiG0G4dGkkzg8XLu5aDyO/Qfr40.YrQck3DFew0CAENdlNYSpUwO');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `hospedaje`
--

CREATE TABLE `hospedaje` (
  `idhotel` int(11) NOT NULL,
  `descripcion` varchar(100) NOT NULL,
  `nombreh` varchar(50) NOT NULL,
  `valoracion` varchar(11) NOT NULL,
  `estancia` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `hospedaje`
--

INSERT INTO `hospedaje` (`idhotel`, `descripcion`, `nombreh`, `valoracion`, `estancia`) VALUES
(2, '8 dias y 7 noches', 'The Westin', '3 estrellas', '8 dias'),
(3, ' 5 noches y 6 dias', 'Hilton', '5 estrellas', '5 dias'),
(4, '3 dias y 2 noches', 'Trivago', '5 estrellas', '3 dias'),
(5, '8 dias y 7 noches', 'New York Times', '5 estrellas', '8 dias');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reservacion`
--

CREATE TABLE `reservacion` (
  `idreservacion` int(5) NOT NULL,
  `idcliente` int(11) NOT NULL,
  `idhotel` int(5) NOT NULL,
  `idtransporte` int(5) NOT NULL,
  `cantdias` int(11) NOT NULL,
  `cantpersonas` int(11) NOT NULL,
  `llegadah` datetime NOT NULL,
  `salidah` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `transporte`
--

CREATE TABLE `transporte` (
  `tipot` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  `clase` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `preciot` int(11) DEFAULT NULL,
  `marca` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `idtransporte` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `transporte`
--

INSERT INTO `transporte` (`tipot`, `clase`, `preciot`, `marca`, `idtransporte`) VALUES
('Avion', 'Clase Turista', 5000, 'magni', 2),
('Tren', 'Primera Clase', 3500, 'magni', 3),
('Avion', 'Clase Turista', 2500, 'interjet', 4),
('Barco', 'Primera Clase', 1500, 'volaris', 5),
('Tren', 'Primera Clase', 2000, 'aeromex', 6),
('Camion', 'Primera Clase', 800, 'interjet', 7),
('Avion', 'Clase Turista', 250, 'volaris', 8),
('Barco', 'Clase Turista', 1500, 'Velez', 10),
('Camion', 'Clase Turista', 700, 'Primera Plus', 11);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `cliente`
--
ALTER TABLE `cliente`
  ADD PRIMARY KEY (`idcliente`);

--
-- Indices de la tabla `hospedaje`
--
ALTER TABLE `hospedaje`
  ADD PRIMARY KEY (`idhotel`);

--
-- Indices de la tabla `reservacion`
--
ALTER TABLE `reservacion`
  ADD PRIMARY KEY (`idreservacion`),
  ADD KEY `idhotel` (`idhotel`),
  ADD KEY `idtransporte` (`idtransporte`),
  ADD KEY `idcliente` (`idcliente`);

--
-- Indices de la tabla `transporte`
--
ALTER TABLE `transporte`
  ADD PRIMARY KEY (`idtransporte`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `cliente`
--
ALTER TABLE `cliente`
  MODIFY `idcliente` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT de la tabla `hospedaje`
--
ALTER TABLE `hospedaje`
  MODIFY `idhotel` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `reservacion`
--
ALTER TABLE `reservacion`
  MODIFY `idreservacion` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `transporte`
--
ALTER TABLE `transporte`
  MODIFY `idtransporte` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `reservacion`
--
ALTER TABLE `reservacion`
  ADD CONSTRAINT `reservacion_ibfk_1` FOREIGN KEY (`idhotel`) REFERENCES `hospedaje` (`idhotel`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `reservacion_ibfk_2` FOREIGN KEY (`idtransporte`) REFERENCES `transporte` (`idtransporte`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `reservacion_ibfk_3` FOREIGN KEY (`idcliente`) REFERENCES `cliente` (`idcliente`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
