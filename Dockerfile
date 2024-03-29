FROM python:latest
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN DJANGO_SUPERUSER_PASSWORD=12345 
RUN DJANGO_SUPERUSER_USERNAME=admin
RUN DJANGO_SUPERUSER_EMAIL=admin@localhost
CMD ["python", "manage.py", "runserver"]
