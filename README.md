# searchTown App

## I - Introduction

### I-1 - Aim of the website
This app give information about French Town. In search field you can fill name or postal code of the town, 
the application will give some information. You can also search other towns around. 
You can find towns around given coordinates. 

### I-2 Requirements

You can directly go at the following [address](http://134.209.82.129), or:

#### Install Python and pip
sudo apt-get install python3-pip python3-dev libpq python3-testresources

#### Dependence for spatialite (an extension of SQLite for geographic tools)
sudo apt-get install binutils libproj-dev gdal-bin
sudo apt-get install libsqlite3-mod-spatialite
sudo apt-get install gdal-bin

#### For deployment on server you could need this
sudo apt-get install nginx
sudo apt install gunicorn

##### Set environment variable
In nano ~/.bashrc add:
export SECRET_KEY='your secret key'
export DJANGO_SETTINGS_MODULE="searchTown.settings"
export NPM_BIN_PATH="/usr/local/bin/npm"

#### Install node
sudo apt update
sudo apt install nodejs
sudo apt install npm
sudo npm install -g n
sudo n stable
npm install nodemon

### I-3 - Get started

1. Clone the project to your machine ```[git clone https://github.com/sebajou/searchTown]```
2. Navigate into the directory ```[cd searchTown]```
3. Source the virtual environment ```[python3 -m env]```
4. Activate venv ```[source env/bin/activate]```
5. Install the dependencies ```[pip3 install -r requirements.txt]```

### I-5 - How to run

1. Run this command to start the backend server for test in the ```[searchTown]``` directory: ```[python manage.py runserver]``` (You have to run this command while you are sourced into the virtual environment)
2. Use your navigator to display the app. Generally : ```[http://127.0.0.1:8000/]```

### I-6 - Website architecture

## II - Database

![Database architecture](media/searchTown_db.png)
*Database architecture*

## III - Backend

The backend is composed by Django and Django Rest Framework. DRF endpoint is requited by the module requests inside django.

## IV - API

Database is fill from data provide by french governmental api for administrative 
[division api-geo](https://api.gouv.fr/documentation/api-geo). 
To fill database run <em>fill_db_from_api.py</em>.

## V - Front

Front is render by Django with Tailwind css. 
