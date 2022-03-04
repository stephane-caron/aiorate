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
This module provides a non-blocking loop frequency limiter in the :class:`Rate`
class.

Note that there is a difference between a (non-blocking) rate limiter and a
(blocking) synchronous clock, which lies in the behavior when skipping cycles.
A rate limiter does nothing if there is no time left, as the caller's rate does
not need to be limited. On the contrary, a synchronous clock waits for the next
tick, which is by definition in the future, so it always waits for a non-zero
duration.
"""

import asyncio
import logging


class Rate:

    """
    Loop frequency limiter.

    Calls to :func:`sleep` are non-blocking most of the time but become
    blocking close to the next clock tick to get more reliable loop
    frequencies.

    This limiter is in essence the same as in the one from pymanoid_. It relies
    on the event loop time never jumping backwards nor forwards, so that it
    does not handle such cases contrary to e.g. rospy.Rate_.

    .. _pymanoid:
        https://github.com/stephane-caron/pymanoid/blob/d3e2098e40656943f2639f90a1ec4269cf730157/pymanoid/sim.py#L140

    .. _rospy.Rate:
        https://github.com/ros/ros_comm/blob/noetic-devel/clients/rospy/src/rospy/timer.py
    """

    last_measurement_time: float
    loop: asyncio.AbstractEventLoop
    margin: float
    measured_period: float
    name: str
    next_time: float
    period: float

    def __init__(self, frequency: float, name: str = "rate_limiter"):
        """
        Initialize rate limiter.

        Args:
            frequency: Desired loop frequency in [Hz].
            name: Human-readable name used for logging.
        """
        loop = asyncio.get_event_loop()
        period = 1.0 / frequency
        assert loop.is_running()
        self.last_measurement_time = loop.time()
        self.loop = loop
        self.margin = 1.0
        self.measured_period = 0.0
        self.name = name
        self.next_time = loop.time() + period
        self.period = period

    async def remaining(self) -> float:
        """
        Get the time remaining until the next expected clock tick.

        Returns:
            Time remaining, in seconds, until the next expected clock tick.
        """
        return self.next_time - self.loop.time()

    async def sleep(self, block_duration: float = 5e-4):
        """
        Sleep the duration required to regulate the loop frequency.

        This function is meant to be called once per loop cycle.

        Args:
            block_duration: the coroutine blocks the event loop for this
                duration (in seconds) before the next tick. It is non-blocking
                before that.

        Note:
            A call to this function will be non-blocking *except* for the last
            ``block_duration`` seconds of the limiter period.

        The block duration helps trim period overshoots and brings the measured
        period much closer to the desired one (< 2% average error vs. 8-12%
        average error with a single asyncio.sleep). Empirically a block
        duration of 0.5 ms gives good behavior at 400 Hz or lower.
        """
        slack = self.next_time - self.loop.time()
        if slack <= 0.0:
            self.margin = 0.0
            if slack < -0.1 * self.period:
                late_ms = -1000.0 * slack
                logging.warning(
                    "%s is late by %f [ms]", self.name, round(late_ms, 1)
                )
        else:  # slack > 0.0
            self.margin = slack / self.period
            block_time = self.next_time - block_duration
            while self.loop.time() < self.next_time:
                if self.loop.time() < block_time:
                    await asyncio.sleep(1e-5)  # non-zero sleep duration
        measurement_time = self.loop.time()
        self.measured_period = measurement_time - self.last_measurement_time
        self.last_measurement_time = measurement_time
        self.next_time = measurement_time + self.period
