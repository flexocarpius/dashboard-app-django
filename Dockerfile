FROM python:3.8

RUN apt-get update && apt-get install nginx vim -y --no-install-recommends
COPY nginx/dashboard-app.conf /etc/nginx/sites-available/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

WORKDIR /

COPY manage.py gunicorn-cfg.py requirements.txt start-server.sh .env ./
COPY app app
COPY authentication authentication
COPY core core

RUN pip install -r requirements.txt

RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py collectstatic

EXPOSE 8000

CMD ["/start-server.sh"]