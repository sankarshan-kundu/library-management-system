# library-management-system
A sample Python-django project for library management system

## Start database with Docker-compose
```
docker-compose up -d
```

## Start Python-Django API
### Start Python Virtual environment with Pipenv
```
cd library
pipenv shell
```
### Migrate database
```
python manage.py makemigrations
python manage.py migrate
```

### Start service
```
python manage.py runserver
```

### Superuser
- admin/admin