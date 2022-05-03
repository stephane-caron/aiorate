:github_url: https://github.com/tasts-robots/aiorate/tree/master/doc/src/example.rst

#######
Example
#######

In short, a loop is rate-regulated this way:

.. code:: python

    import asyncio
    import aiorate

    async def main():
        rate = aiorate.Rate(400.0)  # Hz
        while True:
            loop_time = asyncio.get_event_loop().time()
            print(f"Hello from loop at {loop_time:.3f} s")
            await rate.sleep()

    if __name__ == "__main__":
        asyncio.run(main())

You can await ``rate.sleep()`` anywhere inside the loop.
