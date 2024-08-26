# AIRFLOW AND DAGS

[PRESENTACION DE CLASE](https://docs.google.com/presentation/d/e/2PACX-1vTBrAcC_7Up5Cqfex1K2mrvn1hBOncDRXUD1NW1k60JWv1xPNAxcn6ImFQeV_JxTA/pub?start=false&loop=false&delayms=3000)


### Airflow

**Apache Airflow** es una plataforma de código abierto para crear, programar y monitorear flujos de trabajo programados, conocida como "workflow automation". Proporciona una forma de definir estos flujos de trabajo como código, utilizando Python. Airflow es ampliamente utilizado en el contexto de **ETL (Extract, Transform, Load)**, procesamiento de datos, y otras tareas automatizadas que requieren una gestión eficiente de dependencias y programación.

**Características principales de Airflow:**

- **Definición como código:** Los flujos de trabajo se definen en Python, lo que permite flexibilidad y reutilización.
- **Planificación y Programación:** Airflow permite programar tareas para que se ejecuten en momentos específicos.
- **Gestión de Dependencias:** Maneja automáticamente las dependencias entre tareas, asegurando que se ejecuten en el orden correcto.
- **Escalabilidad:** Puede escalar para manejar grandes volúmenes de datos y tareas complejas.
- **Monitoreo y Mantenimiento:** Proporciona una interfaz gráfica para monitorear el estado de las tareas y flujos de trabajo, facilitando el mantenimiento y resolución de problemas.

### DAG

**DAG** (Directed Acyclic Graph o Grafo Acíclico Dirigido) es una estructura de datos que representa un conjunto de tareas y sus dependencias en un flujo de trabajo de Airflow. Un DAG es esencialmente un grafo donde los nodos representan las tareas y los bordes (o aristas) representan las dependencias entre esas tareas. El término "acíclico" significa que no hay ciclos en el grafo, lo que asegura que no haya dependencias circulares entre las tareas.

**Componentes de un DAG en Airflow:**

- **Tareas (Tasks):** Las unidades individuales de trabajo que se ejecutan.
- **Dependencias (Dependencies):** Las relaciones entre tareas que determinan el orden de ejecución.
- **Programación (Scheduling):** Las reglas que definen cuándo se deben ejecutar las tareas.
- **Configuración:** Los parámetros y configuraciones que controlan la ejecución del DAG.

**Ejemplo sencillo de un DAG en Airflow:**

```python
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime

# Definir los parámetros del DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
}

# Crear el DAG
dag = DAG(
    'example_dag',
    default_args=default_args,
    schedule_interval='@daily',
)

# Definir las tareas
start = DummyOperator(task_id='start', dag=dag)
end = DummyOperator(task_id='end', dag=dag)

# Establecer las dependencias
start >> end
```

En este ejemplo, se define un DAG simple con dos tareas (`start` y `end`) y una dependencia que indica que la tarea `end` debe ejecutarse después de `start`.


--- 

### Conceptos Relevantes al Crear DAGs en Airflow

1. **Dependencias entre Tareas:**
   - Determinar cómo las tareas dependen unas de otras para asegurar el orden correcto de ejecución.
   - Utilizar operadores como `>>` y `<<` para definir dependencias en Python.

2. **Operadores (Operators):**
   - Los operadores son las unidades de trabajo en Airflow. Existen diferentes tipos como `PythonOperator`, `BashOperator`, `DummyOperator`, `SqlOperator`, etc.

3. **Configuración de Parámetros:**
   - `default_args`: Parámetros comunes para las tareas dentro del DAG, como `start_date`, `retries`, `retry_delay`, etc.

4. **Programación (Scheduling):**
   - Definir cuándo y con qué frecuencia se debe ejecutar el DAG utilizando `schedule_interval` (por ejemplo, `@daily`, `@hourly`, `cron`).

5. **Gestión de Dependencias Cíclicas:**
   - Asegurar que el grafo es acíclico para evitar dependencias circulares.

6. **Hooks:**
   - Interfaces para interactuar con servicios externos, como bases de datos o API.

7. **Macros:**
   - Variables predefinidas que pueden ser utilizadas dentro de las tareas para acceder a información como la fecha de ejecución, el id del DAG, etc.

8. **XComs (Cross-communications):**
   - Mecanismo para pasar información entre tareas.

### Ventajas y Desventajas de Airflow

**Ventajas:**

1. **Escalabilidad:**
   - Airflow puede manejar flujos de trabajo complejos y grandes volúmenes de datos.

2. **Flexibilidad:**
   - Al definir los flujos de trabajo en Python, los usuarios pueden crear tareas personalizadas y manejar lógica compleja.

3. **Extensibilidad:**
   - Fácil de extender con operadores y hooks personalizados.

4. **Visualización:**
   - Interfaz gráfica para monitorear y administrar los DAGs, proporcionando visibilidad y control.

5. **Gestión de Dependencias:**
   - Manejo automático de dependencias y ejecución ordenada de tareas.

**Desventajas:**

1. **Curva de Aprendizaje:**
   - Requiere conocimientos de Python y familiarización con la interfaz y conceptos de Airflow.

2. **Complejidad Operacional:**
   - La configuración y el mantenimiento pueden ser complejos, especialmente en entornos de producción grandes.

3. **Latencia:**
   - Puede haber una latencia en la programación y ejecución de tareas debido a la sobrecarga del sistema.

4. **Requiere Infraestructura:**
   - Necesita una infraestructura adecuada para ejecutarse de manera eficiente, lo que puede ser costoso.

### Conceptos de Catchup y Backfilling

**Catchup:**
   - Es una característica que permite que Airflow ejecute todas las instancias pasadas de un DAG que no se hayan ejecutado. Por defecto, `catchup` está habilitado, lo que significa que si un DAG está programado para ejecutarse diariamente y se activa después de varios días, intentará ejecutar todas las ejecuciones diarias pendientes.

   ```python
   dag = DAG(
       'example_dag',
       default_args=default_args,
       schedule_interval='@daily',
       catchup=False  # Desactivar catchup
   )
   ```

**Backfilling:**
   - Similar a `catchup`, el backfilling implica la ejecución de todas las instancias pasadas del DAG para "ponerse al día" con el horario programado. Es útil cuando se necesitan procesar datos históricos.

### Ventajas de las Variables de Contexto dentro de DAGs

1. **Flexibilidad:**
   - Permiten el uso de valores dinámicos y configuración específica para cada ejecución de tareas.

2. **Reusabilidad:**
   - Facilitan la reutilización de tareas y la adaptación de su comportamiento según el contexto.

3. **Control:**
   - Proporcionan mayor control sobre la lógica de ejecución y permiten personalizar las tareas sin modificar el código.

4. **Información de Ejecución:**
   - Proveen acceso a información relevante como fechas, id del DAG, y otros detalles de ejecución.

**Ejemplo de uso de variables de contexto:**

```python
from airflow.operators.python_operator import PythonOperator

def print_context(ds, **kwargs):
    print(f"Execution date is {ds}")
    return 'Context printed'

print_context_task = PythonOperator(
    task_id='print_context',
    provide_context=True,
    python_callable=print_context,
    dag=dag,
)
```

En este ejemplo, `ds` (execution date) es una variable de contexto que se pasa a la función `print_context`.

[DAGSTER VS AIRFLOW](https://dagster.io/blog/dagster-airflow)

[DECLARAR DAGS](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html)