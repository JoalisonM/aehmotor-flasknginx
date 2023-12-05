FROM python:3.10
LABEL maintainer "Rhavy Maia Guedes <rhavy.guedes@ifpb.edu.br>"

RUN apt-get update

RUN mkdir /app
WORKDIR /app
COPY . /app

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_DEBUG=true
ENV FLASK_ENV=development

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

# running Flask as a module
CMD flask db init && \
  flask db migrate && \
  flask db upgrade && \
  flask run