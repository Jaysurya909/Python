import asyncio

async def task(name):
    print(f"Starting {name}")
    await asyncio.sleep(2)  # Simulate a delay (like downloading)
    print(f"{name} done!")
    return name

async def main():
    # Start both tasks without waiting
    k=await asyncio.gather(
        task("Task A"),
        task("Task B")
        )
    print(k)
    
    
asyncio.run(main())
