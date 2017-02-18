import asyncio
import time

def write_to_s3():
  time.sleep(5)
  print('wrote to s3')

def write_to_db():
  time.sleep(1)
  print('wrote to db')


async def main(loop):
  print(1)
  loop.call_soon(write_to_s3)
  print(2)
  loop.call_soon(write_to_db)
  print(3)

if __name__ == '__main__':
  event_loop = asyncio.get_event_loop()
  while True:
    event_loop.run_until_complete(main(event_loop))
  event_loop.close()

