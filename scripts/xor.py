#!/usr/bin/env python3
"""XOR med gjentatt nøkkel.

Skrevet til en reversing-oppgave der et program sammenlignet input med et
hardkodet, kryptert passord. XOR reverserer seg selv, så den samme funksjonen
både krypterer og dekrypterer.

Bruk:
    python xor.py --key jens --hex "2e212d08"
    python xor.py --key jens --text "hello" --out-hex
    python xor.py --key-hex 4142 --file data.bin
"""
import argparse
import sys


def xor(data: bytes, key: bytes) -> bytes:
    if not key:
        raise ValueError("nøkkelen kan ikke være tom")
    return bytes(b ^ key[i % len(key)] for i, b in enumerate(data))


def main(argv=None):
    p = argparse.ArgumentParser(description="XOR med gjentatt nøkkel")
    k = p.add_mutually_exclusive_group(required=True)
    k.add_argument("--key", help="nøkkel som tekst")
    k.add_argument("--key-hex", help="nøkkel som hex")
    d = p.add_mutually_exclusive_group(required=True)
    d.add_argument("--hex", help="input som hex, mellomrom og 0x er lov")
    d.add_argument("--text", help="input som tekst")
    d.add_argument("--file", help="input-fil")
    p.add_argument("--out-hex", action="store_true", help="skriv ut resultatet som hex")
    a = p.parse_args(argv)

    key = a.key.encode() if a.key is not None else bytes.fromhex(a.key_hex)
    if a.hex is not None:
        data = bytes.fromhex(a.hex.replace("0x", "").replace(",", " ").replace(" ", ""))
    elif a.text is not None:
        data = a.text.encode()
    else:
        with open(a.file, "rb") as f:
            data = f.read()

    out = xor(data, key)
    if a.out_hex:
        print(out.hex())
    else:
        sys.stdout.write(out.decode(errors="replace") + "\n")


if __name__ == "__main__":
    main()
