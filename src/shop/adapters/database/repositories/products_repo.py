from typing import Optional

from attr import frozen

from shop.adapters.database.repositories.base import AsyncBaseRepo
from shop.application.shop.entities import Product
from shop.application.shop.interfaces.repositories import IProductsRepo


@frozen
class ProductsRepo(IProductsRepo, AsyncBaseRepo):
    async def get_by_id(self, id_: int) -> Optional[Product]:
        return await self.session.get(Product, id_)
