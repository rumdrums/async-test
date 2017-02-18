import asyncio
import time
import aiohttp
import requests


async def make_request_async():
  return await aiohttp.get('http://www.nytimes.com')


async def make_request_sync():
  return requests.get('http://www.nytimes.com')


async def main():
  while True:
    print(1)
    await make_request_async()
    # await make_request_sync()
    print(2)


if __name__ == '__main__':
  event_loop = asyncio.get_event_loop()
  event_loop.run_until_complete(main())
  event_loop.close()

