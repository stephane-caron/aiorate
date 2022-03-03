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

import asyncio
import logging


class Rate:

    """
    Non-blocking loop frequency limiter.

    Notes
    -----
    This rate limiter is basically the same as in the one from pymanoid_. It is
    not as sophisticated as rospy.Rate_ but does the job with reliable
    repeatability.

    .. _pymanoid:
        https://github.com/stephane-caron/pymanoid/blob/d3e2098e40656943f2639f90a1ec4269cf730157/pymanoid/sim.py#L140

    .. _rospy.Rate:
        https://github.com/ros/ros_comm/blob/noetic-devel/clients/rospy/src/rospy/timer.py

    The difference between a blocking clock and a rate limiter lies in the
    behavior when skipping cycles. A rate limiter does nothing if there is no
    time left, as the caller's rate does not need to be limited. On the
    contrary, a synchronous clock waits for the next tick, which is by
    definition in the future, so it always waits for a non-zero duration.
    """

    last_measurement_time: float
    loop: asyncio.unix_events._UnixSelectorEventLoop
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

    async def sleep(self, block_duration: float = 5e-4):
        """
        Sleep the duration required to regulate the loop frequency.

        This function is meant to be called once per loop cycle.

        Args:
            block_duration: the coroutine blocks the event loop for this
                duration (in seconds) before the next tick. It is non-blocking
                before that.

        The block duration helps trim period overshoots and brings the measured
        period much closer to the desired one (< 2% average error vs. 8-12%
        average error with a single asyncio.sleep). Empirically a block
        duration of 0.5 ms gives good behavior at 400 Hz or lower.
        """
        current_time = self.loop.time()
        slack = self.next_time - current_time
        if slack <= 0.0:
            self.margin = 0.0
            if slack < -0.1 * self.period:
                late_ms = -1000.0 * slack
                logging.warning(
                    f"{self.name} is late by {round(late_ms, 1)} [ms]"
                )
        else:  # slack > 0.
            self.margin = slack / self.period
            block_time = self.next_time - block_duration
            while self.loop.time() < self.next_time:
                if self.loop.time() < block_time:
                    await asyncio.sleep(1e-5)  # non-zero sleep duration
        measurement_time = self.loop.time()
        self.measured_period = measurement_time - self.last_measurement_time
        self.last_measurement_time = measurement_time
        self.next_time = measurement_time + self.period
