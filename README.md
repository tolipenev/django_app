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

## Build steps

<br />

```bash
$ # Get the code
$ git clone https://github.com/tolipenev/django_app.git
$ cd django-app
$
$ # Update Python and pip
$ python -m pip install --upgrade pip
$
$ # Virtualenv modules installation
$ pipenv shell
$
$ # Install modules
$ pip3 install -r pip_requirements.txt
$
$ # Create tables
$ python manage.py makemigrations
$ python manage.py migrate
$
$ # Create Admin
$ python manage.py createsuperuser
$
$ # Start the application (development mode)
$ python manage.py runserver # default port 8000
$
$ # Access the web app in browser: http://127.0.0.1:8000/
$
$
$ # Issues
$ # If you get an error for not existing tables run this command(sometimes doesn't migrate correctly due to virtualenv)
$ python manage.py migrate --run-syncdb
```

<br />


The application can be easily executed in a docker container. The steps:


```bash
$ docker build . ## building the image
```

Visit `http://localhost:8000` in your browser. The app should be up & running.

<br />

## Credits & Links

### [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)

### [Django Bootstrap4](https://pypi.org/project/django-bootstrap4/)

<br />
