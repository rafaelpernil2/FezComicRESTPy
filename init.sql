-- MySQL Script generated by MySQL Workbench
-- Sun Jan 20 20:26:08 2019
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

CREATE USER IF NOT EXISTS 'iweb'@'%' IDENTIFIED BY 'iweb';
GRANT ALL PRIVILEGES ON *.* TO 'iweb'@'%';

-- -----------------------------------------------------
-- Schema iweb
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `iweb` ;

-- -----------------------------------------------------
-- Schema iweb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `iweb` DEFAULT CHARACTER SET utf8 ;
USE `iweb` ;

-- -----------------------------------------------------
-- Table `iweb`.`serie`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `iweb`.`serie` ;

CREATE TABLE IF NOT EXISTS `iweb`.`serie` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(60) NOT NULL,
  `anotacion_privada` VARCHAR(200) NULL DEFAULT NULL,
  `genero` VARCHAR(60) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `nombre_UNIQUE` (`nombre` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `iweb`.`comic`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `iweb`.`comic` ;

CREATE TABLE IF NOT EXISTS `iweb`.`comic` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(60) NOT NULL,
  `isbn` VARCHAR(13) NULL DEFAULT NULL,
  `foto` LONGTEXT NULL DEFAULT NULL,
  `anotacion_privada` VARCHAR(200) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `nombre_UNIQUE` (`nombre` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `iweb`.`comic_has_serie`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `iweb`.`comic_has_serie` ;

CREATE TABLE IF NOT EXISTS `iweb`.`comic_has_serie` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `id_comic` INT(11) NOT NULL,
  `id_serie` INT(11) NOT NULL,
  `anotacion_publica` VARCHAR(200) NULL DEFAULT NULL,
  PRIMARY KEY (`id`,`id_comic`, `id_serie`),
  INDEX `fk_comic_has_serie_serie1_idx` (`id_serie` ASC),
  INDEX `fk_comic_has_serie_comic1_idx` (`id_comic` ASC),
  CONSTRAINT `fk_comic_has_serie_comic1`
    FOREIGN KEY (`id_comic`)
    REFERENCES `iweb`.`comic` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_comic_has_serie_serie1`
    FOREIGN KEY (`id_serie`)
    REFERENCES `iweb`.`serie` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `iweb`.`rol`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `iweb`.`rol` ;

CREATE TABLE IF NOT EXISTS `iweb`.`rol` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `iweb`.`user`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `iweb`.`user` ;

CREATE TABLE IF NOT EXISTS `iweb`.`user` (
  `id` VARCHAR(45) NOT NULL,
  `nombre` VARCHAR(45) NULL DEFAULT NULL,
  `rol_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_user_rol` (`rol_id` ASC),
  CONSTRAINT `fk_user_rol`
    FOREIGN KEY (`rol_id`)
    REFERENCES `iweb`.`rol` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `iweb`.`like`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `iweb`.`like` ;

CREATE TABLE IF NOT EXISTS `iweb`.`like` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` VARCHAR(45) NOT NULL,
  `comic_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`, `comic_id`, `user_id`),
  INDEX `fk_like_user1_idx` (`user_id` ASC),
  INDEX `fk_like_comic1_idx` (`comic_id` ASC),
  CONSTRAINT `fk_like_user1`
    FOREIGN KEY (`user_id`)
    REFERENCES `iweb`.`user` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_like_comic1`
    FOREIGN KEY (`comic_id`)
    REFERENCES `iweb`.`comic` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `iweb`.`comentario`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `iweb`.`comentario` ;

CREATE TABLE IF NOT EXISTS `iweb`.`comentario` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `titulo` VARCHAR(45) NOT NULL,
  `mensaje` VARCHAR(400) NULL,
  `user_id` VARCHAR(45) NOT NULL,
  `comic_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`, `user_id`, `comic_id`),
  INDEX `fk_comentario_user1_idx` (`user_id` ASC),
  INDEX `fk_comentario_comic1_idx` (`comic_id` ASC),
  CONSTRAINT `fk_comentario_user1`
    FOREIGN KEY (`user_id`)
    REFERENCES `iweb`.`user` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_comentario_comic1`
    FOREIGN KEY (`comic_id`)
    REFERENCES `iweb`.`comic` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


INSERT INTO `iweb`.`rol` (`id`, `nombre`) VALUES ('1', 'Admin');
INSERT INTO `iweb`.`rol` (`id`, `nombre`) VALUES ('2', 'Usuario');


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
