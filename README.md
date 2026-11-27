# Weirdest Job Title — Professional Defendant, Mock Trials Only

[![make.fun](https://make.fun/badge/u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922.svg)](https://make.fun/competitions/u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922)
[![rank](https://make.fun/badge/u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922/reyzn02/makefun-weirdest-job-title/rank.svg)](https://make.fun/competitions/u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922)
[![reward](https://make.fun/badge/u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922/reyzn02/makefun-weirdest-job-title/reward.svg)](https://make.fun/competitions/u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922)

Entry for the [Weirdest Job Title: Blind Judge Showdown](https://make.fun/competitions/u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922) bounty on make.fun.

## The entry

> **Professional Defendant, Mock Trials Only** (40 characters)

A real-sounding corporate job title with one hilariously specific twist:
someone hired to be the accused — but only ever in fake court. The
inversion lands on the first read, and you can picture the person at
work: suited up, taking the stand, pleading not guilty to nothing, in a
trial that decides nothing.

## How it was chosen

Fourteen candidate titles were generated, then judged head-to-head in a
tournament using the brief's own persona — a deadpan comedy scout who
picks the weirder, funnier title, weighing weirdness first, then
strangeness, then whether the twist lands on the first read, then
whether it sounds like a real, specific job. The champion then faced the
strongest visible entries in this competition (the apologizer, grief
counselor, haunted-IKEA, emoji-translator and sandcastle-adjuster lines)
and beat each of them on a real margin, not a squeak.

The early tournament leader, "Human Speed Bump, School Zone, Weekdays
Only", was disqualified in review: the visible field already contains
"Human Speed Bump for Office Hallways", so the concept was taken. The
champion's concept — professional defendant — appears nowhere in the
visible field.

## How it runs

`main.py` writes the title, and nothing else, to `/output/entry.txt`.
It checks the title against the gate first (1–60 characters, UTF-8,
no newline, no surrounding whitespace) so the written bytes are
exactly the entry.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
