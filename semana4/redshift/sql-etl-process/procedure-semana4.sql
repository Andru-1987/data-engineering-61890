\c etl_db ;

DROP PROCEDURE IF EXISTS pETL_desastres ;

CREATE OR REPLACE PROCEDURE pETL_desastres() LANGUAGE plpgsql
AS $$
BEGIN
 
    
    WITH joined_data As (
        SELECT
                c.year
            ,   c.temperatura
            ,   c.oxigeno
            ,   d.tsunamis
            ,   d.olas_calor
            ,   d.terremotos
            ,   d.erupciones
            ,   d.incendios  
            ,   m.r_menor15
            ,   m.r_15_a_30
            ,   m.r_30_a_45
            ,   m.r_45_a_60
            ,   m.r_m_a_60

            FROM desastres_final.clima AS c
            JOIN desastres_final.desastres AS d
            USING(year)
            JOIN desastres_final.muertes  AS m
            USING(year)
    ), group_data AS(
        SELECT
            CASE
                WHEN jd.year <= 2026 THEN '2023-2026'
                ELSE '2027-2030' 
            END
            AS cuatrenio
        ,   ROUND(AVG(jd.temperatura),2) AS avg_temperatura
        ,   ROUND(AVG(jd.oxigeno),2) AS avg_oxigeno
        ,   SUM(jd.tsunamis) AS t_tsunamis
        ,   SUM(jd.olas_calor) AS t_olas_calor
        ,   SUM(jd.terremotos) AS t_terremotos
        ,   SUM(jd.erupciones) AS t_erupciones
        ,   SUM(jd.incendios  ) AS t_incendios
        ,   ROUND(AVG(jd.r_menor15 + jd.r_15_a_30), 2) AS avg_muerte_menores
        ,   ROUND(AVG(jd.r_30_a_45 + jd.r_45_a_60), 2) AS avg_muerte_adultos
        ,   ROUND(AVG(jd.r_m_a_60), 2) AS avg_muerte_ancianos
        FROM joined_data AS jd
        GROUP BY cuatrenio
    )
    INSERT INTO desastres_bde.desastres_final (
                cuatrenio
            ,   temp_avg
            ,   oxi_avg
            ,   t_tsunamis
            ,   t_olascalor
            ,   t_terremotos
            ,   t_erupciones
            ,   t_incendios
            ,   m_jovenes_avg
            ,   m_adutos_avg
            ,   m_ancianos_avg
        )
    SELECT 
            cuatrenio
        ,   avg_temperatura
        ,   avg_oxigeno
        ,   t_tsunamis
        ,   t_olas_calor
        ,   t_terremotos
        ,   t_erupciones
        ,   t_incendios
        ,   avg_muerte_menores
        ,   avg_muerte_adultos
        ,   avg_muerte_ancianos
    FROM group_data
        ON CONFLICT (cuatrenio) 
        DO UPDATE SET
            temp_avg = EXCLUDED.temp_avg
        ,   oxi_avg = EXCLUDED.oxi_avg
        ,   t_tsunamis = EXCLUDED.t_tsunamis
        ,   t_olascalor = EXCLUDED.t_olascalor
        ,   t_terremotos = EXCLUDED.t_terremotos
        ,   t_erupciones = EXCLUDED.t_erupciones
        ,   t_incendios = EXCLUDED.t_incendios
        ,   m_jovenes_avg = EXCLUDED.m_jovenes_avg
        ,   m_adutos_avg = EXCLUDED.m_adutos_avg
        ,   m_ancianos_avg = EXCLUDED.m_ancianos_avg
    ;
END;
$$;


CALL pETL_desastres();


SELECT * FROM desastres_bde.desastres_final;