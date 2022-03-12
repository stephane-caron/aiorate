:github_url: https://github.com/stephane-caron/aiorate/tree/master/doc/src/index.rst

.. title:: Table of Contents

#######
aiorate
#######

Loop frequency regulator for `asyncio <https://docs.python.org/3/library/asyncio.html>`_, with an API similar to `rospy.Rate <https://wiki.ros.org/rospy/Overview/Time#Sleeping_and_Rates>`_.

.. toctree::

    installation.rst
    rate-limiter.rst

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

You can download the full documentation as a `PDF document <aiorate.pdf>`_.
