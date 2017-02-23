import asyncio
import time
import aiohttp
import requests


async def make_request_async():
  print('starting')
  return aiohttp.get('http://python.org')


async def make_request_sync():
  return requests.get('http://python.org')


async def main():
  print(1)
  task = asyncio.ensure_future(make_request_async())
  # await make_request_sync()
  print(2)
  result = await task 
  print(result)

if __name__ == '__main__':
  event_loop = asyncio.get_event_loop()
  event_loop.run_until_complete(main())
  event_loop.close()

