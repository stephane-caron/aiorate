# aiorate

[![build](https://img.shields.io/github/workflow/status/stephane-caron/aiorate/CI)](https://github.com/stephane-caron/aiorate/actions)
[![Documentation](https://img.shields.io/badge/docs-online-brightgreen?logo=read-the-docs&style=flat)](https://scaron.info/doc/aiorate/)
[![PyPI package](https://img.shields.io/pypi/v/aiorate)](https://pypi.org/project/aiorate/)
![Status](https://img.shields.io/pypi/status/aiorate)

Loop frequency regulator for [asyncio](https://docs.python.org/3/library/asyncio.html) with an API similar to [``rospy.Rate``](https://wiki.ros.org/rospy/Overview/Time#Sleeping_and_Rates).

## Installation

```sh
pip install aiorate
```

## Usage

The ``[Rate](https://scaron.info/doc/aiorate/rate-limiter.html#aiorate.rate.Rate)`` class provides a non-blocking loop frequency limiter:

* Set the loop frequency in Hz at construction: ``rate = aiorate.Rate(200.0)``
* Call ``await rate.sleep()`` at every loop cycle

## Example

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
