#!/usr/bin/env python3
"""Rebuild tmp/inflight.txt from every batch file this campaign ever emitted.

Rationale: rounds r5-r10 kept the in-flight ledger by hand, so packages that were
still being rewritten were not recorded and a later round re-issued them.  This
script takes the union of every batch file (plus the existing ledger), drops the
batches whose remainders are being relaunched with explicit package lists, and
keeps only the packages that still fail a check - those are the ones that need
protection from double assignment.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path("tools").resolve()))
from audit_guided_examples import BOILERPLATE_MARKERS, FORBIDDEN_CODE_PATTERNS, count_tables  # noqa: E402

BATCHES = Path("tmp/batches")
LEDGER = Path("tmp/inflight.txt")
LEETCODE = Path("dsa/leetcode")

# Batches with no live agent whose remainders are relaunched by explicit list.
RELAUNCHED_BY_HAND = {"r9_boiler_003", "r10_boiler_001"}


def names_in(path: Path) -> set[str]:
    return {ln.strip() for ln in path.read_text(encoding="utf-8").splitlines() if ln.strip()}


def kind(name: str) -> str:
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


assigned: set[str] = set()
if LEDGER.is_file():
    assigned |= names_in(LEDGER)

batch_files = 0
for path in sorted(BATCHES.glob("*.txt")):
    if path.stem.endswith("_done") or path.stem in RELAUNCHED_BY_HAND:
        continue
    assigned |= names_in(path)
    batch_files += 1

for stem in RELAUNCHED_BY_HAND:
    path = BATCHES / f"{stem}.txt"
    if path.is_file():
        assigned -= names_in(path)

counts: dict[str, int] = {}
kept = []
for name in sorted(assigned):
    state = kind(name)
    counts[state] = counts.get(state, 0) + 1
    if state in ("leak", "boiler", "tables"):
        kept.append(name)

LEDGER.write_text("\n".join(kept) + "\n", encoding="utf-8")
print(f"batch files read: {batch_files}")
print(f"distinct packages ever assigned: {len(assigned)}  ({counts})")
print(f"ledger rebuilt with {len(kept)} unresolved in-flight packages")