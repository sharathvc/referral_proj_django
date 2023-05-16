* A user can signup and generate their own referral code.
* A user can share their referral code with others via email
* If the other user accepts and signs up using the same referral code, 100 credits will be given to both the users.
* also recommend friends

 ## Installation

  For windows

  ```python 
  pip install virtualenv
  python -m virtualenv myenv
  myenv/bin/activate
```
 requirements


after installing Django 
using pip install django in the newly created envirornment
# open the project ref_proj

Install PostgreSQL on your system and make sure it's running.
Log in to PostgreSQL using the psql command-line tool with the username and password you set up during installation.
Create a new database for the referral system using the following command:

# setup the postgress database using following commands
CREATE DATABASE referralDB;

Create a new database user with the appropriate permissions to 
access the referral_system database using the following command:

CREATE USER postgres WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE referralDB TO postgres;
#using psql 
credential for database:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('NAME', 'referral'),
        'USER': os.environ.get('USER', 'referral'),
        'PASSWORD': os.environ.get('PASSWORD', 'referral'),
        'HOST': os.environ.get('HOST', 'localhost'),
        'PORT': os.environ.get('PORT', 5432)
    }
}

again open postgressGUI pgadmin 4
select server
select created database
right click go to properties select security tab
to user referral give priviliges C*T*c* click save

then open the django project and in terminal command prompt
run 'python manage.py makemigrations'
run 'python manage.py migrate'
run 'python manage.py runserver'
