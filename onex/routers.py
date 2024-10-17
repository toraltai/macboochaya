import json
from utils.router import Router
from .service import *

onex = Router()

# @onex("/")
# async def home(scope, receive):
#     # print(scope.get('client'))
#     return 200, json.dumps({"message": "Welcome to Onex page!!!"}).encode("utf-8")

@onex("/onex")
async def home(scope, receive):
    return get_data()