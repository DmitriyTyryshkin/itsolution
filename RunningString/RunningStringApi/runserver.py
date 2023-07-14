from waitress import serve

from RunningStringApi.wsgi import application

# documentation: https://docs.pylonsproject.org/projects/waitress/en/stable/api.html

if __name__ == '__main__':
    serve(application, host='localhost', port='8080')

# python manage.py runserver

# python manage.py makemigrations
# python manage.py migrate
