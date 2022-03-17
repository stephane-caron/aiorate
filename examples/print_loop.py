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

keep_going = True


async def main(frequency: float = 100.0):
    """
    Print time at each cycle of a frequency-regulated loop.

    Args:
        frequency: Loop frequency in [Hz].
    """
    rate = aiorate.Rate(frequency, "my_rate_limiter")
    event_loop = asyncio.get_event_loop()
    start_time = event_loop.time()
    while keep_going:
        loop_time = event_loop.time() - start_time
        print(f"Hello from loop at time {loop_time:.3f} [s]")
        await rate.sleep()


if __name__ == "__main__":
    asyncio.run(main())
