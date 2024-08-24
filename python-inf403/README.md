# Projet Python/SQLite INF403

## Installation de l'environnement

### Windows

Installer Python 3 avec l'installeur disponible sur le site officiel:
* 64 bits (à préférer): https://www.python.org/ftp/python/3.9.2/python-3.9.2-amd64.exe
* 32 bits (au cas où): https://www.python.org/ftp/python/3.9.2/python-3.9.2.exe

Suivre les étapes de l'installeur. S'assurer que l'option "Ajouter à la
variable d'environnement PATH" est bien cochée.

### Linux

Dans un terminal:

    sudo apt install -y python3 libsqlite3-dev

Une fois Python installé, il faut installer les dépendances du projet (module
Python SQLite3). Dans un terminal, une fois dans le dossier extrait de
l'archive source:

    pip install --user -r requirements.txt

## Utilisation

Il est possible d'utiliser le code de ce projet de deux façons.

### Utilisation non-interactive

Dans un terminal:

    # Pour Linux
    python3 main.py

    # Pour Windows
    py main.py

Cela va exécuter la méthode main contenue dans le script `main.py`.

### Utilisation interactive

Dans un terminal, on peut exécuter `python3` (`py` sous Windows), puis entrer
le code nécessaire à l'exécution des différentes requêtes. C'est pratique pour
faire des tests rapides:

    $ python3
    Python 3.9.2 (default, Feb 20 2021, 00:00:00)
    [GCC 10.2.1 20201125 (Red Hat 10.2.1-9)] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import main
    >>> from utils import db
    >>> db_file = "data/voile.db"
    >>> conn = db.creer_connexion(db_file)
    >>> main.select_tous_les_bateaux(conn)
    (1, '2013-04-13', 'Pirate', 1005)
    (2, '2011-04-07', 'Pirate', 1006)
    (3, '2017-04-07', 'Classique', 1007)
    >>> 
### Utilisation d'un IDE

Vous pouvez travailler avec un IDE pour rendre plus facile la prise en main et production de code. Vous pouvez choisir votre IDE préféré.

Par exemple, sur PyCharm (version libre Community) : 
https://www.jetbrains.com/pycharm/ 
Pour faire la liaison entre PyCharm et Python:

Add Configuration:
![config1](./doc/img/config_pycharm1.png)
Add New Configuration -> Python:
![config2](./doc/img/config_pycharm2.png)
Pointer vers main.py:
![config3](./doc/img/config_pycharm3.png)
Clicker sur Play pour exécuter le programme:
![config4](./doc/img/config_pycharm4.png)
