FROM python:3.6
RUN mkdir /var/www
WORKDIR /var/www

COPY ./src ./src
COPY ./static ./static
COPY ./templates ./templates
COPY ./uwsgi.ini ./
COPY ./run.py ./
COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

CMD ["uwsgi","--ini","/var/www/uwsgi.ini"]