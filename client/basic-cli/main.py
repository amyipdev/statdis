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

import requests

import api

if len(sys.argv) < 2:
    print(f"{sys.argv[0]}: error: you must provide a host, add -h for help")
    sys.exit(1)

if "-h" in sys.argv:
    print(f"run '{sys.argv[0]} <HOST>' to check a host")
    sys.exit(1)

res = {}
if len(sys.argv) == 3:
    res = requests.get(f"http://{sys.argv[1]}:{sys.argv[2]}").json()
else:
    res = requests.get(f"http://{sys.argv[1]}:11927").json()

api.run(res)
