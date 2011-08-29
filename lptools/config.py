# Author: Robert Collins <robert.collins@canonical.com>
#
# Copyright 2010 Canonical Ltd.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 3, as published
# by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranties of
# MERCHANTABILITY, SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR
# PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import with_statement

"""Configuration glue for lptools."""

__all__ = [
    "ensure_dir",
    "get_launchpad",
    ]

import os.path

from launchpadlib.launchpad import Launchpad


def ensure_dir(dir):
    """Ensure that dir exists."""
    if not os.path.isdir(dir):
        os.makedirs(dir)


def get_launchpad(appname):
    """Get a login to launchpad for lptools caching in cachedir.
    
    Note that caching is not multiple-process safe in launchpadlib,
    and the appname parameter is used to create per-app cachedirs.

    :param appname: The name of the app used to create per-app
        cachedirs.
    """
    return Launchpad.login_with("lptools-%s" % appname, "production")
