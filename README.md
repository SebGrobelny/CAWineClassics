California Wine Classics Site
=================
 
Welcome to Sebastian Grobelny's Django release of the [California Wine Classics website](#https://californiawineclassics.herokuapp.com/)!

Table of contents
=================

  * [California Wine Classics Site](#california-wine-classics-site)
  * [Table of contents](#table-of-contents)
  * [Installation](#installation)
  * [How to Run](#how-to-run)
  * [Design](#design)
    * [Framework Choice](#framework-choice)
    * [models.py](#models.py)
    * [views.py](#views.py)
    * [Output](#output)


 
Installation
============
For this project I used Django 1.11 and Pandas 0.21.0.If your system does not currently have these libraries pleasae install from the command line via pip.
```
pip install django
pip install pandas


```
 
 
 
How to Run
==========

Running the website from the commandline 
```
python manage.py runserver
```
Running my scripts to populate/update the inventory on the site. 

```
python df_inventory.py
python df_load_inventory.py
```

Design
======

Framework Choice
----------------
I chose to build the application in Django due largely to my familiarity with using Python as a server-side language. I previ Since Django offers the Model-View-Template I chose to construct my databases this way and to do my URL-routing in a cleaner more structured way than I had previously done using the Flask applicaiton. Django also offers a Templating language which I took full advantage of when rendering my database queries in still_wine.html and search.html. Djanog also offers a seperate settings.py file for configuring database connections which my app requires.

models.py
----------
I built my models around the requirements the winery had for the attributes in their Contact, and Request forms along with their Inventory requirements. Building Contact and Requests as forms would allow me to use their subsequent classes as ModelForm, which would allow me to save the forms a lot easier when they get submitted in the views.py.


views.py
----------
Here the routing from urls.py takes place and most of the views simply call render_template with the template the user is to get routed to, with the exception of still_wine, search and contact. These deal with form submission as a I mentioned before but do so in a very similiar way. They check if the request is POST and if it is the take the form on the page add the current time and then save. search checks if there is a GET request and if there is it runs a queries based on the attributes the user can search for including variety, AVA, and year. 

df_inventory.py
---------------
This script is necessary to preprocess since the files the winery uses are excel. Here I use a dataframe to extract the excel data and then simply export it to a CSV.

df_load_inventory.py
--------------------
Using the file created by df_inventory.py I then open the file again only this time loading it into my actual models from models.py. I do this locally but in order to see these changes in development on heroku I have to run it through heroku so that the models on there get updated.

```
heroku run python df_load_inventory.py
```

Databases
---------
The local Django project uses the sqlite3 instance listed in settings.py. On Heroku I created a hobby Postgres database that I then connect to my app by updating my settings.py file with DATABASES['default'].update(db_from_env) which takes the database that I designate as my primary database in Heroku. In this database I have all of the models I listed below as tables and I can track and view these databases either through dataclips or logging into the Django admin to view the models.


