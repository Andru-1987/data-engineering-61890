-- Comando original para crear la tabla
CREATE TABLE customers (
    name                          VARCHAR(255),
    industry                      VARCHAR(255),
    project1_id                   INT(6),
    project1_feedback             TEXT,
    project2_id                   INT(6),
    project2_feedback             TEXT,
    contact_person_id             INT(6),
    contact_person_and_role       VARCHAR(300),
    phone_number                  VARCHAR(12),
    address                       VARCHAR(255),
    city                          VARCHAR(255),
    zip                           VARCHAR(5)
  );
-- SOLUCION 1NF
-- Agregar llave primaria
ALTER TABLE customers
    ADD COLUMN id INT(6) AUTO_INCREMENT PRIMARY KEY FIRST;
-- Separar la columna contact_person_and_role
ALTER TABLE customers
    CHANGE COLUMN contact_person_and_role contact_person VARCHAR(300);

ALTER TABLE customers
    ADD COLUMN contact_person_role VARCHAR(300) AFTER contact_person;
    
-- Mover las columnas project_ids y project_feedbacks a una nueva tabla project_feddbacks
ALTER TABLE customers
DROP COLUMN project1_id,
DROP COLUMN project1_feedback,
DROP COLUMN project2_id,
DROP COLUMN project2_feedback;

CREATE TABLE project_feedbacks (
    id                  INT(6) AUTO_INCREMENT PRIMARY KEY,
    project_id          INT(6),
    customer_id         INT(6),
    project_feedback    TEXT
);


-- Mover esas columnas a una tabla que contenga la información de contacto de las personas
ALTER TABLE customers
DROP COLUMN contact_person,
DROP COLUMN contact_person_role,
DROP COLUMN phone_number;

-- crear la tabla contact_persons con un id respectivo
CREATE TABLE contact_persons (
    id              INT(6) PRIMARY KEY,
    name            VARCHAR(300),
    role            VARCHAR(300),
    phone_number    VARCHAR(15)
);

-- Eliminar la columna ciudad de customers y crear una nueva tabla zips para almacenar esto
ALTER TABLE customers
DROP COLUMN city;

CREATE TABLE zips (
    zip   VARCHAR(5) PRIMARY KEY, 
    city  VARCHAR(255)
);