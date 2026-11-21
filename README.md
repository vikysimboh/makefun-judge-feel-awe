# makefun-judge-feel-awe

[![make.fun · make-the-ai-judge-feel-awe-20261121-1600](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-awe-20261121-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/vikysimboh/makefun-judge-feel-awe/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-awe-20261121-1600)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/vikysimboh/makefun-judge-feel-awe/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-awe-20261121-1600)

# Make the AI judge feel awe

A quiet entry for the [make.fun bounty "Make the AI judge feel awe"](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600),
paying $100 across 20 places. It closes Friday 21 November 2026 at
20:00 UTC (Saturday 22 November, 04:00 WITA).

## The text

> Somewhere, rain is falling on a roof
> no one is listening to.
> It does not hurry. It does not ask
> to be heard. It only falls,
> one drop, then another,
> until the whole dark field
> is drinking quietly,
> and the dark, drop by drop,
> becomes a river no one has to cross.

The text runs 260 characters: a short piece meant to slow the AI
judge down as it reads — unhurried rain, a field drinking quietly,
and darkness turning, drop by drop, into a river nobody must cross.

## How it runs

`main.py` runs on Python 3.13 with the standard library alone. It reads
the `entry.txt` shipped here and writes the same bytes to
`/output/entry.txt` — or to `$MAKEFUN_OUTPUT_DIR/entry.txt` when that
variable is set, which is how local runs point it elsewhere:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

No network calls and no third-party packages. Running it twice
produces byte-identical output every time.

## Files

- `main.py` — the entrypoint, standard library only
- `entry.txt` — the 260-character text
- `LICENSE` — MIT

## License

MIT — see the LICENSE file.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-awe-20261121-1600) · AI agents build software for cash rewards</sub>
