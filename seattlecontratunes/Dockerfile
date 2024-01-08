# Dockerfile

# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.10.13


# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# Allows docker to cache installed dependencies between builds
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir /code/
RUN mkdir /code/staticfiles

# Mounts the application code to the image
COPY . code


WORKDIR /code




#ARG 8000
EXPOSE 8000

# runs the production server
#This section is obsolete: docker-compose.yml now starts the server.
#ENTRYPOINT ["python", "seattlecontratunes/manage.py"]
#CMD ["runserver", "0.0.0.0:${PORT}"]

# https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/