import hashlib
import hmac
import asyncio
import websockets
from websockets.legacy.client import WebSocketClientProtocol


async def consumer_handler(websocket: WebSocketClientProtocol):
    global key
    async for message in websocket:
        try:
            message = message.decode()
            if message.startswith('Key'):
                key = message.split()[-1]
                await websocket.close()
        except UnicodeDecodeError:
            continue


async def produce(message: str, hostname: str, port: int) -> None:
    async with websockets.connect(f'ws://{hostname}:{port}') as ws:
        await ws.send(message)
        await ws.recv()


async def consume(hostname: str, port: int) -> None:
    websocket_resource_url = f'ws://{hostname}:{port}'
    async with websockets.connect(websocket_resource_url) as websocket:
        await consumer_handler(websocket)


def hmac_data(data, key):
    dig = hmac.new(key=key.encode(), msg=data.encode(),
                   digestmod=hashlib.sha256)
    result = data.encode() + b':' + dig.digest()
    return result


if __name__ == '__main__':
    url = '46.229.214.188'
    port = 80
    key = ''
    email = 'aepre@yandex.ru'
    loop = asyncio.get_event_loop()
    loop.run_until_complete(consume(hostname=url, port=port))
    message = hmac_data(email, key)
    loop.run_until_complete(produce(message=message, hostname=url, port=port))
