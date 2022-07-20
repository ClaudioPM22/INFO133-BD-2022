-- MySQL dump 10.19  Distrib 10.3.34-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: biobio_test
-- ------------------------------------------------------
-- Server version	10.3.34-MariaDB-0ubuntu0.20.04.1

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
-- Table structure for table `dueños`
--

DROP TABLE IF EXISTS `dueños`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dueños` (
  `id_dueños` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(100) DEFAULT NULL,
  `Tipo` varchar(10) DEFAULT NULL,
  `Fecha_adquisicion` date DEFAULT NULL,
  PRIMARY KEY (`id_dueños`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dueños`
--

LOCK TABLES `dueños` WRITE;
/*!40000 ALTER TABLE `dueños` DISABLE KEYS */;
/*!40000 ALTER TABLE `dueños` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `medio_de_prensa`
--

DROP TABLE IF EXISTS `medio_de_prensa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `medio_de_prensa` (
  `id_medio` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(100) DEFAULT NULL,
  `Fecha_Creación` date DEFAULT NULL,
  `URL` varchar(500) DEFAULT NULL,
  `Región` varchar(4) DEFAULT NULL,
  `País` varchar(10) DEFAULT NULL,
  `Idioma` varchar(20) DEFAULT NULL,
  `Tipo` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id_medio`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `medio_de_prensa`
--

LOCK TABLES `medio_de_prensa` WRITE;
/*!40000 ALTER TABLE `medio_de_prensa` DISABLE KEYS */;
/*!40000 ALTER TABLE `medio_de_prensa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `menciona`
--

DROP TABLE IF EXISTS `menciona`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `menciona` (
  `id_noticia` int(11) NOT NULL,
  `id_persona` int(11) NOT NULL,
  PRIMARY KEY (`id_noticia`,`id_persona`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `menciona`
--

LOCK TABLES `menciona` WRITE;
/*!40000 ALTER TABLE `menciona` DISABLE KEYS */;
/*!40000 ALTER TABLE `menciona` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `noticia`
--

DROP TABLE IF EXISTS `noticia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `noticia` (
  `id_noticia` int(11) NOT NULL AUTO_INCREMENT,
  `URL` varchar(500) DEFAULT NULL,
  `Titulo` varchar(300) DEFAULT NULL,
  `fecha_publicaion` date DEFAULT NULL,
  `Contenido` text DEFAULT NULL,
  `id_medio` int(11) DEFAULT NULL,
  `id_persona` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_noticia`),
  KEY `fk1` (`id_medio`),
  CONSTRAINT `fk1` FOREIGN KEY (`id_medio`) REFERENCES `medio_de_prensa` (`id_medio`) ON DELETE SET NULL ON UPDATE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `noticia`
--

LOCK TABLES `noticia` WRITE;
/*!40000 ALTER TABLE `noticia` DISABLE KEYS */;
INSERT INTO `noticia` VALUES (1,'https://elcontraste.cl/martes-19-de-julio-reporte-de-casos-por-comunas-en-el-biobio/19/07/2022/','Martes 19 de julio: Reporte de casos por comunas en el Biobío','2022-07-19','Este martes 19 de julio, se reportaron 316 casos nuevos de coronavirus. Con ello, el total de contagiados llegó a 399.450 personas, de las cuales 2.796 están activas.\nLos fallecidos, la cifra se mantuvo en 3.693 en la región. Además, hay 683 fallecimientos probables, totalizando 4.376.\nLas comunas con mayor tasa de activos por cada 100 mil habitantes corresponden a Contulmo, con 252,8 casos activos; Santa Bárbara, con 239,9 casos y Concepción, con 232,7 casos. Además, las comunas que presentan la mayor cantidad de casos activos, son Concepción con 554; seguida de Los Ángeles con 338 y Talcahuano, con 304 casos activos.',NULL,NULL),(2,'https://elcontraste.cl/delincuente-fue-herido-de-un-escopetazo-en-mulchen/19/07/2022/','Delincuente fue herido de un escopetazo en Mulchén','2022-07-19','Un hombre de 51 años de edad, fue herido de un escopetazo la noche del lunes en la comuna de Mulchén.\nEl hecho ocurrió pasadas las 20 horas, cuando se solicitó la concurrencia de personal de la 2ª Comisaría de Carabineros hasta el centro asistencial por un paciente que ingresó con impactos balísticos en su cuerpo.\nAhí, pudieron constatar que se trata de un delincuente que registra al menos 5 causas penales por robo con violencia, tráfico de drogas y hurto.',NULL,NULL),(3,'https://elcontraste.cl/banda-dedicada-al-abigeato-fue-detenida-en-cabrero-atropellaron-a-un-carabinero/18/07/2022/','Banda dedicada al abigeato fue detenida en Cabrero: Atropellaron a un Carabinero','2022-07-18','Un amplio despliegue policial permitió detener a una banda dedicada al abigeato en la comuna de Cabrero. Todo el procedimiento terminó con 4 detenidos y un Carabinero atropellado.\nEl procedimiento se realizó la tarde de este domingo, cerca de las 18:45 horas. Ahí, personal de servicio, recibió un llamado al Plan Cuadrante, por el faenamiento y robo de dos vacunos desde Pemuco, provincia de Diguillín.\nEl dueño de los animales, enterado de lo ocurrido, inició un seguimiento a la camioneta Fiat modelo Fullback.',NULL,NULL),(4,'https://elcontraste.cl/lunes-18-de-julio-reporte-de-casos-por-comunas-en-el-biobio/18/07/2022/','Lunes 18 de julio: Reporte de casos por comunas en el Biobío','2022-07-18','Este lunes 18 de julio, se reportaron 410 casos nuevos de Covid-19 en la región del Biobío. Con ello, los casos totales llegan a 399.129, de los cuales 3.434 están activos.\nLos fallecidos, aumentó en 3 personas, pasando de 3.690 a 3.693 en la región. Además, hay 683 fallecimientos probables, totalizando 4.376.\n',NULL,NULL),(5,'https://elcontraste.cl/domingo-17-de-julio-reporte-de-casos-por-comunas-en-el-biobio/17/07/2022/','Domingo 17 de julio: Reporte de casos por comunas en el Biobío','2022-07-17','Este domingo 17 de julio se informaron 703 casos nuevos de coronavirus. Con ello, se acumulan 398.707 contagiados, de los cuales 3.521 están activos.\nLos fallecidos, aumentó en 3 personas, pasando de a 3.687 a 3.690 en la región. Además, hay 683 fallecimientos probables, totalizando 4.373.\nLas comunas con mayor tasa de activos por cada 100 mil habitantes corresponden a Contulmo, con 379,1 casos activos; Santa Bárbara, con 328,9 casos y San Rosendo, con 304,6 casos. Además, las comunas que presentan la mayor cantidad de casos activos, son Concepción con 719; seguida de Los Ángeles con 427 y Talcahuano, con 356 casos activos.',NULL,NULL),(6,'https://elcontraste.cl/sismo-de-44-grados-afecto-a-los-angeles/16/07/2022/','Sismo de 4,5 grados afectó a Los Ángeles','2022-07-16','Un sismo de 4,5º grados de magnitud afectó la tarde de este sábado a la región del Biobío.\nEl movimiento se registró a las 18:33 y su epicentro estuvo a 15 kilómetros al Este de Los Ángeles.\nSegún se pudo percibir, el movimiento tuvo una duración de breves segundos, pero la fuerza logró dejar evidencias en lámparas u objetos de las viviendas.',NULL,NULL),(7,'https://elcontraste.cl/encuentran-sin-vida-al-hombre-desaparecido-en-nacimiento/16/07/2022/','Encuentran sin vida al hombre desaparecido en Nacimiento','2022-07-16','La tarde de este sábado cerca de las 12:30, se logró encontrar el cuerpo sin vida de Luis Fernando Jara Araya, quien desapareció el pasado 29 de junio en el sector La Laguna de la comuna de Nacimiento.\nRecordemos que durante las últimas semanas, diversos equipos de búsqueda intentaban dar con su paradero.\nDe esta manera, el hallazgo ocurrió precisamente en el río Culenco, donde se encuentran las unidades de emergencia y la familia para poder retirar el cuerpo.',NULL,NULL),(8,'https://elcontraste.cl/operativo-de-la-pdi-en-laja-permite-la-captura-de-una-traficante/16/07/2022/','Operativo de la PDI en Laja permite la captura de una traficante','2022-07-16','La Policía de Investigaciones logró la detención de una traficante de drogas en la comuna de Laja.\nEl trabajo fue desarrollado la madrugada del viernes por parte del Grupo Microtráfico Cero perteneciente a la Brigada de Investigación Criminal y Contra el Crimen Organizado de Cabrero.\nLuego de una investigación realizada por la policía, se logró establecer que en el sector Altos del Laja, una mujer usaba su domicilio particular, para realizar la dosificación y posteriormente la venta de drogas en el sector.',NULL,NULL),(9,'https://elcontraste.cl/sabado-16-de-julio-reporte-de-casos-por-comunas-en-el-biobio/16/07/2022/','Sábado 16 de julio: Reporte de casos por comunas en el Biobío','2022-07-16','Este sábado 16 de julio de 2022, la Seremi de Salud informó 715 casos nuevos de coronavirus. Con ello, el total de contagiados desde el primer día de pandemia en la región, llega a 397.968. De ellos, 3.410 están activos, es decir, pueden contagiar la enfermedad.\nLos fallecidos, aumentó en 17 personas, pasando de 3.670 a 3.687 en la región. Además, hay 683 fallecimientos probables, totalizando 4.370.\nLas comunas con mayor tasa de activos por cada 100 mil habitantes corresponden a Santa Bárbara, con 349,5 casos activos; San Rosendo, con 332,3 casos y Concepción, con 285,6 casos. Además, las comunas que presentan la mayor cantidad de casos activos, son Concepción con 680; seguida de Los Ángeles con 426 y Talcahuano, con 346 casos activos.',NULL,NULL),(10,'https://elcontraste.cl/carabineros-logro-frustrar-robo-la-asociacion-de-canalistas-en-mulchen/15/07/2022/','Carabineros logró frustrar robo la Asociación de Canalistas en Mulchén','2022-07-15','Carabineros logró frustrar un robo a la Asociación de Canalistas de Mulchén, la noche del jueves.\nEl hecho ocurrió a las 20:45 horas, cuando la administración de Canalistas Biobío Sur, avisaron a la unidad policial que desconocidos habían forzado y destruido la reja perimetral. En ese lugar, se encuentra la estación de telemetría que regula el estado de las aguas de los canales de regadío.\nLos delincuentes, buscaban sustraer desde el interior diversas especies.',NULL,NULL),(11,'https://elcontraste.cl/martes-19-de-julio-reporte-de-casos-por-comunas-en-el-biobio/19/07/2022/','Martes 19 de julio: Reporte de casos por comunas en el Biobío','2022-07-19','Este martes 19 de julio, se reportaron 316 casos nuevos de coronavirus. Con ello, el total de contagiados llegó a 399.450 personas, de las cuales 2.796 están activas.\nLos fallecidos, la cifra se mantuvo en 3.693 en la región. Además, hay 683 fallecimientos probables, totalizando 4.376.\nLas comunas con mayor tasa de activos por cada 100 mil habitantes corresponden a Contulmo, con 252,8 casos activos; Santa Bárbara, con 239,9 casos y Concepción, con 232,7 casos. Además, las comunas que presentan la mayor cantidad de casos activos, son Concepción con 554; seguida de Los Ángeles con 338 y Talcahuano, con 304 casos activos.',NULL,NULL),(12,'https://elcontraste.cl/delincuente-fue-herido-de-un-escopetazo-en-mulchen/19/07/2022/','Delincuente fue herido de un escopetazo en Mulchén','2022-07-19','Un hombre de 51 años de edad, fue herido de un escopetazo la noche del lunes en la comuna de Mulchén.\nEl hecho ocurrió pasadas las 20 horas, cuando se solicitó la concurrencia de personal de la 2ª Comisaría de Carabineros hasta el centro asistencial por un paciente que ingresó con impactos balísticos en su cuerpo.\nAhí, pudieron constatar que se trata de un delincuente que registra al menos 5 causas penales por robo con violencia, tráfico de drogas y hurto.',NULL,NULL),(13,'https://elcontraste.cl/banda-dedicada-al-abigeato-fue-detenida-en-cabrero-atropellaron-a-un-carabinero/18/07/2022/','Banda dedicada al abigeato fue detenida en Cabrero: Atropellaron a un Carabinero','2022-07-18','Un amplio despliegue policial permitió detener a una banda dedicada al abigeato en la comuna de Cabrero. Todo el procedimiento terminó con 4 detenidos y un Carabinero atropellado.\nEl procedimiento se realizó la tarde de este domingo, cerca de las 18:45 horas. Ahí, personal de servicio, recibió un llamado al Plan Cuadrante, por el faenamiento y robo de dos vacunos desde Pemuco, provincia de Diguillín.\nEl dueño de los animales, enterado de lo ocurrido, inició un seguimiento a la camioneta Fiat modelo Fullback.',NULL,NULL),(14,'https://elcontraste.cl/lunes-18-de-julio-reporte-de-casos-por-comunas-en-el-biobio/18/07/2022/','Lunes 18 de julio: Reporte de casos por comunas en el Biobío','2022-07-18','Este lunes 18 de julio, se reportaron 410 casos nuevos de Covid-19 en la región del Biobío. Con ello, los casos totales llegan a 399.129, de los cuales 3.434 están activos.\nLos fallecidos, aumentó en 3 personas, pasando de 3.690 a 3.693 en la región. Además, hay 683 fallecimientos probables, totalizando 4.376.\n',NULL,NULL),(15,'https://elcontraste.cl/domingo-17-de-julio-reporte-de-casos-por-comunas-en-el-biobio/17/07/2022/','Domingo 17 de julio: Reporte de casos por comunas en el Biobío','2022-07-17','Este domingo 17 de julio se informaron 703 casos nuevos de coronavirus. Con ello, se acumulan 398.707 contagiados, de los cuales 3.521 están activos.\nLos fallecidos, aumentó en 3 personas, pasando de a 3.687 a 3.690 en la región. Además, hay 683 fallecimientos probables, totalizando 4.373.\nLas comunas con mayor tasa de activos por cada 100 mil habitantes corresponden a Contulmo, con 379,1 casos activos; Santa Bárbara, con 328,9 casos y San Rosendo, con 304,6 casos. Además, las comunas que presentan la mayor cantidad de casos activos, son Concepción con 719; seguida de Los Ángeles con 427 y Talcahuano, con 356 casos activos.',NULL,NULL),(16,'https://elcontraste.cl/sismo-de-44-grados-afecto-a-los-angeles/16/07/2022/','Sismo de 4,5 grados afectó a Los Ángeles','2022-07-16','Un sismo de 4,5º grados de magnitud afectó la tarde de este sábado a la región del Biobío.\nEl movimiento se registró a las 18:33 y su epicentro estuvo a 15 kilómetros al Este de Los Ángeles.\nSegún se pudo percibir, el movimiento tuvo una duración de breves segundos, pero la fuerza logró dejar evidencias en lámparas u objetos de las viviendas.',NULL,NULL),(17,'https://elcontraste.cl/encuentran-sin-vida-al-hombre-desaparecido-en-nacimiento/16/07/2022/','Encuentran sin vida al hombre desaparecido en Nacimiento','2022-07-16','La tarde de este sábado cerca de las 12:30, se logró encontrar el cuerpo sin vida de Luis Fernando Jara Araya, quien desapareció el pasado 29 de junio en el sector La Laguna de la comuna de Nacimiento.\nRecordemos que durante las últimas semanas, diversos equipos de búsqueda intentaban dar con su paradero.\nDe esta manera, el hallazgo ocurrió precisamente en el río Culenco, donde se encuentran las unidades de emergencia y la familia para poder retirar el cuerpo.',NULL,NULL),(18,'https://elcontraste.cl/operativo-de-la-pdi-en-laja-permite-la-captura-de-una-traficante/16/07/2022/','Operativo de la PDI en Laja permite la captura de una traficante','2022-07-16','La Policía de Investigaciones logró la detención de una traficante de drogas en la comuna de Laja.\nEl trabajo fue desarrollado la madrugada del viernes por parte del Grupo Microtráfico Cero perteneciente a la Brigada de Investigación Criminal y Contra el Crimen Organizado de Cabrero.\nLuego de una investigación realizada por la policía, se logró establecer que en el sector Altos del Laja, una mujer usaba su domicilio particular, para realizar la dosificación y posteriormente la venta de drogas en el sector.',NULL,NULL),(19,'https://elcontraste.cl/sabado-16-de-julio-reporte-de-casos-por-comunas-en-el-biobio/16/07/2022/','Sábado 16 de julio: Reporte de casos por comunas en el Biobío','2022-07-16','Este sábado 16 de julio de 2022, la Seremi de Salud informó 715 casos nuevos de coronavirus. Con ello, el total de contagiados desde el primer día de pandemia en la región, llega a 397.968. De ellos, 3.410 están activos, es decir, pueden contagiar la enfermedad.\nLos fallecidos, aumentó en 17 personas, pasando de 3.670 a 3.687 en la región. Además, hay 683 fallecimientos probables, totalizando 4.370.\nLas comunas con mayor tasa de activos por cada 100 mil habitantes corresponden a Santa Bárbara, con 349,5 casos activos; San Rosendo, con 332,3 casos y Concepción, con 285,6 casos. Además, las comunas que presentan la mayor cantidad de casos activos, son Concepción con 680; seguida de Los Ángeles con 426 y Talcahuano, con 346 casos activos.',NULL,NULL),(20,'https://elcontraste.cl/carabineros-logro-frustrar-robo-la-asociacion-de-canalistas-en-mulchen/15/07/2022/','Carabineros logró frustrar robo la Asociación de Canalistas en Mulchén','2022-07-15','Carabineros logró frustrar un robo a la Asociación de Canalistas de Mulchén, la noche del jueves.\nEl hecho ocurrió a las 20:45 horas, cuando la administración de Canalistas Biobío Sur, avisaron a la unidad policial que desconocidos habían forzado y destruido la reja perimetral. En ese lugar, se encuentra la estación de telemetría que regula el estado de las aguas de los canales de regadío.\nLos delincuentes, buscaban sustraer desde el interior diversas especies.',NULL,NULL);
/*!40000 ALTER TABLE `noticia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `personas`
--

DROP TABLE IF EXISTS `personas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `personas` (
  `id_persona` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(100) DEFAULT NULL,
  `Profesion` varchar(50) DEFAULT NULL,
  `Fecha_nacimiento` date DEFAULT NULL,
  `Nacionalidad` varchar(30) DEFAULT NULL,
  `Popularidad` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_persona`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `personas`
--

LOCK TABLES `personas` WRITE;
/*!40000 ALTER TABLE `personas` DISABLE KEYS */;
INSERT INTO `personas` VALUES (1,'Luis Fernando Jara Araya','0','0000-00-00','0',0),(2,'Luis Fernando Jara Araya','0','0000-00-00','0',0);
/*!40000 ALTER TABLE `personas` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-07-20 16:59:03
