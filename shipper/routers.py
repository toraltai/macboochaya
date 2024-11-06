import json
from utils.router import Router
from .service import *


shipper = Router()


@shipper("/shipper")
async def home(scope, receive):
    pass