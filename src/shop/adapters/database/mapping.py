from sqlalchemy.orm import registry

from shop.adapters.database.tables.products import products_table
from shop.application.shop.entities import Product

mapper = registry()

mapper.map_imperatively(
    Product,
    products_table,
)
