# Get all the modules from pwnlib
from __future__ import annotations

from pwnlib import *
from pwnlib.asm import *
from pwnlib.encoders import *
from pwnlib.filepointer import *
from pwnlib.filesystem import *
from pwnlib.flag import *
from pwnlib.log import getLogger
from pwnlib.regsort import *
from pwnlib.replacements import *
from pwnlib.runner import *
from pwnlib.ui import *
from pwnlib.util.cyclic import *
from pwnlib.util.fiddling import *
from pwnlib.util.getdents import *
from pwnlib.util.hashes import *
from pwnlib.util.lists import *
from pwnlib.util.misc import *
from pwnlib.util.packing import *
from pwnlib.util.splash import *
from pwnlib.util.web import *

# Promote these modules, so that "from pwn import *" will let you access them


log = getLogger("pwnlib.exploit")
error = log.error
warning = log.warning
warn = log.warning
info = log.info
debug = log.debug
success = log.success

try:
    import colored_traceback
except ImportError:
    pass
else:
    try:
        colored_traceback.add_hook()
    except Exception:
        # Exception: curses.error
        # colored_traceback (curses.setupterm()) fails if TERM is unset.
        # This is not critical, so we just ignore it.
        # We cannot import `curses` for `curses.error` because it is not
        # available on all platforms (e.g. Windows).
        pass

# Equivalence with the default behavior of "from import *"
# __all__ = [x for x in tuple(globals()) if not x.startswith('_')]
