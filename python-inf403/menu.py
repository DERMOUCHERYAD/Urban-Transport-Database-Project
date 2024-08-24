import time
import os
import sys
from Selection import *
from Insertion import * 
from Delete import *
from Views import *


def press_any_key(message):
    input(message)


def clear_console():
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')


def afficher_bienvenue():
    terminal_width = os.get_terminal_size().columns
    bienvenue = "B I E N V E N U E"
    padding = (terminal_width - len(bienvenue)) // 2

    print("\033[1;34m*" * terminal_width + "\033[0m")  # Gras et bleu
    print("\033[1;34m*" + " " * (terminal_width - 2) + "*\033[0m")
    print("\033[1;34m*\033[0m" + " " * (padding - 1) + "\033[1;31m" + bienvenue + "\033[0m" + " " * (padding - 1) + "\033[1;34m*\033[0m")  # Gras et rouge pour "BIENVENUE"
    print("\033[1;34m*" + " " * (terminal_width - 2) + "*\033[0m")
    print("\033[1;34m*" * terminal_width + "\033[0m")

    time.sleep(1)  # Attendre 1 seconde avant d'afficher le menu

    
def menu_afficher_table(conn):
    clear_console()
    print("-" * 30)
    print("\033[1;34mAffichage des tables :\033[0m")  # Gras et bleu
    options = [
        "Clients",
        "Lignes",
        "Vehicules",
        "Trajets",
        "Programmations",
        "Reservations",
        "Quitter"]
    
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    print("-" * 30)

    choix = int(input("Entrez le numéro de l'option choisie : "))
    clear_console()
    if 1 <= choix <= len(options):
        
        if choix == 1:
            print(f"\033[1;35mAffichage de la table {options[choix - 1]} :\033[0m")  # Gras et magenta
            select_Clients(conn)
        elif choix == 2:
            print(f"\033[1;35mAffichage de la table {options[choix - 1]} :\033[0m")  # Gras et magenta
            select_Lignes(conn)
        elif choix == 3:
            print(f"\033[1;35mAffichage de la table {options[choix - 1]} :\033[0m")  # Gras et magenta
            select_Vehicules(conn)
        elif choix == 4:
            print(f"\033[1;35mAffichage de la table {options[choix - 1]} :\033[0m")  # Gras et magenta
            select_Trajets(conn)
        elif choix == 5:
            print(f"\033[1;35mAffichage de la table {options[choix - 1]} :\033[0m")  # Gras et magenta
            select_Programmations(conn)
        elif choix == 6:
            print(f"\033[1;35mAffichage de la table {options[choix - 1]} :\033[0m")  # Gras et magenta
            select_Reservations(conn)         
        elif choix == 7:
            print(f"\033[1;35mQuitter....\033[0m")  # Gras et magenta
            press_any_key("\nAppuyez sur Entrée pour revenir vers le menu principale...")
            return
        
        press_any_key("\nAppuyez sur Entrée pour revenir...")
        clear_console()
        menu_afficher_table(conn)
    else:
        print("\033[1;31mErreur : Option incorrecte.\033[0m")  # Gras et rouge
        press_any_key("\nAppuyez sur Entrée pour revenir...")
        clear_console()
        menu_afficher_table(conn)  
    
def menu_requete(conn):
    clear_console()
    print("-" * 80)
    print("\033[1;35;40m Requêtes :\033[0m")  # Gras et bleu
    options = [
        "Afficher les détails de la réservation par numéro client",
        "Consultation des clients utilisant à la fois le tramway et le bus",
        "Identifiez le/les client(s) fidèle(s)",
        "Quitter"
    ]
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    print("-" * 80)

    choix = int(input("Entrez le numéro de l'option choisie : "))
    clear_console()
    if 1 <= choix <= len(options):
        
        if choix == 1:
            print(f"\033[1;35m{options[choix - 1]} :\033[0m")  # Gras et magenta
            select_reservations_clients(conn)
        elif choix == 2:
            print(f"\033[1;35m{options[choix - 1]} :\033[0m")  # Gras et magenta
            clients_metro_bus_infos(conn)
        elif choix == 3:
            print(f"\033[1;35m{options[choix - 1]} :\033[0m")  # Gras et magenta
            client_fidele(conn)
         
        
        elif choix == 4:
            print(f"\033[1;35mQuitter....\033[0m")  # Gras et magenta
            press_any_key("\nAppuyez sur Entrée pour revenir vers le menu principale...")
            return
        
        press_any_key("\nAppuyez sur Entrée pour revenir...")
        clear_console()
        menu_requete(conn)
    else:
        print("\033[1;31mErreur : Option incorrecte.\033[0m")  # Gras et rouge
        press_any_key("\nAppuyez sur Entrée pour revenir...")
        clear_console()
        menu_requete(conn)

