# Дистрибутив базового образа
FROM python:3.7.2

# Контактная информация
LABEL maintainer="sp8997778@gmail.com" \
      description="python:v3.7.2 for simple-django-project"

RUN pip install virtualenv
RUN mkdir /envs
RUN virtualenv /envs/

RUN ls -la /envs/bin/activate
RUN . /envs/bin/activate

# Клонирование Git репозитория
RUN git clone "https://github.com/SergeiPetkov/simple-django-project.git"

# Установка рабочей директории
WORKDIR /simple-django-project

# Обновления необходимые перед установкой зависимостей (ошибка You should consider upgrading via the 'pip install --upgrade pip' command.)
RUN pip install --upgrade setuptools
RUN pip install --upgrade pip

#  Изменение источников пакетов
#RUN sed -i -e 's/deb.debian.org/archive.debian.org/g' -e 's|security.debian.org|archive.debian.org/|g' -e '/stretch-updates/d' /etc/apt/sources.list

# Установка всех зависимостей из requirements.txt
RUN pip install -r requirements.txt

#RUN apt-get update && apt-get install apt-file -y && apt-file update && apt-get install vim -y
CMD ["sleep", "infinity"]

