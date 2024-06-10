# <center>QUERY PLANNING | DISTRIBUTION | SORT KEYS </center>

- [QUERY EXECTURION PLAN](https://dbeaver.com/docs/dbeaver/Query-Execution-Plan/)
- [QUERY PLANNER ONLINE](https://explain.dalibo.com/)
- [QUERY ANALYZER](https://planetscale.com/blog/what-is-a-query-planner)
- [SARGABLE PREDICATES](https://medium.com/codex/sargable-predicates-and-null-values-in-sql-server-c43ec3d8b108)

---

**PARA OBSERVAR EL TIEMPO DE EJECUCION**
```SQL
SELECT query, starttime, endtime, DATEDIFF(ms, starttime, endtime) AS execution_time
FROM stl_query
ORDER BY starttime DESC;
```

**PARA VER LAS ULTIMAS 10 EJECUCIONES**
```SQL
SELECT query, DATEDIFF(ms, starttime, endtime) AS execution_time, starttime
FROM stl_query
WHERE starttime > GETDATE() - INTERVAL '1 day'
ORDER BY execution_time DESC
LIMIT 10;
```

**PLAN DE EJECUCION**
```SQL
EXPLAIN select * from agents;
```

**ORDEN POR TAMAÑO DE LA TABLA**
```sql
SELECT "table", size
FROM svv_table_info
ORDER BY size DESC;
```

# <center>SORT KEYS</center>


Amazon Redshift is a fully managed, petabyte-scale data warehouse service in the cloud. It allows you to analyze large datasets and offers high performance. One key feature that can significantly impact query performance in Redshift is the use of sort keys. Sort keys determine the order in which data is physically stored on disk, and choosing the right sort key can optimize the performance of queries that filter or join data on specific columns.

### Types of Sort Keys in Amazon Redshift

1. **Compound Sort Keys**:
   - A compound sort key is made up of one or more columns, and the data is sorted in the order specified by the columns.
   - The first column in the sort key has the highest sort priority, followed by the second column, and so on.
   - It is ideal for queries that filter or group by a subset of the leading columns in the sort key.

2. **Interleaved Sort Keys**:
   - An interleaved sort key gives equal weight to each column in the sort key.
   - This allows for more balanced query performance across multiple columns, especially when queries filter on different columns in different combinations.
   - Useful when you have queries that filter on multiple columns and these columns are not always the same.

### Choosing Sort Keys

1. **Compound Sort Keys**:
   - Use a compound sort key when you often filter, group, or join data on a single column or the leading columns.
   - Suitable for time-series data where queries are frequently filtered by a date or timestamp column.
   - Example:
     ```sql
     CREATE TABLE sales (
         sale_id INT,
         sale_date DATE,
         customer_id INT,
         amount DECIMAL(10, 2)
     )
     COMPOUND SORTKEY (sale_date, customer_id);
     ```

2. **Interleaved Sort Keys**:
   - Use an interleaved sort key when queries need to filter on multiple columns and the filtering columns can vary.
   - Provides balanced performance across all the columns in the sort key.
   - Example:
     ```sql
     CREATE TABLE sales (
         sale_id INT,
         sale_date DATE,
         customer_id INT,
         amount DECIMAL(10, 2)
     )
     INTERLEAVED SORTKEY (sale_date, customer_id);
     ```

### Best Practices for Sort Keys

1. **Analyze Query Patterns**:
   - Examine your query patterns to identify which columns are frequently used in WHERE clauses, GROUP BY, and JOIN conditions.
   - Choose sort keys based on the columns that are most frequently used in these operations.

2. **Load and Vacuum Operations**:
   - Regularly vacuum your tables to ensure the sort key columns remain sorted and to reclaim space from deleted rows.
   - Use the `VACUUM` command to resort data and remove deleted rows.

3. **Distribution Keys and Sort Keys**:
   - Coordinate your distribution keys and sort keys for optimal performance.
   - If a column is frequently used in joins, consider making it both a distribution key and a sort key.

4. **Column Encoding**:
   - Use appropriate column encoding to reduce disk I/O and improve query performance.
   - Redshift can automatically apply column encoding based on your data.

### Example Scenarios

- **Scenario 1: Time-Series Data**:
  If you have a table that stores time-series data, like logs or sales records, and your queries mostly filter by date, a compound sort key with the date column as the leading column would be beneficial.
  
  ```sql
  CREATE TABLE events (
      event_id INT,
      event_date DATE,
      event_type VARCHAR(50),
      event_value INT
  )
  COMPOUND SORTKEY (event_date, event_type);
  ```

- **Scenario 2: Multi-Dimensional Data**:
  If your queries filter on multiple dimensions such as customer ID, product ID, and region, and these filters can vary, an interleaved sort key would be more appropriate.

  ```sql
  CREATE TABLE sales (
      sale_id INT,
      sale_date DATE,
      customer_id INT,
      product_id INT,
      region VARCHAR(50),
      amount DECIMAL(10, 2)
  )
  INTERLEAVED SORTKEY (customer_id, product_id, region);
  ```

By carefully choosing the right sort key based on your query patterns and table structure, you can significantly improve the performance of your Amazon Redshift queries.



# <center>DISTRIBUTION STYLE</center>

Amazon Redshift's distribution styles determine how data is distributed across the nodes in a Redshift cluster. Properly choosing the distribution style can optimize query performance by minimizing data movement and maximizing parallel processing. There are four primary distribution styles in Amazon Redshift:

### 1. **KEY Distribution**

**Description**:
- Rows with the same value in the distribution key column(s) are stored on the same node.
- Ideal for optimizing joins between large tables on the distribution key column.

**Usage**:
- Use when joining large tables on a specific column.
- Ensures that rows with the same distribution key value reside on the same node, reducing the need for data redistribution during joins.

**Example**:
```sql
CREATE TABLE orders (
    order_id INT,
    customer_id INT,
    order_date DATE,
    total DECIMAL(10, 2)
)
DISTKEY (customer_id);
```

### 2. **EVEN Distribution**

**Description**:
- Distributes rows evenly across all nodes.
- Provides a uniform distribution of data, avoiding data skew.

**Usage**:
- Use for tables where no clear distribution key can be identified.
- Ideal for tables that are not frequently joined or where queries do not involve large data redistribution.

**Example**:
```sql
CREATE TABLE products (
    product_id INT,
    product_name VARCHAR(100),
    price DECIMAL(10, 2)
)
DISTSTYLE EVEN;
```

### 3. **ALL Distribution**

**Description**:
- Copies the entire table to all nodes.
- Ensures that small lookup tables are available locally on each node, avoiding data movement.

**Usage**:
- Use for small dimension tables that are frequently joined with large fact tables.
- Not suitable for large tables due to storage overhead.

**Example**:
```sql
CREATE TABLE regions (
    region_id INT,
    region_name VARCHAR(50)
)
DISTSTYLE ALL;
```

### 4. **AUTO Distribution**

**Description**:
- Redshift automatically selects the optimal distribution style based on the table’s size and schema.
- Simplifies table creation by letting Redshift choose the best distribution strategy.

**Usage**:
- Use when you prefer to let Redshift manage the distribution style.
- Beneficial for initial table creation, especially if unsure about the best distribution style.

**Example**:
```sql
CREATE TABLE sales (
    sale_id INT,
    sale_date DATE,
    customer_id INT,
    amount DECIMAL(10, 2)
)
DISTSTYLE AUTO;
```

### Best Practices for Choosing Distribution Styles

1. **Analyze Query Patterns**:
   - Evaluate the common queries run against your tables, especially joins and aggregations.
   - Identify columns frequently used in joins and consider using them as distribution keys.

2. **Consider Table Size**:
   - Use `DISTSTYLE ALL` for small lookup tables to avoid data movement.
   - For large tables, consider `DISTKEY` or `DISTSTYLE EVEN` to balance load across nodes.

3. **Minimize Data Skew**:
   - Ensure an even distribution of data across nodes to prevent skew.
   - Avoid using columns with a small number of distinct values as distribution keys.

4. **Regularly Monitor and Adjust**:
   - Monitor query performance and data distribution.
   - Adjust distribution styles as data volume and query patterns change.

### Example Scenarios

- **Scenario 1: Joining Large Tables**:
  If you have a large `orders` table and a large `customers` table, both with `customer_id` as a common join column, use `DISTKEY` on `customer_id`.

  ```sql
  CREATE TABLE orders (
      order_id INT,
      customer_id INT,
      order_date DATE,
      total DECIMAL(10, 2)
  )
  DISTKEY (customer_id);
  
  CREATE TABLE customers (
      customer_id INT,
      customer_name VARCHAR(100),
      customer_email VARCHAR(100)
  )
  DISTKEY (customer_id);
  ```

- **Scenario 2: Small Dimension Tables**:
  If you have a small `regions` table used for lookups, use `DISTSTYLE ALL`.

  ```sql
  CREATE TABLE regions (
      region_id INT,
      region_name VARCHAR(50)
  )
  DISTSTYLE ALL;
  ```

By selecting the appropriate distribution style for each table, you can optimize your Amazon Redshift cluster for performance, reducing data movement and ensuring efficient query execution.