from datetime import datetime
from decimal import Decimal
from typing import Optional

import attr


@attr.dataclass
class Product:
    """
    Товар
    """
    title: str
    price: Decimal

    created_at: datetime
    updated_at: datetime

    id: Optional[int] = None
