-- SQLite
-- Sukuriame "Kategorijos" lentelę
CREATE TABLE Kategorijos (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  pavadinimas TEXT
);

-- Sukuriame "Prekes" lentelę
CREATE TABLE Prekes (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  pavadinimas TEXT,
  aprasymas TEXT,
  kategorijos_id INTEGER REFERENCES Kategorijos(id)
);