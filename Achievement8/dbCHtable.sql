CREATE DATABASE databaseCH

CREATE TABLE databaseCH.table (TickTime DOUBLE, Speed DOUBLE, Day INT) 
ENGINE=Memory

SELECT TickTime, Day, Speed FROM db.table
WHERE (Day=1 and Speed > 6454579) or (Day=2 and Speed > 7459340) or (Day=7 and Speed >= 1321078)
ORDER BY Day Desc

#1    6.454579e+06
#2    7.459340e+06
#7    1.321078e+07
