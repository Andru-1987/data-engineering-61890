\c etl_db;

SELECT
    (EXTRACT(YEAR FROM fecha_evento) - EXTRACT(YEAR FROM fecha_evento) % 10)::TEXT || '-' || (EXTRACT(YEAR FROM fecha_evento) - EXTRACT(YEAR FROM fecha_evento) % 10 + 9)::TEXT AS decade,
    COUNT(*) AS number_of_events,
    AVG((fecha_evento - CURRENT_DATE)::INTEGER) AS average_days,
    SUM(CASE WHEN nombre_evento LIKE 'D%' THEN 1 ELSE 0 END) AS D_events,
    SUM(CASE WHEN nombre_evento LIKE 'A%' THEN 1 ELSE 0 END) AS A_events
FROM eventos_apocalipticos
GROUP BY decade
ORDER BY decade ASC;
