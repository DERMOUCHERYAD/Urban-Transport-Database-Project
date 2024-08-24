import sqlite3
from datetime import datetime

def insert_Client(conn):
    try:
        cur = conn.cursor()
        num_c = int(input("Entrer le numero du client: "))
        nom_c = input("Entrer le nom du client: ")
        email = input("Entrer l'email du client (...@gmail.com): ")
        if("@gmail.com" not in email):
            print("L'adresse email n'est pas valide :(")
            return
        
        cur.execute("""
                    INSERT INTO Clients VALUES(%d, '%s', '%s');
                    """%(num_c, nom_c, email))
        conn.commit()
    
    except ValueError:
        print("Erreur de valeur: veuillez entrer le meme type de valeur")

    except sqlite3.IntegrityError as e:

        if "UNIQUE constraint failed: Clients.numero_client" in str(e):
            print(f"Erreur: Client numero: {num_c} existe deja dans la base de donne.")
        else:
            print("Erreur: IntegrityError - ", e)

def insert_Ligne(conn):
    try:
        cur = conn.cursor()
        num_l = int(input("Entrer le numero de la ligne: "))
        nom_l = input("Entrer le nom de la ligne: ")
        cur.execute("""
                    INSERT INTO Lignes VALUES(%d, '%s');
                    """%(num_l, nom_l))
        conn.commit()
    
    except ValueError:
        print("Erreur de valeur: veuillez entrer le meme type de valeur")

    except sqlite3.IntegrityError as e:

        if "UNIQUE constraint failed: Lignes.numero_ligne" in str(e):
            print(f"Erreur: Ligne numero: {num_l} existe deja dans la base de donne.")
        else:
            print("Erreur: IntegrityError - ", e)

def insert_Vehicule(conn):
    try:
        cur = conn.cursor()
        matricule_v = int(input("Entrer le numero de matricule de votre véhicule: "))
        type_v = input("Merci de choisir le type des véhicule parmi les type proposé:\n Tramway,Bus,Navette,Voiture: ")
        capacite_max = int(input("Entrer la capacité maximale de votre véhicule selon les contraintes: "))
        
        cur.execute("""
                    INSERT INTO Vehicules VALUES(%d, '%s', '%d');
                    """%(matricule_v, type_v, capacite_max))
        conn.commit()
    
    except ValueError:
        print("Erreur de valeur: veuillez entrer le meme type de valeur")

    except sqlite3.IntegrityError as e:

        if "UNIQUE constraint failed: Vehicules.matricule_vehicule" in str(e):
            print(f"Erreur: Vehicule numero: {matricule_v} existe deja dans la base de donne.")
        else:
            print("Erreur: IntegrityError - ", e)

def insert_Trajet(conn):
    try:
        cur = conn.cursor()
        num_t = int(input("Entrer le numero du trajet: "))
        point_depart_t = input("Entrer le point de depart de trajet: ")
        point_arrivee_t = input("Entrer le point d'arrivée de trajet: ")
        duree_t = float(input("Entrer la durée du trajet: "))
        num_l = int(input("Entrer le numero du ligne: "))
        
        cur.execute("""
                    INSERT INTO Trajets VALUES(%d, '%s', '%s','%f','%d');
                    """%(num_t, point_depart_t, point_arrivee_t,duree_t,num_l))
        conn.commit()
    
    except ValueError:
        print("Erreur de valeur: veuillez entrer le meme type de valeur")

    except sqlite3.IntegrityError as e:

        if "UNIQUE constraint failed: Trajets.numero_trajet" in str(e):
            print(f"Erreur: Trajet numéro: {num_t} existe deja dans la base de donne.")
        else:
            print("Erreur: IntegrityError - ", e)

def insert_Programmation(conn):
    try:
        cur = conn.cursor()
        matricule_v = int(input("Entrer le numero de matricule de votre véhicule: "))
        num_t = int(input("Entrer le numero du trajet: "))
 
        
        cur.execute("""
                    INSERT INTO Programmations VALUES(%d, '%d');
                    """%(matricule_v, num_t))
        conn.commit()
    
    except ValueError:
        print("Erreur de valeur: veuillez entrer le meme type de valeur")

    except sqlite3.IntegrityError as e:

        if "UNIQUE constraint failed: Programmations.matricule_vehicule" in str(e) and "UNIQUE constraint failed: Programmations.numero_trajet" in str(e) :
            print(f"Erreur: Le matricule,trajet: {matricule_v,num_t} existe deja dans la base de donne.")
        else:
            print("Erreur: IntegrityError - ", e)


def insert_Reservation(conn):
    try:
        cur = conn.cursor()
        num_r = int(input("Entrer le numero de réservation: "))
        input_date = input("Enter la date de reservation yyyy-mm-dd : ")
        date_r = datetime.strptime(input_date, "%Y-%m-%d")  # Correction du format et ajout de .date()
        input_date = input("Enter l'heure de reservation h:m : ")
        heure_r = datetime.strptime(input_date, "%H:%M") # Correction du format et ajout de .time()
        num_c = int(input("Entrer le numero du client: "))
        num_t = int(input("Entrer le numero du trajet: "))

        # Utilisation de paramètres de requête pour éviter les attaques par injection SQL
        cur.execute("""
                    INSERT INTO Reservations VALUES(?, ?, ?, ?, ?);
                    """, (num_r, date_r, heure_r, num_c, num_t))
        conn.commit()
    
    except ValueError as ve:
        print("Erreur de valeur:", ve)

    except sqlite3.IntegrityError as e:
        if "UNIQUE constraint failed: Reservations.numero_reservation" in str(e):
            print(f"Erreur: Réservation numéro {num_r} existe déjà dans la base de données.")
        elif "UNIQUE constraint failed: Reservations.numero_trajet" in str(e):
            print(f"Erreur: Trajet numéro {num_t} existe déjà dans la base de données.")
        else:
            print("Erreur: IntegrityError - ", e)
