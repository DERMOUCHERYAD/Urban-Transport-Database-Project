import sqlite3


def delete_Client(conn):
    try:
        cur = conn.cursor()
        num_C = int(input("Entrer le Numero du Client: "))

        cur.execute("""
                    SELECT numero_client
                    FROM Clients;
                    """)
        
        rows = cur.fetchall()

        l = []

        for row in rows:
            l.append(row)

        new_list = [item[0] for item in l]

        if(num_C not in new_list):
            print("Le numero de client n'existe pas la suppression a echoue :(")
    
        cur.execute("""
                    DELETE FROM Clients WHERE numero_client = %d;
                    """%(num_C))
        conn.commit()

    except ValueError:
        print("Erreur de valeur: veuillez entrer le meme type de valeur")

    except sqlite3.IntegrityError as e:

        if "UNIQUE constraint failed: Clients.numero_client" in str(e):
            print(f"Erreur: Client numero: {num_C} existe deja dans la base de donne.")
        else:
            print("Erreur: IntegrityError - ", e)


def delete_Reservation(conn):
    try:
        cur = conn.cursor()
        num_r = int(input("Entrer le Numero de la Reservation: "))

        cur.execute("""
                    SELECT numero_reservation
                    FROM Reservations;
                    """)
        
        rows = cur.fetchall()

        l = []

        for row in rows:
            l.append(row)

        new_list = [item[0] for item in l]

        if(num_r not in new_list):
            print("Le numero de reservation n'existe pas la suppression a echoue :(")
    
        cur.execute("""
                    DELETE FROM Reservations WHERE numero_reservation = %d;
                    """%(num_r))
        conn.commit()

    except ValueError:
        print("Erreur de valeur: veuillez entrer le meme type de valeur")

    except sqlite3.IntegrityError as e:

        if "UNIQUE constraint failed: Reservations.numero_reservation" in str(e):
            print(f"Erreur: Reservation numero: {num_r} existe deja dans la base de donne.")
        else:
            print("Erreur: IntegrityError - ", e)




