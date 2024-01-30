-- SQLite
CREATE TABLE Studentai (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  vardas VARCHAR(50),
  pavarde VARCHAR(50),
  el_pastas VARCHAR(100),
  telefonas VARCHAR(20)
);


CREATE TABLE Kursai (
  id INTEGER PRIMARY KEY,
  pavadinimas VARCHAR(50),
  aprasymas TEXT
);


CREATE TABLE StudentuKursai (
  id INTEGER PRIMARY KEY,
  studento_id INTEGER REFERENCES Studentai(id),
  kurso_id INTEGER REFERENCES Kursai(id)
);