# About this document

This project is part of programming Boot Camp 2020 course.

## Prerequisites

- Visual Studio Code: https://code.visualstudio.com/download
- Python: https://www.python.org/downloads/
- Git: https://git-scm.com/downloads
- DBeaver: https://dbeaver.io/download/ (community version)

## Creating public key and adding it to GitHub

- https://www.inmotionhosting.com/support/website/ssh/how-to-add-ssh-keys-to-your-github-account/

## Installing pipenv

- https://pypi.org/project/pipenv/

## Creating virtual enviroment and installing Django

    pipenv install django

## Install some other cool stuff

    pipenv install tqdm
    pipenv install termcolor

## Entering virtualenv

    pipenv shell

**How to run Python commands without entering pipenv shell?**

## Make sure to add virtualenv as correct path in Virtual Studio Code

- Settings: https://dl.dropboxusercontent.com/s/i2164uoo5qbm7ct/2020-11-04_10-43-30.png

## Check that Django is installed correctly

    python -m django --version

## Create new Django application

    django-admin startproject bootcamp

## Start development server

    python manage.py runserver

**How to start dev server on other ports and bind to other IPs?**

## Create your application

    python manage.py startapp companydata

## Download data from AvoinData.fi

- Download CSV file from https://www.avoindata.fi/data/en_GB/dataset/yritykset/resource/4055cf20-65bb-432c-9ada-fb043e038383 and place it in bootcamp2020-demo/bootcamp as prhdata.csv

## Create required models in Django

Open companydata/models.py and replace it with following content

    from django.db import models
    from django.utils import timezone

    class Company(models.Model):

        class Meta:
            ordering = ['name']

        name = models.CharField(max_length=255, unique=True)
        business_id = models.CharField(max_length=255, unique=True)
        company_form = models.CharField(max_length=255)
        business_line = models.CharField(max_length=255)
        registration_date = models.CharField(max_length=255)
        address = models.CharField(max_length=255)
        postcode = models.CharField(max_length=255)
        city = models.CharField(max_length=255)

        

        created     = models.DateTimeField(editable=False)
        modified    = models.DateTimeField()

        def save(self, *args, **kwargs):
            ''' On save, update timestamps '''
            if not self.id:
                self.created = timezone.now()
            self.modified = timezone.now()
            return super(Company, self).save(*args, **kwargs)

        def __str__(self):
            return self.name

## Add your application to settings.py (project root folder)

Make sure your INSTALLED_APPS section looks like this:

    INSTALLED_APPS = [
        'companydata',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ]

## Create management command

- Create new directory bootcamp/companydata/management/commands and create new file within that directory csv2db.py
- Insert code below into csv2db.py

```python
from django.core.management.base import BaseCommand, CommandError
from companydata.models import Company
from django.conf import settings
from termcolor import cprint
import csv
import os
os.system('color')
from tqdm import tqdm

class Command(BaseCommand):
    help="Imports data from csv file to database"

    def handle(self, *args, **options):
        cprint(f'\nProcessing prh data, grab a coffee!', 'green', attrs=['reverse'])

        num_lines = sum(1 for line in open('prhdata.csv'))
        
        with tqdm(total=num_lines) as pbar:
            with open('prhdata.csv', encoding='utf-8') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=";")
                line_count = 0

                for row in csv_reader:
                    if line_count != 0:
                        Company.objects.update_or_create(name=row[0], business_id=row[1], company_form=row[2], business_line=row[3],
                                                    registration_date=row[5], address=row[6], postcode=row[7], city=row[8])
                        line_count+=1
                        pbar.update(1)
                    else:
                        line_count+=1
                pbar.close()
                cprint(f'\nProcessed {line_count} lines!', 'green', attrs=['reversed'])
```

## Run migrate command to create database tables

    python manage.py migrate && python manage.py makemigrations

## Check that database and tables actually exist using DBeaver

- This is how it should look like: https://dl.dropboxusercontent.com/s/7vpgf0hnju8kty6/dbeaver_2020-11-03_20-26-51.png

## Create root user

    python manage.py createsuperuser

## Install Django REST Framework

    pipenv install djangorestframework

## Adding Django REST framework to installed apps

Make sure to add "rest_framework" to list of installed apps.

## Create new file in companydata dir called serializers.py

Make sure file contents as displayed below:

    from rest_framework import serializers
    from . import models

    class CompanySerializer(serializers.ModelSerializer):
        class Meta:
            model = models.Company
            fields = ('name','business_id', 'company_form', 'business_line', 'registration_date', 'city', 'address', 'postcode')

## Create urls.py in companydata

Replace content of the file with following:

    from django.conf.urls import url
    from . import views

    urlpatterns = [
        url(r'/', views.CompanyList.as_view()),
    ]

## Modify views.py

Modify views.py so it looks as follows:

    from rest_framework import generics
    from . import serializers, models

    class CompanyList(generics.ListAPIView):
        serializer_class = serializers.CompanySerializer
        queryset = models.Company.objects.all()
 
## Add companydata urls to project's urls

Make sure project's urls.py file looks as follows:

