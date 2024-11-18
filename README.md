
# PyTradeGames

#### Video Demo:

https://youtu.be/u-eGv0J1bhk

## Objective:

Create a web application to work like a social network specifically for people who collect video games in physical media.  

A community where those people can connect, talk to each other, find new games and negotiate them, in order to improve their collection and make new friends.

## Description

This is a Final Project for CS50x.

You can clone and test it as you like (instructions below).

The project was idealized to work like a community where people can register their games and find other games to complete the collection.  

The user must create an account, providing an username, password and email. After that, he or she must register all of its games, so they can be visible to the other users.  

Once everything is ready, the user might search in the users page for the desired games and try to negotiate them with their owners.

After the conclusion of a trade, both users must finish it and rate the other from 1 to 5. The average rate score of a user is shown to everyone in the users page, this way, the community can identify worst users, and ignore them.

## Programming Languages

**Python3** was used for the back-end of the whole application with the **Flask** Framework. For the front-end, the language used was **JavaScript**, besides **HTML5** and **CSS3** (with support of **Bootstrap 5**), for markup and design. And for the Database it was a mix of **SQLite** and Python, using **SQLAlchemy**.

## Implementation

#### Back-end

The back-end was developed with Python3 and Flask, using the app factory pattern for the project layout, where and object 'app' is instantiated once, and it is passed to factories where it is changed and returned with some other function or feature.

The management of the configuration and environment files, and also the factories integration, was implemented with **DynaConf**.

In this project, flask extensions were used to implement the app factory, and by feature, they are:

- Login management (Flask-Login)
  - Manages user session, login and logout, restrict views to logged-in users and protect session cookies
- Admin Interface (Flask-Admin)
  - Creates an user-friendly interface for database management.
- Database ORM (Flask-SQLAlchemy)
  - Simplifies the implementation of SQLAlchemy
- Database Migrations (Flask-Migrate)
  - Handles SQLAlchemy migrations using Alembic to became almost automatic
  
#### Front-end

The front-end was designed using HTML5, CSS3 and, for a few features, JavaScript.

Along with CSS, it was used the Bootstrap 5 Framework, to make the webpage responsive, mobile-first, to any device.

JavaScript was used mostly to perform some dynamicaly interactions with the user, such as modal interfaces and automatic filters on tables.

#### Database

The database is implemented in SQLite but trough SQLAlchemy, a ORM (Object Relational Mapper) for Python.

It means that, while the database is still a SQLite Database, the creation and CRUD manipulation is implemented in Python, referencing each table as an object, which makes it much easier to develop. 

## Project Layout

For this project, the app factory pattern was used for the architecture and directory layout, which means that the package ```app.py``` only creates the app instance, and all the configuration and modifications of this object are made by other packages that are called by it, passing the object as a parameter.

It makes the whole project more maintainable, bug-safe, and scalable.

Using this pattern makes the decision to change any extension easier, because you just need to alter the code of that single extension, and the application will assume that new feature in the next time it initializes.

The layout may look scary at first, but it is very organized and easy to understand. Here is an example of how it looks after the installation and configuration.

```py
.
├── .venv    # The virtual environment created to run the application
├── instance    # The directory containing the databases
│   ├── database.db    # Each database the application has (developing, production, etc.)
├── PyTradeGames    # Package containing the actual application
│   ├── blueprints    # Contains all the project's blueprints
│   │   ├── webui    # Blueprints associated with user interface
│   │   │   ├── static    # Contains the static files of the views (css, images, js files)
│   │   │   ├── templates    # Contains the HTML files, preferably organized in folders by context
│   │   │   ├── views.py    # File with the implementation of the views
│   ├── ext    # Contains all the extensions that will receive the app object and modify it, adding more features.
│   │   ├── configuration    # It is where the Dynaconf extension is initialized
│   │   ├── database    # Contains the creation of the database models and the migrations
│   │   │   ├── migrations    # Flask-Migrate implementation
│   │   │   ├── models.py    # Database creation and initialization
│   │   ├── cli    # Definition of the CLI commands used especifically in the project
│   │   │   ├── models.py    # I created this file to serve information for database population
│   │   ├── admin    # Flask-Admin implementation
│   │   ├── authentication    # Flask-Login implementation
│   ├── app.py    # The code that creates the application and start the configuration
├── .env    # This holds variables such as the name of the app, the working environment (debug, production...), port, etc
├── requirements.txt    # A list of all the packages necessary to the application work
└── settings.toml    # This is to hold your application settings
```

_Every folder inside the PyTradeGames package has a \_\_init\_\_.py file, because it is necessary for the Python interpreter to recognize it as a package in order to import it from other packages, and, in more than some cases, it has the code to initialize a extension or a view._
_Also, when you run the application for the first time, it will automatically create inside every folder a \_\_pycache\_\_ where it keeps the cache created._

## Installation

First of all, you must clone this repository to your PC.  

Then you must create a virtual environment where you are gonna run the application. For it you must open the terminal on the main directory of the project and type

```shell
python -v venv .venv
```

This will create a /.venv on your project directory, now you should activate it

```shell
.venv\Scripts\Activate.ps1
```

With the virtualenv created and activated, now you must install all the packages needed for the application to work, using the python package manager 'pip'. All packages are listed on the file requirements.txt, and you might install them all with a single command.

```shell
pip install -U -r .\requirements.txt
```

Now we have everything we need to run the application, but before that, we must create and populate our database, for that, a few CLI commands were created to make things easier.

```shell
flask create-db
flask populate-db
```

An example datababe will be randomnly created for tests, and later it can be edited in the admin page or directly by SQLite queries.

Every user created will have the same username and password, and already a few games registered for each one.

All done! Now we just need to start the application by typing

```shell
flask run
```

And the terminal should return sometingh like this

```
 * Serving Flask app 'PyTradeGames/app.py'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.0.2:5000
Press CTRL+C to quit
```

It means your application is running on debug mode, and you can access it on both IP addresses provided.

The line 'Running on all addresses (0.0.0.0)' means that any device connected on the same network can acces the application.

## References

- Python -> https://www.python.org/
- HTML -> https://www.w3schools.com/html/
- CSS -> https://www.w3schools.com/css/
- JavaScript -> https://www.w3schools.com/js/
- SQL -> https://www.w3schools.com/sql/
- Flask -> https://flask.palletsprojects.com/en/stable/
- Flask-Admin -> https://flask-admin.readthedocs.io/en/latest/
- Flask-Login -> https://flask-login.readthedocs.io/en/latest/
- Flask-SQLAlchemy -> https://flask-sqlalchemy.readthedocs.io/en/stable/
- Flask-Migrate -> https://flask-migrate.readthedocs.io/en/latest/
- App Factory Pattern (Portuguese) -> https://www.youtube.com/watch?v=-qWySnuoaTM&t=5821s