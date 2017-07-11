# Dili Management System

DMS is a system for collecting, sorting, retrieving and processing information of the residents in barangay which is used, or desired, by one of more managers, in the performance of their duties. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Installing

Get the latest version of the following:

* Install Python at https://www.python.org/downloads/ or with your operating system’s package manager.

* Install XAMPP at https://www.apachefriends.org/download.html.

* Install Git at https://git-scm.com/downloads or with your operating system’s package manager.

* Install Node at https://nodejs.org/en/.
Then run this command on your command prompt to install Bower.

```
npm install -g bower
```

* Clone the project and to install it's dependencies.

```
mkdir code
cd code
git clone https://github.com/gilbertlcsndle/dms.git
pip install tmp/requirements.txt
bower install
```

* Open the XAMPP and start Apache and MySQL.

* Then apply the migration to the database and create a superuser.

```
python manage.py migrate
python manage.py createsuperuser
```

### Usage

* Open the XAMPP and start Apache and MySQL.

* By using your command prompt, cd to the directory where you clone the project.

```
cd code\dms
```

* Then run the server.

```
python manage.py runserver
```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

