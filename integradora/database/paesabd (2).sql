-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 24-11-2026 a las 01:40:59
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `paesabd`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clientes`
--

CREATE TABLE `clientes` (
  `id` int(11) NOT NULL,
  `nombre` varchar(150) NOT NULL,
  `telefono` varchar(20) NOT NULL,
  `email` varchar(100) NOT NULL,
  `direccion` varchar(250) NOT NULL,
  `numDireccion` int(11) NOT NULL,
  `colonia` varchar(50) NOT NULL,
  `rfc` varchar(13) NOT NULL,
  `fechaRegistro` date NOT NULL,
  `estatus` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `clientes`
--

INSERT INTO `clientes` (`id`, `nombre`, `telefono`, `email`, `direccion`, `numDireccion`, `colonia`, `rfc`, `fechaRegistro`, `estatus`) VALUES
(1, 'equipo de desarrrollo', '6181112236', 'esteeselgmail@gmail.com', 'cualquiera', 0, 'col.cualquiera', 'IAI081012HG4', '2011-03-26', 'activo'),
(2, 'arauco', '618-111-5566', 'arauco@gmail.com', '6 de enero', 512, 'col. constitucion ', 'ABC010101ABC', '2026-10-30', 'activo');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cotizaciones`
--

CREATE TABLE `cotizaciones` (
  `numCotizacion` int(11) NOT NULL,
  `total` int(11) NOT NULL,
  `estado` text NOT NULL,
  `revisado` int(11) NOT NULL,
  `ordenCompra` int(11) DEFAULT NULL,
  `docOrdenCompra` varchar(100) DEFAULT NULL,
  `tiempo` int(11) NOT NULL,
  `trabajadores` int(11) NOT NULL,
  `id_cliente` int(11) DEFAULT NULL,
  `descripcion` varchar(250) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `cotizaciones`
--

INSERT INTO `cotizaciones` (`numCotizacion`, `total`, `estado`, `revisado`, `ordenCompra`, `docOrdenCompra`, `tiempo`, `trabajadores`, `id_cliente`, `descripcion`) VALUES
(2, 4000, 'en revision', 1, 304224, 'araucoProyecto.pdf', 15, 4, 2, 'bancas de la cafeteria en la planta de arauco'),
(3, 0, 'nuevo', 6, NULL, NULL, 19, 3, 2, 'abc');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `materiales`
--

CREATE TABLE `materiales` (
  `id` int(11) NOT NULL,
  `nombre` varchar(40) NOT NULL,
  `descrpcion` varchar(250) NOT NULL,
  `medida` varchar(40) NOT NULL,
  `precioU` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `comprado` tinyint(1) NOT NULL,
  `cotizacion` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `materiales`
--

INSERT INTO `materiales` (`id`, `nombre`, `descrpcion`, `medida`, `precioU`, `cantidad`, `comprado`, `cotizacion`) VALUES
(1, 'Tubo cuadrado de acero', 'Tubo cuadrado de acero 1\" x 1\"', 'metro', 120, 25, 1, 2),
(2, 'Lámina de acero', 'Lámina de acero calibre 18', 'Hoja', 950, 2, 1, 2),
(3, 'Tornillo ', 'Tornillo 1/4\"', 'Piezas', 4, 40, 1, 2),
(4, 'Tuerca ', 'Tuerca 1/4\"', 'Piezas', 2, 40, 1, 2),
(5, 'Electrodo', 'Electrodo para soldar', 'Caja', 180, 1, 1, 2),
(6, 'a', 'b', 'a', 850, 4, 0, 2),
(7, 'Lámina de acero', 'Cubierta superior para superficie de trabajo.', '1.20 m x 2.40 m x 1/4\"', 3200, 1, 0, 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `proyectos`
--

CREATE TABLE `proyectos` (
  `id` int(11) NOT NULL,
  `fechaInicio` date NOT NULL,
  `fechaFinal` date NOT NULL,
  `cometarios` text NOT NULL,
  `estatus` text NOT NULL,
  `ordenProyecto` int(11) NOT NULL,
  `estatusCob` varchar(40) NOT NULL,
  `fechaEntreg` date NOT NULL,
  `fechaPago` date NOT NULL,
  `totalPagar` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `proyectos`
--

INSERT INTO `proyectos` (`id`, `fechaInicio`, `fechaFinal`, `cometarios`, `estatus`, `ordenProyecto`, `estatusCob`, `fechaEntreg`, `fechaPago`, `totalPagar`) VALUES
(2, '2026-11-05', '0000-00-00', 'proyecto de mesa para comedor en arauco esta a punto de ser terminado faltan algunos detalles', 'en proceso', 2, 'sin fecha de pago', '0000-00-00', '0000-00-00', 4000),
(3, '2026-11-05', '0000-00-00', 'no se han presentado inconvenientes', 'en proceso', 2, 'sin fecha de pago', '0000-00-00', '0000-00-00', 4000);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `trabajadores`
--

CREATE TABLE `trabajadores` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `apellido1` varchar(50) NOT NULL,
  `apellido2` varchar(50) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `puesto` varchar(50) NOT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `estatus` varchar(20) DEFAULT 'activo',
  `fechaRegistro` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `trabajadores`
--

INSERT INTO `trabajadores` (`id`, `nombre`, `apellido1`, `apellido2`, `username`, `password`, `puesto`, `telefono`, `email`, `estatus`, `fechaRegistro`) VALUES
(1, 'eduardo', 'trujillo', '', 'eduartrus', 'Eduard0.T', 'supervisor sistemas', '6182702252', 'eduardotrujillosoto', 'activo', '2026-11-04 00:51:33'),
(2, 'erick', 'trujillo', '', 'ericktrus', '3rick7ru', 'supervisor sistemas', '618-222-2222', 'ericktrujillo2007@gmail.com', 'activo', '2026-11-06 01:37:49'),
(3, 'Carlos', 'Mendoza', 'Hernández', 'cmendoza', '$2y$10$a12.b.Cd3E.1uV1tOXI9cM5b/4Xn9o.v7W0T88kE0I9N6K7L8M9N0', 'herrero especialista', '6181239876', 'carlos.mendoza@paesa.com.mx', 'activo', '2026-08-01 15:00:00'),
(4, 'José Luis', 'Ramírez', 'Gómez', 'jlramirez', '$2y$10$b23.c.De4F.2wW2uPYJ0dN6c/5Yo0p.w8X1U99lF1J0O7L8M9N0O1', 'soldador certificado', '6182348765', 'jl.ramirez@paesa.com.mx', 'inactivo', '2026-08-15 06:00:00'),
(5, 'Roberto', 'García', 'Valenzuela', 'rgarcia', '$2y$10$c34.d.Ef5G.3xX3vQZK1eO7d/6Zp1q.x9Y2V00mG2K1P8M9N0O1P2', 'armador industrial', '6183457654', 'roberto.garcia@paesa.com.mx', 'activo', '2026-09-01 14:15:00'),
(6, 'Miguel Ángel', 'Torres', 'López', 'mtorres', '$2y$10$d45.e.Fg6H.4yY4wRAL2fP8e/7Aq2r.y0Z3W11nH3L2Q9N0O1P2Q3', 'pintor industrial', '6184566543', 'miguel.torres@paesa.com.mx', 'activo', '2026-09-10 17:20:00'),
(7, 'Fernando', 'Sánchez', 'Castro', 'fsanchez', '$2y$10$e56.f.Gh7I.5zZ5xSBM3gQ9f/8Br3s.z1A4X22oI4M3R0O1P2Q3R4', 'soldador argonero', '6185675432', 'fernando.sanchez@paesa.com.mx', 'activo', '2026-09-20 20:00:00'),
(8, 'Alejandro', 'Vargas', 'Ríos', 'avargas', '$2y$10$f67.g.Hi8J.6aA6yTCN4hR0g/9Cs4t.a2B5Y33pJ5N4S1P2Q3R4S5', 'tornero / fresador', '6186784321', 'alejandro.vargas@paesa.com.mx', 'activo', '2026-10-01 14:00:00'),
(9, 'Daniel', 'Morales', 'Ibarra', 'dmorales', '$2y$10$g78.h.Ij9K.7bB7zUDO5iS1h/0Dt5u.b3C6Z44qK6O5T2Q3R4S5T6', 'auxiliar de taller', '6187893210', 'daniel.morales@paesa.com.mx', 'activo', '2026-10-15 18:45:00'),
(10, 'Manuel', 'González', 'Reyes', 'mgonzalez', '$2y$10$h89.i.Jk0L.8cC8aVEP6jT2i/1Eu6v.c4D7A55rL7P6U3R4S5T6U7', 'auxiliar general (disponible)', '6188902109', 'manuel.gonzalez@paesa.com.mx', 'inactivo', '2026-06-01 13:30:00'),
(11, 'Eduardo', 'Trujillo', 'Soto', 'edtrus', '$2y$10$e84.g.Hj9N.3yX3vQzK1eO7d/6Zp1q.x9Y2W10mG2K1P9L8M7N6O5', 'supervisor sistemas', '6182702252', 'eduardotrujillosoto@gmail.com', 'activo', '2026-11-04 06:51:33'),
(12, 'pepe', 'Trujillo', 'Soto', 'ertrus', '$2y$10$f95.h.Ik0O.4zY4wRAL2fP8e/7Aq2r.y0Z3X11nH3L2Q0M9N8O7P6', 'supervisor sistemas', '6182222222', 'ericktrujillo@gmail.com', 'activo', '2026-11-06 06:00:00');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `cotizaciones`
--
ALTER TABLE `cotizaciones`
  ADD PRIMARY KEY (`numCotizacion`),
  ADD KEY `fk_cotizaciones_clientes` (`id_cliente`),
  ADD KEY `fk_cotizaciones_revisado` (`revisado`);

--
-- Indices de la tabla `materiales`
--
ALTER TABLE `materiales`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_materiales_cotizaciones` (`cotizacion`);

--
-- Indices de la tabla `proyectos`
--
ALTER TABLE `proyectos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_proyectos_ordenproyecto` (`ordenProyecto`);

--
-- Indices de la tabla `trabajadores`
--
ALTER TABLE `trabajadores`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `clientes`
--
ALTER TABLE `clientes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `cotizaciones`
--
ALTER TABLE `cotizaciones`
  MODIFY `numCotizacion` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `materiales`
--
ALTER TABLE `materiales`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `proyectos`
--
ALTER TABLE `proyectos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `trabajadores`
--
ALTER TABLE `trabajadores`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `cotizaciones`
--
ALTER TABLE `cotizaciones`
  ADD CONSTRAINT `fk_cotizaciones_clientes` FOREIGN KEY (`id_cliente`) REFERENCES `clientes` (`id`),
  ADD CONSTRAINT `fk_cotizaciones_revisado` FOREIGN KEY (`revisado`) REFERENCES `trabajadores` (`id`);

--
-- Filtros para la tabla `materiales`
--
ALTER TABLE `materiales`
  ADD CONSTRAINT `fk_materiales_cotizaciones` FOREIGN KEY (`cotizacion`) REFERENCES `cotizaciones` (`numCotizacion`);

--
-- Filtros para la tabla `proyectos`
--
ALTER TABLE `proyectos`
  ADD CONSTRAINT `fk_proyectos_ordenproyecto` FOREIGN KEY (`ordenProyecto`) REFERENCES `cotizaciones` (`numCotizacion`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
