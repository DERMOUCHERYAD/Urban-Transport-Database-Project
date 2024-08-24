# Urban-Transport-Database-Project
This repository focuses on a Database Development (BDD) project designed to manage urban public transportation systems. Using SQL for database management and Python for data analysis


# Python/SQLite Project INF403

## Environment Setup

### Windows

Install Python 3 using the installer available on the official website:
* 64-bit (preferred): [Download 64-bit Python 3.9.2](https://www.python.org/ftp/python/3.9.2/python-3.9.2-amd64.exe)
* 32-bit (if necessary): [Download 32-bit Python 3.9.2](https://www.python.org/ftp/python/3.9.2/python-3.9.2.exe)

Follow the installer steps. Ensure that the "Add Python to PATH" option is checked.

### Linux

In a terminal:

```bash
sudo apt install -y python3 libsqlite3-dev
```

Once Python is installed, install the project dependencies (Python SQLite3 module). In a terminal, navigate to the folder extracted from the source archive:

```bash
pip install --user -r requirements.txt
```

## Usage

You can use the code in this project in two ways.

### Non-Interactive Usage

In a terminal:

```bash
# For Linux
python3 main.py

# For Windows
py main.py
```

This will execute the `main` method contained in the `main.py` script.

### Interactive Usage

In a terminal, you can run `python3` (`py` on Windows), then enter the necessary code to execute various queries. This is useful for quick testing:

```python
$ python3
Python 3.9.2 (default, Feb 20 2021, 00:00:00)
[GCC 10.2.1 20201125 (Red Hat 10.2.1-9)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import main
>>> from utils import db
>>> db_file = "data/voile.db"
>>> conn = db.create_connection(db_file)
>>> main.select_all_boats(conn)
(1, '2013-04-13', 'Pirate', 1005)
(2, '2011-04-07', 'Pirate', 1006)
(3, '2017-04-07', 'Classic', 1007)
>>> 
```

### Using an IDE

You can work with an IDE to make coding easier and more efficient. You can choose your preferred IDE.

For example, on PyCharm (Community Edition):
[PyCharm](https://www.jetbrains.com/pycharm/) 

To link PyCharm with Python:

**Add Configuration:**
![config1](./doc/img/config_pycharm1.png)

**Add New Configuration -> Python:**
![config2](./doc/img/config_pycharm2.png)

**Point to `main.py`:**
![config3](./doc/img/config_pycharm3.png)

**Click Play to run the program:**
![config4](./doc/img/config_pycharm4.png)
