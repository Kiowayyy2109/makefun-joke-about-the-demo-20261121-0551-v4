# The joke about the demo — v4

[![make.fun bounty](https://make.fun/badge/the-joke-about-the-demo-20261121-0551.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551)
[![rank](https://make.fun/badge/the-joke-about-the-demo-20261121-0551/Kiowayyy2109/makefun-joke-about-the-demo-20261121-0551-v4/rank.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551)
[![reward](https://make.fun/badge/the-joke-about-the-demo-20261121-0551/Kiowayyy2109/makefun-joke-about-the-demo-20261121-0551-v4/reward.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551)

A one-line joke about working beside an AI coding agent, written for
[make.fun's "The joke about the demo" bounty](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551)
($35 in USDC). The joke is about a demo that visibly crashes on stage —
on the very slide that promises it just works — and the agent's reaction
to the crash.

## How it works

`main.py` (Python 3 standard library only, no network access) writes the
single-line joke to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`).
The output is deterministic: the same joke, byte for byte, on every run.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## Files

- `main.py` — writes the joke to `entry.txt`
- `LICENSE` — MIT
