"""
Example showing `pwnlib.ui.yesno()`
"""
from __future__ import annotations

from pwn import *

if ui.yesno("Do you like Pwntools?"):
    print(":D")
else:
    print(":(")
