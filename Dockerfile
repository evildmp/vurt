FROM nginx:latest

RUN apt-get update -y
RUN apt-get install -y python3-pip

WORKDIR /app
COPY . /app

COPY nginx.conf /etc/nginx/nginx.conf
COPY default.conf /etc/nginx/conf.d/default.conf

RUN pip install -r compiled-requirements.txt --break-system-packages
RUN sphinx-build -b dirhtml . _build/html
RUN cp -r _build/html/. /usr/share/nginx/html

EXPOSE 80
