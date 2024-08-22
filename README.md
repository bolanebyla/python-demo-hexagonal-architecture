# Демо проект с использованием гексагональной архитектуры

Вдохновлено проектом [Classic](https://github.com/variasov/classic-demo-simple-shop) автора [@variasov](https://github.com/variasov)

## Зависимости
- PostgreSQL
- [poetry](https://python-poetry.org/)


## Запуск проекта

### Переменные окружения
- **DB_URL** - подключение к БД (пример: `postgresql+asyncpg://demo:demo@localhost:8300/demo_shop`)

### Сборка
```shell
poetry build --format wheel
```

### Установка проекта как пакета
```shell
pip install dist/*.whl
```

### Применение миграций

```shell
python -m shop.run.alembic_runner upgrade head
```
*alembic_runner это обертка, аргументы просто проксируются в cli alembic
```shell
python -m shop.run.alembic_runner <other args>
```

### Запуск API

#### uvicorn
```shell
uvicorn shop.run.shop_api:app --host=0.0.0.0 --port=8000
```

#### python
```shell
python -m shop.run.shop_api.py
```

## Запуск проекта для разработки
*при необходимости развернуть БД в docker-compose
```shell
docker-compose -f .\deployment\docker-compose.local.yaml up -d --build
```
Установить зависимости
```shell
poetry install
```

Каталог `src/` является корневым для python модулей проекта, 
например в IDE можно его пометить как sources_root
(в случае запуска из консоли, нужно определить `PYTHONPATH` и сослать на этот каталог)

Запустить необходимые компоненты из `src/shop/run/`


### Развертывание в контейнере
Изучить Dockerfile в каталоге развертывания (`deployment/`), собрать контейнер с необходимой командой запуска (выбрать нужный entrypoint.sh)

### Openapi документация
- Файл документации доступен по адресу http://127.0.0.1:8000/openapi.json
- Swagger доступен по адресу http://127.0.0.1:8000/docs