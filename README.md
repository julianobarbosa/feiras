

# feiras

feiras is a [REST Api][2] sample utilization. It is built with [Python][0] using the [Django Web Framework][1].

This project has the following basic apps:

* core (database definition for using on Django Admin)

## Installation

### Quick start

To set up a development environment quickly, first install Python 3. It
comes with virtualenv built-in. So create a virtual env by:

    1. `$ python3 -m venv feiras`
    2. `$ . feiras/bin/activate`

Install all dependencies:

    pip install -r requirements.txt

Run migrations:

    python manage.py migrate

Run import csv file

    python manage.py import_csv

Run tests

    python manage.py test

Create a super user

    python manage.py createsuperuser


### Detailed instructions

`/api/feiras/`
GET a list of all feiras
`http://127.0.0.1:8000/api/feiras/`

`/api/feiras/<id>/`
GET a detail for feiras

`/api/feiras/<id>/delete/`
Delete a Feiras, Login is required

`/api/feiras/<id>/edit/`
Edit a Feiras, Login as required

`/api/feiras/create/`
Create a Feiras, Login as required



Take a look at the docs for more information.

[0]: https://www.python.org/
[1]: https://www.djangoproject.com/
[2]: http://www.django-rest-framework.org/
