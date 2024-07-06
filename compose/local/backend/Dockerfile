FROM python:3.11-slim-buster
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install -y -q --no-install-recommends build-essential libpq-dev
RUN apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false
RUN rm -rf /var/lib/apt/lists/*

ENV HOME=/home/app
RUN mkdir $HOME
WORKDIR $HOME

RUN pip install --upgrade pip

COPY ./src/requirements /requirements
RUN pip install -r /requirements/local.txt

COPY ./compose/local/backend/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./compose/local/backend/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

WORKDIR /app/src

ENTRYPOINT ["/entrypoint"]
