import json
from .service import func
from utils.router import Router


lifeshop = Router()


@lifeshop("/lifeshop")
async def home(scope, receive):
    # print(scope.get('client'))
    data = func()
    return 200, json.dumps({"data": [data]}).encode("utf-8")
