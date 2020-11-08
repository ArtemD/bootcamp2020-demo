# About this document

This project is part of programming Boot Camp 2020 course.

## Prerequisites

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

- You can read more about pipenv shell here: https://pipenv-fork.readthedocs.io/en/latest/basics.html


## Make sure to add virtualenv as correct path in Virtual Studio Code

![](https://dl.dropboxusercontent.com/s/dbl88zxo036namv/2020-11-08_11-24-07.gif)

- You can read more about Visual Studio Code Python settings here: https://olav.it/2017/03/04/pipenv-visual-studio-code/

## Check that Django is installed correctly

![](https://dl.dropboxusercontent.com/s/vgry1xjlaza31wx/2020-11-08_11-43-20.gif)

```console
python -m django --version
```

- If you're having issues with Django installation, please look into excellent installation documentation: https://docs.djangoproject.com/en/3.1/topics/install/

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
web: gunicorn bootcamp.wsgi
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

## Create Heroku instance

![](https://dl.dropboxusercontent.com/s/pardbzfpydpa9sv/2020-11-07_11-49-13.gif)

```console
heroku create
```

*Make sure to run it from the root folder*.

- You can learn more about creating apps using heroku cli here: https://devcenter.heroku.com/articles/creating-apps

# Set correct buildpack for our project

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
git push heroku main
# Prey and cross your fingers!
```

Now you should be able to see your new shiney web app url: https://dl.dropboxusercontent.com/s/ohn0ux5jjs22952/Code_2020-11-03_22-43-18.png

## Create a free account and initialize a free database

Register a free account over at elephantsql.com

![Setting up SQL]( https://dl.dropboxusercontent.com/s/ccfd0aiisrg2988/2020-11-05_20-40-07.gif "Setting up SQL")

## Connecting to Heroku database

```console
pipenv install dj-database-url
```

Then add the following to the bottom of settings.py:

```python
# Adding support for database urls
import dj_database_url

DATABASES['default'] = dj_database_url.config(f'postgres://amvmzgrd:PASSWORD@rogue.db.elephantsql.com:5432/amvmzgrd', conn_max_age=600, ssl_require=True)
#DATABASES['default'] = dj_database_url.config(f'sqlite:///{BASE_DIR}/db.sqlite3')
```

Make sure to use database URL from EelephantSQL

## Pushing to Heroku

Now with PostgreSQL database connection added create migrations, run migrate and push to heroku. In addition to this you have to create superuser again.

```console
python manage.py makemigrations && python manage.py migrate
python manage.py createsuperuser
git add *
git commit -avm 'PostgreSQL enabled Django'
git push heroku
```
