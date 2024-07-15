DROP SCHEMA IF EXISTS norm;
CREATE SCHEMA norm;

-- Comando original para crear la tabla
CREATE TABLE norm.customers (
    name                          VARCHAR(255),
    industry                      VARCHAR(255),
    project1_id                   INT,
    project1_feedback             TEXT,
    project2_id                   INT,
    project2_feedback             TEXT,
    contact_person_id             INT,
    contact_person_and_role       VARCHAR(300),
    phone_number                  VARCHAR(12),
    address                       VARCHAR(255),
    city                          VARCHAR(255),
    zip                           VARCHAR(5)
  );


-- SOLUCION 1NF
-- Agregar llave primaria
ALTER TABLE norm.customers
    ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY FIRST;

-- Separar la columna contact_person_and_role
ALTER TABLE norm.customers
    CHANGE COLUMN contact_person_and_role contact_person VARCHAR(300);

ALTER TABLE norm.customers
    ADD COLUMN contact_person_role VARCHAR(300) AFTER contact_person;

-- Mover las columnas project_ids y norm.project_feedbacks a una nueva tabla project_feddbacks
ALTER TABLE norm.customers
    DROP COLUMN project1_id,
    DROP COLUMN project1_feedback,
    DROP COLUMN project2_id,
    DROP COLUMN project2_feedback;



CREATE TABLE norm.project_feedbacks (
    id                  INT AUTO_INCREMENT PRIMARY KEY,
    project_id          INT,
    customer_id         INT,
    project_feedback    TEXT
);


-- Mover esas columnas a una tabla que contenga la información de contacto de las personas
ALTER TABLE norm.customers
    DROP COLUMN contact_person,
    DROP COLUMN contact_person_role,
    DROP COLUMN phone_number;

-- crear la tabla norm.contact_persons con un id respectivo
CREATE TABLE norm.contact_persons (
    id              INT PRIMARY KEY,
    name            VARCHAR(300),
    role            VARCHAR(300),
    phone_number    VARCHAR(15)
);

-- Eliminar la columna ciudad de norm.customers y crear una nueva tabla zips para almacenar esto
ALTER TABLE norm.customers
    DROP COLUMN city;

CREATE TABLE norm.zips (
    zip   VARCHAR(5) PRIMARY KEY, 
    city  VARCHAR(255)
);