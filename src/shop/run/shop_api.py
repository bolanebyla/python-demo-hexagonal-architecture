import uvicorn
from shop.adapters.api.app import app

if __name__ == '__main__':
    uvicorn.run(app, host='localhost', log_level='debug')
