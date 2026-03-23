-- --------------------------------------------------------
-- 主機:                           127.0.0.1
-- 伺服器版本:                        10.11.7-MariaDB - mariadb.org binary distribution
-- 伺服器作業系統:                      Win64
-- HeidiSQL 版本:                  12.6.0.6765
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- 傾印 arduino 的資料庫結構
CREATE DATABASE IF NOT EXISTS `arduino` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */;
USE `arduino`;

-- 傾印  資料表 arduino.music 結構
CREATE TABLE IF NOT EXISTS `music` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `frequency` text DEFAULT NULL,
  `name` text DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 正在傾印表格  arduino.music 的資料：~4 rows (近似值)
REPLACE INTO `music` (`id`, `frequency`, `name`) VALUES
	(1, '659:0.5,622:0.5,659:0.5,622:0.5,659:0.5,494:0.5,587:0.5,523:0.5,440:1.5,0:0.0,330:0.5,440:0.5,494:1.5,330:0.5,415:0.5,494:0.5,523:1.5,659:0.5,622:0.5,659:0.5,622:0.5,659:0.5,494:0.5,587:0.5,523:0.5,440:1.5,0:0.0,330:0.5,440:0.5,494:1.5,330:0.5,523:0.5,494:0.5,440:1.5', 'For Alice'),
	(2, '261:0.8,261:0.8,294:0.8,261:0.8,349:0.8,330:1.6,261:0.8,261:0.8,294:0.8,261:0.8,392:0.8,349:1.6,261:0.8,261:0.8,523:0.8,440:0.8,349:0.8,330:0.8,294:1.6,466:0.8,466:0.8,440:0.8,349:0.8,392:0.8,349:1.6', 'Happy Birthday'),
	(3, '262:0.5,294:0.5,330:0.5,349:0.5,392:0.5,440:0.5,494:0.5,523:0.5', 'Do-Re-Mi'),
	(4, '262:0.5,262:0.5,392:0.5,392:0.5,440:0.5,440:0.5,392:0.5,0:0.1,349:0.7,349:0.5,330:0.5,330:0.5,294:0.5,294:0.5,262:0.5,0:0.1,392:0.7,392:0.5,349:0.5,349:0.5,330:0.5,330:0.5,294:0.5,0:0.1,392:0.7,392:0.5,349:0.5,349:0.5,330:0.5,330:0.5,294:0.5,0:0.1', 'Little Star');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
