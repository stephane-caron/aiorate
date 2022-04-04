#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2022 Stéphane Caron
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import asyncio

import aiorate

names = ["foo", "bar", "land"]
example_duration = 1.0  # seconds


async def spin_loop(frequency: float, name: str):
    """
    Print time at each cycle of a frequency-regulated loop.

    Args:
        frequency: Loop frequency in hertz.
        name: Loop name.
    """
    rate = aiorate.Rate(frequency, "first_loop")
    event_loop = asyncio.get_event_loop()
    start_time = event_loop.time()
    loop_time = 0.0
    while loop_time < example_duration:
        loop_time = event_loop.time() - start_time
        print(f"Hello from {name} ({frequency} Hz) at time {loop_time:.3f} s")
        await rate.sleep()


async def main():
    await asyncio.gather(
        spin_loop(100.0, names[0]),
        spin_loop(200.0, names[1]),
        spin_loop(400.0, names[2]),
    )


if __name__ == "__main__":
    asyncio.run(main())
    print(f"Hint: grep this output on {'/'.join(names)} to check loop rates")
