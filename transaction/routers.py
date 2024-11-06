from utils.router import Router
from .service import *


transaction = Router()


@transaction("/drop")
async def som_rub_usd(scope, receive):
    return transfer()