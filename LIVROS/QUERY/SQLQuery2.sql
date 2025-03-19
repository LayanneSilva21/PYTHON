SELECT A.ContactName,A.Region,B.ContactName,B.Region
FROM Customers A, Customers B
WHERE A.Region = B.Region

SELECT *
FROM Employees

SELECT A.FirstName,A.LastName,A.HireDate,B.FirstName,B.LastName,B.HireDate
FROM Employees A, Employees B
WHERE DATEPART(YEAR,A.HireDate) = DATEPART(YEAR,B.HireDate)

SELECT *
FROM [Order Details]

SELECT A.ProductID,A.UnitPrice,A.Discount,B.ProductID,B.UnitPrice,B.Discount
FROM [Order Details] A, [Order Details] B
WHERE A.Discount = b.Discount

