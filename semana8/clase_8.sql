-- CREANDO UNA TABLA DE PRUEBA TEST

CREATE TABLE andru_ocatorres_coderhouse.tabla_test_driven (
	name VARCHAR(30),
	dob TIMESTAMP SORTKEY,
	zip INTEGER,
	ssn VARCHAR(9)
)diststyle all;


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



