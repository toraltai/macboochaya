import json

class Router:
    def __init__(self):
        self.routes = {}

    async def lifespan(self, scope, receive, send):
        """
        Обрабатывает события жизненного цикла приложения.
        """
        await send({"type": "lifespan.startup.complete"})
        try:
            while True:
                message = await receive()
                if message["type"] == "lifespan.shutdown":
                    break
        finally:
            # Обработка события завершения работы приложения
            await send({"type": "lifespan.shutdown.complete"})

    def __call__(self, path):
        def wrapper(func):
            self.routes[path] = func
            return func
        return wrapper
    

    def include_router(self, router, prefix=''):
        for path, func in router.routes.items():
            self.routes[prefix + path] = func


    def route(self, path):
        def wrapper(func):
            self.routes[path] = func
            return func
        return wrapper


    async def handle_request(self, scope, receive, send):
        path = scope['path']
        if path in self.routes:
            # Убедитесь, что возвращаемый объект включает JSON-строку
            status_code, response_body = await self.routes[path](scope, receive)
        else:
            status_code = 404
            response_body = json.dumps({"error": "Not Found"})

        # Убедитесь, что response_body закодирован в байты перед отправкой
        await send({
            'type': 'http.response.start',
            'status': status_code,
            'headers': [(b'content-type', b'application/json')],
        })

        # Преобразуем тело в байты, если оно не закодировано
        if isinstance(response_body, str):
            response_body = response_body.encode("utf-8")

        await send({
            'type': 'http.response.body',
            'body': response_body,
        })
