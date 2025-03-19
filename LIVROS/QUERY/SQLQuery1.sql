SELECT *
FROM production.Product
WHERE Weight > 500 and Weight <= 700

SELECT*
FROM HumanResources.Employee
WHERE MaritalStatus= 'M' and SalariedFlag = '1'

SELECT *
FROM person.person
WHERE FirstName = 'Peter' and LastName ='Krebs'

SELECT *
FROM Person.EmailAddress
WHERE BusinessEntityID = '26'

SELECT count(DISTINCT title)
FROM Person.Person

SELECT count(*)
FROM Production.Product

SELECT count(DISTINCT Name)
FROM Production.Product

SELECT count(Size)
FROM Production.Product

SELECT TOP 10 *
FROM Production.Product

SELECT *
FROM Person.Person
ORDER BY FirstName asc, LastName desc

SELECT FirstName, LastName
FROM Person.Person
ORDER BY FirstName asc, LastName desc

SELECT TOP 10 *
FROM Production.Product
ORDER BY ListPrice desc

SELECT TOP 10 ProductID
FROM Production.Product
ORDER BY ListPrice desc

SELECT TOP 4 Name, ProductNumber
FROM Production.Product
ORDER BY ProductID asc

SELECT *
FROM Production.Product
WHERE ListPrice between 1000 and 1500;

SELECT *
FROM HumanResources.Employee
WHERE HireDate between '2009/01/01' and '2010/01/01'
ORDER BY HireDate

SELECT *
FROM Person.Person
WHERE BusinessEntityID IN (2,7,13)

SELECT *
FROM Person.Person
WHERE FirstName like '%to'

SELECT Count(ListPrice)
FROM Production.Product
WHERE ListPrice > 1500

SELECT Count(LastName)
FROM Person.Person
WHERE LastName like 'P%'

SELECT Count(DISTINCT City)
FROM person.Address

SELECT Distinct (City)
FROM Person.Address

SELECT COUNT(*)
FROM Production.Product
WHERE Color = 'red'
AND ListPrice between 500 and 1000

SELECT COUNT(*)
FROM Production.Product
WHERE Name like '%road%';

SELECT TOP 10 sum(LineTotal) AS "Soma"
FROM Sales.SalesOrderDetail

SELECT TOP 10 MIN(LineTotal) AS "MINIMO"
FROM Sales.SalesOrderDetail

SELECT *
FROM Sales.SalesOrderDetail

SELECT SpecialOfferID, SUM(UnitPrice)
FROM Sales.SalesOrderDetail
GROUP BY SpecialOfferID

SELECT LOWER(JobTitle) AS "CARGOS" 
FROM HumanResources.Employee 

SELECT TOP 10 AVG(LineTotal)
FROM Sales.SalesOrderDetail

SELECT ProductID, COUNT(ProductID) AS "CONTAGEM"
FROM Sales.SalesOrderDetail
GROUP BY ProductID

SELECT *
FROM Person.Person

SELECT FirstName, COUNT(FirstName) AS "CONTAGEM"
FROM Person.Person
GROUP BY FirstName

SELECT AVG(ListPrice)
FROM Production.Product
WHERE Color = 'Silver'

SELECT COUNT(MiddleName)
FROM Person.Person
GROUP BY MiddleName

SELECT MiddleName, COUNT(FirstName)
FROM Person.Person
GROUP BY MiddleName

SELECT *
FROM Production.Product

SELECT ProductID, AVG(OrderQty) AS "QUANTIDADE"
FROM Sales.SalesOrderDetail 
GROUP BY ProductID 

SELECT *
FROM Production.WorkOrder

SELECT TOP 10 productID, SUM(LineTotal) AS "CONTAGEM"
FROM Sales.SalesOrderDetail
GROUP BY ProductID
ORDER BY SUM(LineTotal) desc;

SELECT ProductID, COUNT(productID) "Contagem",
AVG(OrderQTY) AS "QUANTIDADE"
FROM Production.WorkOrder
GROUP BY ProductID

SELECT FirstName, COUNT(FirstName) AS "QUANTIDADE"
FROM Person.Person
GROUP BY FirstName
HAVING COUNT(FirstName) > 10 

SELECT ProductID, SUM(LineTotal) AS "TOTAL"
FROM Sales.SalesOrderDetail
GROUP BY ProductID
HAVING SUM(LineTotal) between 162000 and 500000

SELECT FirstName, COUNT(FirstName) AS "QUANTIDADE"
FROM Person.Person
WHERE Title = 'Mr.'
GROUP BY FirstName
HAVING COUNT (FirstName) > 10

SELECT *
FROM Person.Address

SELECT StateProvinceID, COUNT(StateProvinceID) AS "QUANTIDADE"
FROM Person.Address
GROUP BY StateProvinceID
HAVING COUNT(StateProvinceID) > 1000

SELECT ProductID, AVG(LineTotal) AS "QUANTIDADE"
FROM Sales.SalesOrderDetail
GROUP BY ProductID
HAVING AVG(LineTotal) < 1000000

SELECT FirstName AS "Nome", LastName AS "Sobrenome"
FROM Person.Person

SELECT ProductNumber AS "Nome Produto"
FROM Production.Product

SELECT UnitPrice AS "Preço Unitário"
FROM Sales.SalesOrderDetail

SELECT *
FROM Person.EmailAddress

SELECT *
FROM Person.Person

SELECT p.BusinessEntityID, p.FirstName, p.LastName, pe.EmailAddress
FROM Person.Person AS P
INNER JOIN Person.EmailAddress PE on p.BusinessEntityID = pe.BusinessEntityID


