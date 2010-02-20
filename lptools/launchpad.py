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

__all__ = [
    'Launchpad',
    ]

"""Wrapper class for launchpadlib with tweaks."""

from launchpadlib.launchpad import Launchpad as UpstreamLaunchpad

class Launchpad(UpstreamLaunchpad):
    """Launchpad object with bugfixes."""

    def load(self, url_string):
        """Load an object.
        
        Extended to support url_string being a relative url.
        """
        if not url_string.startswith('https:'):
            return UpstreamLaunchpad.load(self, str(self._root_uri) + url_string)
        else:
            return UpstreamLaunchpad.load(self, url_string)
