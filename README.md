# aiorate

[![Build](https://img.shields.io/github/workflow/status/tasts-robots/aiorate/CI)](https://github.com/tasts-robots/aiorate/actions)
[![Coverage](https://coveralls.io/repos/github/tasts-robots/aiorate/badge.svg?branch=master)](https://coveralls.io/github/tasts-robots/aiorate?branch=master)
[![Documentation](https://img.shields.io/badge/docs-online-brightgreen?logo=read-the-docs&style=flat)](https://tasts-robots.org/doc/aiorate/)
[![PyPI version](https://img.shields.io/pypi/v/aiorate)](https://pypi.org/project/aiorate/)

Loop frequency regulator for [asyncio](https://docs.python.org/3/library/asyncio.html) with an API similar to [``rospy.Rate``](https://wiki.ros.org/rospy/Overview/Time#Sleeping_and_Rates).

**This project is archived as it has been superseded by [loop-rate-limiters](https://github.com/stephane-caron/loop-rate-limiters).**

## Installation

```sh
pip install aiorate
```

## Usage

The [``Rate``](https://tasts-robots.org/doc/aiorate/rate-limiter.html#aiorate.rate.Rate) class provides a non-blocking loop frequency limiter:

* Set the loop frequency in Hz at construction: ``rate = aiorate.Rate(200.0)``
* Call ``await rate.sleep()`` at every loop cycle

Here is what it looks like in practice:

```python
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
```

Check out the [examples](examples/) folder for more advance use cases, such as multiple loops running simultaneously at different rates.
