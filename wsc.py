import asyncio

async def a():
    print("Hello")
    await asyncio.sleep(7)
    print("sayonara")
    return "one"

async def b():
    print("hi")
    await asyncio.sleep(5)
    print("bye")
    return "two"

async def main():
    zz = a()
    xx = b()
    result = await asyncio.gather(zz,xx)
    print(result)#리스트로 반환하는구나 asyncio.gather

print("Main Start")
asyncio.run(main())
print("Main End")

# loop = asyncio.get_event_loop()
# loop.run_until_complete(a())
# loop.close()