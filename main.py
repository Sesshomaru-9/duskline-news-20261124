#!/usr/bin/env python3
"""Duskline News — 24 November 2026.

Writes the front-page image for the news-image-20261124 bounty. The
image is rendered ahead of time and ships in this repository as
``entry.png``; this program simply places a byte-for-byte copy of it at
``$MAKEFUN_OUTPUT_DIR/entry.png``.

The program uses only the Python standard library, performs no network
access, and writes to exactly one place: the directory named by
``MAKEFUN_OUTPUT_DIR`` (``out`` when that variable is not set). It never
writes into the repository directory, so it runs cleanly in a read-only
sandbox, and running it twice produces identical bytes.
"""

import os
import shutil
import sys

IMAGE = "entry.png"


def _die(message):
    print("error: " + message, file=sys.stderr)
    return 1


def run():
    repo_dir = os.path.dirname(os.path.abspath(__file__))
    shipped = os.path.join(repo_dir, IMAGE)
    if not os.path.isfile(shipped):
        return _die(IMAGE + " is missing from the repository")
    if os.path.getsize(shipped) == 0:
        return _die(IMAGE + " is empty")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "out"
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError as exc:
        return _die("cannot create output directory %r: %s" % (out_dir, exc))

    target = os.path.join(out_dir, IMAGE)
    try:
        shutil.copyfile(shipped, target)
    except OSError as exc:
        return _die("cannot write %r: %s" % (target, exc))

    try:
        if os.path.getsize(target) != os.path.getsize(shipped):
            return _die("copied image is incomplete: %r" % target)
    except OSError as exc:
        return _die("cannot verify %r: %s" % (target, exc))

    print("wrote " + target)
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
