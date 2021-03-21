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

import sys


def run(res: dict):
    if "api" not in res.keys():
        print(f"{sys.argv[0]}: error: malformed response:\n{res}")
    versions = {
        "1": v1
    }
    versions[str(res["api"])](res)


def v1(res: dict):
    print(f"API version: {res['api']}\n"
          f"CPU load 1m: {res['cpu']['load_1m']}\n"
          f"CPU load 5m: {res['cpu']['load_5m']}\n"
          f"CPU load 15m: {res['cpu']['load_15m']}\n"
          f"Logical processors: {res['cpu']['nproc']}\n"
          f"CPU estimated usage: {res['cpu']['sys']}\n"
          f"Total memory (bytes): {res['mem']['total']}\n"
          f"Available memory (bytes): {res['mem']['available']}\n"
          f"Root disk size: {res['disk']['rsize']}\n"
          f"Root disk used: {res['disk']['rused']}")
