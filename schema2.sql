-- Table Livres
DROP TABLE IF EXISTS Livres;
CREATE TABLE Livres (
    ID_Livre INT PRIMARY KEY AUTOINCREMENT,
    Titre VARCHAR(255),
    Auteur VARCHAR(255),
    Annee_de_publication INT,
    Genre VARCHAR(100),
    Nombre_exemplaires_disponibles INT
);

-- Table Utilisateurs
DROP TABLE IF EXISTS Utilisateurs;
CREATE TABLE Utilisateurs (
    ID_Utilisateur INT PRIMARY KEY AUTOINCREMENT,
    Nom VARCHAR(100),
    Prenom VARCHAR(100),
    Adresse_email VARCHAR(255),
    Mot_de_passe VARCHAR(255),
    Est_Administrateur BOOLEAN
);

-- Table Emprunts
DROP TABLE IF EXISTS Emprunts;
CREATE TABLE Emprunts (
    ID_Emprunt INT PRIMARY KEY AUTOINCREMENT,
    ID_Utilisateur INT,
    ID_Livre INT,
    Date_Emprunt DATE,
    Date_Retour_Prevue DATE,
    Date_Retour_effectif DATE,
    FOREIGN KEY (ID_Utilisateur) REFERENCES Utilisateurs(ID_Utilisateur),
    FOREIGN KEY (ID_Livre) REFERENCES Livres(ID_Livre)
);

-- Table Stocks (Facultatif)
DROP TABLE IF EXISTS Stocks;
CREATE TABLE Stocks (
    ID_Stock INT PRIMARY KEY AUTOINCREMENT,
    ID_Livre INT,
    Date_Ajout DATE,
    Date_Suppression DATE,
    FOREIGN KEY (ID_Livre) REFERENCES Livres(ID_Livre)
);
