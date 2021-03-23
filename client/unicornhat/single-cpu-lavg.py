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
import time

import requests
import unicornhat

def run(host: str, brightness: float):
    unicornhat.set_all(0, 0, 0)
    unicornhat.brightness(brightness)
    unicornhat.show()
    alive = True
    while alive:
        try:
            res = requests.get(f"http://{host}").json()
            util = res["load_1m"] / res["nproc"]
            red = (0 + util) * 255
            green = (1 - util) * 255
            unicornhat.set_all(int(red), int(green), 0)
            unicornhat.show()
            time.sleep(0.5)
        except KeyboardInterrupt:
            alive = False


if len(sys.argv) < 2:
    print("error: you must provide a host")
    sys.exit(1)

brightness = 0.5
if len(sys.argv) == 3:
    brightness = float(sys.argv[2])

run(sys.argv[1], brightness)
