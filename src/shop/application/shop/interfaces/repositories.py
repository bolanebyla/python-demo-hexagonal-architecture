from abc import ABC, abstractmethod
from typing import Optional

from ..entities import Product


class IProductsRepo(ABC):
    """
    Репозиторий для работы с товарами
    """

    @abstractmethod
    async def get_by_id(self, id_: int) -> Optional[Product]:
        """
        Получает товар из хранилища по идентификатору
        """
        ...
