\c nivelacion_database;

SELECT * 
FROM agents
WHERE name ~ '^M|O';



SELECT *
FROM customers 
WHERE occupation LIKE '%Engineer%'
ORDER BY occupation;


SELECT CustomerID, Name,
    CASE
        WHEN Age >= 30 THEN 'Yes'
        WHEN Age <  30 THEN 'No'
        ELSE 'Missing Data'
    END AS Over30
FROM customers
ORDER BY Name DESC;


SELECT CallID, Cu.CustomerID, Name, ProductSold,
    CASE
        WHEN Age >= 30 THEN 'Yes'
        WHEN Age <  30 THEN 'No'
        ELSE 'Missing Data'
    END AS Over30
FROM customers Cu
JOIN calls Ca ON Ca.CustomerID = Cu.CustomerID
WHERE Occupation LIKE '%Engineer%'
ORDER BY Name DESC ;


SELECT SUM(ProductSold) AS TotalSales, COUNT(*) AS NCalls
FROM customers Cu
JOIN calls Ca ON Ca.CustomerID = Cu.CustomerID
WHERE Occupation LIKE '%Engineer%';


SELECT Name AS AgentName, COUNT(*) AS NCalls, MIN(Duration) AS Shortest, MAX(Duration) AS Longest, ROUND(AVG(Duration),2) AS AvgDuration, SUM(ProductSold) AS TotalSales
FROM calls C
    JOIN agents A ON C.AgentID = A.AgentID
WHERE PickeDup = 1
GROUP BY Name
ORDER BY Name;

SELECT a.name,
SUM(
   CASE
       WHEN productsold = 0 THEN duration
       ELSE 0
   END)/SUM(
   CASE
       WHEN productsold = 0 THEN 1
       ELSE 0
   END)
AS avgWhenNotSold ,
SUM(
   CASE
       WHEN productsold = 1 THEN duration
       ELSE 0
   END)/SUM(
       CASE WHEN productsold = 1 THEN 1
       ELSE 0
   END
AS avgWhenSold
FROM calls c
JOIN agents a ON c.agentid = a.agentid
GROUP BY a.name
ORDER BY 1;