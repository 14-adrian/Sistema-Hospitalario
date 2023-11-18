-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 18-11-2023 a las 19:46:26
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `hospital_db`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cita`
--

CREATE TABLE `cita` (
  `idCita` int(11) NOT NULL,
  `Nombre Medico` varchar(150) NOT NULL,
  `Nombre Paciente` varchar(150) NOT NULL,
  `tipoConsulta` varchar(45) NOT NULL,
  `fechaSolicitud` varchar(50) NOT NULL,
  `estado` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `cita`
--

INSERT INTO `cita` (`idCita`, `Nombre Medico`, `Nombre Paciente`, `tipoConsulta`, `fechaSolicitud`, `estado`) VALUES
(4444, 'Leonidas Adrian Mendoza Flores', 'Joel Omar Martinez Ramirez', 'l', '2023-10-26', 'Inactivo'),
(100001, 'Juan Alberto Rivera Hernandez', 'Luis Andres Martinez Herrera', 'Urgencias', '19/10/2023', 'Inactivo'),
(123456, 'Carlos Alberto Moran Sanchez', 'Joel Omar Martinez Ramirez', 'Especializada', '15/10/2023', 'Activo'),
(556060, 'Juan Alberto Rivera Hernandez', 'Joel Omar Martinez Ramirez', 'Especializado', '2023-10-26', 'Activo'),
(909090, 'Alejandra Esther Mendez Lopez', 'Luis Andres Martinez Herrera', 'Urgencias', '11/02/2023', 'Activo');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `diagnostico`
--

CREATE TABLE `diagnostico` (
  `idDiagnostico` int(11) NOT NULL,
  `Paciente` varchar(100) NOT NULL,
  `Medico` varchar(100) NOT NULL,
  `id_Cita` varchar(11) NOT NULL,
  `descripcion` varchar(45) DEFAULT NULL,
  `medicina` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `diagnostico`
--

INSERT INTO `diagnostico` (`idDiagnostico`, `Paciente`, `Medico`, `id_Cita`, `descripcion`, `medicina`) VALUES
(1920, 'Luis Andres Martinez Herrera', 'Juan Alberto Rivera Hernandez', '123123', 'Dolor de cabeza y tos', 'Jarabe para la tos');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `medicina`
--

CREATE TABLE `medicina` (
  `idMedicina` int(11) NOT NULL,
  `Descripcion` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `medicina`
--

INSERT INTO `medicina` (`idMedicina`, `Descripcion`) VALUES
(4444, 'Acetaminofen'),
(9999, 'Jarabe para la tos');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `medico`
--

CREATE TABLE `medico` (
  `idMedico` int(11) NOT NULL,
  `especialidad` varchar(45) NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `telefono` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `fechaNacimiento` varchar(45) NOT NULL,
  `sexo` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `medico`
--

INSERT INTO `medico` (`idMedico`, `especialidad`, `nombre`, `telefono`, `email`, `fechaNacimiento`, `sexo`) VALUES
(1001, 'Dentista', 'Juan Alberto Rivera Hernandez', '2222-2295', 'juan@correo.com', '01/01/1979', 'M'),
(1002, 'Neurologo', 'Jerson Mauricio Herrera Herrera', '2222-4469', 'jerson@correo.com', '02/01/92', 'M'),
(1111, 'Cardiologo', 'Leonidas Adrian Mendoza Flores', '4444-4444', 'coeee@correo.com', '14/02/01', 'M'),
(1199, 'Pediatra', 'Carlos Alberto Moran Sanchez', '2233-4455', 'carAMS@correo.com', '10/05/1985', 'M'),
(1293, 'Dentista', 'Juan Manuel Jimenez Perez', '2223-4445', 'juanMJ@correo.com', '22/02/1995', 'M'),
(5050, 'Ginecologo', 'Alejandra Esther Mendez Lopez', '2224-4443', 'alem@correo.com', '22/12/1994', 'F'),
(8090, 'Psicologo', 'Raul Alejandro Vazquez Hernandez', '2222-2123', 'raulvh@correo.com', '09/02/1995', 'M');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `paciente`
--

CREATE TABLE `paciente` (
  `dui` int(11) NOT NULL,
  `nombrePaciente` varchar(45) NOT NULL,
  `telefonoPaciente` varchar(45) DEFAULT NULL,
  `correoPaciente` varchar(45) NOT NULL,
  `fechaNacimiento` varchar(45) NOT NULL,
  `sexoPaciente` varchar(45) NOT NULL,
  `alturaPaciente` varchar(45) DEFAULT NULL,
  `pesoPaciente` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `paciente`
--

INSERT INTO `paciente` (`dui`, `nombrePaciente`, `telefonoPaciente`, `correoPaciente`, `fechaNacimiento`, `sexoPaciente`, `alturaPaciente`, `pesoPaciente`) VALUES
(111222333, 'Joel Omar Martinez Ramirez', '2555-4443', 'joel@correo.com', '01/02/2003', 'M', '1.80m', '160lb'),
(123456788, 'Luis Andres Martinez Herrera', '2455-6666', 'luis@correo.com', '10/05/1985', 'M', '1.80m', '190lb'),
(123456789, 'Leonidas Adrian Mendoza Flores', '2222-2294', 'leo@mail.com', '14/02/2001', 'M', '1.75m', '185lb');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `Nombre` varchar(200) NOT NULL,
  `Correo` varchar(100) NOT NULL,
  `DUI` varchar(20) NOT NULL,
  `Cargo` varchar(30) NOT NULL,
  `Contraseña` varchar(32) NOT NULL,
  `Usuario` varchar(16) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `Nombre`, `Correo`, `DUI`, `Cargo`, `Contraseña`, `Usuario`) VALUES
(1, 'Admin', 'admin1@admin.com', '--', '--', 'admin', 'admin'),
(2, 'Leonidas Adrian Mendoza Flores', 'leo@mail.com', '123412342', 'Medico', '12345', 'leo14');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `cita`
--
ALTER TABLE `cita`
  ADD PRIMARY KEY (`idCita`);

--
-- Indices de la tabla `diagnostico`
--
ALTER TABLE `diagnostico`
  ADD PRIMARY KEY (`idDiagnostico`);

--
-- Indices de la tabla `medicina`
--
ALTER TABLE `medicina`
  ADD PRIMARY KEY (`idMedicina`);

--
-- Indices de la tabla `medico`
--
ALTER TABLE `medico`
  ADD PRIMARY KEY (`idMedico`);

--
-- Indices de la tabla `paciente`
--
ALTER TABLE `paciente`
  ADD PRIMARY KEY (`dui`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
