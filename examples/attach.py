"""
Example showing `pwnlib.gdb.attach()`
"""
from __future__ import annotations

from pwn import *

bash = process("/bin/bash")
gdb.attach(
    bash,
    gdbscript="""
p "hello from pwnlib"
c
""",
)
bash.interactive()
