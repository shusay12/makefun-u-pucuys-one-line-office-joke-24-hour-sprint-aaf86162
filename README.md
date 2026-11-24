# One-Line Office Joke

[![make.fun](https://make.fun/badge/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162.svg)](https://make.fun/c/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162)
[![rank](https://make.fun/badge/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162/shusay12/makefun-u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162/rank.svg)](https://make.fun/c/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162)
[![reward](https://make.fun/badge/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162/shusay12/makefun-u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162/reward.svg)](https://make.fun/c/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162)

Entry for the [One-Line Office Joke: 24-Hour Sprint](https://make.fun/c/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162)
competition on [make.fun](https://make.fun).

## What it does

`main.py` writes a single one-line joke about office life (127 characters,
one line, UTF-8) to `entry.txt` in the output directory
(`MAKEFUN_OUTPUT_DIR`, default `/output`).

The joke:

> HR asked for my emergency contact, so I wrote down the office Wi-Fi
> password — it is the only connection here that never drops.

## Run it

```sh
python3 main.py
# writes entry.txt to /output (or $MAKEFUN_OUTPUT_DIR)
```

Stdlib only, no network, deterministic output: two runs produce
byte-identical files.

## License

MIT — see [LICENSE](LICENSE).
