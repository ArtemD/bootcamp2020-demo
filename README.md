# About this document

This project is part of programming Boot Camp 2020 course.

## Table of content

- [About this document](#about-this-document)
  - [Table of content](#table-of-content)
- [Prerequisites](#prerequisites)
  - [Creating public key and adding it to GitHub](#creating-public-key-and-adding-it-to-github)
    - [Creating SSH keys](#creating-ssh-keys)
    - [Adding public key to GitHub](#adding-public-key-to-github)
  - [Installing pipenv](#installing-pipenv)
  - [Creating virtual environment and installing Django](#creating-virtual-environment-and-installing-django)
  - [Install some other cool stuff](#install-some-other-cool-stuff)
  - [Entering virtualenv](#entering-virtualenv)
  - [Make sure to add virtualenv as correct path in Virtual Studio Code](#make-sure-to-add-virtualenv-as-correct-path-in-virtual-studio-code)
  - [Check that Django is installed correctly](#check-that-django-is-installed-correctly)
- [Working with Django](#working-with-django)
  - [Create new Django application](#create-new-django-application)
  - [Start development server](#start-development-server)
  - [Create your application](#create-your-application)
  - [Download data from AvoinData.fi](#download-data-from-avoindatafi)
  - [Create required models in Django](#create-required-models-in-django)
  - [Add your application to settings.py (project root folder)](#add-your-application-to-settingspy-project-root-folder)
  - [Create management command](#create-management-command)
  - [Run migrate command to create database tables](#run-migrate-command-to-create-database-tables)
  - [Check that database and tables actually exist using DBeaver](#check-that-database-and-tables-actually-exist-using-dbeaver)
  - [Create administrator user](#create-administrator-user)
  - [Adding models to admin view](#adding-models-to-admin-view)
  - [Check that models are now displayed in admin interface](#check-that-models-are-now-displayed-in-admin-interface)
  - [Install Django REST Framework](#install-django-rest-framework)
  - [Adding Django REST framework to installed apps](#adding-django-rest-framework-to-installed-apps)
  - [Create new file in companydata dir called serializers.py](#create-new-file-in-companydata-dir-called-serializerspy)
  - [Create urls.py in companydata](#create-urlspy-in-companydata)
  - [Modify views.py](#modify-viewspy)
  - [Add companydata urls to project's urls](#add-companydata-urls-to-projects-urls)
  - [Run csv2db command](#run-csv2db-command)
  - [View data in DBeaver using SQL command Select](#view-data-in-dbeaver-using-sql-command-select)
  - [Checking that our API works correctly](#checking-that-our-api-works-correctly)
  - [Create new Django app that will house actual interface](#create-new-django-app-that-will-house-actual-interface)
  - [Add interface app to installed apps](#add-interface-app-to-installed-apps)
  - [Create your first template](#create-your-first-template)
  - [Modify views.py for interface app](#modify-viewspy-for-interface-app)
  - [Bind interface index view to project default url ('/')](#bind-interface-index-view-to-project-default-url-)
  - [Time to host this puppy! Let's install prerequisites for Heroku](#time-to-host-this-puppy-lets-install-prerequisites-for-heroku)
  - [Tell Heroku that this is a Python project](#tell-heroku-that-this-is-a-python-project)
  - [Modify Django settings so it's Heroku aware](#modify-django-settings-so-its-heroku-aware)
  - [Login to Heroku via cli](#login-to-heroku-via-cli)
  - [Create a .gitignore file so in future we don't commit temp files to our repo](#create-a-gitignore-file-so-in-future-we-dont-commit-temp-files-to-our-repo)
  - [Time to add our code to git](#time-to-add-our-code-to-git)
- [Publishing your code to Heroku cloud service](#publishing-your-code-to-heroku-cloud-service)
  - [Create Heroku instance](#create-heroku-instance)
  - [Move Pipfile and Pipfile.lock to bootcamp directory](#move-pipfile-and-pipfilelock-to-bootcamp-directory)
  - [Set correct buildpack for our project](#set-correct-buildpack-for-our-project)
  - [Push your code to heroku](#push-your-code-to-heroku)
  - [Create a free account and initialize a free database](#create-a-free-account-and-initialize-a-free-database)
  - [Connecting to Heroku database](#connecting-to-heroku-database)
  - [Setting correct PostgreSQL credentials in a secure manner](#setting-correct-postgresql-credentials-in-a-secure-manner)
  - [Pushing to Heroku](#pushing-to-heroku)
  - [Creating PostgreSQL database structure and populating it with data](#creating-postgresql-database-structure-and-populating-it-with-data)
  - [Push PostgreSQL enabled version of our application to Heroku](#push-postgresql-enabled-version-of-our-application-to-heroku)
  - [Make sure that it works](#make-sure-that-it-works)
- [Publishing your code on GitHub & setting up CI](#publishing-your-code-on-github--setting-up-ci)
  - [Creating your private repository](#creating-your-private-repository)
  - [Setting up continues integration over at Heroku](#setting-up-continues-integration-over-at-heroku)
- [Project files and directories](#project-files-and-directories)

# Prerequisites

- Visual Studio Code: https://code.visualstudio.com/download
- Python: https://www.python.org/downloads/
- Git: https://git-scm.com/downloads
- DBeaver: https://dbeaver.io/download/ (community version)

## Creating public key and adding it to GitHub

- Read more about the process here: https://www.inmotionhosting.com/support/website/ssh/how-to-add-ssh-keys-to-your-github-account/

### Creating SSH keys

![](https://dl.dropboxusercontent.com/s/x5i546jgsd3go8x/2020-11-08_10-39-27.gif)

### Adding public key to GitHub

![](https://dl.dropboxusercontent.com/s/g5lfcqr08zmfdbk/2020-11-08_10-56-32.gif)


## Installing pipenv

![](https://dl.dropboxusercontent.com/s/ljxlumw0k0p57wc/2020-11-08_10-42-09.gif)

- Read more about pipenv: https://realpython.com/pipenv-guide/

## Creating virtual environment and installing Django

![](https://dl.dropboxusercontent.com/s/9jdstpdkk67ubow/2020-11-08_10-43-49.gif)


```console
pipenv install django
```

- Read more about Django: https://djangostars.com/blog/why-we-use-django-framework/

## Install some other cool stuff

![](https://dl.dropboxusercontent.com/s/2fti16wnms1je4l/2020-11-08_10-45-39.gif)

```console
pipenv install tqdm
pipenv install termcolor
```

- Read more about tqdm here: https://github.com/tqdm/tqdm
- Read more about termcolor here: https://pypi.org/project/termcolor/

## Entering virtualenv

![](https://dl.dropboxusercontent.com/s/ppdywfh38g10s71/2020-11-08_10-47-01.gif)


```console
pipenv shell
```

:warning: Remember that you need to always make sure that you're working within virtual enviroment before running any ```python manage.py``` commands. :warning: 

- You can read more about pipenv shell here: https://pipenv-fork.readthedocs.io/en/latest/basics.html


## Make sure to add virtualenv as correct path in Virtual Studio Code

![](https://dl.dropboxusercontent.com/s/01hssf8kqgc2nuc/2020-11-11_20-21-27.gif)

- You can read more about Visual Studio Code Python settings here: https://olav.it/2017/03/04/pipenv-visual-studio-code/

## Check that Django is installed correctly

![](https://dl.dropboxusercontent.com/s/vgry1xjlaza31wx/2020-11-08_11-43-20.gif)

```console
python -m django --version
```

- If you're having issues with Django installation, please look into excellent installation documentation: https://docs.djangoproject.com/en/3.1/topics/install/

# Working with Django

## Create new Django application

![](https://dl.dropboxusercontent.com/s/ryf30e69cfgk9q7/2020-11-07_10-01-01.gif)

```console
django-admin startproject bootcamp
```

- You can read more about project directory structure here: https://djangobook.com/mdj2-django-structure/

## Start development server

![](https://dl.dropboxusercontent.com/s/mnp226xa69ip0ez/2020-11-07_10-09-45.gif)

```console
python manage.py runserver
```

You can stop runserver any time by pressing Ctrl+C

If you see error similar to one below then it means you're not using virtual enviroment. You can fix it by running ```pipenv shell```.

```console
ImportError: Couldn't import Django. Are you sure it's installed and available on your PYTHONPATH environment variable? 
Did you forget to activate a virtual environment?
```

- You can read more about Django development server here: https://docs.djangoproject.com/en/3.1/ref/django-admin/#runserver 


## Create your application

![](https://dl.dropboxusercontent.com/s/ei7udt7i4pxt9bc/2020-11-07_10-16-15.gif)

```console
python manage.py startapp companydata
```

Make sure that 'companydata' directory is created within bootcamp folder.

- Read more about application structure here: https://docs.djangoproject.com/en/3.1/ref/applications/


## Download data from AvoinData.fi

![](https://dl.dropboxusercontent.com/s/23dad2gcdhvz6yy/2020-11-07_10-39-49.gif)

- Download CSV file from https://www.avoindata.fi/data/en_GB/dataset/yritykset/resource/4055cf20-65bb-432c-9ada-fb043e038383 and place it in bootcamp directory as prhdata.csv
- You can read more about parsing CSV files in Python here: https://realpython.com/python-csv/

## Create required models in Django

![](https://dl.dropboxusercontent.com/s/56ie6lzm0wurwzy/2020-11-07_10-41-21.gif)

Open companydata/models.py and replace it with following content

```python
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
```

- You can read more about models here: https://docs.djangoproject.com/en/3.1/topics/db/models/

## Add your application to settings.py (project root folder)

![](https://dl.dropboxusercontent.com/s/rfrfple55tdypi4/2020-11-07_10-45-06.gif)

Make sure your INSTALLED_APPS section looks like this:

```python
INSTALLED_APPS = [
    'companydata',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

- You can read more about INSTALLED_APP here: https://docs.djangoproject.com/en/3.1/ref/settings/#installed-apps

## Create management command

![](https://dl.dropboxusercontent.com/s/0frdemsfiy3ungd/2020-11-07_10-47-37.gif)

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

- You can read more about creating manage.py commands here: https://docs.djangoproject.com/en/3.1/howto/custom-management-commands/

## Run migrate command to create database tables

![](https://dl.dropboxusercontent.com/s/ysw6m82gn8rbp95/2020-11-07_10-49-54.gif)

```console
python manage.py makemigrations && python manage.py migrate
```

- You can learn more about migrations here: https://docs.djangoproject.com/en/3.1/topics/migrations/

## Check that database and tables actually exist using DBeaver

![](https://dl.dropboxusercontent.com/s/jrjbwp48nnvzbsw/2020-11-07_10-53-32.gif)

## Create administrator user

![](https://dl.dropboxusercontent.com/s/i71ptsxbhmddw3f/2020-11-07_10-55-48.gif)

```console
python manage.py createsuperuser
```

- You can read more about user management in Django here: https://docs.djangoproject.com/en/3.1/ref/django-admin/#createsuperuser

## Adding models to admin view

![](https://dl.dropboxusercontent.com/s/683oefj0ux7s3e7/2020-11-07_11-00-17.gif)

Open companydata/admin.py and replace it with following content:

```python
from django.contrib import admin
from django.db import models

from companydata.models import Company

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name','business_id','city',)
    search_fields = ['name','business_id', ]
    list_filter = ('city',)

admin.site.register(Company, CompanyAdmin)
```

- You can read more about exposing models to admin interface here: https://docs.djangoproject.com/en/3.1/ref/contrib/admin/#module-django.contrib.admin

## Check that models are now displayed in admin interface

![](https://dl.dropboxusercontent.com/s/jm87olajos1p4ga/2020-11-07_11-03-15.gif)

## Install Django REST Framework

![](https://dl.dropboxusercontent.com/s/lhqd3yvj1lamxm2/2020-11-07_11-06-28.gif)

```console
pipenv install djangorestframework
```

- You can read about Django REST Framework here: https://www.django-rest-framework.org/

## Adding Django REST framework to installed apps

![](https://dl.dropboxusercontent.com/s/bm6y5hyzh4jrh3u/2020-11-07_11-08-38.gif)

Make sure to add "rest_framework" to list of installed apps.

## Create new file in companydata dir called serializers.py

![](https://dl.dropboxusercontent.com/s/kmr9l70qp87ffwp/2020-11-07_11-11-42.gif)

Make sure file contents as displayed below:

```python
from rest_framework import serializers
from . import models

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = ('name','business_id', 'company_form', 'business_line', 'registration_date', 'city', 'address', 'postcode')
```

- You can learn more about serializers here: https://www.django-rest-framework.org/api-guide/serializers/

## Create urls.py in companydata



Replace content of the file with following:

![](https://dl.dropboxusercontent.com/s/vre27f7kwbw3ax4/2020-11-07_11-15-39.gif)

```python
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'/', views.CompanyList.as_view()),
]
```

- You can read more about urls in Django here: https://docs.djangoproject.com/en/3.1/topics/http/urls/

## Modify views.py

![](https://dl.dropboxusercontent.com/s/4o5ouqt37lg3qjk/2020-11-07_11-17-33.gif)

Modify views.py so it looks as follows:

```python
from rest_framework import generics
from . import serializers, models

class CompanyList(generics.ListAPIView):
    serializer_class = serializers.CompanySerializer
    queryset = models.Company.objects.all()
```

- Read more about views here: https://docs.djangoproject.com/en/3.1/topics/http/views/

## Add companydata urls to project's urls

![](https://dl.dropboxusercontent.com/s/qr7wd37diomxgr8/2020-11-07_11-19-08.gif)

Modify project's urls.py to look like this:

```python
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
```

## Run csv2db command

![](https://dl.dropboxusercontent.com/s/a3oozf757esjbzt/2020-11-07_11-24-19.gif)

Run following command for a while (so we can populate our database with some data) and feel free to cancel it (pressing ctrl+C) any time. Due to CSV file not being sanitized program will abort at some point anyway.

```console
python manage.py csv2db
```

- You can read more about starting and stopping programs in terminal here: https://www.howtogeek.com/howto/ubuntu/keyboard-shortcuts-for-bash-command-shell-for-ubuntu-debian-suse-redhat-linux-etc/

## View data in DBeaver using SQL command Select

![](https://dl.dropboxusercontent.com/s/s2020krur55nfyf/2020-11-07_11-28-05.gif)

## Checking that our API works correctly

![](https://dl.dropboxusercontent.com/s/p7pcsqp06eoo3ly/2020-11-07_11-29-51.gif)

Once runserver is running check following url http://127.0.0.1:8000/api/?format=json and make sure it displays database data in JSON format.

## Create new Django app that will house actual interface

![](https://dl.dropboxusercontent.com/s/juugfvau46x3nit/2020-11-07_11-31-02.gif)

```console
python manage.py startapp interface
```

## Add interface app to installed apps

![](https://dl.dropboxusercontent.com/s/9n222rawg50xtt7/2020-11-07_11-31-42.gif)

Make sure interface app is added to list of installed apps

## Create your first template

![](https://dl.dropboxusercontent.com/s/b5p5dcz51jp9hir/2020-11-07_11-33-05.gif)

Create index.html file in interface/template (create template dir) with following contents:

```html
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
```

- You can learn more about amazing word of Django templates here: https://docs.djangoproject.com/en/3.1/topics/templates/

## Modify views.py for interface app

![](https://dl.dropboxusercontent.com/s/0rfl8d6oltc3yei/2020-11-07_11-34-17.gif)

Make sure views.py in interface directory looks as follows:

```python
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
```

## Bind interface index view to project default url ('/')

![](https://dl.dropboxusercontent.com/s/iixfvf1hk9ycc82/2020-11-07_11-35-11.gif)

Modify project's urls.py to look like this:

```python
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
```

## Time to host this puppy! Let's install prerequisites for Heroku

![](https://dl.dropboxusercontent.com/s/m2e73atezky5zoc/2020-11-07_11-37-52.gif)

![](https://dl.dropboxusercontent.com/s/vbz7ng8kbi0g3lj/2020-11-07_11-38-28.gif)

![](https://dl.dropboxusercontent.com/s/6digindsp62rp4c/2020-11-07_11-39-23.gif)

- Install Heroku CLI: https://devcenter.heroku.com/articles/getting-started-with-python
- Register for Heroku free account: https://signup.heroku.com/dc
- Install gunicorn and django-heroku using pipenv

## Tell Heroku that this is a Python project

![](https://dl.dropboxusercontent.com/s/pk9cq39yh96bmt3/2020-11-07_12-03-17.gif)

Create new file in repository root called Procfile (notice, no extension) with following content:

```
web: gunicorn bootcamp.wsgi --log-file - --log-level debug
```

- You can dive into Procfile secrets here: https://devcenter.heroku.com/articles/procfile

## Modify Django settings so it's Heroku aware

![](https://dl.dropboxusercontent.com/s/f2kxkhcwyql8us4/2020-11-07_11-43-12.gif)

Add the following import statement to the top of settings.py:

```python
import django_heroku
```

Then add the following to the bottom of settings.py:

```python
# Activate Django-Heroku.
django_heroku.settings(locals())
```

- You can read more about django-heroku package here: https://pypi.org/project/django-heroku/

## Login to Heroku via cli

![](https://dl.dropboxusercontent.com/s/ki3cd64pnr5vuib/2020-11-07_11-46-28.gif)

```console
heroku login
```

Running this command will open a new browser window.

- You can read more about heroku cli commands here: https://devcenter.heroku.com/articles/heroku-cli-commands


## Create a .gitignore file so in future we don't commit temp files to our repo

![](https://dl.dropboxusercontent.com/s/sh0cpa1m1v2v8k8/2020-11-07_11-55-32.gif)


```
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
.pybuilder/
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
#   For a library or package, you might want to ignore these files since the code is
#   intended to run in multiple environments; otherwise, check them in:
# .python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# PEP 582; used by e.g. github.com/David-OConnor/pyflow
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# Visual Studio Code related files
.vscode/
*.code-workspace
.history/

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/
```

- You can read more about gitignore files here: https://www.pluralsight.com/guides/how-to-use-gitignore-file

## Time to add our code to git

![](https://dl.dropboxusercontent.com/s/2f6duqpsleu3mkf/2020-11-07_11-57-18.gif)

```console
git init
git add .
git commit -m "Initial commit"
```

# Publishing your code to Heroku cloud service

## Create Heroku instance

![](https://dl.dropboxusercontent.com/s/pardbzfpydpa9sv/2020-11-07_11-49-13.gif)

```console
heroku create
```

*Make sure to run it from the root folder*.

- You can learn more about creating apps using heroku cli here: https://devcenter.heroku.com/articles/creating-apps

## Move Pipfile and Pipfile.lock to bootcamp directory

![](https://dl.dropboxusercontent.com/s/gyoor7vyell4322/2020-11-08_20-46-02.gif)

```console
# Run exit command only if you are already within pipenv shell
exit
pipenv --rm
mv Pipfile* bootcamp/
pipenv install
pipenv shell
```

:warning: Using commands above we're destroying virtual enviroment we have created and we re-create it under bootcamp directory.  This is done for following reasons :warning:

- We created virtual enviroment only for django, but we couldn't place Pipfile and Pipfile.lock in directory that didn't exist (we need ```pipenv install django``` in order to run ```django-admin createproject bootcamp```).
- Heroku expects Pipfile within Django project directory.
- In our BootCamp course we'll have different projects in the parent folder so it makes sense that django specific Pipfile and Pipfile.lock are placed in the bootcamp directory.

## Set correct buildpack for our project

![](https://dl.dropboxusercontent.com/s/wrlbzjbrcui90on/2020-11-07_11-59-49.gif)

```console
heroku buildpacks:set https://github.com/timanovsky/subdir-heroku-buildpack
heroku buildpacks:add heroku/python
heroku config:set PROJECT_PATH=bootcamp/
```

Make sure to run this command in the root folter (same folder where there is bootcamp folder and nothing else).

- You can learn more about buildpacks here: https://devcenter.heroku.com/articles/buildpacks and about subdir-heroku-buildpack here: https://github.com/timanovsky/subdir-heroku-buildpack

## Push your code to heroku

```console
git push
git push heroku main:master
# Prey and cross your fingers!
```

:warning: Replace main with the name of your branch if your branch is not named "main". :warning:

Now you should be able to see your new shiney web app url: https://dl.dropboxusercontent.com/s/ohn0ux5jjs22952/Code_2020-11-03_22-43-18.png

- You can read more about using Git with Heroku here: https://devcenter.heroku.com/articles/git

## Create a free account and initialize a free database

Register a free account over at [elephantsql.com](https://customer.elephantsql.com/signup)

![](https://dl.dropboxusercontent.com/s/rcpxxe8x0loaek0/2020-11-08_20-57-24.gif)

- You can learn more about PostgreSQL here: http://postgresguide.com/
- You can see how PostgreSQL compares to other databases here: https://www.digitalocean.com/community/tutorials/sqlite-vs-mysql-vs-postgresql-a-comparison-of-relational-database-management-systems

## Connecting to Heroku database

![](https://dl.dropboxusercontent.com/s/etx3a6761aykrvj/2020-11-08_21-42-20.gif)

```console
pipenv install dj-database-url
```

Then add the following to the bottom of settings.py:

```python
# Adding support for database urls
import dj_database_url
import os

DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

if (os.environ.get('DB_URL')):
    DATABASES['default'] = dj_database_url.parse(os.environ.get('DB_URL'))
else:
    DATABASES['default'] = dj_database_url.parse(f'sqlite:///{BASE_DIR}/db.sqlite3')
```

Make sure to use database URL from EelephantSQL. You can use "copy database URL" icon found near the URL itself (see screenshot below):

![](https://dl.dropboxusercontent.com/s/is1sayt9ai92zif/brave_2020-11-08_20-58-42.png)

## Setting correct PostgreSQL credentials in a secure manner

![](https://dl.dropboxusercontent.com/s/yynia9pvqrohzoh/2020-11-08_21-44-33.gif)

:warning: Please note that your PostgreSQL URL will differ from mine as it's unique for every single user, host and so on. :warning:

```python
heroku config:set DB_URL='postgres://cfzfsdrn:2MHu9Uv8BHdZD3CKP7HsZhXdkgUWt6Wg@balarama.db.elephantsql.com:5432/cfzfsdrn'
```

## Pushing to Heroku

![](https://dl.dropboxusercontent.com/s/7r1jbbcnlw6yk43/2020-11-08_21-15-35.gif)

```console
git add ../
git commit -m "Added support for new database"
git push heroku main:master
```

## Creating PostgreSQL database structure and populating it with data

![](https://dl.dropboxusercontent.com/s/qy1wdnjcqy46sk0/2020-11-08_21-54-37.gif)

```console
export DB_URL='postgres://cfzfsdrn:2MHu9Uv8BHdZD3CKP7HsZhXdkgUWt6Wg@balarama.db.elephantsql.com:5432/cfzfsdrn'
python manage.py migrate
python manage.py createsuperuser
python manage.py csv2db
unset DB_URL
```

Commands listed above achieve following:

- Switch to using production SQL server (by setting DB_URL variable locally)
- Create database structure based on our models
- Create admin user
- Run csv2db and populate database with data from CSV file (notice that I pressed Ctrl+C since I didn't want to wait for all data to be processed)
- Destroy local variable using unset so Django will revert to using SQLite

You can read more about working with variables in terminal here: [https://linuxize.com/post/how-to-set-and-list-environment-variables-in-linux/](https://linuxize.com/post/how-to-set-and-list-environment-variables-in-linux/)

## Push PostgreSQL enabled version of our application to Heroku

![](https://dl.dropboxusercontent.com/s/8faxiir4jrsa65y/2020-11-08_22-04-51.gif)

```console
git add ../
git commit -m 'PostgreSQL enabled Django'
git push heroku main:master
```

## Make sure that it works

![](https://dl.dropboxusercontent.com/s/5g9rb1bj8qz69lm/2020-11-08_22-07-08.gif)

# Publishing your code on GitHub & setting up CI

## Creating your private repository

![](https://dl.dropboxusercontent.com/s/7fojqhoem8za2n5/2020-11-08_22-12-21.gif)

- You can read more about using Git and GitHub over here: https://www.freecodecamp.org/news/the-beginners-guide-to-git-github/

## Setting up continues integration over at Heroku

![](https://dl.dropboxusercontent.com/s/fr4mxzsp5c97tzy/2020-11-08_22-20-18.gif)

```console
heroku info 
```

Make sure to select repository in Heroku which you previously created.

# Project files and directories

Below you can see all project files and directories as well as their brief description

```
├── LICENSE                         <<< LICENSE FILE
├── README.md                       <<< PROJECT README FILE
├── Workspace.code-workspace        <<< My local Workspace file used to quick open the project in VSC
├── bootcamp                        <<< Django project directory that houses everything
│   ├── Pipfile                     <<< pipenv files used to install required dependencies
│   ├── Pipfile.lock                <<< pipenv files used to install required dependencies
│   ├── Procfile                    <<< Heroku specific file that tells heroku what application to start
│   ├── bootcamp                    <<< project settings folder
│   │   ├── __init__.py             <<< Python module initialization file
│   │   ├── asgi.py                 <<< File used to start Django on ASGI servers
│   │   ├── settings.py             <<< Project settings
│   │   ├── urls.py                 <<< Project URLs
│   │   └── wsgi.py                 <<< File used to start Django on WSGI server (used on Heroku)
│   ├── companydata                 <<< Django application folder
│   │   ├── __init__.py             <<< Python module initialization file
│   │   ├── admin.py                <<< File that tells Django what application models to display in admin and how
│   │   ├── apps.py                 <<< Application specific configurations
│   │   ├── management              <<< Management specific functionality
│   │   │   └── commands            <<< Management (manage.py) commands
│   │   │       └── csv2db.py       <<< Our command that we can invoke using python manage.py csv2db
│   │   ├── migrations              <<< Database migrations
│   │   │   ├── 0001_initial.py     <<< Migration file
│   │   │   ├── 0002_auto_20201103_2028.py <<< Migration file
│   │   │   └── __init__.py         <<< Python module initialization file
│   │   ├── models.py               <<< Application models
│   │   ├── serializers.py          <<< Serializer used by Django REST framework
│   │   ├── tests.py                <<< Tests
│   │   ├── urls.py                 <<< Application specific URLs
│   │   └── views.py                <<< Application views
│   ├── db.sqlite3                  <<< Local SQLite database
│   ├── interface                   <<< Application folder
│   │   ├── __init__.py             <<< Python module initialization file
│   │   ├── admin.py                <<< File that tells Django what application models to display in admin and how
│   │   ├── apps.py                 <<< Application specific configurations
│   │   ├── migrations              <<< Database migrations
│   │   │   └── __init__.py         <<< Python module initialization file
│   │   ├── models.py               <<< Application models
│   │   ├── templates               <<< Application templates
│   │   │   └── index.html          <<< index.html template
│   │   ├── tests.py                <<< Tests
│   │   └── views.py                <<< Application views
│   ├── manage.py                   <<< Django management tool
│   ├── prhdata.csv                 <<< CSV data we use for this project
│   └── staticfiles                 <<< Static files (images etc.) if there are any
```
