# Lab-32

## Author: Ethan Albers

## Setup
~~~
docker compose up -d
docker compose run web python manage.py migrate
docker compose run web python manage.py createsuper
~~~

## Using API
- Access developement server with http://0.0.0.0:8000/
- Use `/admin` to add to database using super user created during setup
- use `/api/v1/profiles` to access list of profiles
- use `/api/v1/profiles/#` to access and edit details of each profile