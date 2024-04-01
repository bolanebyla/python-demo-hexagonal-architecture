from fastapi import APIRouter, Depends

from shop.adapters.api.composites import create_products_service
from shop.application.shop.services import ProductsService

products_router = APIRouter(prefix='/products')


@products_router.get('/get/{product_id}')
async def get_product(
        product_id: int,
        products_service: ProductsService = Depends(create_products_service),
):
    product = await products_service.get_product(id_=product_id)
    return {
        'id': product.id,
        'title': product.title,
        'price': product.price,
        'created_at': product.created_at,
        'updated_at': product.updated_at,
    }
