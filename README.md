# simple-django-project
## Installation
#### Prerequisites
Install MySQL server on the machine based on your Operating System.
Reference: [https://dev.mysql.com/doc/refman/5.5/en/](https://dev.mysql.com/doc/refman/5.5/en/)

#### Clone git repository
```bash
git clone "https://github.com/Manisha-Bayya/simple-django-project.git"
```

#### Install requirements
```bash
cd simple-django-project/
pip install -r requirements.txt
```

#### Get sample data
```bash
# open mysql bash
mysql -u <mysql-user> -p

# Give absolute path of file
mysql> source ~/simple-django-project/world.sql
mysql> exit;

```
#### Edit project settings
```bash
# open settings file
vim panorbit/settings.py

# Edit Database configurations with your mysql configurations.
# Search for DATABASES section.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'world',
        'USER': '<mysql-user>',
        'PASSWORD': '<mysql-password>',
        'HOST': '<mysql-host>',
        'PORT': '<mysql-port>',
    }
}

# Edit email configurations.
# Search for email configurations
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = '<your-email>'
EMAIL_HOST_PASSWORD = '<your-email-password>'
EMAIL_PORT = 587

# save the file
```
#### Run the server
```bash
python manage.py makemigrations
python manage.py migrate

# For search feature we need to index certain tables to haystack. For that run below command.
python manage.py rebuild_index

# Run the server
python manage.py runserver 0:8001

# your server is up on port 8001
```
Try opening [http://localhost:8001](http://localhost:8001) in browser.
Now you are good to go.

### URLs
#### Signup: [http://localhost:8001/signup](http://localhost:8001/signup)
#### Login: [http://localhost:8001/login](http://localhost:8001/login)
#### home for search: [http://localhost:8001/](http://localhost:8001/)
#### country page: [http://localhost:8001/country/kenya](http://localhost:8001/country/kenya)
#### Logout: [http://localhost:8001/logout](http://localhost:8001/logout)
