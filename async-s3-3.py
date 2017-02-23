import aiobotocore
import asyncio
import sys
import time
from cloud.aws import AsyncioBotocore


async def write_to_s3(loop, f):
  bucket = 'jaymell-test'
  s3 = AsyncioBotocore('s3', 'us-west-2')
  await s3.put_object(Bucket=bucket, 
                      Key=os.path.basename(f),
                      Body=open(f))

  print('wrote to s3')


async def main(loop, f):
  print(1)
  await write_to_s3(loop, f)
  print(2)


if __name__ == '__main__':
  event_loop = asyncio.get_event_loop()
  while True:
    event_loop.run_until_complete(main(event_loop, '/home/james/Videos/2017-02-10T10:31:40.867162.avi'))
  event_loop.close()

