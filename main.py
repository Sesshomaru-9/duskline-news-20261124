#!/usr/bin/env python3
"""Duskline News -- 24 November 2026.

Front-page image for the make.fun bounty ``news-image-20261124``
("Sum up 24 November's world news in one image"), entered as
@sesshomaru-9.

The image is rendered ahead of time and ships in this repository as
``entry.png``; this program simply places a byte-for-byte copy of it at
``$MAKEFUN_OUTPUT_DIR/entry.png``.

The program uses only the Python standard library, performs no network
access, and writes to exactly one place: the directory named by the
``MAKEFUN_OUTPUT_DIR`` environment variable (a temporary directory when
that variable is not set). It never writes into the repository directory,
so it runs cleanly in a read-only sandbox, and running it twice produces
identical bytes. After copying, it verifies with SHA-256 that the copy
matches the shipped file byte for byte. As a safety net, it refuses to
run at all when the requested output directory lies inside the
repository, so a misconfigured environment can never pollute the repo.
"""

import hashlib
import os
import shutil
import sys
import tempfile

IMAGE = "entry.png"


def _sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


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

    try:
        source_hash = _sha256(shipped)
    except OSError as exc:
        return _die("cannot read %r: %s" % (shipped, exc))

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or tempfile.gettempdir()
    out_dir_abs = os.path.abspath(out_dir)
    if os.path.commonpath([out_dir_abs, repo_dir]) == repo_dir:
        return _die("output directory %r is inside the repository; "
                    "set MAKEFUN_OUTPUT_DIR elsewhere" % out_dir)
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
        copied_hash = _sha256(target)
    except OSError as exc:
        return _die("cannot verify %r: %s" % (target, exc))
    if copied_hash != source_hash:
        return _die("copied image does not match the shipped file "
                     "(sha256 mismatch)")

    print("wrote " + target + " (sha256 " + copied_hash + ")")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
