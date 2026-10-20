#!/usr/bin/env python3
"""Konverter mellom hex, tekst, base64 og ASCII-koder.

Bruk:
    python hexconv.py hex2text 63727970746f
    python hexconv.py hex2b64 72bca9b68fc1
    python hexconv.py text2hex crypto
    python hexconv.py codes2text 99 114 121 112 116 111
"""
import base64
import sys


def hex2bytes(s: str) -> bytes:
    return bytes.fromhex(s.replace(" ", "").replace("0x", ""))


COMMANDS = {
    "hex2text": lambda a: hex2bytes("".join(a)).decode("ascii", errors="replace"),
    "hex2b64": lambda a: base64.b64encode(hex2bytes("".join(a))).decode("ascii"),
    "b642hex": lambda a: base64.b64decode("".join(a)).hex(),
    "text2hex": lambda a: " ".join(a).encode().hex(),
    "codes2text": lambda a: "".join(chr(int(x)) for x in a),
}


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if len(argv) < 2 or argv[0] not in COMMANDS:
        print(__doc__.strip())
        return 1
    print(COMMANDS[argv[0]](argv[1:]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
