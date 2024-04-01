from starlette.responses import JSONResponse

from shop.application.base.errors import AppError
from fastapi import Request


def app_error_handler(request: Request, exc: AppError) -> JSONResponse:
    return JSONResponse(
        status_code=400,
        content={
            'message': exc.message,
            'code': exc.code,
        },
    )
