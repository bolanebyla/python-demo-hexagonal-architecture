from fastapi import FastAPI

from shop.adapters.api.exception_handlers import app_error_handler
from shop.adapters.api.v1.routers import v1_router
from shop.application.base.errors import AppError

app = FastAPI()
app.include_router(v1_router)

app.add_exception_handler(AppError, app_error_handler)
