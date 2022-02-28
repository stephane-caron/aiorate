# aiorate

[![build](https://img.shields.io/github/workflow/status/stephane-caron/aiorate/CI)](https://github.com/stephane-caron/aiorate/actions)
[![PyPI package](https://img.shields.io/pypi/v/aiorate)](https://pypi.org/project/aiorate/)
![Status](https://img.shields.io/pypi/status/aiorate)

Loop frequency regulation for [asyncio](https://docs.python.org/3/library/asyncio.html), with an API similar to [rospy.Rate](https://wiki.ros.org/rospy/Overview/Time#Sleeping_and_Rates).

## Installation

```sh
pip install aiorate
```

## Usage

```python
async def my_loop():
    frequency = 400.0  # [Hz]
    rate = aiorate.Rate(frequency, "my_rate_limiter")
    while keep_going:
        do_loop_things()
        await rate.sleep()
```
