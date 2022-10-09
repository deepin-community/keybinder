"""
``keybinder`` is a python module for registering global key bindings,
for gtk-based applications.

This module originates in `Tomboy`_ and has been widely reused without
having a separate release. This package has taken the python module
for Tomboy's keybinder from the `Deskbar Applet`_ project, and broken
it out to a standalone module.

The module is licenced under the GNU General Public License v2 (or at
your option, any later version), see the included file COPYING for
details.

.. _Tomboy:            http://projects.gnome.org/tomboy/
.. _`Deskbar Applet`:  http://projects.gnome.org/deskbar-applet/

Homepage: http://kaizer.se/wiki/python-keybinder/
"""

__version__ = "0.3.1"

# gtk has to be setup
# this is to avoid warning spew if you plainly
# import keybinder; normally applications always use gtk themselves
import gtk
from _keybinder import *
