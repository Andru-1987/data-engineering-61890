RESTORE DATABASE [AdventureWorks2022]
FROM DISK = N'/backup/AdventureWorks2022.bak'
WITH 
    MOVE 'AdventureWorks2022' TO '/var/opt/mssql/data/AdventureWorks2022.mdf',
    MOVE 'AdventureWorks2022_Log' TO '/var/opt/mssql/data/AdventureWorks2022_log.ldf',
    NOUNLOAD,
    STATS = 5;
