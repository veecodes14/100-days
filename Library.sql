'''DAY 49''' 
 
CREATE TABLE books (
    id INT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    year_published INT
);

INSERT INTO books (id, title, author, year_published)
VALUES
    (1, 'Things Fall Apart', 'Chinua Achebe', 1958),
    (2, 'Half of a Yellow Sun', 'Chimamanda Ngozi Adichie', 2006),
    (3, 'The No. 1 Ladies’ Detective Agency', 'Alexander McCall Smith', 1998),
    (4, 'Season of Migration to the North', 'Tayeb Salih', 1966),
    (5, 'The Beautyful Ones Are Not Yet Born', 'Ayi Kwei Armah', 1968);

SELECT * 
FROM books;

SELECT * 
FROM books 
WHERE author = 'Chimamanda Ngozi Adichie';

UPDATE books 
SET year_published = 1960
WHERE title = 'Things Fall Apart';

DELETE FROM books 
WHERE title = 'The No. 1 Ladies’ Detective Agency';

CREATE TABLE borrowers (
    borrower_id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255),
    phone_number VARCHAR(20)
);