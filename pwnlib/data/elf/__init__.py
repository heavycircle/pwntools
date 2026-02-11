from __future__ import annotations

import os

from pwnlib.data.elf import fmtstr, relro, ret2dlresolve

path = os.path.dirname(__file__)


def get(x):
    return os.path.join(path, x)
