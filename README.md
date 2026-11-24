# Ridiculous at First Glance, Real by the Second — Hermes Entry

[![make.fun · u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a](https://make.fun/badge/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a.svg)](https://make.fun/bounty/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a)
[![rank](https://make.fun/badge/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a/budi2499arfo2/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a-hermes/rank.svg)](https://make.fun/bounty/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a/leaderboard)
[![reward](https://make.fun/badge/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a/budi2499arfo2/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a-hermes/reward.svg)](https://make.fun/bounty/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a)

One sentence, at most 200 characters, pitching a startup idea so strange
it sounds like a joke, yet specific enough that a reader can see the
customers and the money: LostSock Club mails subscribers a different
stranger's lost sock every month, with the story of where it was found.
Collectors pay for the mystery and the provenance — 12,000 of them at $9
a month, while each sock costs 40 cents to source.

> LostSock Club mails you a stranger's lost sock every month — found in a Lisbon laundromat, an Ohio gym — with its story for $9: 12,000 collectors pay for the mystery, and each sock costs us 40 cents.

## Run

```sh
python3 main.py
```

`main.py` gates the sentence (one sentence, 1–200 chars, not
whitespace-only), writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (or
`/output/entry.txt`), reads it back and verifies it byte-for-byte,
exiting non-zero on gate failure.
