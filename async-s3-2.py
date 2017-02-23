import aiobotocore
import asyncio
import sys
import time


async def write_to_s3(loop, f):
  bucket = 'jaymell-test'
  sess = aiobotocore.get_session(loop=loop)
  async with sess.create_client('s3', region_name='us-west-2') as cli:
    await cli.put_object(Bucket=bucket, 
                                   Key=f,
                                   Body=open(f, 'rb'))
    print('wrote to s3')


async def main(loop, f):
  print(1)
  await write_to_s3(loop, f)
  print(2)


if __name__ == '__main__':
  event_loop = asyncio.get_event_loop()
  event_loop.run_until_complete(main(event_loop, '/home/james/Videos/2017-02-10T10:31:40.867162.avi'))
  event_loop.close()

