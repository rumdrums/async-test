import aiohttp
import asyncio
import async_timeout

async def fetch(session, url):
    print('starting')
    with async_timeout.timeout(10):
        async with session.get(url) as response:
            return await response.text()

async def main(loop):
    async with aiohttp.ClientSession(loop=loop) as session:
        print(1)
        task = asyncio.ensure_future(fetch(session, 'http://python.org'))
        await asyncio.sleep(0)
        print(2)
        result = await task
    print(result)

loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))