Modify project's urls.py to look like this:

    """bootcamp URL Configuration

    The `urlpatterns` list routes URLs to views. For more information please see:
        https://docs.djangoproject.com/en/3.1/topics/http/urls/
    Examples:
    Function views
        1. Add an import:  from my_app import views
        2. Add a URL to urlpatterns:  path('', views.home, name='home')
    Class-based views
        1. Add an import:  from other_app.views import Home
        2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
    Including another URLconf
        1. Import the include() function: from django.urls import include, path
        2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
    """
    from django.contrib import admin
    from django.urls import path, include
    import companydata

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('api', include('companydata.urls')),
    ]

## Run runserver and check JSON output

 Once runserver is running check following url http://127.0.0.1:8000/api/?format=json and make sure it displays database data in JSON format.

 ## Create new Django app that will house actual interface

    python manage.py startapp interface


## Add interface app to installed apps

Make sure interface app is added to list of installed apps

## Create your first template

Create index.html file in interface/template (create template dir) with following contents:

    <html>
    <head>
        <title>Our simple Django application</title>
        <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/v/dt/jq-3.3.1/jszip-2.5.0/dt-1.10.22/b-1.6.5/b-html5-1.6.5/fh-3.1.7/r-2.2.6/sc-2.0.3/sb-1.0.0/sp-1.2.1/sl-1.3.1/datatables.min.css"/>
    
        <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/pdfmake/0.1.36/pdfmake.min.js"></script>
        <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/pdfmake/0.1.36/vfs_fonts.js"></script>
        <script type="text/javascript" src="https://cdn.datatables.net/v/dt/jq-3.3.1/jszip-2.5.0/dt-1.10.22/b-1.6.5/b-html5-1.6.5/fh-3.1.7/r-2.2.6/sc-2.0.3/sb-1.0.0/sp-1.2.1/sl-1.3.1/datatables.min.js"></script>
    </head>
    <body>

        <h1>List of registered companies of Finland</h1>

        <table id="companies" class="display">
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Business ID</th>
                    <th>Company form</th>
                    <th>Business line code</th>
                    <th>Registration date</th>
                    <th>City</th>
                    <th>Address</th>
                    <th>Postcode</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Row 1 Data 1</td>
                    <td>Row 1 Data 2</td>
                </tr>
                <tr>
                    <td>Row 2 Data 1</td>
                    <td>Row 2 Data 2</td>
                </tr>
            </tbody>
        </table>

    <script>
    $(document).ready(function() {
        $('#companies').DataTable( {
            "ajax": {
                "url": "/api/?format=json",
                "dataSrc": ""
            },
            "pageLength": 20,
            "columns": [
                { "data": "name" },
                { "data": "business_id" },
                { "data": "company_form" },
                { "data": "business_line" },
                { "data": "registration_date" },
                { "data": "city" },
                { "data": "address" },
                { "data": "postcode" }
            ]
        } );
    } );
    </script>

    </body>
    </html>

## Modify views.py for interface app

Make sure views.py in interface directory looks as follows:

    from django.shortcuts import render

    def index(request):
        return render(request,'index.html')

## Bind interface index view to project default url ('/')

Modify project's urls.py to look like this:

    """bootcamp URL Configuration

    The `urlpatterns` list routes URLs to views. For more information please see:
        https://docs.djangoproject.com/en/3.1/topics/http/urls/
    Examples:
    Function views
        1. Add an import:  from my_app import views
        2. Add a URL to urlpatterns:  path('', views.home, name='home')
    Class-based views
        1. Add an import:  from other_app.views import Home
        2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
    Including another URLconf
        1. Import the include() function: from django.urls import include, path
        2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
    """
    from django.contrib import admin
    from django.urls import path, include
    import companydata
    from interface.views import index

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('api', include('companydata.urls')),
        path('', index),
    ]

## Time to host this puppy! Let's install prerequisites for Heroku

- Install Heroku CLI: https://devcenter.heroku.com/articles/getting-started-with-python
- Register for Heroku free account: https://signup.heroku.com/dc
- Install gunicorn and django-heroku using pipenv

## Tell Heroku that this is a Python project

Create new file in repository root called Procfile (notice, no extension) with following content:

    web: gunicorn bootcamp.wsgi

## Modify Django settings so it's Heroku aware

Add the following import statement to the top of settings.py:

    import django_heroku

Then add the following to the bottom of settings.py:

    # Activate Django-Heroku.
    django_heroku.settings(locals())

## Login to Heroku via cli

    heroku login

Running this command will open a new browser window

## Create Heroku instance

    heroku create

## Create WSGI file

Create new file called wsgi.py inside bootcamp folder with following contents:

    import os
    from django.core.wsgi import get_wsgi_application

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bootcamp.settings")
    application = get_wsgi_application()

## Create requirements.txt for Heroku

    pip freeze >requirements.txt

# Set correct buildpack

    heroku buildpacks:clear if necessary
    heroku buildpacks:set https://github.com/timanovsky/subdir-heroku-buildpack
    heroku buildpacks:add heroku/python
    heroku config:set PROJECT_PATH=bootcamp/

## Commit your code (we're almost there)

    git add *
    git commit -av -m "Initial real commit"
    git push
    git push heroku main
    # Prey and cross your fingers!

## SUCCESS

Now you should be able to see your new shiney web app url: https://dl.dropboxusercontent.com/s/ohn0ux5jjs22952/Code_2020-11-03_22-43-18.png

## Next time...databases, heroku, security...oh my! :)
