from __future__ import annotations

from pwnlib.commandline import (
    asm,
    checksec,
    common,
    constgrep,
    cyclic,
    debug,
    disablenx,
    disasm,
    elfdiff,
    elfpatch,
    errno,
    hex,
    libcdb,
    phd,
    pwnstrip,
    scramble,
    shellcraft,
    template,
    unhex,
    update,
    version,
)
from pwnlib.commandline.common import parser as parser

commands = {
    "asm": asm.main,
    "checksec": checksec.main,
    "constgrep": constgrep.main,
    "cyclic": cyclic.main,
    "debug": debug.main,
    "disasm": disasm.main,
    "disablenx": disablenx.main,
    "elfdiff": elfdiff.main,
    "elfpatch": elfpatch.main,
    "errno": errno.main,
    "hex": hex.main,
    "libcdb": libcdb.main,
    "phd": phd.main,
    "pwnstrip": pwnstrip.main,
    "scramble": scramble.main,
    "shellcraft": shellcraft.main,
    "template": template.main,
    "unhex": unhex.main,
    "update": update.main,
    "version": version.main,
}


def main():
    common.entrypoint(commands)


if __name__ == "__main__":
    main()
