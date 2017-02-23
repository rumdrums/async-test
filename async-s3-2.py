import aiobotocore
import asyncio
import sys
import time


async def write_to_s3(loop, f):
  print('starting')
  bucket = 'jaymell-test'
  sess = aiobotocore.get_session(loop=loop)
  async with sess.create_client('s3', region_name='us-west-2') as cli:
    await cli.put_object(Bucket=bucket, 
                         Key=f,
                         Body=open(f, 'rb'))
    print('wrote to s3')


async def main(loop, f):
  # while True:
  #   print(1)
  #   result = write_to_s3(loop, f)
  #   time.sleep(2)
  #   print(2)
  #   await result
  tasks = []
  for i in range(0,10):
    task = asyncio.ensure_future(write_to_s3(loop, f))
    tasks.append(task)
  await asyncio.wait(tasks)

if __name__ == '__main__':
  event_loop = asyncio.get_event_loop()
  event_loop.run_until_complete(main(event_loop, 
                                     '/tmp/test'))
  event_loop.close()

