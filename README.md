# Dili Management System

DMS is a system for collecting, sorting, retrieving and processing information of the residents in barangay which is used, or desired, by one of more managers, in the performance of their duties. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Installing

Get the latest version of the following:

* Install Python at https://www.python.org/downloads/ or with your operating system’s package manager.

* Download [get-pip.py](https://bootstrap.pypa.io/get-pip.py) to a folder on your computer. Open a command prompt window and navigate to the folder containing `get-pip.py`. Then run `python get-pip.py`. This will install pip.

* Install XAMPP at https://www.apachefriends.org/download.html.

* Install Git at https://git-scm.com/downloads or with your operating system’s package manager.

* Install Node at https://nodejs.org/en/.
Then run this command on your command prompt to install Bower `npm install -g bower`.

* Make a new folder and navigate to it using your command prompt.

* Then clone the project `git clone https://github.com/gilbertlcsndle/dms.git` and install it's dependencies `pip install tmp/requirements.txt && bower install`.

* Open the XAMPP and start Apache and MySQL.

* Go to localhost/phpmyadmin and create a database called 'dms'.

* Open your command prompt and apply the migration to the database `python manage.py migrate` and create a superuser `python manage.py createsuperuser`.

### Usage

* Open the XAMPP and start Apache and MySQL.

* By using your command prompt, go to the folder from where you clone the project `cd path/to/dms`.

* Then run the server `python manage.py runserver`.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

