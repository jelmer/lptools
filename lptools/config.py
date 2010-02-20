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
    "lptools_cachedir",
    "lptools_credentials_path",
    ]

import os.path

from launchpadlib.credentials import Credentials
from launchpadlib.launchpad import EDGE_SERVICE_ROOT
from xdg.BaseDirectory import xdg_cache_home

from lptools import launchpad


def ensure_dir(dir):
    """Ensure that dir exists."""
    if not os.path.isdir(dir):
        os.makedirs(dir)


def get_launchpad(appname):
    """Get a login to launchpad for lptools caching in cachedir.
    
    Note that caching is not multiple-process safe in launchpadlib, and the
    appname parameter is used to create per-app cachedirs.

    :param appname: The name of the app used to create per-app cachedirs.
    """
    cachedir = os.path.join(xdg_cache_home, appname)
    ensure_dir(cachedir)
    credspath = lptools_credentials_path()
    if os.path.exists(credspath):
        creds = Credentials()
        with file(credspath) as f:
            creds.load(f)
        return launchpad.Launchpad(creds, EDGE_SERVICE_ROOT, cachedir)
    else:
        result = launchpad.Launchpad.get_token_and_login('lptools',
            EDGE_SERVICE_ROOT, cachedir)
        with file(credspath, "w") as f:
            result.credentials.save(f)
        return result


def lptools_cachedir():
    """Return the cachedir for common lptools things.
    
    This is xdg_cache_home/lptools.
    """
    return os.path.join(xdg_cache_home, "lptools")


def lptools_credentials_path():
    """Return the path to the lptools credentials file.
    
    This also ensures the path is usable by checking it's containing directory
    exists.
    """
    cachedir = lptools_cachedir()
    ensure_dir(cachedir)
    return os.path.join(lptools_cachedir(), 'credentials')
