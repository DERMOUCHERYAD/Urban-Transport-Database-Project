from termcolor import colored
from prettytable import PrettyTable
from colorama import Fore, Style
from datetime import datetime


# --------------------------------Des fonction pour afficher les tables de la base de données----------------------------------------- 
def select_Clients(conn):
    cur = conn.cursor()
    cur.execute("""
                SELECT  *
                FROM Clients;
                """)

    rows = cur.fetchall()

    table = PrettyTable()
    table.field_names = ["numero_client", "nom_client", "adresse_email_client"]
    
    for row in rows:
        table.add_row(row)
    
    print(table)



def select_Lignes(conn):
    cur = conn.cursor()
    cur.execute("""
                SELECT  *
                FROM Lignes;
                """)

    rows = cur.fetchall()

    table = PrettyTable()
    table.field_names = ["numero_ligne", "nom_ligne"]
    
    for row in rows:
        table.add_row(row)
    
    print(table)

def select_Vehicules(conn):
    cur = conn.cursor()
    cur.execute("""
                SELECT  *
                FROM Vehicules;
                """)

    rows = cur.fetchall()

    table = PrettyTable()
    table.field_names = ["matricule_vehicule", "type_vehicule", "capacite_max_passager_vehicule"]
    
    for row in rows:
        table.add_row(row)
    
    print(table)

def select_Trajets(conn):
    cur = conn.cursor()
    cur.execute("""
                SELECT  *
                FROM Trajets;
                """)

    rows = cur.fetchall()

    table = PrettyTable()
    table.field_names = ["numero_trajet", "point_depart_trajet", "point_arrivee_trajet","duree_trajet","numero_ligne"]
    
    for row in rows:
        table.add_row(row)
    
    print(table)

def select_Programmations(conn):
    cur = conn.cursor()
    cur.execute("""
                SELECT  *
                FROM Programmations;
                """)

    rows = cur.fetchall()

    table = PrettyTable()
    table.field_names = ["matricule_vehicule", "numero_trajet"]
    
    for row in rows:
        table.add_row(row)
    
    print(table)

def select_Reservations(conn):
    cur = conn.cursor()
    cur.execute("""
                SELECT  *
                FROM Reservations;
                """)

    rows = cur.fetchall()

    table = PrettyTable()
    table.field_names = ["numero_reservation", "date_reservation", "heure_reservation", "numero_client", "numero_trajet"]
    
    for row in rows:
        table.add_row(row)
    
    print(table)

# ----------------Des fonctions pour affcher les requetes proposées----------------------------

def select_reservations_clients(conn):
    # Afficher toutes les informations de la réservation de chaque client par son numéro
    cur = conn.cursor()

    # Demander à l'utilisateur d'entrer le numéro du client
    client_number = input("Entrez le numéro du client que vous souhaitez rechercher : ")

    # Exécuter la requête SQL avec une jointure
    cur.execute("""
        SELECT Clients.numero_client, Clients.nom_client, Clients.adresse_email_client, 
               Reservations.numero_reservation, Reservations.date_reservation, Reservations.heure_reservation
        FROM Clients
        LEFT JOIN Reservations ON Clients.numero_client = Reservations.numero_client
        WHERE Clients.numero_client = ?
    """, (client_number,))

    rows = cur.fetchall()

    if rows:
        print(Fore.GREEN + Style.BRIGHT + "CLIENT TROUVÉ")        
        print(Style.RESET_ALL)  # Réinitialiser la couleur à la normale
        print(Fore.GREEN + Style.BRIGHT + "Informations du client :")        
        print(Style.RESET_ALL)
        print("Numéro client:", rows[0][0])
        print("Nom client:", rows[0][1])
        print("Adresse email client:", rows[0][2])
        
        print(Fore.GREEN + Style.BRIGHT + "\nRéservations du client :")        
        print(Style.RESET_ALL) 
        table = PrettyTable()
        table.field_names = ["Numero Reservation", "Date Reservation", "Heure Reservation"]
        for row in rows:
            table.add_row(row[3:])  # Ignorer les informations du client déjà affichées
        print(table)
    else:
        print(Fore.RED + "CLIENT NON TROUVÉ / IL N'A PAS DE RESERVATION")
        print(Style.RESET_ALL)  # Réinitialiser la couleur à la normale



