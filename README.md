# Backend with Django
A Hackpack by VandyHacks

Django is a Python-based free and open-source web framework,
which follows the model-template-view architectural pattern.
This hackpack provides you with the building blocks for a **custom
API** in Django using `djangorestframework`.

Django REST Framework is a free and open-source Python library
that facilitates the easier creation of APIs with Django as it
provides important classes and functions that are specific to
RESTApis.

## What is an API? Do I need one?

An API—or Application Programming Interface—is a set of functions
that enables you to access/mutate your application's data.

The main concept is: you have a database with data, so you create
a *server* to access that data.

There are 4 main operations you can have in a RESTful API:
- `GET` enables you to access your database and returns data based on a query (i.e., search terms)
- `POST` enables you to create a new piece of data in your database,
according to the model (schema) you specified.
- `PUT` enables you to modify data that *that already exist* on the database
- `DELETE` enables you to delete data from your database

## Basic Django Architecture

### Models

Everything starts by the definition of the **models**, that is the
architecture of the data you will store in your database. For example:
```python
class Person(models.Model):
    
    name = models.CharField(max_length=100)
    # more fields here

```
`Person` is a `Model` (inherited by the official Django class) that has a name of type `CharField`
(think of it as a string). This will create a *table* named "People" (Well this is not the exact name, but
 that's what it means.) which will have one column named "Name" and we can 
 enter People objects with a field `name`.
 
### Views

Views are the functions that we define to access or mutate our data. This is
where you define your `get`/`post`/... methods and how they work.

It is important that we choose *how to access our data* and *in what form* we return them. For returning
data we are going to use something called **JSON Format**. Think of JSON objects as Python
dictionaries. For example:
```python
{
    "name": "John"
}
```
The above object can be a Person according to the model definition above.

### URLs

All those amazing functions you wrote will be accessible through a URL. For example when you access
`http://localhost:8000/artists/` in your browser, you automatically perform a `GET` request
to that URL. In your project, you'll be able to programmatically specify what type of request
you make (or you could use a tool such as [Postman](https://www.getpostman.com/)).

## How to use this Hackpack

1. Click the *Use Template* button on this repo. This will automatically create your own repository
that uses this source code.
2. `git clone` the repository to your local machine
3. `cd` into the `hackpack` directory
4. Create a new python [virtual environment](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/).
5. `source <env_name>/bin/activate` to activate your environment
6. `pip install -r requirements.txt` to install dependencies
7. `python manage.py makemigrations && python manage.py migrate` to migrate the database
8. Run your server with `python manage.py runserver`.

You're all set!

## Requirements

- You should have Python installed to use this hackpack. You can find it [here](https://www.python.org).