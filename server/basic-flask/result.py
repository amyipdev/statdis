# SPDX-License-Identifier: GPL-2.0-only
#
# statdis: The Server Statistics Display System
#
# Copyright (C) 2021
# Amy Parker. All rights reserved.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; only version 2 is in compliance.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# You can also contact the creator of this program for the address of
# the Free Software Foundation to receive a copy of the License by mail.
#

import psutil


class Result:
    def __init__(self):
        # make this more efficient by only calling psutil.somefunction only once?
        self.api = 1
        self.cpu = {
            # the use of psutil here allows for this to be detected on windows.
            # however, on windows, it can sometimes not function correctly.
            # this can be found in the documentation for psutil. it emulates
            # posix process load
            "load_1m": psutil.getloadavg()[0],
            "load_5m": psutil.getloadavg()[1],
            "load_15m": psutil.getloadavg()[2],
            "nproc": psutil.cpu_count(),
            # this interval is arbitrary and should be regularly overridden
            # also, percentage utilization is an innacurate measurement.
            # todo: add load current
            "sys": psutil.cpu_percent(interval=None)
        }
        self.mem = {
            "total": psutil.virtual_memory().total,
            "available": psutil.virtual_memory().available
        }
        # todo: fix these problems
        # there are notable problems here. for one thing, per the psutil docs:
        #
        # UNIX usually reserves 5% of the total disk space for the root user. total
        # and used fields on UNIX refer to the overall total and used space, whereas
        # free represents the space available for the user and percent represents the
        # user utilization (see source code). That is why percent value may look 5%
        # bigger than what you would expect it to be.
        #
        # this does not work on Windows; Windows would require patching for C:\. in
        # addition, POSIX systems without a root won't work. This will throw a lot of
        # OSErrors which can be patched out later.
        self.disk = {
            "rsize": psutil.disk_usage('/').total,
            "rused": psutil.disk_usage('/').used
        }
        # todo: add the following
        # - system uptime
        # - temperatures system
        # - network stats
