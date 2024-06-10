\c etl_db ;
DROP SCHEMA IF EXISTS desastres_final;
CREATE SCHEMA desastres_final;
DROP SCHEMA IF EXISTS desastres_bde;
CREATE SCHEMA desastres_bde;

CREATE TABLE
    desastres_final.clima (
        year INT NOT NULL PRIMARY KEY,
        temperatura NUMERIC NOT NULL,
        oxigeno NUMERIC NOT NULL
    );

INSERT INTO
    desastres_final.clima
VALUES
    (2023, 22.5, 230),
    (2024, 22.7, 228.6),
    (2025, 22.9, 227.5),
    (2026, 23.1, 226.7),
    (2027, 23.2, 226.4),
    (2028, 23.4, 226.2),
    (2029, 23.6, 226.1),
    (2030, 23.8, 225.1);

CREATE TABLE
    desastres_final.desastres (
        year INT NOT NULL PRIMARY key,
        tsunamis INT NOT NULL,
        olas_calor INT NOT NULL,
        terremotos INT NOT NULL,
        erupciones INT NOT NULL,
        incendios INT NOT NULL
    );

INSERT INTO
    desastres_final.desastres
VALUES
    (2023, 2, 15, 6, 7, 50),
    (2024, 1, 12, 8, 9, 46),
    (2025, 3, 16, 5, 6, 47),
    (2026, 4, 12, 10, 13, 52),
    (2027, 5, 12, 6, 5, 41),
    (2028, 4, 18, 3, 2, 39),
    (2029, 2, 19, 5, 6, 49),
    (2030, 4, 20, 6, 7, 50);

CREATE TABLE
    desastres_final.muertes (
        year INT NOT NULL PRIMARY key,
        r_menor15 INT NOT NULL,
        r_15_a_30 INT NOT NULL,
        r_30_a_45 INT NOT NULL,
        r_45_a_60 INT NOT NULL,
        r_m_a_60 INT NOT NULL
    );

INSERT INTO
    desastres_final.muertes
VALUES
    (2023, 1000, 1300, 1200, 1150, 1500),
    (2024, 1200, 1250, 1260, 1678, 1940),
    (2025, 987, 1130, 1160, 1245, 1200),
    (2026, 1560, 1578, 1856, 1988, 1245),
    (2027, 1002, 943, 1345, 1232, 986),
    (2028, 957, 987, 1856, 1567, 1756),
    (2029, 1285, 1376, 1465, 1432, 1236),
    (2030, 1145, 1456, 1345, 1654, 1877);

--< schema final>--
CREATE TABLE
    desastres_bde.desastres_final (
        cuatrenio VARCHAR(20) NOT NULL PRIMARY KEY,
        temp_avg NUMERIC NOT NULL,
        oxi_avg NUMERIC NOT NULL,
        t_tsunamis INT NOT NULL,
        t_olascalor INT NOT NULL,
        t_terremotos INT NOT NULL,
        t_erupciones INT NOT NULL,
        t_incendios INT NOT NULL,
        m_jovenes_avg NUMERIC NOT NULL,
        m_adutos_avg NUMERIC NOT NULL,
        m_ancianos_avg NUMERIC NOT NULL
    );