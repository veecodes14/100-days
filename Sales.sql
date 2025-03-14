'''DAY 47 & 48'''

CREATE TABLE Product (
    id SERIAL PRIMARY KEY,           
    product_name VARCHAR(255) NOT NULL,  
    category VARCHAR(100) NOT NULL,     
    price DECIMAL(10, 2) NOT NULL       
);

INSERT INTO Product (product_name, category, price)
VALUES
    ('Laptop', 'Electronics', 899.99),
    ('T-shirt', 'Clothing', 19.99),
    ('Headphones', 'Electronics', 129.99),
    ('Coffee Maker', 'Home Appliances', 49.99),
    ('Smartphone', 'Electronics', 699.99);

SELECT * FROM Product

CREATE TABLE Sales (
    id SERIAL PRIMARY KEY,                
    product_id INT NOT NULL,              
    quantity_sold INT NOT NULL,          
    sale_date DATE NOT NULL,              
    total_price DECIMAL(10, 2) NOT NULL,  
    FOREIGN KEY (product_id) REFERENCES Product(id)  
);

INSERT INTO Sales (product_id, quantity_sold, sale_date, total_price)
VALUES
    (1, 2, '2025-03-10', 1799.98),  
    (2, 5, '2025-03-09', 99.95),    
    (3, 1, '2025-03-08', 129.99),   
    (4, 3, '2025-03-07', 149.97),   
    (5, 4, '2025-03-06', 2799.96);

SELECT * FROM Sales

SELECT product_name, price FROM Product;

SELECT * 
FROM Sales 
LIMIT 2;

SELECT * 
FROM sales 
WHERE total_price > 100;

SELECT DISTINCT category FROM Product;

SELECT COUNT(*) AS total_products
FROM Product;

SELECT SUM(total_price) AS total_sales
FROM Sales;

SELECT AVG(price) AS average_price
FROM Product;