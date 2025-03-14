CREATE TABLE Users (
    user_id INT PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(100),
    registration_date DATE
);

INSERT INTO Users (user_id, first_name, last_name, email, password, registration_date) 
VALUES 
(1, 'Ama', 'Vanetta', 'ama.vanetta@x.com', 'password123', '2025-01-15'),
(2, 'Frank', 'Afrane', 'frank.afrane@x.com', 'password456', '2025-02-01');

CREATE TABLE IncomeSources (
    income_id INT PRIMARY KEY,
    user_id INT,
    source_name VARCHAR(100),
    monthly_income DECIMAL(10, 2),
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

INSERT INTO IncomeSources (income_id, user_id, source_name, monthly_income)
VALUES 
(1, 1, 'Salary', 3000.00),
(2, 1, 'Freelancing', 1200.00),
(3, 2, 'Salary', 2500.00);

CREATE TABLE ExpenseCategories (
    category_id INT PRIMARY KEY,
    category_name VARCHAR(100)
);

INSERT INTO ExpenseCategories (category_id, category_name) 
VALUES 
(1, 'Rent'),
(2, 'Utilities'),
(3, 'Groceries'),
(4, 'Entertainment'),
(5, 'Transportation');

CREATE TABLE Transactions (
    transaction_id INT PRIMARY KEY,
    user_id INT,
    category_id INT,
    amount DECIMAL(10, 2),
    transaction_date DATE,
    transaction_type VARCHAR(10) CHECK (transaction_type IN ('Income', 'Expense')),
    description TEXT,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (category_id) REFERENCES ExpenseCategories(category_id)
);

INSERT INTO Transactions (transaction_id, user_id, category_id, amount, transaction_date, transaction_type, description)
VALUES 
(1, 1, 1, 1000.00, '2025-02-01', 'Expense', 'Monthly rent payment'),
(2, 1, 2, 150.00, '2025-02-05', 'Expense', 'Electricity bill'),
(3, 1, 3, 200.00, '2025-02-10', 'Expense', 'Groceries'),
(4, 1, 4, 100.00, '2025-02-15', 'Expense', 'Movie night'),
(5, 1, 5, 50.00, '2025-02-20', 'Expense', 'Bus fare'),
(6, 2, 1, 2500.00, '2025-02-10', 'Income', 'Monthly salary'),
(7, 2, 3, 300.00, '2025-02-12', 'Expense', 'Groceries'),
(8, 2, 4, 80.00, '2025-02-18', 'Expense', 'Dinner with friends');

SELECT SUM(monthly_income) AS total_income
FROM IncomeSources
WHERE user_id = 1;

SELECT t.transaction_id, t.amount, t.transaction_date, t.transaction_type, ec.category_name
FROM Transactions t
JOIN ExpenseCategories ec ON t.category_id = ec.category_id
WHERE t.user_id = 1 AND t.transaction_date BETWEEN '2025-01-01' AND '2025-03-31';
