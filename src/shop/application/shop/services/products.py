from attr import frozen
from pydantic import validate_call

from ..entities import Product
from ..errors import ProductNotFound
from ..interfaces.repositories import IProductsRepo


@frozen
class ProductsService:
    products_repo: IProductsRepo

    @validate_call
    async def get_product(self, id_: int) -> Product:
        """
        Получает товар по идентификатору
        """
        product = await self.products_repo.get_by_id(id_=id_)

        if not product:
            raise ProductNotFound(product_id=id_)

        return product