SELECT TOP 10 *
FROM Production.Product

SELECT TOP 10 *
FROM Production.ProductSubcategory

SELECT pr.ListPrice AS "Preço",pr.Name AS "Nome",pc.Name
FROM Production.Product Pr
INNER JOIN Production.ProductSubcategory PC on PC.ProductSubcategoryID = pr.ProductSubcategoryID

SELECT TOP 10 *
FROM Person.BusinessEntityAddress AS BA 
INNER JOIN Person.Address PA on PA.AddressID = BA.AddressID

SELECT TOP 10 *
FROM Person.PhoneNumberType

SELECT TOP 10 * 
FROM Person.PersonPhone -- BusinessEntity - --AS PH

SELECT TOP 10 *
FROM Person.PersonPhone AS PH
INNER JOIN Person.PhoneNumberType PN on PN.PhoneNumberTypeID = PH.PhoneNumberTypeID

SELECT ph.BusinessEntityID AS "ID", pn.Name AS "Nome", pn.PhoneNumberTypeID AS "TIPO NUM", ph.PhoneNumber AS "TELEFONE"
FROM Person.PersonPhone AS PH
INNER JOIN Person.PhoneNumberType PN on PN.PhoneNumberTypeID = ph.PhoneNumberTypeID

SELECT TOP 10 * 
FROM person.StateProvince  -- APELIDO  PS

SELECT TOP 10 *
FROM Person.Address  -- APELIDO PA

SELECT pa.AddressID AS "ID ESTADO", pa.City AS "CIDADE", pa.StateProvinceID AS "NUMERO ESTADO", ps.Name AS "NOME DO ESTADO"
FROM Person.Address AS PA
INNER JOIN Person.StateProvince PS on PS.StateProvinceID = PA.StateProvinceID

SELECT [ProductID], [Name], [ProductNumber] FROM
Production.Product WHERE Name like '%Chain%'
UNION
SELECT [ProductID], [Name], [ProductNumber] FROM
Production.Product WHERE Name like '%Decal%'

SELECT FirstName, Title
FROM Person.Person
WHERE Title = 'Mr.'
UNION
SELECT FirstName, Title
FROM Person.Person
WHERE MiddleName = 'A'

SELECT *
FROM Person.Address

SELECT *
FROM Person.ContactType

SELECT *
FROM Production.Product

SELECT *
FROM Production.ProductSubcategory

--SUBQUERYS

SELECT *
FROM Production.Product
WHERE ListPrice > (SELECT AVG(ListPrice) FROM Production.Product)

SELECT *
FROM HumanResources.Employee
--WHERE JobTitle = (SELECT (JobTitle) FROM HumanResources.Employee)

SELECT *
FROM Person.StateProvince
--WHERE JobTitle = 'Design Engineer'

SELECT FirstName
FROM Person.Person
WHERE BusinessEntityID IN (
SELECT BusinessEntityID FROM HumanResources.Employee
WHERE JobTitle ='Design Engineer')

SELECT FirstName, LastName
FROM Person.Person
WHERE BusinessEntityID IN(
SELECT BusinessEntityID FROM HumanResources.Employee
WHERE MaritalStatus ='M')

SELECT p.FirstName
FROM Person.Person as P
INNER JOIN HumanResources.Employee E ON P.BusinessEntityID = E.BusinessEntityID
AND E.JobTitle = 'Design Engineer'


SELECT *
FROM HumanResources.Employee

SELECT *
FROM HumanResources.EmployeePayHistory

SELECT *
FROM Person.StateProvince 

SELECT *
FROM Person.Address

SELECT DISTINCT ps.StateProvinceID, ps.StateProvinceCode, ps.Name, pa.StateProvinceID
FROM Person.StateProvince as PS
INNER JOIN Person.Address PA ON PS.StateProvinceID = PA.StateProvinceID

SELECT *
FROM Sales.SalesOrderDetail --> s

SELECT *
FROM Sales.SpecialOfferProduct

SELECT s.SpecialOfferID,s.OrderQty, s.UnitPriceDiscount, ss.SpecialOfferID
FROM Sales.SalesOrderDetail S
INNER JOIN Sales.SpecialOfferProduct SS ON S.SpecialOfferID = SS.SpecialOfferID

SELECT *
FROM Sales.CountryRegionCurrency --AS SR

SELECT *
FROM Sales.Currency --AS SC

SELECT sc.CurrencyCode, sc.Name, sr.CountryRegionCode, sr.CurrencyCode
FROM Sales.Currency AS SC
INNER JOIN Sales.CountryRegionCurrency SR ON SC.CurrencyCode = SR.CurrencyCode

SELECT pv.ProductID, pv.StandardPrice, pv.BusinessEntityID, po.UnitPrice, po.OrderQty, po.ProductID, pd.BusinessEntityID
FROM Purchasing.ProductVendor AS PV
INNER JOIN Purchasing.PurchaseOrderDetail PO ON PV.ProductID = PO.ProductID
INNER JOIN Purchasing.Vendor PD ON PD.BusinessEntityID = PV.BusinessEntityID

SELECT cc.CustomerID, cd.CompanyName, cd.Country, cd.city, cd.Region, cd.Phone, cd.CustomerID
FROM CustomerCustomerDemo AS CC
INNER JOIN Customers AS CD ON CD.CustomerID = CD.CustomerID
--INNER JOIN Customers CD ON CD.Country = DE.Country 










