import json
from utils.router import Router
from .service import *

onex = Router()

# @onex("/")
# async def home(scope, receive):
#     # print(scope.get('client'))
#     return 200, json.dumps({"message": "Welcome to Onex page!!!"}).encode("utf-8")

@onex("/onex_at_warehouse")
async def home(scope, receive):
    return at_warehouse()


@onex("/onex_on_the_way")
async def home(scope, receive):
    return on_the_way()


@onex("/onex_ready")
async def home(scope, receive):
    return ready()