#!/usr/bin/env python3
"""Finn SQLite-databaser ut fra filheaderen, uansett filendelse.

Skrevet til mobiletterforskning, der databaser fra apper ofte mangler .db-endelse.
En fil regnes som SQLite hvis den starter med bytene b"SQLite format 3\\x00".

Bruk:
    python is_sqlite.py <fil eller mappe> [-r] [--only-hits]

Avslutter med kode 0 hvis minst én SQLite-fil ble funnet, ellers 1.

Lagre treffene i en fil:
    python is_sqlite.py ./data -r --only-hits > sqlite_hits.txt
"""
import argparse
from pathlib import Path
from typing import Iterator, Tuple

SQLITE_HEADER = b"SQLite format 3\x00"


def is_sqlite_file(path: Path) -> bool:
    try:
        with path.open("rb") as f:
            return f.read(len(SQLITE_HEADER)) == SQLITE_HEADER
    except OSError:
        return False


def scan_path(path: Path, recursive: bool = False) -> Iterator[Tuple[Path, bool]]:
    if path.is_file():
        yield path, is_sqlite_file(path)
        return
    if not path.is_dir():
        return
    files = path.rglob("*") if recursive else path.iterdir()
    for p in files:
        if p.is_file():
            yield p, is_sqlite_file(p)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Finn SQLite-databaser ut fra filheaderen")
    ap.add_argument("path", help="fil eller mappe som skal skannes")
    ap.add_argument("-r", "--recursive", action="store_true", help="skann også undermapper")
    ap.add_argument("--only-hits", action="store_true", help="skriv bare ut SQLite-filer")
    a = ap.parse_args(argv)

    found = False
    for p, hit in scan_path(Path(a.path), a.recursive):
        found = found or hit
        if hit:
            print(p if a.only_hits else f"{p}\tsqlite")
        elif not a.only_hits:
            print(f"{p}\tikke sqlite")
    return 0 if found else 1


if __name__ == "__main__":
    raise SystemExit(main())
