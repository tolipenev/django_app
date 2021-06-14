# Adrian App Django

Application for models created with Django, Bootstrap4 and Crispy-Forms

<br />

> Features

- SQLite DB
- Bootstrap4 CDN, Crispy-Forms(better login and register styles)
- User login/registration
- Admin panel with control over models
- Basic layout with sidebar navigation
- Deployment scripts: Docker, pipenv

<br />

## Deployment

<br />

> Command Line

```bash
$ # Get the code
$ git clone https://github.com/tolipenev/django_app.git
$ cd django-app
$
$ # Update Python and pip
$ python -m pip install --upgrade pip
$
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ virtualenv env
$ .\env\Scripts\activate
$
$ # Install modules
$ pip3 install -r requirements.txt
$
$ # Create tables
$ python manage.py makemigrations
$ python manage.py migrate
$
$ # Start the application (development mode)
$ python manage.py runserver # default port 8000
$
$ # Access the web app in browser: http://127.0.0.1:8000/
```

<br />

> Docker

The application can be easily executed in a docker container. The steps:

> Get the code

```bash
$ git clone https://github.com/tolipenev/django_app.git
$ cd django-app
```

> Start the app in Docker

```bash
$ sudo docker-compose pull && sudo docker-compose build && sudo docker-compose up -d
```

Visit `http://localhost:5005` in your browser. The app should be up & running.

<br />

## Credits & Links

### [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)

### [Django Bootstrap4](https://pypi.org/project/django-bootstrap4/)

<br />
