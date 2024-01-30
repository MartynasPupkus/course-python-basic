CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date DATE,
    total DECIMAL(18,2),
    mokytoju_id INTEGER REFERENCES mokytojai(id)
);

INSERT INTO orders (date, total, mokytoju_id)
    VALUES(DATE("2020-01-29"), 100.00, 1);
