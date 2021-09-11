FROM python:3.7-alpine

RUN echo "@testing http://dl-cdn.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories

RUN apk add --update --no-cache py3-numpy py3-pandas@testing

# Continue from here

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

COPY Export_Log_Clean.csv .

# Install any dependencies
RUN apk add --no-cache --update \
    python3 python3-dev gcc \
    gfortran musl-dev g++ \
    libffi-dev openssl-dev \
    libxml2 libxml2-dev \
    libxslt libxslt-dev \
    libjpeg-turbo-dev zlib-dev

RUN pip install --upgrade pip

ADD requirements.txt .

RUN pip install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY app.py .

COPY Export_Log_Clean.csv .

# Specify the command to run on container start
CMD [ "python", "./app.py" ]
