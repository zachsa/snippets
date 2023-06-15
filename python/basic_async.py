import asyncio
import random


async def func(i, s):
    print(i, s)


async def schedule(i):
    s = random.randint(0, 2000)
    await asyncio.sleep(s / 1000)
    await func(i, s)


async def main():
    tasks = []
    for i in range(10):
        tasks.append(asyncio.create_task(schedule(i)))
    await asyncio.gather(*tasks)


asyncio.run(main())
