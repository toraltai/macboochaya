import urllib.parse
import json
from utils.router import Router
from .service import *


transaction = Router()

"""Нужно передавать число вот таким образом drop?amount=10000"""
@transaction("/drop") 
async def som_rub_usd(scope, receive):
    query_string = scope.get('query_string', b'').decode('utf-8')
    params = urllib.parse.parse_qs(query_string)
    amount = params.get('amount', [None])[0]

    data = transfer(amount)
    return 200, json.dumps({"data": [data]}).encode("utf-8")