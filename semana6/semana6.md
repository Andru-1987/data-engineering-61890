# Semana 6 ->  Pandas y DataFrames

**Verificacion de error de clase de la semana 5**
> [Ir a link](semana5/__main__.py)
---

- [PANDAS](https://pandas.pydata.org/)
- [DATAFRAMES](https://www.databricks.com/glossary/what-are-dataframes)

---

[Temario Semana 6](https://docs.google.com/presentation/d/e/2PACX-1vR3JUyNb2hruK57Ux-daRk141sibYvLSbr9ilwfrwKfsAgFA6Jh55VZz8RompzqhA/pub?start=false&loop=false&delayms=3000)

[SAMPLE DE PRIMERA ENTREGA ](./semana6/sample_entregable)

Perfecto, a continuación se incluye la información proporcionada dentro de la documentación del proyecto ETL, específicamente para el desafío de crear una tabla en Redshift e ingerir datos desde la API de GitHub utilizando Python.

---

# Documentación del Proyecto ETL

## Introducción
El presente documento describe el proyecto de ETL (Extract, Transform, Load) diseñado para la ingestión de datos desde la API de GitHub hacia una tabla en Amazon Redshift. El objetivo del proyecto es crear una pipeline de datos automatizada que permita extraer datos de la API de GitHub, transformarlos y cargarlos en una base de datos Redshift para su análisis posterior.

## Tabla de Contenidos
1. [Introducción](#introducción)
2. [Arquitectura del Sistema](#arquitectura-del-sistema)
3. [Componentes del Proceso ETL](#componentes-del-proceso-etl)
    - [Extracción](#extracción)
    - [Transformación](#transformación)
    - [Carga](#carga)
4. [Tecnologías Utilizadas](#tecnologías-utilizadas)
5. [Planificación del Proyecto](#planificación-del-proyecto)
6. [Consideraciones de Seguridad](#consideraciones-de-seguridad)
7. [Pruebas y Validación](#pruebas-y-validación)
8. [Conclusión](#conclusión)
9. [Anexos](#anexos)

## Arquitectura del Sistema
La arquitectura del sistema ETL para este proyecto incluye los siguientes componentes:
- **Fuente de Datos**: API de GitHub.
- **Servidor ETL**: Máquina local o servidor en la nube configurado con un entorno Python virtual (venv).
- **Destino de Datos**: Tabla en Amazon Redshift.

## Componentes del Proceso ETL

### Extracción
En esta fase, los datos se extraen de la API de GitHub.

#### Procedimiento de Extracción
- **Fuente de Datos**: API de GitHub.
- **Método de Extracción**: Llamadas a la API utilizando requests en Python.
- **Frecuencia de Extracción**: Diaria.

### Transformación
La transformación implica convertir los datos extraídos en un formato adecuado (dataframe) y realizar cualquier limpieza o estructuración necesaria.

#### Procedimiento de Transformación
- **Operaciones de Limpieza**: Filtrado de datos irrelevantes.
- **Operaciones de Normalización**: Estructuración de los datos en un dataframe de pandas.
- **Transformaciones Adicionales**: Conversión de tipos de datos y manejo de valores nulos.

### Carga
En esta fase, los datos transformados se cargan en una tabla de Amazon Redshift.

#### Procedimiento de Carga
- **Destino de Datos**: Tabla en Amazon Redshift.
- **Método de Carga**: Utilización de la biblioteca psycopg2 en Python para insertar datos.
- **Frecuencia de Carga**: Diaria.

## Tecnologías Utilizadas
- **Lenguajes de Programación**: Python.
- **Bibliotecas de Python**: requests, pandas, psycopg2.
- **Entorno Virtual**: venv.
- **Bases de Datos**: Amazon Redshift.

## Planificación del Proyecto
La planificación del proyecto ETL sigue las siguientes fases:
1. **Recolección de Requisitos**: [Fecha de Inicio - Fecha de Fin]
2. **Diseño del Sistema**: [Fecha de Inicio - Fecha de Fin]
3. **Implementación**: [Fecha de Inicio - Fecha de Fin]
4. **Despliegue**: [Fecha de Inicio - Fecha de Fin]
5. **Mantenimiento**: Actualizaciones y monitoreo continuo.

## Consideraciones de Seguridad
- **Acceso a Datos**: Uso de credenciales almacenadas en el archivo .env.
- **Encriptación**: Datos sensibles en tránsito a través de HTTPS: _No implementado_
- **Monitoreo y Auditoría**: Logs de ejecución del script ETL.

## Pruebas y Validación:
_Opcional a implementar_
- **Pruebas Unitarias**: Pruebas para cada función individual en los módulos DataConn y DataRetriever.
- **Pruebas de Integración**: Validación del flujo completo desde la extracción hasta la carga.
- **Validación de Datos**: Comparación de los datos cargados en Redshift con los datos originales de la API de GitHub.

## Implementación del Proyecto

### Creación de la Tabla en Redshift
[sql_query_creation.sql](./sample_entregable/sql_query_creation.sql)


### Configuración del Entorno Virtual (VENV) en Python
1. Crear y activar el entorno virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```
2. Instalar las dependencias necesarias:
    ```bash
    pip install -r requirements.txt
    ```

### Configuración del Archivo .env
Crear un archivo `.env` en el directorio del proyecto con el siguiente contenido:
```
REDSHIFT_HOST=<tu_host_de_redshift>
REDSHIFT_PORT=<puerto_de_redshift>
REDSHIFT_DBNAME=<nombre_de_la_base_de_datos>
REDSHIFT_USER=<tu_usuario>
REDSHIFT_PASSWORD=<tu_contraseña>
```

### Estructura del Proyecto y Clases Principales

#### Archivo `__main__.py`
[archivo main](./sample_entregable/__main__.py)

## Conclusión
El proyecto ETL para la ingestión de datos desde la API de GitHub hacia Amazon Redshift ha sido diseñado para automatizar la extracción, transformación y carga de datos, permitiendo así un análisis eficiente y preciso de los datos de GitHub.

## Anexos
- **Glosario de Términos**: [Definiciones de Términos Técnicos Utilizados]
- **Referencias**: [Enlaces a Documentación Relevante, Artículos, etc.]
- **Diagramas y Esquemas**: [Diagrama de Flujo del Proceso ETL, Diagrama de Arquitectura, etc.]
