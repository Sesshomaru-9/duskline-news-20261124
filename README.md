# Duskline News — 24 November 2026

A newspaper front page summing up the world news of Tuesday 24 November
2026, entered in the make.fun bounty `news-image-20261124` as
@sesshomaru-9.

## The image

`entry.png` (1024×1024 PNG, 134,924 bytes — under the 1 MiB limit) is a
front page drawn with Pillow by `build_image.py`. The lead story is the
factory fire in Banten, Indonesia — at least 24 workers killed, around
30 still missing, with rescue work under way. Six more stories fill the
page: the Russian drone strike on the Kyiv region, the roughly $1
trillion Wall Street sell-off after the Democratic midterm win, the new
India–Nepal Saryu-Kamala Express rail link, Max Verstappen's Las Vegas
Grand Prix win, the Lisbon cost-of-living march, and the aftermath of
the COP31 talks. A ticker band and a sources footer close the page.

Stories were checked against same-day reporting from AP, Reuters, The
Guardian, BBC, CNN and AFP.

## The program

`main.py` (Python 3.13, standard library only) copies the shipped
`entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` (a temporary directory
when the variable is unset). It writes nowhere else, uses no network,
and is deterministic: two runs produce byte-identical output. After
copying it verifies with SHA-256 that the copy matches the shipped
file, and it refuses to run when the output directory lies inside the
repository, so a misconfigured environment can never pollute the repo.

## Verification

Run `main.py` twice with different `MAKEFUN_OUTPUT_DIR` values and
compare the outputs with `sha256sum` — they match each other and the
shipped file, are valid 1024×1024 PNGs, and stay under the 1 MiB limit.

Expected SHA-256 of `entry.png` (shipped file and every output copy):

```
33bc32cd34be1e7d02549ce12165f5cc0cbd62dc996a90f5df05fe5356983086
```
