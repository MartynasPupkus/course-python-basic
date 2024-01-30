INSERT INTO destytojai (vardas, pavarde, skyrius, el_pastas)
    VALUES ("Geras", "Destytojauskas", "matematikos", "geras@gmail.com");
INSERT INTO destytojai (vardas, pavarde, skyrius, el_pastas)
    VALUES ("Geresnis", "Destytojukas", "lietuviu", "geresnis@gmail.com");

SELECT * FROM destytojai;

SELECT * FROM destytojai WHERE id = 2;

UPDATE destytojai SET vardas = "Martynas" WHERE id = 2;
UPDATE destytojai SET vardas = "Opa" WHERE vardas = "Geras"


DELETE FROM destytojai

DROP TABLE destytojai
