# API for library management system

## Start Python-Django API
### Start Python Virtual environment with Pipenv
```
pipenv shell
pipenv sync
```
### Migrate database
```
cd library/
python manage.py makemigrations
python manage.py migrate
```

### Start service
```
python manage.py runserver
```
#### Service URLs:
- Admin: http://localhost:8000/admin
- LMS: http://localhost:8000/lms
