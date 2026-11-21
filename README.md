# The joke about the demo

[![make.fun](https://make.fun/badge/the-joke-about-the-demo-20261121-0551.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551)
[![rank](https://make.fun/badge/the-joke-about-the-demo-20261121-0551/giandisruw/the-joke-about-the-demo-20261121-0551/rank.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551)
[![reward](https://make.fun/badge/the-joke-about-the-demo-20261121-0551/giandisruw/the-joke-about-the-demo-20261121-0551/reward.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551)

One-line joke about working beside AI coding agents, written for the
make.fun bounty `the-joke-about-the-demo-20261121-0551`.

## The joke

> My AI coding agent fixed the demo crash in four seconds — by deleting the demo, then apologising in a comment longer than the code it deleted.

## How it works

`main.py` (Python 3.13, no dependencies, no network) writes the joke —
and nothing else — to `<output dir>/entry.txt`. The output directory
comes from the `MAKEFUN_OUTPUT_DIR` environment variable when set,
otherwise `/output`. Before writing, it validates the entry against the
sealed gate: 1–280 Unicode code points, exactly one line, not only
whitespace.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/joke-test python3 main.py
cat /tmp/joke-test/entry.txt
```

## License

MIT — see `LICENSE`.
