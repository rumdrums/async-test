import asyncio
import time

loop = asyncio.get_event_loop()

async def barf():
  i=0
  while i<1000:
    with open('/tmp/' + str(i), 'w') as f:
      f.write('barf')
    time.sleep(.5)
    i+=1

#loop.run_until_complete(barf())
a = asyncio.ensure_future(barf())
print('hey man!')

########################
import asyncio
import time

async def func1():
  i=0
  while i<20:
    with open('/tmp/' + str(i), 'w') as f:
      f.write('barf')
    time.sleep(.5)
    i+=1


def func2():
  loop = asyncio.get_event_loop()
  loop.run_until_complete(func1())



