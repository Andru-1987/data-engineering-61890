DROP DATABASE IF EXISTS nivelacion_database;
CREATE DATABASE nivelacion_database;
\c nivelacion_database ; 


CREATE TABLE agents (
    agentid     SERIAL PRIMARY KEY
,   name        VARCHAR(100)
) ;

CREATE TABLE customers (
    customerid  SERIAL PRIMARY KEY
,   name        VARCHAR(100)
,   occupation  VARCHAR(200)
,   email       VARCHAR(200)
,   company     VARCHAR(200)
,   phonenumber VARCHAR(200)
,   age         INT
) ;


CREATE TABLE calls (
    callid      SERIAL PRIMARY KEY
,   agentid     INT
,   customerid  INT
,   pickedup    INT
,   duration    INT
,   productsold INT
) ;


COPY agents 
FROM '/sql_nivelacion/data/agents.csv' 
DELIMITER ',' 
CSV HEADER;


COPY customers(customerid, name, occupation, email, company, phonenumber, age) 
FROM '/sql_nivelacion/data/customers.csv' 
DELIMITER ',' 
CSV HEADER;


COPY calls(callid, agentid, customerid, pickedup, duration, productsold) 
FROM '/sql_nivelacion/data/calls.csv' 
DELIMITER ',' 
CSV HEADER;





