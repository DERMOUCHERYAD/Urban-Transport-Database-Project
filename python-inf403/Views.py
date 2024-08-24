from termcolor import colored
from prettytable import PrettyTable
from colorama import Fore, Style
from datetime import datetime


# --------------------------------Des fonction pour afficher le contenu de notre view ----------------------------------------- 
def select_inf_clients_Res(conn):
    cur = conn.cursor()
    cur.execute("""
                SELECT  *
                FROM Vue_Client_Reservation_Ligne;
                """)

    rows = cur.fetchall()

    table = PrettyTable()
    table.field_names = ["numero_client", "adresse_email_client","nom_ligne"]
    
    for row in rows:
        table.add_row(row)
    
    print(table)


def select_nbrRes_mois(conn):
    cur = conn.cursor()
    cur.execute("""
                SELECT  *
                FROM Vue_Reservations_Par_Mois;
                """)

    rows = cur.fetchall()

    table = PrettyTable()
    table.field_names = ["mois", "nombre_reservations"]
    
    for row in rows:
        table.add_row(row)
    
    print(table)

def select_trajets_bus(conn):
    cur = conn.cursor()
    cur.execute("""
                SELECT  *
                FROM Vue_Trajets_Avec_Bus_Programmes;
                """)

    rows = cur.fetchall()

    table = PrettyTable()
    table.field_names = ["point_depart_trajet", "point_arrivee_trajet","matricule_vehicule"]
    
    for row in rows:
        table.add_row(row)
    
    print(table)



