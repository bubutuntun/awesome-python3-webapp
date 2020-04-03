import asyncio
import logging

from aiohttp import web


def index(request):
    return web.Response(body='<h1>hello</h1>',headers={'content-type':'text/html'})

async def init():
    app=web.Application()
    app.router.add_route('GET','/',index)
    app_runner=web.AppRunner(app)
    await app_runner.setup()
    srv = await  loop.create_server(app_runner.server, 'localhost', '9000')

    # srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)

    logging.info('server started at http://127.0.0.1:9000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init())
loop.run_forever()