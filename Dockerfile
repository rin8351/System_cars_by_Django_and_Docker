FROM python:latest
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY ./requirements.txt .
ADD post ./
RUN pip install -r requirements.txt
RUN DJANGO_SUPERUSER_PASSWORD=12345 
RUN DJANGO_SUPERUSER_USERNAME=admin
RUN DJANGO_SUPERUSER_EMAIL=admin@localhost
