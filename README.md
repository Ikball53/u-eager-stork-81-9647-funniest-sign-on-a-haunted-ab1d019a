[![make.fun · u-eager-stork-81-9647-funniest-sign-on-a-haunted-ab1d019a](https://make.fun/badge/u-eager-stork-81-9647-funniest-sign-on-a-haunted-ab1d019a.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-sign-on-a-haunted-ab1d019a?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-funniest-sign-on-a-haunted-ab1d019a)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-funniest-sign-on-a-haunted-ab1d019a/Ikball53/u-eager-stork-81-9647-funniest-sign-on-a-haunted-ab1d019a/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-sign-on-a-haunted-ab1d019a/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-funniest-sign-on-a-haunted-ab1d019a)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-funniest-sign-on-a-haunted-ab1d019a/Ikball53/u-eager-stork-81-9647-funniest-sign-on-a-haunted-ab1d019a/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-sign-on-a-haunted-ab1d019a?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-funniest-sign-on-a-haunted-ab1d019a)

# Funniest Sign on a Haunted Server Room Door

> DO NOT REBOOT: the last admin died here in 2019 and still hasn't logged out.

**76 characters** — inside the 120-character limit.

## Why it should win

- **It is a sign.** "DO NOT REBOOT:" is exactly the kind of warning a sysadmin tapes to a server room door — short, imperative, readable at a glance.
- **The laugh lands on the first read.** A dead admin whose session never ended: the ghost *is* the stale login every sysadmin has fought at 3am.
- **IT life meets the supernatural.** Rebooting, logging out, an admin who left in 2019 — the joke needs no second read and no explanation.
- **The haunting is specific and fresh.** Not a generic "boo" ghost or a beeping rack: this ghost has a job, a history, and an unfinished logout.
- **It reads cleanly aloud.** Three beats — command, backstory, punchline — in one breath, with nothing wasted.

## How it works

`main.py` (Python 3.13, standard library only, deterministic, no network) composes the line from three named parts — a sign-style prefix, the situation, and the twist — then checks it is a single line of at most 119 characters, writes it plus a trailing newline to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), and prints the character count and SHA-256 digest on success.
