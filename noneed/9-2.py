import asyncio

# async def async_func1():
#     print("Hello")

# # async_func1()
# # asyncio.run(async_func1())

# loop = asyncio.get_event_loop()
# loop.run_until_complete(async_func1())
# loop.close()

async def make_americano():
    print("AAA strat")
    await asyncio.sleep(3)
    print("AAA end")
    return "Americano"

async def make_latte():
    print("LLL strat")
    await asyncio.sleep(5)
    print("LLL end")
    return "Latte"

async def main():
    coro1 = make_americano()
    coro2 = make_latte()
    result = await asyncio.gather(coro1, coro2)
    print(result)

print("main start")
asyncio.run(main())
print("main end")