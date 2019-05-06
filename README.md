# FezComicRESTPy
A Django REST Framework REST API backend for FezComic. This project is prepared to work with MySQL and SQLite and containerized using Docker
## Table of Contents
- [Software Requirements Specification](#software-requirements-specification)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Credits](#credits)
- [License](#license)
## Software Requirements Specification
It will be uploaded at some point to serve as a reference.
## Installation
**Requirements:**
* [**Docker**](https://www.docker.com/)

***Additional requirements without using Docker:***
* [**Python 3**](https://www.python.org/downloads/)

**Steps without Docker:**

Install Python 3 and create a virtual environment
```
$ python3 -m venv env
```
Activate the virtual environment
```
$ source env/bin/activate
```
Download all dependencies
```
$ pip install -r requirements.txt
```
If you want to use SQLite, change ``managed = False`` to ``managed = True`` in **models.py** and then launch the following commands
```
$ python manage.py makemigrations FezComicServerPython
$ python manage.py migrate
```
If you prefer MySQL, run **init.sql** script on your MySQL server and make sure **settings.py** DATABASES configuration points to your server. By default it connects to ``localhost`` using the port ``3306``

**Steps using Docker:**

Simply build the container
```
$ docker-compose build
```

## Usage
**Usage without Docker**

Run a local server using your Python3 virtual environment
```
(env) $ python manage.py runserver
```

**Usage with Docker**

Run the container. If you chose **MySQL** this command also generates the required tables and role information when launched for the first time
```
$ docker-compose up
```

## Contributing
There is no plan regarding contributions in this project
## Credits
This web application has been developed by:

**Rafael Pernil Bronchalo** - *Software Architect and Developer* 

* [github/rafaelpernil](https://github.com/rafaelpernil2)

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
