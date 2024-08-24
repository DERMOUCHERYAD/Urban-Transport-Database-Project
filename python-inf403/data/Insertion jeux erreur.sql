INSERT INTO Clients VALUES (1,'Moh','Moh@gmail.com');
INSERT INTO Clients VALUES (2, 'Ryad', 'Ryad@gmail.com');
INSERT INTO Clients VALUES (3, 'Yacine', 'Yacine@gmail.com');

INSERT INTO Lignes VALUES (100, 'A');
INSERT INTO Lignes VALUES (200, 'B');
INSERT INTO Lignes VALUES (300, 'C');

INSERT INTO Trajets VALUES (10, 'Akbou', 'Boudouaou',20,100);
INSERT INTO Trajets VALUES (20, 'Harrach', 'Bejaia',30,200);
INSERT INTO Trajets VALUES (30, 'Chavant', 'Boudouaou',45.5,300);

INSERT INTO Reservations VALUES (1000, '2024-04-13', '13:00',1,10);    /* Ajouter contrainte heure de depart et arrivee avec heure de reservation */
INSERT INTO Reservations VALUES (2000, '2024-04-10', '10:00',2,20);
INSERT INTO Reservations VALUES (3000, '2024-04-12', '13:00',3,30);

INSERT INTO Vehicules VALUES (1546,'Tramway',120);
INSERT INTO Vehicules VALUES (5464,'Bus',210);
INSERT INTO Vehicules VALUES (4640,'Voiture',20);

INSERT INTO Programmations VALUES (1546,20);
INSERT INTO Programmations VALUES (5464,10);
INSERT INTO Programmations VALUES (5464,30);

 