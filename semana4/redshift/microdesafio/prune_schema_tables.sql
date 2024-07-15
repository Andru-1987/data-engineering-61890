CREATE OR REPLACE PROCEDURE pruner(schema_name VARCHAR(200))
LANGUAGE plpgsql
AS $$
DECLARE
    r RECORD;
BEGIN
    SELECT tablename FROM pg_tables WHERE schemaname = CONCAT('"',schema_name,'"');

    FOR r IN (SELECT tablename FROM pg_tables WHERE schemaname = schema_name) LOOP
        EXECUTE 'DROP TABLE IF EXISTS ' || quote_ident(r.tablename) || ' CASCADE';
    END LOOP;
END;
$$;