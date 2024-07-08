\c etl_db ;

DROP PROCEDURE IF EXISTS MoveDataToProd ;

CREATE OR REPLACE PROCEDURE MoveDataToProd () LANGUAGE plpgsql
AS $$
BEGIN
  DECLARE 
      error_msg VARCHAR(255);

  BEGIN

    INSERT INTO prod.prediccion_fin_mundo (id_evento, nombre_evento, fecha_evento, descripcion_evento, dias_faltantes, fuente_prediccion)
    SELECT 
      id_evento
    , nombre_evento
    , fecha_evento
    , descripcion_evento
    , (fecha_evento - CURRENT_DATE) AS dias_faltantes
    , 'NERT' AS fuente_prediccion
    FROM stage.eventos_apocalipticos;

    EXCEPTION WHEN UNIQUE_VIOLATION THEN
        error_msg := 'Error: Duplicate event found. Data transfer aborted.';
        RAISE NOTICE '%', error_msg;
        RAISE EXCEPTION '%', error_msg;
        ROLLBACK;
    
    -- For other exceptions, roll back the transaction
    WHEN OTHERS THEN
        error_msg := 'Error during data transfer. Rolling back...';
        RAISE NOTICE '%', error_msg;
        RAISE EXCEPTION '%', error_msg;
        ROLLBACK;
  END;

  -- Delete transferred data from stage table
  DELETE FROM stage.eventos_apocalipticos 
  WHERE id_evento IN (SELECT id_evento FROM prod.prediccion_fin_mundo);

  -- Commit the transaction
  COMMIT;
END;
$$;


CALL MoveDataToProd();