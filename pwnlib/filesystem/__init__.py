"""
Handles file abstraction for local vs. remote (via ssh)
"""
from __future__ import annotations

from pwnlib.filesystem.path import Path
from pwnlib.filesystem.ssh import SSHPath

__all__ = ["SSHPath", "Path"]
