-- CREANDO UNA TABLA DE PRUEBA TEST

CREATE TABLE andru_ocatorres_coderhouse.tabla_test_driven (
	name VARCHAR(30),
	dob TIMESTAMP SORTKEY,
	zip INTEGER,
	ssn VARCHAR(9)
)diststyle all;

INSERT INTO
  andru_ocatorres_coderhouse.tabla_test_driven (name, dob, zip, ssn)
VALUES
  ('John Doe', '1980-01-01', 12345, '123456789'),
  ('Jane Smith', '1990-02-02', 23456, '234567890'),
  ('Alice Johnson', '1985-03-03', 34567, '345678901'),
  ('Bob Brown', '1975-04-04', 45678, '456789012'),
  ('Charlie Davis', '2000-05-05', 56789, '567890123'),
  ('Diana Evans', '1995-06-06', 67890, '678901234'),
  ('Frank Green', '1988-07-07', 78901, '789012345'),
  ('Grace Harris', '1978-08-08', 89012, '890123456'),
  ('Hank Irving', '1968-09-09', 90123, '901234567'),
  ('Ivy Johnson', '2002-10-10', 12345, '012345678');


-- GENERACION DE UN USUARIO CON SU RESPECTIVO PASSWORD CREATE USER

CREATE USER ander_de PASSWORD 'Pass1234';

-- LISTAR USUARIOS CREADOS
SELECT
    u.usename,
    s.schemaname,
    has_schema_privilege(u.usename,s.schemaname,'create') AS user_has_select_permission,
    has_schema_privilege(u.usename,s.schemaname,'usage') AS user_has_usage_permission
FROM
    pg_user u
CROSS JOIN
    (SELECT DISTINCT schemaname FROM pg_tables) s
WHERE
    
    s.schemaname = 'andru_ocatorres_coderhouse'
    AND u.usename LIKE '%_de';
   
   
 -- GENERACION DE GRUPOS CREAR GRUPO 
   
CREATE GROUP los_power_trio WITH USER andru_data_scientist;

-- VERIFICACION DE LA CREACION DE LOS GRUPOS EXISTENTES 
select *
from pg_user , pg_group
where pg_user.usesysid = ANY(pg_group.grolist) and 
      pg_group.groname='los_power_trio';
     

-- AGREGADO DE USUARIOS AL GRUPO
ALTER GROUP 
	los_power_trio 
DROP USER andru_data_scientist ; 

ALTER GROUP 
	los_power_trio 
ADD USER ander_de ;



-- SOBRE COLUMNAS
GRANT SELECT(name, dob, zip) 
	ON andru_ocatorres_coderhouse.tabla_test_driven 
	TO GROUP los_power_trio;

   
-- GARANTIZAMOS LOS PERMISOS AL GRUPO
GRANT ALL ON SCHEMA andru_ocatorres_coderhouse 
	TO GROUP los_power_trio;



