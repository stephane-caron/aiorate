#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2022 The aiorate authors.
#
# This file is part of aiorate.
#
# aiorate is free software: you can redistribute it and/or modify it under the
# terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# aiorate is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with aiorate. If not, see <http://www.gnu.org/licenses/>.

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
