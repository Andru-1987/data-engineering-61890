## CREACION ETL

Imagina que en tu empresa diversos científicos han generado pronósticos sobre eventos catastróficos que ocurrirán en el planeta Tierra en lo que resta del siglo XXI. Para esto debes generar una tabla llamada prediccion_fin_mundo que contenga el id_evento, nombre_evento, fecha_evento, descripcion_evento, dias_faltantes y fuente_prediccion  a partir de la tabla eventos_apocalipticos.

Para esto deberás crear un proceso de ETL que reciba la información de artículos y autores cumpliendo las siguientes características:

- Crear la tabla llamada “eventos_apocalipticos”
- Insertar en la tabla del paso 1 los registros
- Crear la tabla “prediccion_fin_mundo”
- Generar una query que a partir de la tabla de origen permita rellenar la tabla destino
- Además deberás responder está pregunta: ¿Cuál es el número promedio de días restantes hasta los eventos apocalípticos en cada década, y cuántos eventos comienzan con la letra 'D' y la letra 'A' en cada década?.


-- Update today