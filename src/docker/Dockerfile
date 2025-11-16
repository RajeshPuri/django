FROM python:3.12-alpine

WORKDIR /app/

RUN apk update \
    && apk add --no-cache \
    tzdata make \
    gcc g++ musl-dev libffi-dev openssl-dev \
    curl cargo \
    python3-dev jpeg-dev zlib-dev rust \
    postgresql-dev \
    geos geos-dev \
    gdal gdal-dev \
    proj proj-dev \
    build-base openssh


# RUN python3 -m pip install --upgrade pip

# RUN pip install --no-cache-dir -r requirements.txt
# RUN pip3 install supervisor

# RUN mkdir -p /var/log/supervisor

# RUN mkdir -p /etc/supervisor/conf.d/

COPY . /app

# COPY ./ssh/sync.sh /root/sync.sh

# COPY ./ssh/sshd_config /etc/ssh/sshd_config

# COPY ./supervisor/supervisord.conf /etc/supervisord.conf

# COPY ./supervisor/supervisor.conf /etc/supervisor/conf.d/supervisor.conf

# COPY ./gunicorn_config.py /root/gunicorn_config.py

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

RUN poetry config installer.max-workers 10
RUN poetry install --no-root --no-interaction --no-ansi

ENV PYTHONPATH=/app

ENV TZ Asia/Kathmandu

RUN chmod +x /app/entrypoint.sh

# RUN chmod +x /root/sync.sh

ENTRYPOINT ["sh", "/app/entrypoint.sh"]
