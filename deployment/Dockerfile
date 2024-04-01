# Стадия сборки
FROM python:3.11-slim as build
# Глобальные переменные стадии сборки
ENV USERNAME=app
ENV PIP_CONFIG_FILE=/app/pip.conf

# Установка бинарных пакетов
RUN apt update \
    && apt install -y unixodbc-dev
# Копирование кода
COPY ./src /app/src
COPY pyproject.toml poetry.lock README.md app/

WORKDIR /app

# Установка зависимостей python
RUN pip install --upgrade pip \
    && pip install poetry \
    && poetry build --format wheel \
    && pip install dist/*.whl
    ## && rm -fr /app/pip.conf
# Смена пользователя
RUN groupadd -r $USERNAME &&\
    useradd -r -g $USERNAME -d /home/$USERNAME -s /sbin/nologin -c "Docker image user" app
# Копирование скриптов запуска
COPY --chown=app:app ./deployment/entrypoints/entrypoint*.sh /usr/local/bin/

RUN chmod +x /usr/local/bin/entrypoint*.sh
# Определение стартовой директории и пользователя
WORKDIR /usr/local/lib/python3.11/site-packages/

USER $USERNAME
# ===================================================
# Стадия тестов
#FROM build as tests
# Глобальные переменные стадии тестов
#ENV PIP_CONFIG_FILE=/app/pip.conf
# Определение стартовой директории и пользователя
#USER root
#WORKDIR /app
# Копирование тестов
#COPY ./components/backend/tests ./tests
#COPY ./components/backend/pip.conf /app/pip.conf

# Установка зависимостей тестов
#RUN pip install --no-cache-dir .[dev]
# Запуск тестов
#RUN pytest tests/unit # директория может меняться
# ===================================================
# Перетегирование основного образа
FROM build as final
