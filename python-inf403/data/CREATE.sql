DROP TABLE IF EXISTS Reservations;
DROP TABLE IF EXISTS Programmations;
DROP TABLE IF EXISTS Trajets;
DROP TABLE IF EXISTS Vehicules;
DROP TABLE IF EXISTS Clients;
DROP TABLE IF EXISTS Lignes;

-- Pour activer les FKs
PRAGMA FOREIGN_KEYS=ON;

CREATE TABLE Lignes(
numero_ligne INTEGER PRIMARY KEY NOT NULL ,
nom_ligne TEXT NOT NULL 
);

CREATE TABLE Reservations(
numero_reservation INTEGER PRIMARY KEY NOT NULL,
date_reservation DATE NOT NULL ,
heure_reservation TEXT NOT NULL,
numero_client INTEGER NOT NULL ,
numero_trajet INTEGER NOT NULL UNIQUE ,
   
CONSTRAINT fk_numero_client FOREIGN KEY (numero_client) REFERENCES Clients(numero_client),
CONSTRAINT fk_numero_trajet FOREIGN KEY (numero_trajet) REFERENCES Trajets(numero_trajet)   /* Une clé unique est aussi étrangère */
);


CREATE TABLE Trajets(
numero_trajet INTEGER PRIMARY KEY NOT NULL,
point_depart_trajet TEXT NOT NULL,
point_arrivee_trajet TEXT NOT NULL,
duree_trajet REAL NOT NULL,
numero_ligne INTEGER NOT NULL ,
CONSTRAINT fk_numero_ligne FOREIGN KEY (numero_ligne) REFERENCES Lignes(numero_ligne),
CONSTRAINT ck_duree_trajet  CHECK (duree_trajet >0 )
);


CREATE TABLE Clients(
numero_client INTEGER PRIMARY KEY NOT NULL ,
nom_client TEXT NOT NULL,
adresse_email_client TEXT NOT NULL
 
);

CREATE TABLE Vehicules( 
matricule_vehicule  INTEGER PRIMARY KEY NOT NULL,
type_vehicule TEXT NOT NULL ,
capacite_max_passagers_vehicule INTEGER NOT NULL ,
CONSTRAINT ck_capacite_max_passagers_vehicule  CHECK (capacite_max_passagers_vehicule >0),

 CONSTRAINT ck_type_vehicule CHECK                                                 
   (
      type_vehicule='Tramway' AND (capacite_max_passagers_vehicule <=132 ) 
   OR type_vehicule='Bus' AND (capacite_max_passagers_vehicule <=63 ) 
   OR type_vehicule='Navette' AND (capacite_max_passagers_vehicule <=32 ) 
   OR type_vehicule='Voiture' AND (capacite_max_passagers_vehicule <=5 ) 
   )
							 
);
 

CREATE TABLE Programmations(

matricule_vehicule INTEGER  NOT NULL,
numero_trajet INTEGER NOT NULL,

CONSTRAINT pk_matricule_vehicule_numero_trajet PRIMARY KEY (matricule_vehicule, numero_trajet),
CONSTRAINT fk_matricule_vehicule FOREIGN KEY (matricule_vehicule) REFERENCES Vehicules(matricule_vehicule),
CONSTRAINT fk_numero_trajet FOREIGN KEY (numero_trajet) REFERENCES Trajets(numero_trajet)
);
