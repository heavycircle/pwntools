"""
Encode shellcode to avoid input filtering and impress your friends!
"""
from __future__ import annotations

from pwnlib.encoders import amd64, arm, i386, mips
from pwnlib.encoders.encoder import Encoder, alphanumeric, encode, line, null, printable, scramble
