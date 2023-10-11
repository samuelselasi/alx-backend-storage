-- MySQL dump 10.13  Distrib 5.7.30, for Linux (x86_64)
--
-- Host: localhost    Database: holberton
-- ------------------------------------------------------
-- Server version	5.7.30-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `names`
--

DROP TABLE IF EXISTS `names`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `names` (
  `name` varchar(255) DEFAULT NULL,
  `score` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `names`
--

LOCK TABLES `names` WRITE;
/*!40000 ALTER TABLE `names` DISABLE KEYS */;
INSERT INTO `names` VALUES ('tetgdstryl',63),('mgilzevvvu',125),('amswbfvkgz',150),('yxelwofllq',106),('qjxfzerloh',142),('gkwjrsasno',70),('sjhjdnbrez',143),('ppzvjfmvww',143),('uioylamjuq',84),('zfrmtqltvi',73),('nrynrfhsfw',193),('ghqusgbxze',126),('ajkliszewx',196),('nffjnxhlqw',72),('tcztsxcfze',174),('bewwrvpgjg',176),('pmirwzmaxz',189),('zxficeagnq',185),('prvwttvcpd',179),('anvyjhjumi',180),('pqrkfsomwa',79),('nmgqtxlcql',192),('kcdtgkyfgv',121),('hwhfpjpyuk',89),('jnwbeguihg',171),('jeumuymxaf',77),('pxydfojeak',123),('rimctfitfv',58),('zfpfeqdtpg',198),('viyvsryvgi',100),('mokgwklsyt',57),('zmyysotohr',122),('wdiqruoblu',161),('lueegcpbio',92),('chghbkqadb',83),('lwhpjsieox',191),('lcsqykvkul',183),('usgfjwfzpf',63),('analcbkkum',122),('sncnrhpebw',150),('amlzlzpxbb',98),('bcjjlvwygx',196),('ucvmtcspjt',197),('zphxmfkoxn',125),('hfmelyepzn',138),('hyhptitauf',121),('yddzwktqrn',92),('vslkakzzbz',144),('nltrerjbcw',159),('fujwuwnoof',64),('cvsitmypwg',139),('mlduwbzgbt',69),('rvmgvjxwqy',159),('gdwqbquhyg',145),('ykjpquoznb',87),('wxgmsgetos',114),('fturufwxkh',50),('ajrcfaiyld',164),('cjudwbgiqx',167),('arfexyobyi',182),('xupuqbckgz',119),('mdaibpqtfo',130),('ksrsxspsfn',146),('zkuoegxypd',80),('xzfxtrwlyt',77),('hiqwwxranv',151),('gbgzfgsxhc',86),('cyvqmiawop',79),('rfphpojhqx',179),('nghwcpvlpc',197),('oacyvtsjpk',75),('xdrmxthpnu',71),('vbelgutbaz',76),('iaosldhghz',188),('nxraiyryep',96),('iptvjcksqy',58),('itbdyzwzdu',83),('xlzphiyeum',148),('bukcmuzqew',85),('ttqiliiqfk',125),('nvaiavtxsy',69),('hnlxbjeiah',159),('ppkxwjwksy',127),('fehkbynxzc',95),('bisssqunou',148),('iobkqvxcwv',95),('kwjbpihfxx',125),('amddukyiwz',145),('jhnymbyquu',101),('tgaovfbjtr',126),('euygdeulgo',91),('cdejjybrba',53),('iwzzfjfxbl',134),('enbufisukm',96),('uqgyvltjem',67),('zkfvffdoky',102),('bkuekcblnd',103),('aiompkywxu',141),('auxffpbldd',150),('wpueufcinq',186),('dkmavfabgd',76),('bgovnnbbvt',167),('sjbpqwzusm',187),('lnxxsxilvu',139),('efrmedkdjl',177),('zjuoryvdvy',57),('frwwgggpfp',177),('fputputelm',113),('onafbgvhsb',196),('iyzftaijyx',184),('kxbnwvdapo',111),('wfkfkomymy',158),('gavnibumqz',82),('qghigyabzp',53),('qpzmcnmshf',164),('awddaqwbmw',76),('mfhsahwtny',64),('aomagvxxpv',50),('kzayaysgqx',63),('nqknsqween',178),('tlcmktrtug',101),('ifqkgkeyqv',136),('nvmdlygtlf',63),('nuitfmxzpd',191),('rhzjbqnvja',146),('renvyevfgm',86),('vvnqnltazx',188),('onajhzraax',145),('oiobpvkvrg',74),('mzoxphvqzh',183),('actqhfwgve',83),('nprcoskraw',192),('mhonuxeory',130),('yqictmaboc',69),('sbdryeqckf',152),('entwkvajau',79),('zdxbxncwua',139),('orzhrhqpww',108),('cafmdeqmro',124),('kmeqyjrfpi',83),('fmokajvpvn',153),('golwvhwjjc',162),('pgddwlvkrn',109),('qikwqwglsc',185),('iajjozqswm',78),('yjadclutpo',198),('aujjevkwsn',125),('yqsyopnclt',107),('rslqabcbie',67),('meerdtjmuj',159),('ktygorupas',91),('gtjwjutkdu',65),('hyoisxzulf',78),('sabdyytrpl',144),('tlrbjxpoqy',127),('yrmixirpmc',171),('lwczsnwina',180),('cbnbxrrvgi',182),('tbyxsphtgf',156),('tuzrdzynoq',191),('hkghmluwcd',105),('buhpewbehr',133),('scenuypzsh',87),('jhujcyzkdc',50),('gvaahhdrdr',86),('unumhagjei',114),('muyndtsbuc',60),('ieqkvomgmq',193),('zmnlalhhvi',115),('miscqdvizu',129),('tmxavfpgmj',62),('jwykhqmhup',78),('ppeaukfbqo',137),('dekcpeyzpx',83),('rtjjxlgliv',84),('eraesxqiad',94),('byqauobexg',118),('hbgwixpwom',153),('ifbnaaglto',109),('xxiuolgklq',152),('bnlabaxoia',173),('qlhagyjwtx',162),('cwzgsndozl',103),('mtflktumte',145),('lppruxzhxj',114),('tebttgcvdj',112),('besgfodmot',58),('rguuuzvvlp',197),('lgjkmrmmyf',155),('duabgdrfzh',79),('hdtwojhqxn',78);
/*!40000 ALTER TABLE `names` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-06-09  8:01:13
