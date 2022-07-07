import hashlib
import hmac
import asyncio
import logging

import websockets
from websockets.exceptions import ConnectionClosedError
from websockets.legacy.client import WebSocketClientProtocol

logging.basicConfig(level=logging.INFO)


def hmac_data(data, key):
    dig = hmac.new(key=key.encode(), msg=data.encode(),
                   digestmod=hashlib.sha256)
    result = data.encode() + b':' + dig.digest()
    return result


async def create_sock(hostname: str, port: int) -> None:
    async with websockets.connect(f'ws://{hostname}:{port}') as ws:
        await consume(ws)


async def send_answer(ws, message: str) -> None:
    await ws.send(message)


async def consume(ws: WebSocketClientProtocol) -> None:
    try:
        async for message in ws:
            try:
                message = message.decode()
                if message.startswith('Key'):
                    key = message.split()[-1]
                    message = hmac_data(email, key)
                    await send_answer(ws, message)
            except UnicodeDecodeError:
                continue
    except ConnectionClosedError:
        logging.info(f'{ws.remote_address} disconnects')


if __name__ == '__main__':
    url = '46.229.214.188'
    port = 80
    email = 'aepre@yandex.ru'
    loop = asyncio.get_event_loop()
    loop.run_until_complete(create_sock(url, port))
    loop.run_forever()
