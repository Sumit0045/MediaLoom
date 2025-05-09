FROM python:3.10.4-slim-buster
RUN apt update && apt upgrade -y
RUN apt-get -y install git
COPY requirements.txt .

RUN pip3 install wheel
RUN pip3 install --no-cache-dir -U -r requirements.txt
WORKDIR /app
COPY . .
CMD python3 -m MediaLoom
