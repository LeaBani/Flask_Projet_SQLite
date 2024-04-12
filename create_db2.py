import sqlite3

# Connexion à la base de données SQLite
connection = sqlite3.connect('database2.db')

# Ouverture du fichier contenant le schéma SQL
with open('schema2.sql') as f:
    connection.executescript(f.read())

# Création d'un curseur pour exécuter des requêtes SQL
cur = connection.cursor()

# Ajout des données d'exemple dans la table Utilisateurs
cur.execute("INSERT INTO Utilisateurs (Nom, Prenom, Adresse_email, Mot_de_passe, Est_Administrateur) VALUES (?, ?, ?, ?, ?)",
            ('Dupont', 'Emilie', 'emilie.dupont@example.com', 'motdepasse123', 0))
cur.execute("INSERT INTO Utilisateurs (Nom, Prenom, Adresse_email, Mot_de_passe, Est_Administrateur) VALUES (?, ?, ?, ?, ?)",
            ('Leroux', 'Lucas', 'lucas.leroux@example.com', 'motdepasse456', 0))
cur.execute("INSERT INTO Utilisateurs (Nom, Prenom, Adresse_email, Mot_de_passe, Est_Administrateur) VALUES (?, ?, ?, ?, ?)",
            ('Admin', 'Admin', 'admin@example.com', 'admin123', 1))

# Ajout des données d'exemple dans la table Livres
cur.execute("INSERT INTO Livres (Titre, Auteur, Annee_de_publication, Genre, Nombre_exemplaires_disponibles) VALUES (?, ?, ?, ?, ?)",
            ('Harry Potter à l\'école des sorciers', 'J.K. Rowling', 1997, 'Fantasy', 5))
cur.execute("INSERT INTO Livres (Titre, Auteur, Annee_de_publication, Genre, Nombre_exemplaires_disponibles) VALUES (?, ?, ?, ?, ?)",
            ('Le Seigneur des Anneaux', 'J.R.R. Tolkien', 1954, 'Fantasy', 3))
cur.execute("INSERT INTO Livres (Titre, Auteur, Annee_de_publication, Genre, Nombre_exemplaires_disponibles) VALUES (?, ?, ?, ?, ?)",
            ('1984', 'George Orwell', 1949, 'Dystopie', 7))

# Commit des changements et fermeture de la connexion
connection.commit()
connection.close()
