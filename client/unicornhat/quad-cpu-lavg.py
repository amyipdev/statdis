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

def run(hosts: list, brightness: float):
    unicornhat.set_all(0, 0, 0)
    unicornhat.brightness(brightness)
    unicornhat.show()
    alive = True
    while alive:
        try:
            util = [{}, {}, {}, {}]
            for x in range(4):
                res = requests.get(f"http://{hosts[x]}").json()
                util[x] = {
                    "id": x,
                    "util": res["cpu"]["load_1m"] / res["cpu"]["nproc"]
                }
            for x in util:
                update_quadrant(x["util"], x["id"])
        except KeyboardInterrupt:
            alive = False
        time.sleep(0.5)
    unicornhat.off()

def update_quadrant(util: float, qn: int):
    bx = (qn & 2) * 2
    by = (qn & 1) * 4
    r = int((0 + util) * 255)
    g = int((1 - util) * 255)
    for ax in range(4):
        for ay in range(4):
            unicornhat.set_pixel(ax + bx, ay + by, r, g, 0)
    unicornhat.show()

if len(sys.argv) < 5:
    print("error: please provide at least 5 hosts")

brightness = 0.5
if len(sys.argv) == 6:
    brightness = float(sys.argv[5])

run(sys.argv[1:5], brightness)
