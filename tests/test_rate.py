#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2022 Stéphane Caron.
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

import unittest

import aiorate


class TestRate(unittest.TestCase):
    def setUp(self):
        """
        Prepare test fixture.
        """
        pass

    def test_module(self):
        self.assertIsNotNone(aiorate.Rate)


if __name__ == "__main__":
    unittest.main()
