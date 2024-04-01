from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from shop.adapters import database
from shop.application.shop.services import ProductsService


class DB:
    settings = database.DBSettings()

    engine = database.create_engine_from_settings(settings=settings)
    session_factory = database.create_session_factory(engine=engine)


async def get_db_session() -> AsyncSession:
    async with DB.session_factory() as session:
        yield session


def create_products_repo(
        session: AsyncSession = Depends(get_db_session)
) -> database.ProductsRepo:
    return database.ProductsRepo(session=session)


def create_products_service(
        products_repo: database.ProductsRepo = Depends(create_products_repo)
) -> ProductsService:
    return ProductsService(products_repo=products_repo)
