-- SQLite
CREATE TABLE vadovai (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  vardas VARCHAR(255) NOT NULL,
  pavarde VARCHAR(255) NOT NULL
);

CREATE TABLE darbuotojai (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  vardas VARCHAR(255) NOT NULL,
  pavarde VARCHAR(255) NOT NULL,
  fk_vadovas_id INTEGER REFERENCES vadovai(id)
);

INSERT INTO vadovai (id, vardas, pavarde)
VALUES (1, "Martynas", "Pupkus")

