import asyncio
import time

async def register_callback(my_future, callback):
  # time.sleep(10)
  my_future.add_done_callback(callback)


async def write_to_s3(my_future):
  print('wrote to s3')
  my_future.set_result(None)


def write_to_db(my_future):
  print('wrote to db')


async def main():
  s3_future = asyncio.Future()
  db_future = asyncio.Future()
  await write_to_s3(s3_future)
  await register_callback(s3_future, write_to_db)

if __name__ == '__main__':
  event_loop = asyncio.get_event_loop()
  event_loop.run_until_complete(main())
  event_loop.close()
