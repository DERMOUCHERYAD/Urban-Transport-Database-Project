-- Affiche les noms et adresses e-mail des clients ayant effectué des réservations, ainsi que le nom de la ligne de trajet associée à chaque réservation.
DROP VIEW IF EXISTS Vue_Client_Reservation_Ligne;
CREATE VIEW Vue_Client_Reservation_Ligne AS
SELECT 
    C.nom_client,
    C.adresse_email_client,
    L.nom_ligne
FROM 
    Clients C
JOIN 
    Reservations R ON C.numero_client = R.numero_client
JOIN 
    Trajets T ON R.numero_trajet = T.numero_trajet
JOIN 
    Lignes L ON T.numero_ligne = L.numero_ligne;

 ---------------------------------------------------------------------------------------------------------------------------
 -- Afficher le nombre de réservation dans chaque mois
DROP VIEW IF EXISTS Vue_Reservations_Par_Mois;
CREATE VIEW Vue_Reservations_Par_Mois AS
SELECT
    strftime('%Y-%m', R.date_reservation) AS mois,
    COUNT(*) AS nombre_reservations
FROM
    Reservations R
GROUP BY
    strftime('%Y-%m', R.date_reservation);
	
--------------------------------------------------------------------------------------------------------------	
--Afficher les trajets programmées par un bus avec le matricule de chaque bus 
DROP VIEW IF EXISTS  Vue_Trajets_Avec_Bus_Programmes;
CREATE VIEW Vue_Trajets_Avec_Bus_Programmes AS
SELECT DISTINCT
    T.point_depart_trajet,
    T.point_arrivee_trajet,
    V.matricule_vehicule
FROM
    Trajets T,
    Programmations P,
    Vehicules V
WHERE
    T.numero_trajet = P.numero_trajet
    AND P.matricule_vehicule = V.matricule_vehicule
    AND V.type_vehicule = 'Bus';



