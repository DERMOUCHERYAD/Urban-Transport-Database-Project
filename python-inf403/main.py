#!/usr/bin/python3

from utils import db
from menu import *
 
def main():
    # Nom de la BD à créer
    db_file = "data/voile.db"

    # Créer une connexion a la BD
    conn = db.creer_connexion(db_file)

    # Remplir la BD
    db.mise_a_jour_bd(conn, "data/CREATE.sql")
    db.mise_a_jour_bd(conn, "data/VIEWS.sql")
    db.mise_a_jour_bd(conn, "data/Jeux de donnes max.sql")

    menu_principale(conn)
    

if __name__ == "__main__":
    main()
