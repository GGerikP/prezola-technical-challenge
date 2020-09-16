FROM alpine:3.10

ENV PYTHONUNBUFFERED 1

# Prepare app folder
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Install requirements (some need extra stuff for compiling)
COPY requirements.txt /usr/src/app/requirements.txt
RUN apk add --no-cache --update curl python3
RUN apk add --no-cache --update build-base python3-dev linux-headers &&\
    pip3 install --no-cache-dir -r requirements.txt &&\
    apk del build-base python3-dev linux-headers

# Copy our (updated) app
COPY . /usr/src/app

# Define everything necessary to start our server
#HEALTHCHECK CMD curl --fail http://localhost/status || exit 1
EXPOSE 80
#CMD ["uwsgi", "--need-app", "--ini", "uwsgi.ini"]
