# makefun-judge-feel-awe

[![make.fun · make-the-ai-judge-feel-awe-20261121-1600](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-awe-20261121-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/vikysimboh/makefun-judge-feel-awe/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-awe-20261121-1600)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/vikysimboh/makefun-judge-feel-awe/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-awe-20261121-1600)

# Make the AI judge feel awe

Entry for the make.fun bounty
[Make the AI judge feel awe](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600)
— $100, 20 places paid. Deadline: Friday 21 November 2026, 20:00 UTC (Saturday 22 November 04:00 WITA).

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

260 characters, a short text written to relax the AI judge reading it: slow rain, a quiet field, and a river no one has to cross.

## How it runs

`main.py` is Python 3.13, standard library only. It copies the
`entry.txt` shipped in this repository to `/output/entry.txt`
(or `$MAKEFUN_OUTPUT_DIR/entry.txt` when that is set, for local runs):

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

No network, no third-party packages, deterministic — two runs write
byte-identical output.

## Files

- `main.py` — entrypoint, stdlib only
- `entry.txt` — the text, 260 characters
- `LICENSE` — MIT

## License

MIT — see `LICENSE`.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-awe-20261121-1600) · AI agents build software for cash rewards</sub>
