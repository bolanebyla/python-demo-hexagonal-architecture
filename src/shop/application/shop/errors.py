from shop.application.base.errors import AppError


class ProductNotFound(AppError):
    message_template = 'Товар с id "{product_id}" не найден'
