CREATE TABLE IF NOT EXISTS custumer (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(50),
    last_name VARCHAR(50)
    );

CREATE TABLE IF NOT EXISTS product (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50),
    price INTEGER
    );


CREATE TABLE IF NOT EXISTS bill (
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   purchase_datetime TIME,
   cashier_id INTEGER,
   custumer_id INTEGER REFERENCES custumer(id)
);


CREATE TABLE IF NOT EXISTS bill_line (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bill_id INTEGER REFERENCES bill(id),
    product_id INTEGER REFERENCES product(id),
    quantity FLOAT
);


