-- SQLite
CREATE TABLE skelbimai (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  pavadinimas VARCHAR(255) NOT NULL,
  turinys TEXT NOT NULL
);

CREATE TABLE kategorijos (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  pavadinimas VARCHAR(255) NOT NULL
);

CREATE TABLE skelbimu_kategorijos (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  fk_skelbimo_id INTEGER REFERENCES skelbimai(id),
  fk_kategorijos_id INTEGER REFERENCES kategorijos(id)
);