def menu_insertion(conn):
    clear_console()
    print("-" * 30)
    print("\033[1;32;40m Insertion dans les table :\033[0m")  # Gras et bleu
    options = [
        "Clients",
        "Lignes",
        "Vehicules",
        "Trajets",
        "Programmations",
        "Reservations",
        "Quitter"
        ]
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    print("-" * 30)

    choix = int(input("Entrez le numéro de l'option choisie : "))
    clear_console()
    if 1 <= choix <= len(options):
        
        if choix == 1:
            print(f"\033[1;35mInsertion dans la table {options[choix - 1]} :\033[0m")  # Gras et magenta
            insert_Client(conn)
        elif choix == 2:
            print(f"\033[1;35mInsertion dans la table {options[choix - 1]} :\033[0m")  # Gras et magenta
            insert_Ligne(conn)
        elif choix == 3:
            print(f"\033[1;35mInsertion dans la table {options[choix - 1]} :\033[0m")  # Gras et magenta
            insert_Vehicule(conn)
        elif choix == 4:
            print(f"\033[1;35mInsertion dans la table {options[choix - 1]} :\033[0m")  # Gras et magenta
            insert_Trajet(conn)
        elif choix == 5:
            print(f"\033[1;35mInsertion dans la table {options[choix - 1]} :\033[0m")  # Gras et magenta
            insert_Programmation(conn)
        elif choix == 6:
            print(f"\033[1;35mInsertion dans la table {options[choix - 1]} :\033[0m")  # Gras et magenta
            insert_Reservation(conn)
        elif choix == 7:
            print(f"\033[1;35mQuitter....\033[0m")  # Gras et magenta
            press_any_key("\nAppuyez sur Entrée pour revenir vers le menu principale...")
            return
        
        press_any_key("\nAppuyez sur Entrée pour revenir...")
        clear_console()
        menu_insertion(conn)
    else:
        print("\033[1;31mErreur : Option incorrecte.\033[0m")  # Gras et rouge
        press_any_key("\nAppuyez sur Entrée pour revenir...")
        clear_console()
        menu_insertion(conn)


def menu_views(conn):
    clear_console()
    print("-" * 50)
    print("\033[1;32;40m Views : \033[0m")  # Gras et bleu
    options = [
        "Informations sur les Réservations Clients par Ligne",
        "Nombre de reservations dans un mois",
        "Trajée programés Par Bus",
        "Quitter"
    ]
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    print("-" * 50)

    choix = int(input("Entrez le numéro de l'option choisie : "))
    clear_console()
    if 1 <= choix <= len(options):
        
        if choix == 1:
            print(f"\033[1;35m{options[choix - 1]} :\033[0m")  # Gras et magenta
            select_inf_clients_Res(conn)
        elif choix == 2:
            print(f"\033[1;35m{options[choix - 1]} :\033[0m")  # Gras et magenta
            select_nbrRes_mois(conn)
        elif choix == 3:
            print(f"\033[1;35m{options[choix - 1]} :\033[0m")  # Gras et magenta
            select_trajets_bus(conn)
        elif choix == 4:
            print(f"\033[1;35mQuitter....\033[0m")  # Gras et magenta
            press_any_key("\nAppuyez sur Entrée pour revenir vers le menu principale...")
            return
        
        press_any_key("\nAppuyez sur Entrée pour revenir...")
        clear_console()
        menu_views(conn)
    else:
        print("\033[1;31mErreur : Option incorrecte.\033[0m")  # Gras et rouge
        press_any_key("\nAppuyez sur Entrée pour revenir...")
        clear_console()
        menu_views(conn)



def menu_delete(conn):
    clear_console()
    print("-" * 30)
    print("\033[91m\033[1mSuppression :\033[0m")  # Gras et bleu
    options = [
        "Clients",
        "Reservations",
        "Quitter"
    ]
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    print("-" * 30)

    choix = int(input("Entrez le numéro de l'option choisie : "))
    clear_console()
    if 1 <= choix <= len(options):
        
        if choix == 1:
            print(f"\033[1;35mSuppression du {options[choix - 1]} :\033[0m")  # Gras et magenta
            delete_Client(conn)
        elif choix == 2:
            print(f"\033[1;35mSuppression de  {options[choix - 1]} :\033[0m")  # Gras et magenta
            delete_Reservation(conn)
        elif choix == 3:
            print(f"\033[1;35mQuitter....\033[0m")  # Gras et magenta
            press_any_key("\nAppuyez sur Entrée pour revenir vers le menu principale...")
            return
        
        press_any_key("\nAppuyez sur Entrée pour revenir...")
        clear_console()
        menu_delete(conn)
    else:
        print("\033[1;31mErreur : Option incorrecte.\033[0m")  # Gras et rouge
        press_any_key("\nAppuyez sur Entrée pour revenir...")
        clear_console()
        menu_delete(conn)       




# La fonction du menu principale:
def menu_principale(conn):

    iteration = 1

    if iteration == 1:
            afficher_bienvenue()
            press_any_key("\nAppuyez sur Entrée pour continuer...")
            clear_console()
    
    while True:
        print("*" * 30)
        print("\033[1;33mMenu principal :\033[0m")  # Gras et jaune
        print("1. Consulter la base de données")
        print("2. Afficher les requêtes suggérées ")
        print("3. Insertion des données")
        print("4. Consulter les Views")
        print("5. Suppression de données")
        print("6. Quitter")
        print("*" * 30)
        choix = input("Veuillez entrer le numéro de l'option choisie : ")

        if choix == "1":
            menu_afficher_table(conn)
        # elif choix == "2":
        elif choix == "2":
            menu_requete(conn)
        elif choix == "3":
            menu_insertion(conn)
        elif choix == "4":
            menu_views(conn)    
        elif choix == "5":
            menu_delete(conn)              
        elif choix == "6":
            print("\033[1;32mAu revoir !\033[0m")  # Gras et vert
            break
        else:
            press_any_key("\n\033[1;31mErreur : Commande incorrecte. Appuyez sur Entrée pour continuer...\033[0m")
        clear_console()

        iteration += 1

