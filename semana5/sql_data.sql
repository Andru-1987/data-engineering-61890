SHOW TABLES
FROM
SCHEMA "data-engineer-database"."andru_ocatorres_coderhouse";

DROP TABLE IF EXISTS andru_ocatorres_coderhouse.stage_yfinance_google;

CREATE TABLE stage_yfinance_google(
	specific_area	VARCHAR(200)
,   stock_actions   VARCHAR(50)
,   revenue         VARCHAR(50)
,   value           VARCHAR(50)
,   avg_data        VARCHAR(50)
,   date_to_stage      DATE
);


SELECT  
*
FROM andru_ocatorres_coderhouse.stage_yfinance_google ;
