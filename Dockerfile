# base python image
FROM python:3.6

# install netcat
RUN apt-get update && \
    apt-get clean

# set working directory
WORKDIR /usr/src/app

# add and install requirements
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# add app
COPY . /usr/src/app

EXPOSE 5000

# run server
CMD gunicorn --workers 2 --bind 0.0.0.0:5000 -m 007 wsgi:app
