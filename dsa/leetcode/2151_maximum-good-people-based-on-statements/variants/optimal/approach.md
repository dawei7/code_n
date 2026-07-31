## General

**Treat a classification as a bitmask**

With at most fifteen people, every good-or-bad classification can be
enumerated. Represent one classification by an $n$-bit mask: bit $i$ is one
exactly when person $i$ is assumed good.

For each mask, inspect only rows belonging to people marked good. Every `0` or
`1` in such a row must equal the corresponding target bit; a `2` imposes no
condition. Rows belonging to people marked bad are ignored because bad people
may either lie or tell the truth. Reject the mask at its first mismatch.

A mask that survives all checks is consistent because every required truthful
statement matches its classification. Every possible classification appears
as one mask, so taking the greatest set-bit count among surviving masks cannot
miss a better answer.

## Complexity detail

Let $n$ be the number of people. There are $2^n$ masks, and validating one may
inspect $n^2$ matrix entries, for $O(2^n n^2)$ time. The mask, counters, and
loop indices use $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Backtracking with propagated assignments:** Propagating statements from
  assumed-good people can prune contradictions early, but its worst case still
  explores exponentially many classifications.
- **Enumerate ternary states:** Allowing good, bad, and undecided states creates
  $3^n$ encodings and performs avoidable work.
- Statements by a person assumed bad impose no restrictions, even when they
  happen to agree with the final classification.
- `2` means no statement and never needs to match a classification bit.
- A consistent all-good mask yields the upper bound $n$.
- It is possible for every nonempty good set to be contradictory, in which
  case the all-bad mask proves the answer is zero.
