## Semana 7
### MicroDesafio
_[Presentacion](https://docs.google.com/presentation/d/e/2PACX-1vQ8QsB2QqcNWIBV6dOsB2Ay7xKgChfApjVwA1XXkf6R99RJ6aanyXs-rUQ5ulw6Eg/pub?start=false&loop=false&delayms=3000)_

Recientemente, científicos de toda Latinoamérica han decidido unir esfuerzos creando la cumbre por el cambio climático y preservación de la especie humana. Reuniendo a todos los países latinoamericanos (por mencionar algunos: México, Argentina, Brasil, Chile, Colombia, Paraguay, Venezuela, Uruguay, Bolivia, Ecuador y Perú) y contando con la colaboración de USA.
Afianzando con esto el esfuerzo conjunto de todas las naciones para ponerle freno a nuestra posible extinción.


### Consigna

Durante los foros efectuados, surgió como necesidad el analizar el impacto que han tenido los siguientes fenómenos durante los últimos 5 años dentro de los países participantes en esta cumbre (Argentina, Brasil, Chile, Colombia, México, Perú, Venezuela, Uruguay, Paraguay, Bolivia y Ecuador): ["Sea Level", Wheater",'Temperatures','Carbon Dioxide','Global Warming']: 

* Acceder a la herramienta Pytrends y buscar las tendencias de las palabras mencionadas para cada país (Seleccionar por lo menos 5 países de los mencionado)

* Se sugiere utilizar el método interest_over_time

* Generar un dataframe para cada país donde se alojen los resultados para luego enviar los resultados a Redshift
* Crear una base de datos llamada FIN_DEL_MUNDO en Redshift
Conectarte por medio de SQLAlchemy o Psycopg2 a la base de datos
* Crear una tabla en Redshiftpara cada país con el nombre asociado al código de dos dígitos (https://www.iban.com/country-codes)  alimentando los resultados obtenidos de Pytrends 


## psycopg2 vs SQLAlchemy

| Feature         | psycopg2                                    | SQLAlchemy                                          |
|-----------------|---------------------------------------------|-----------------------------------------------------|
| Type            | Database adapter                            | ORM library and SQL toolkit                        |
| Purpose         | Interact with PostgreSQL databases         | Interact with multiple database engines             |
| Functionality   | Low-level interface for executing SQL commands, managing connections, handling transactions | ORM for mapping Python objects to database tables, SQL toolkit for query building |
| Level of Abstraction | Low-level, requires writing SQL queries directly | High-level, provides abstraction over SQL queries, supports ORM |
| Performance     | Known for efficiency and performance      | Offers flexibility and abstraction, may have slightly more overhead |
| Suitability     | Developers comfortable with SQL, need direct control over PostgreSQL interactions | Developers preferring higher-level abstraction, multiple database support |
| Learning Curve  | Easier for SQL-savvy developers            | Steeper due to ORM and higher-level abstraction    |

