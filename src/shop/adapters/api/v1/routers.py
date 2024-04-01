from fastapi import APIRouter
from .controllers.products import products_router

v1_router = APIRouter(prefix='/v1')

v1_router.include_router(products_router, tags=['Товары'])
