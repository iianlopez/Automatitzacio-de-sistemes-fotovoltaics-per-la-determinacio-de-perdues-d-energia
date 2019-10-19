-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 17-09-2019 a las 16:06:14
-- Versión del servidor: 10.1.38-MariaDB
-- Versión de PHP: 7.3.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `hiperion`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `dades`
--

CREATE TABLE `dades` (
  `id` int(10) UNSIGNED NOT NULL,
  `id_dispositiu` int(10) UNSIGNED DEFAULT NULL,
  `data` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `w` double NOT NULL,
  `v` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `dades`
--

INSERT INTO `dades` (`id`, `id_dispositiu`, `data`, `w`, `v`) VALUES
(8, 2, '2019-08-06 16:11:30', 130.21, 22.32),
(9, 2, '2019-08-06 16:12:42', 130.438, 22.319),
(10, 2, '2019-08-06 16:15:55', 121.442, 22.052),
(11, 2, '2019-08-28 14:55:02', 69.259, 11.586),
(12, 2, '2019-09-10 16:26:33', 0, -0.01),
(13, 2, '2019-09-10 16:30:27', 0, -0.01),
(14, 2, '2019-09-11 15:17:03', 0, -0.01),
(15, 2, '2019-09-11 15:26:01', 2.17, 0.326),
(16, 2, '2019-09-11 15:26:40', 37.438, 6.202),
(17, 2, '2019-09-11 15:29:08', 0, -0.011),
(18, 2, '2019-09-11 16:01:51', 0, -0.011),
(19, 2, '2019-09-11 16:03:30', 0, -0.011),
(20, 2, '2019-09-11 16:05:14', 0, -0.011),
(21, 2, '2019-09-11 16:06:32', 0, -0.01),
(22, 2, '2019-09-11 16:36:05', 0, -0.01),
(23, 2, '2019-09-11 16:42:09', 0, -0.012),
(24, 2, '2019-09-11 17:07:04', 0, -0.01),
(25, 2, '2019-09-11 17:13:45', 0, -0.011),
(26, 2, '2019-09-11 18:24:42', 0, -0.011),
(27, 2, '2019-09-11 18:32:51', 0, -0.01),
(28, 2, '2019-09-16 17:59:35', 0, -0.01);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `dadessensorllum`
--

CREATE TABLE `dadessensorllum` (
  `id` int(10) UNSIGNED NOT NULL,
  `id_dispositiu` int(10) UNSIGNED DEFAULT NULL,
  `data` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `lux` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `dispositius`
--

CREATE TABLE `dispositius` (
  `id` int(10) UNSIGNED NOT NULL,
  `posicio` varchar(50) DEFAULT NULL,
  `tara` int(11) DEFAULT NULL,
  `info` varchar(256) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `dispositius`
--

INSERT INTO `dispositius` (`id`, `posicio`, `tara`, `info`) VALUES
(1, 'Servidor', NULL, 'Sensor Local'),
(2, 'Placa Exemple', NULL, 'Placa Exemple');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `dades`
--
ALTER TABLE `dades`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_dispositiu` (`id_dispositiu`);

--
-- Indices de la tabla `dispositius`
--
ALTER TABLE `dispositius`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `dades`
--
ALTER TABLE `dades`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT de la tabla `dispositius`
--
ALTER TABLE `dispositius`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `dades`
--
ALTER TABLE `dades`
  ADD CONSTRAINT `dades_ibfk_1` FOREIGN KEY (`id_dispositiu`) REFERENCES `dispositius` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
