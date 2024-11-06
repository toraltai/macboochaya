import json
from utils.router import Router
from utils.response import Response
from onex.routers import onex
from lifeshop.routers import lifeshop
from transaction.routers import transaction

api_router = Router()
api_router.include_router(lifeshop, prefix='/api/v1')
# api_router.include_router(shipper, prefix='/api/v1')
api_router.include_router(onex, prefix='/api/v1')
api_router.include_router(transaction, prefix='/api/v1')


@api_router('/')
async def home(scope, receive):
    return 200, json.dumps({"message": "Welcome!!!"}).encode("utf-8")


async def app(scope, receive, send):
    if scope['type'] == 'lifespan':
        await api_router.lifespan(scope, receive, send)
    elif scope['type'] == 'http':
        await api_router.handle_request(scope, receive, send)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
