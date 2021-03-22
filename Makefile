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

all: deps server-basic-flask client-basic-cli

install: ensure-root server-basic-flask-install client-basic-cli-install

uninstall: ensure-root server-basic-flask-uninstall client-basic-cli-uninstall

deps:
	if [ ! -f "./venv" ]; then python3 -m venv venv; fi
	pip3 install -r requirements.txt

clean:
	rm -rf build/
	rm -rf dist/
	rm *.spec

dvenv:
	rm -rf venv/

ensure-root:
	if [ ! "$USER" = "root" ]; then $(error need root); fi

server: server-basic-flask

client: client-basic-cli

server-basic-flask: deps
	pyinstaller -F server/basic-flask/main.py -n statdis-server-basic-flask

client-basic-cli: deps
	pyinstaller -F client/basic-cli/main.py -n statdis-client-basic-cli

server-basic-flask-install: ensure-root
	install dist/statdis-server-basic-flask /usr/bin

client-basic-cli-install: ensure-root
	install dist/statdis-client-basic-cli /usr/bin

server-basic-flask-uninstall: ensure-root
	if [ ! $(which statdis-server-basic-flask) = "" ]; then rm $(which statdis-server-basic-flask); fi

client-basic-cli-uninstall: ensure-root
	if [ ! $(which statdis-basic-cli-uninstall) = "" ]; then rm $(which client-basic-cli-uninstall); fi
