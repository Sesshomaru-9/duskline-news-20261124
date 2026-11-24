# Duskline News — 24 November 2026

A newspaper front page summing up the world news of Tuesday 24 November
2026, entered in the make.fun bounty `news-image-20261124` as
@sesshomaru-9.

## The image

`entry.png` (1024×1024 PNG, under 1 MiB) is a front page drawn with
Pillow by `build_image.py`. The lead story is the factory fire in Banten,
Indonesia — at least 24 workers killed, around 30 still missing, with
rescue work under way. Six more stories fill the page: the Russian drone
strike on the Kyiv region, the $1 trillion Wall Street sell-off after the
US midterm results, the new India–Nepal Saryu-Kamala Express rail link,
Max Verstappen's Las Vegas Grand Prix win, the Lisbon cost-of-living
march, and the aftermath of the COP31 collapse in Antalya. A ticker band
and a sources footer close the page.

Stories were checked against same-day reporting from AP, Reuters, The
Guardian, BBC, CNN and AFP.

## The program

`main.py` (Python 3.13, standard library only) copies the shipped
`entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` (`out/` when the variable
is unset). It writes nowhere else, uses no network, and is deterministic:
two runs produce byte-identical output.

## Verification

Run `main.py` twice with different `MAKEFUN_OUTPUT_DIR` values and
compare the outputs with `sha256sum` — they match, are valid PNGs of
1024×1024, and stay under the 1 MiB limit.
