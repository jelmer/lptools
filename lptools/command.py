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

"""Command abstraction for the CLI parts of lptools.

To use:

* in your front end script define a docstring - this is used for global help.

* from this module import *

* derive commands from LaunchpadCommand and call them cmd_NAME.

* At the bottom of your script, do::

  if __name__ == '__main__':
      main()
"""

__all__ = [
    'LaunchpadCommand',
    'main',
    ]

from bzrlib import commands, ui, version_info as bzr_version_info
import sys

def list_commands(command_names):
    mod = sys.modules['__main__']
    command_names.update(commands._scan_module_for_commands(mod))
    return command_names


def get_command(cmd_or_None, cmd_name):
    if cmd_name is None:
        return cmd_help()
    elif cmd_name == 'help':
        return cmd_help()
    try:
        return sys.modules['__main__']['cmd_' + cmd_name]()
    except KeyError:
        return cmd_or_None


class LaunchpadCommand(commands.Command):
    """Base class for commands working with launchpad."""

    def run_argv_aliases(self, argv, alias_argv=None):
        # This might not be unique-enough for a cachedir; can do
        # lp-milestones/cmdname if needed.
        self.launchpad = config.get_launchpad('lp-milestones')
        return commands.Command.run_argv_aliases(self, argv, alias_argv)


class cmd_help(commands.Command):
    """Show help on a command or other topic."""

    # Can't use the stock bzrlib help, because the help indices aren't quite
    # generic enough.
    takes_args = ['topic?']
    def run(self, topic=None):
        if topic is None:
            self.outf.write(sys.modules['__main__'].__doc__)
        else:
            import bzrlib.help
            bzrlib.help.help(topic)


def do_run_bzr(argv):
    if bzr_version_info > (2, 2, 0):
        # in bzr 2.2 we can disable bzr plugins so bzr commands don't show
        # up.
        return commands.run_bzr(argv, lambda:None, lambda:None)
    else:
        return commands.run_bzr(argv)


def main():
    commands.Command.hooks.install_named_hook('list_commands', list_commands,
        "list")
    commands.Command.hooks.install_named_hook('get_command', get_command,
        "get")
    ui.ui_factory = ui.make_ui_for_terminal(sys.stdin, sys.stdout, sys.stderr)
    sys.exit(commands.exception_to_return_code(do_run_bzr, sys.argv[1:]))
