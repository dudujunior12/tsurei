FROM python:3.11.4-alpine3.17

RUN apk add --no-cache --upgrade bash

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONBUFFERED 1

EXPOSE 8000

COPY /tsurei ./tsurei
COPY /scripts/ ./scripts

WORKDIR /tsurei

RUN python -m venv /venv

ENV PATH="/scripts:/venv/bin:$PATH"

RUN pip install --upgrade pip && \
 pip install -r requirements.txt && \
 mkdir -p /tsurei/tsurei/static && \
 mkdir -p /tsurei/tsurei/static/manga && \
 chmod -R 755 /tsurei/tsurei/static/manga && \
 chmod -R 755 /tsurei/tsurei/static && \
 chmod -R +x /scripts/

# USER tsurei

CMD ["/bin/sh", "/scripts/commands.sh"]
