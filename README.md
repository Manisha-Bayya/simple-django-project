# simple-django-project 
## Installation

## Prerequisites
Install Docker.  Follow the steps form the below reference document based on your Operating System. Reference: https://docs.docker.com/engine/install/

1. Clone git repository
git clone https://github.com/SergeiPetkov/simple-django-project.git

2. Creating an image from a Dockerfile
docker build -t django:v1 .

3. Change compose.yaml
"- /home/.../simple-django-project/world.sql:/mysql-files/world.sql"

4. Deploy with docker compose
docker compose up -d

5. Execute SQL script from .sql file
docker exec -i simple-django-project-db-1 mysql -u root -h simple-django-project-db-1 -p -e "use world; source /mysql-files/world.sql;"
# -h вопрос по этой части команды (в каких случаях применяеть а в каких не нужно)

6. Sequential execution of commands
# /bin/sh -c "python manage.py makemigrations && python manage.py migrate && python manage.py rebuild_index"
docker exec -it container_id python manage.py makemigrations
docker exec -it container_id python manage.py migrate
docker exec -it container_id python manage.py rebuild_index
docker exec -it container_id python manage.py runserver 0:8001





