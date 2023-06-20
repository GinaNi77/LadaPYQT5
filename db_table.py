script = """
DROP SCHEMA IF EXISTS `avto` ;

CREATE SCHEMA IF NOT EXISTS `avto` DEFAULT CHARACTER SET utf8 ;
USE `avto` ;

DROP TABLE IF EXISTS `avto`.`Customers` ;

CREATE TABLE IF NOT EXISTS `avto`.`Customers` (
  `customer_id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `address` VARCHAR(45) NULL,
  `phone` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  PRIMARY KEY (`customer_id`));

DROP TABLE IF EXISTS `avto`.`Cars` ;

CREATE TABLE IF NOT EXISTS `avto`.`Cars` (
  `car_id` INT NOT NULL AUTO_INCREMENT,
  `brand` VARCHAR(45) NULL,
  `model` VARCHAR(45) NULL,
  `production_year` INT NULL,
  `engine_power` INT NULL,
  `trunk_volume` INT NULL,
  `price` DECIMAL(10,2) NULL,
  PRIMARY KEY (`car_id`));

DROP TABLE IF EXISTS `avto`.`Orders` ;

CREATE TABLE IF NOT EXISTS `avto`.`Orders` (
  `order_id` INT NOT NULL AUTO_INCREMENT,
  `customer_id` INT NOT NULL,
  `car_id` INT NOT NULL,
  `order_date` DATE NULL,
  `status` VARCHAR(45) NULL,
  `total_cost` DECIMAL(10,2) NULL,
  PRIMARY KEY (`order_id`),
  CONSTRAINT `car_id`
    FOREIGN KEY (`car_id`)
    REFERENCES `avto`.`Cars` (`car_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `customer_id`
    FOREIGN KEY (`customer_id`)
    REFERENCES `avto`.`Customers` (`customer_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


DROP TABLE IF EXISTS `avto`.`Employees` ;

CREATE TABLE IF NOT EXISTS `avto`.`Employees` (
  `employee_id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NULL,
  `position` VARCHAR(45) NULL,
  `salary` VARCHAR(45) NULL,
  `hire_date` DATE NULL,
  PRIMARY KEY (`employee_id`));


DROP TABLE IF EXISTS `avto`.`Service` ;

CREATE TABLE IF NOT EXISTS `avto`.`Service` (
  `service_id` INT NOT NULL AUTO_INCREMENT,
  `car_id` INT NOT NULL,
  `employee_id` INT NOT NULL,
  `service_date` DATE NULL,
  `description` VARCHAR(45) NULL,
  `cost` DECIMAL(10,2) NULL,
  PRIMARY KEY (`service_id`),
  CONSTRAINT `employee_id`
    FOREIGN KEY (`employee_id`)
    REFERENCES `avto`.`Employees` (`employee_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `car_idS`
    FOREIGN KEY (`car_id`)
    REFERENCES `avto`.`Cars` (`car_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
"""