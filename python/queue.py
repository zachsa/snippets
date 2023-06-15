import asyncio
import random


async def worker(queue):
    while True:
        # Dequeue the next task from the queue
        task = await queue.get()

        # Run the task
        s = random.randint(0, 2000)
        await asyncio.sleep(s / 1000)
        print(f"Task {task} finished with sleep time {s/1000:.3f} seconds")

        # Mark the task as done
        queue.task_done()


async def main():
    # Create a queue to hold the tasks
    queue = asyncio.Queue()

    # Enqueue the tasks
    for i in range(10):
        queue.put_nowait(i)

    # Create a fixed number of worker coroutines
    num_workers = 4
    workers = [asyncio.create_task(worker(queue)) for _ in range(num_workers)]

    # Wait for all tasks to be processed
    await queue.join()

    # Cancel the worker coroutines
    for w in workers:
        w.cancel()

    # Wait for the worker coroutines to finish
    await asyncio.gather(*workers, return_exceptions=True)


asyncio.run(main())
