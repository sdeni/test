FROM python:3.6-buster
ENV PYTHONUNBUFFERED 1

ARG USER_UID
ARG USER_GID

# RUN addgroup --gid $USER_GID django && adduser --disabled-password --gecos "" --ingroup django --uid "$USER_UID" django #alpine

RUN useradd -r -u $USER_UID -g root django # ubuntu/centos
# USER django

RUN mkdir /code
WORKDIR /code
COPY ./requirements.txt /code/

# alpine install psycopg2
#RUN apk add --no-cache --virtual .build-deps \
#    gcc \
#    python3-dev \
#    musl-dev \
#    postgresql-dev \
#    && pip install --no-cache-dir psycopg2 \
#    && apk del --no-cache .build-deps

RUN pip install -r requirements.txt

RUN chown -R django /code
USER django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]