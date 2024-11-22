-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3307
-- Tiempo de generación: 09-11-2024 a las 04:01:07
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bibliotec`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `libros`
--

CREATE TABLE `libros` (
  `id` int(11) NOT NULL,
  `titulo` varchar(255) NOT NULL,
  `editorial` varchar(255) NOT NULL,
  `autor` varchar(255) NOT NULL,
  `numero_paginas` int(11) NOT NULL,
  `edicion` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `libros`
--

INSERT INTO `libros` (`id`, `titulo`, `editorial`, `autor`, `numero_paginas`, `edicion`) VALUES
(1, 'Ingeniería de control moderna', 'Pearson', 'Katsuhiko Ogata', 904, '2010'),
(2, 'Python a fondo', 'Marcombo', 'Óscar Ramírez Jiménez', 79, '2021'),
(3, 'Crepúsculo', 'Penguin Random House Grupo Editorial.', 'Stephenie Meyer', 576, '2017'),
(4, 'Harry Potter y la piedra filosofal', 'De bolsillo', 'Joanne Rowling', 256, '1998'),
(5, 'Harry Potter y la cámara secreta', 'De bolsillo', 'Joanne Rowling', 296, '2000'),
(6, 'Harry Potter y el prisionero de Azkaban', 'De bolsillo', 'Joanne Rowling', 360, '2002'),
(7, 'Harry Potter y el cáliz de fuego', 'De bolsillo', 'Joanne Rowling', 672, '2003'),
(8, 'Python 2', 'Pearson', 'Óscar Ramírez Jiménez', 333, '2017'),
(9, 'Python 222', 'Conacyt', 'Óscar Morse', 882, '2019'),
(10, 'Python 2', 'Pearson', 'Óscar Ramírez Jiménez', 333, '2017'),
(11, 'Python 2', 'Pearson', 'Óscar Ramírez Jiménez', 333, '2017'),
(14, 'Python 3', 'GTA', 'Edgar Brizuela', 1000, '2022'),
(17, 'R Software', 'MSC', 'Santiago Arceo', 890, '2024'),
(18, 'Astronomía básica ', 'MSC', 'Santiago Arceo', 244, '2023'),
(19, 'Astronomía avanzada', 'MSC', 'Santiago Arceo', 278, '2024'),
(20, 'Astronomía intermedia', 'MSC', 'Santiago Arceo', 122, '2018'),
(21, 'Astronomía ', 'MSC', 'Santiago Arceo', 12244, '2018'),
(22, 'Astronomía espacial', 'SCD', 'Santiago Arceo', 3345, '2024'),
(23, 'Tres metros sobre el cielo', 'Planeta', 'Federico Moccia', 370, '2009');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `libros`
--
ALTER TABLE `libros`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `libros`
--
ALTER TABLE `libros`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
