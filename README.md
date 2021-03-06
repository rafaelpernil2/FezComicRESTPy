# FezComicRESTPy
A Django REST Framework REST API backend for FezComic. This project is prepared to work with MySQL and SQLite and containerized using Docker. For SQLite use ``master`` branch and for MySQL use ``mysql`` branch
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
``` shell
$ python3 -m venv env
```
Activate the virtual environment
``` shell
$ source env/bin/activate
```
Download all dependencies
``` shell
$ pip install -r requirements.txt
```
If you want to use SQLite, change ``managed = False`` to ``managed = True`` in **models.py** and then launch the following commands
``` shell
$ python manage.py makemigrations FezComicServerPython
$ python manage.py migrate
```
Or if you prefer to use MySQL, run **init.sql** script on your MySQL database and then create a file named ``.env`` with your database configuration:
``` properties
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER=yourDatabaseUser
MYSQL_ROOT_PASSWORD=yourDatabaseRootPassword
MYSQL_PASSWORD=yourDatabasePassword
```
This file is used by [**theskumar/python_dotenv**](https://github.com/theskumar/python-dotenv) library to add those variables to the environment, which **settings.py** consumes.

*Notes:*

- You may use [**.env.sample**](.env.sample) as a reference

- Do not rename ``MYSQL_USER``, ``MYSQL_ROOT_PASSWORD`` and ``MYSQL_PASSWORD`` if you are using Docker. Those names are reserved by MySQL Docker image.


**Steps using Docker:**

Simply build the container
``` shell
$ docker-compose build
```

## Usage
**Usage without Docker**

Run a local server using your Python3 virtual environment
``` shell
(env) $ python manage.py runserver
```

**Usage with Docker**

If you prefer to use MySQL, create a file named ``.env`` with your database configuration:
``` properties
MYSQL_HOST=db
MYSQL_PORT=3306
MYSQL_USER=yourDatabaseUser
MYSQL_ROOT_PASSWORD=yourDatabaseRootPassword
MYSQL_PASSWORD=yourDatabasePassword
```
This file is used by [**theskumar/python_dotenv**](https://github.com/theskumar/python-dotenv) library to add those variables to the environment, which **settings.py** consumes.

*Notes:*

- You may use [**.env.sample**](.env.sample) as a reference

- Make sure your ``MYSQL_HOST`` is set to ``db``. Otherwise, Django won't be able to locate the autogenerated database. That is because ``db`` is the name of the database service defined at **docker-compose.yml**

- Do not rename ``MYSQL_USER``, ``MYSQL_ROOT_PASSWORD`` and ``MYSQL_PASSWORD`` if you are using Docker. Those names are reserved by MySQL Docker image.


Run the container.

``` shell
$ docker-compose up
```
Also, if you want to build, run and leave it as a background process, run the following command
``` shell
$ docker-compose up --build --detach
```


## Contributing
There is no plan regarding contributions in this project
## Credits
This web application has been developed by:

**Rafael Pernil Bronchalo** - *Software Architect and Developer*

* [github/rafaelpernil2](https://github.com/rafaelpernil2)

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