def clients_metro_bus_infos(conn):
    #affiche les informations des clients ayant effectué des réservations à la fois pour les trajets en tramway et en bus.
    curs = conn.cursor()
    # Définir la requête SQL
    query = """
    SELECT *
    FROM Clients
    WHERE numero_client IN (
        SELECT numero_client 
        FROM Reservations
        JOIN Trajets ON Reservations.numero_trajet = Trajets.numero_trajet
        JOIN Programmations ON Trajets.numero_trajet = Programmations.numero_trajet
        JOIN Vehicules ON Programmations.matricule_vehicule = Vehicules.matricule_vehicule
        WHERE type_vehicule = 'Tramway'

        INTERSECT

        SELECT numero_client 
        FROM Reservations
        JOIN Trajets ON Reservations.numero_trajet = Trajets.numero_trajet
        JOIN Programmations ON Trajets.numero_trajet = Programmations.numero_trajet
        JOIN Vehicules ON Programmations.matricule_vehicule = Vehicules.matricule_vehicule
        WHERE type_vehicule = 'Bus'
    )
    """

    # Exécuter la requête SQL
    curs.execute(query)

    # Récupérer tous les résultats
    results = curs.fetchall()

    # Créer une table pour afficher les résultats
    table = PrettyTable()
    table.field_names = ["Numéro du client", "Nom du client", "Adresse e-mail"]

    # Ajouter les résultats à la table
    if results:
        for client in results:
            table.add_row([client[0], client[1], client[2]])

        # Afficher la table
        print("Informations des clients ayant réservé à la fois en tramway et en bus :")
        print(table)
    else:
        print("Aucun client n'a réservé à la fois en tramway et en bus.")


from prettytable import PrettyTable

def client_fidele(conn):
    curs = conn.cursor()
    
    # Définir la requête SQL
    # Cette requête utilise une clause WITH pour calculer le nombre maximum de réservations
    # dans une sous-requête nommée max_reservations, puis elle joint cette sous-requête avec la table Clients et la table Reservations 
    # pour sélectionner les clients ayant le nombre maximal de réservations. 
    # La fonction COUNT() est utilisée pour compter le nombre de réservations pour chaque client.
    query = """
    WITH max_reservations AS (
        SELECT MAX(compteur_reservations) AS max_reservations
        FROM (
            SELECT numero_client, COUNT(*) AS compteur_reservations
            FROM Reservations
            GROUP BY numero_client
        )
    )
    SELECT Clients.numero_client, nom_client, adresse_email_client, COUNT(*) AS nb_reservations
    FROM Clients
    JOIN Reservations ON Clients.numero_client = Reservations.numero_client
    JOIN max_reservations ON true
    GROUP BY Clients.numero_client
    HAVING COUNT(*) = (SELECT max_reservations FROM max_reservations);
    """

    # Exécuter la requête SQL
    curs.execute(query)
    clients_fideles = curs.fetchall()

    # Afficher les informations des clients avec le maximum de réservations dans un tableau
    if clients_fideles:
        max_reservations = clients_fideles[0][3]  # Récupérer le nombre maximum de réservations
        table = PrettyTable()
        table.field_names = ["Numéro du client", "Nom du client", "Adresse e-mail du client"]

        for client in clients_fideles:
            table.add_row([client[0], client[1], client[2]])

        print("Clients avec le maximum de réservations (", max_reservations, " réservations) :")
        print(table)
    else:
        print("Aucun client trouvé avec le maximum de réservations.")
