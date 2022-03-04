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

"""
Test  rate limiter.
"""

import asyncio
import unittest

import aiorate


class TestRate(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        """
        Initialize a rate with 1 ms period.
        """
        self.rate = aiorate.Rate(1000.0)

    async def test_init(self):
        self.assertIsNotNone(self.rate)

    async def test_remaining(self):
        await self.rate.sleep()
        await asyncio.sleep(self.rate.period)
        remaining = await self.rate.remaining()
        self.assertLess(remaining, 0.0)

    async def test_sleep(self):
        await self.rate.sleep()
        await self.rate.sleep()  # presumably slack > 0.0
        await asyncio.sleep(self.rate.period)
        await self.rate.sleep()  # now for sure slack < 0.0


if __name__ == "__main__":
    unittest.main()
