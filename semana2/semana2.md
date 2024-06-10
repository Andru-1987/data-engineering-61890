# <center>Introducción al Data Engineering<center>
[_Presentacion clase 2_](https://docs.google.com/presentation/d/e/2PACX-1vQ5KtWhf9MPj-0eGOHh3n8KEzG97lvhqPUHAX9QYrFiJeBjZu7v7_Ta9Bc1NMNXXg/pub?start=false&loop=false&delayms=3000)


### ¿Qué es Big Data?

Big Data se refiere al análisis y procesamiento de grandes conjuntos de datos que son demasiado complejos para ser tratados con métodos tradicionales de procesamiento de datos. Estos conjuntos de datos suelen caracterizarse por tener un alto volumen, velocidad y variedad.

### Las 3 V de Big Data:

- **Volumen:** Se refiere a la cantidad masiva de datos generados y almacenados.
- **Velocidad:** Hace referencia a la rapidez con la que se generan y se deben procesar los datos.
- **Variedad:** Se refiere a los diferentes tipos de datos que se generan y se deben manejar.

### Las 5 V de Big Data:

Además de las 3 V mencionadas anteriormente, se suelen agregar:

- **Veracidad:** Se refiere a la confiabilidad y precisión de los datos.
- **Valor:** Hace referencia a la capacidad de extraer información valiosa y relevante de los datos.

### ¿Qué es un Ingeniero de Datos?

Un Ingeniero de Datos es un profesional encargado de diseñar, construir y mantener sistemas y arquitecturas de datos. Su trabajo incluye la creación de pipelines de datos, el diseño de bases de datos, la optimización de consultas y la gestión de la infraestructura necesaria para el procesamiento y análisis de grandes volúmenes de datos.

### Diferencias entre sistemas OLTP y OLAP:

- **OLTP (Online Transaction Processing):**
  - Orientado a transacciones.
  - Diseñado para manejar transacciones de negocio en tiempo real.
  - Esquemas normalizados.
  - Ejemplo: Sistema de ventas en línea, sistemas de reserva de vuelos.

- **OLAP (Online Analytical Processing):**
  - Orientado a análisis.
  - Diseñado para análisis y consulta de grandes volúmenes de datos.
  - Esquemas desnormalizados o estrella.
  - Ejemplo: Sistemas de inteligencia empresarial, data warehouses.

---

<details>
<summary>agents table</summary>
<b>Tabla agents</b>
<li> Esta tabla parece contener información sobre los agentes y sus nombres.</li>
<li> Se trata de una tabla que contiene información sobre los agentes de la compañía, lo que sugiere que se usa para transacciones de negocio y no para análisis o reportes.</li>
<li>Por lo tanto, esta tabla pertenece a un sistema OLTP.</li>

</details> 

| agentid |      name       |
|---------|-----------------|
|    0    | Michele Williams|
|    1    | Jocelyn Parker  |

---
<details>
<summary>calls table</summary>
<b>Tabla calls </b>
<li>Esta tabla parece contener información sobre las llamadas, incluyendo la duración y si se vendió algún producto.</li>
<li>Es probable que esta tabla se utilice para el seguimiento de las transacciones de las llamadas, lo que sugiere que se usa para transacciones en tiempo real.</li>
<li>Por lo tanto, esta tabla también pertenece a un sistema OLTP.</li>
</details> 

| callid | agentid | customerid | pickedup | duration | productsold |
|--------|---------|------------|----------|----------|-------------|
|   0    |   10    |    179     |    0     |    0     |      0      |
|   1    |    5    |    691     |    1     |   116    |      0      |

---

<details>
<summary>customer table</summary>
 <b>Tabla customer:</b>
    <li> Esta tabla parece contener información sobre los clientes, incluyendo su nombre, ocupación, edad, etc.</li>
    <li> Esta información podría utilizarse para análisis y generación de reportes sobre los clientes y sus características.</li>
    <li> Por lo tanto, esta tabla pertenece a un sistema OLAP.</li>
</details> 

| customerid |       name        | occupation  |              email              |            company            | phonenumber | age |
|------------|-------------------|-------------|--------------------------------|-------------------------------|-------------|-----|
|     0      |   David Melton    | Unemployed  |        DMelton@zoho.com        | Morris, Winters and Ramirez  | 409-093-0748|  16 |
|     1      | Michael Gonzalez  |   Student   |  Gonzalez_Michael@yahoo.com   |       Hernandez and Sons     | 231-845-0673|  19 |

---

## <center> Arquitectura de una base de datos</center>

La arquitectura de una base de datos se refiere a la estructura fundamental y el diseño de cómo se organiza, almacena, gestiona y accede a los datos dentro de un sistema de gestión de bases de datos (DBMS). Aunque existen diferentes tipos de arquitecturas de bases de datos, una arquitectura típica de base de datos relacional se puede dividir en tres niveles principales:

1. **Nivel Externo o de Usuario (Vistas de Usuario)**:
   - Este nivel es el más alto y está más cerca del usuario final.
   - Proporciona una interfaz para que los usuarios interactúen con la base de datos.
   - Los usuarios no tienen que preocuparse por la estructura interna de la base de datos.
   - Pueden acceder a los datos utilizando consultas y comandos en lenguajes como SQL.

2. **Nivel Conceptual o Lógico (Esquema de Base de Datos)**:
   - Este nivel describe la estructura de toda la base de datos.
   - Define la organización de los datos y las relaciones entre las distintas entidades.
   - Incluye el esquema de la base de datos, que define las tablas, los campos, las claves primarias y externas, etc.
   - Oculta los detalles de almacenamiento físico de los datos.

3. **Nivel Interno o de Almacenamiento (Almacenamiento Físico)**:
   - Este nivel está más cerca del hardware y se encarga de cómo se almacenan físicamente los datos en el disco.
   - Incluye detalles de cómo se organizan los datos en bloques de disco, índices, etc.
   - Los DBMS se encargan de traducir las consultas del nivel lógico al nivel físico.

Además de estos tres niveles, la arquitectura de una base de datos también puede incluir componentes como:

- **DBMS (Sistema de Gestión de Bases de Datos)**:
  - El software que administra y facilita el acceso a la base de datos.
  - Se encarga de la creación, modificación y eliminación de datos, así como de las consultas y transacciones.
  - Ejemplos: MySQL, PostgreSQL, SQL Server, Oracle, etc.

- **Controladores (Drivers)**:
  - Permiten la conexión entre la base de datos y las aplicaciones.
  - Proporcionan una interfaz para que los programas puedan interactuar con la base de datos a través de consultas y actualizaciones.

- **Red de Comunicación**:
  - La infraestructura que permite la comunicación entre los usuarios, las aplicaciones y los servidores de bases de datos.

Cada uno de estos componentes trabaja en conjunto para garantizar que los datos estén disponibles, sean seguros y se puedan acceder de manera eficiente. La arquitectura de una base de datos puede variar dependiendo del tipo de DBMS, los requisitos de la aplicación y las necesidades de los usuarios.

---

Documentacion adicional creada por : **@Andru-1987**