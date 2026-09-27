#!/usr/bin/env python3
"""Derive the next work round from the live audit state.

Classification is exclusive and priority-ordered, exactly like the audit:
  1. code leak   - a forbidden language fence is still present
  2. boilerplate - a known template filler string is still present
  3. table debt  - fewer than two real GFM tables

Usage: python tmp/next_round.py <round-label> [boiler_batch] [boiler_count] [table_batch] [table_count]
Every round recomputes from the worktree, so a batch that already passed is
simply not re-emitted; rounds are idempotent and safe to re-run.

Parallel safety
---------------
`tmp/inflight.txt` is the in-flight ledger. Packages named there are skipped so a
second round can be launched while the first is still running without assigning
one package to two agents. Earlier rounds kept that file by hand and forgot to
record their own assignments, which let round 10 re-issue packages that round 9
was still rewriting; both agents then overwrote each other's lessons.

The ledger is therefore maintained automatically now:

* every batch this script emits is appended to the ledger as it is written;
* `--prune` (also run at the start of every derivation) drops ledger entries
  whose package now passes every check, because landed work no longer needs
  protection;
* `--settle <batch-file>` drops one batch's packages, for when a batch has been
  abandoned or its remainder is being relaunched with an explicit package list.

Usage notes: `--settle` accepts a path or a bare batch name under tmp/batches/.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path("tools").resolve()))
from audit_guided_examples import BOILERPLATE_MARKERS, FORBIDDEN_CODE_PATTERNS, count_tables  # noqa: E402

LEETCODE = Path("dsa/leetcode")
BATCHES = Path("tmp/batches")
LEDGER = Path("tmp/inflight.txt")


def read_ledger() -> set[str]:
    if not LEDGER.is_file():
        return set()
    return {ln.strip() for ln in LEDGER.read_text(encoding="utf-8").splitlines() if ln.strip()}


def write_ledger(names: set[str]) -> None:
    LEDGER.write_text("\n".join(sorted(names)) + ("\n" if names else ""), encoding="utf-8")


def classify(name: str) -> str:
    """Return 'leak', 'boiler', 'tables', 'ok' or 'missing' for one package."""
    path = LEETCODE / name / "guided_example.md"
    if not path.is_file():
        return "missing"
    text = path.read_text(encoding="utf-8")
    if any(pat.search(text) for pat, _ in FORBIDDEN_CODE_PATTERNS):
        return "leak"
    if any(marker in text for marker in BOILERPLATE_MARKERS):
        return "boiler"
    if count_tables(text) < 2:
        return "tables"
    return "ok"


def prune(ledger: set[str]) -> set[str]:
    """Drop entries whose package no longer needs protection."""
    return {name for name in ledger if classify(name) not in ("ok", "missing")}


def settle(target: str) -> None:
    path = Path(target)
    if not path.is_file():
        path = BATCHES / (target if target.endswith(".txt") else f"{target}.txt")
    if not path.is_file():
        raise SystemExit(f"settle: no such batch file: {target}")
    names = {ln.strip() for ln in path.read_text(encoding="utf-8").splitlines() if ln.strip()}
    before = read_ledger()
    write_ledger(before - names)
    print(f"settled {path.name}: removed {len(before & names)}, ledger now {len(before - names)}")


if len(sys.argv) > 1 and sys.argv[1] == "--settle":
    settle(sys.argv[2])
    raise SystemExit(0)

label = sys.argv[1] if len(sys.argv) > 1 else "r"
# Two independent numbers per kind: the *size* of one batch and the *total*
# number of packages to hand out this round. Passing a size where a total was
# meant still runs, but emits one full batch plus a short remainder file - which
# is how r12_boiler_002 came to hold a single package and r12_tables_002 three.
# The plan line below makes that visible before any agent is launched.
boiler_batch = int(sys.argv[2]) if len(sys.argv) > 2 else 6
boiler_count = int(sys.argv[3]) if len(sys.argv) > 3 else 30
table_batch = int(sys.argv[4]) if len(sys.argv) > 4 else 8
table_count = int(sys.argv[5]) if len(sys.argv) > 5 else 40

if boiler_count < boiler_batch or table_count < table_batch:
    raise SystemExit(
        f"refusing to run: a total ({boiler_count}, {table_count}) smaller than one "
        f"batch size ({boiler_batch}, {table_batch}) is almost certainly an "
        f"argument-order mistake; the signature is "
        f"<label> <boiler_size> <boiler_total> <table_size> <table_total>"
    )

inflight = prune(read_ledger())
write_ledger(inflight)

leaks, boiler, tables = [], [], []
for pkg in sorted(LEETCODE.iterdir()):
    if not pkg.is_dir() or not (pkg / "metadata.json").is_file():
        continue
    if pkg.name in inflight:
        continue
    kind = classify(pkg.name)
    if kind == "leak":
        leaks.append(pkg.name)
    elif kind == "boiler":
        boiler.append(pkg.name)
    elif kind == "tables":
        tables.append(pkg.name)

print(f"in-flight (skipped): {len(inflight)}")
print(f"remaining: leaks={len(leaks)} boilerplate={len(boiler)} table_debt={len(tables)}")
print(f"  next leak head      : {leaks[:3]}")
print(f"  next boilerplate head: {boiler[:3]}")
print(f"  next table head     : {tables[:3]}")

boiler_take = min(boiler_count, len(boiler))
table_take = min(table_count, len(tables))
print(
    f"plan: boilerplate {boiler_take} packages in batches of {boiler_batch} -> "
    f"{-(-boiler_take // boiler_batch)} file(s); tables {table_take} in batches of "
    f"{table_batch} -> {-(-table_take // table_batch)} file(s)"
)

BATCHES.mkdir(parents=True, exist_ok=True)
assigned: set[str] = set()


def emit(prefix: str, items: list[str]) -> None:
    for index, group in enumerate(
        (items[i : i + size] for i in range(0, len(items), size)), start=1
    ):
        (BATCHES / f"{prefix}_{index:03d}.txt").write_text(
            "\n".join(group) + "\n", encoding="utf-8"
        )
        assigned.update(group)
        print(f"  {prefix}_{index:03d}.txt -> {len(group)} packages  ({group[0]} .. {group[-1]})")


size = boiler_batch
emit(f"{label}_boiler", boiler[:boiler_count])
size = table_batch
emit(f"{label}_tables", tables[:table_count])

# Record what was just handed out so the next derivation cannot re-issue it.
write_ledger(inflight | assigned)
print(f"ledger: {len(inflight)} -> {len(inflight | assigned)} entries")