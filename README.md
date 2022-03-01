# aiorate

[![build](https://img.shields.io/github/workflow/status/stephane-caron/aiorate/CI)](https://github.com/stephane-caron/aiorate/actions)
[![PyPI package](https://img.shields.io/pypi/v/aiorate)](https://pypi.org/project/aiorate/)
![Status](https://img.shields.io/pypi/status/aiorate)

Loop frequency regulation for [asyncio](https://docs.python.org/3/library/asyncio.html) with an API similar to [``rospy.Rate``](https://wiki.ros.org/rospy/Overview/Time#Sleeping_and_Rates).

## Installation

```sh
pip install aiorate
```

## Example

```python
import asyncio
import aiorate

async def main():
    frequency = 400.0  # [Hz]
    rate = aiorate.Rate(frequency, "my_rate_limiter")
    while True:
        loop_time = asyncio.get_event_loop().time()
        print(f"Hello from loop at {loop_time:.3f} [s]")
        await rate.sleep()

if __name__ == "__main__":
    asyncio.run(main())
```
