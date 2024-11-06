import json
from utils.router import Router
from .service import *


transaction = Router()

"""Нужно передавать число вот таким образом drop?amout=10000"""
@transaction("/drop") 
async def som_rub_usd(scope, receive):
    params = scope.get('query_params', {})
    amount = params.get('amount', 100)

    data = transfer(amount)
    return 200, json.dumps({"data": [data]}).encode("utf-8")