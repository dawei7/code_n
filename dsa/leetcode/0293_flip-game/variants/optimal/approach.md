## General
**A move is determined by one starting position**

There is no game-tree search in this problem: only the immediate next states are requested. A legal move is completely
identified by the left position `i` of an adjacent `++` pair. The candidate scans those possible starts from left to
right.

Only after confirming a pair is legal, construct `currentState[:i] + "--" + currentState[i + 2:]`. This changes
exactly two symbols and preserves every other position. Since every legal move has one such starting position, the
scan produces all and only the requested states.

**Overlap is intentional**

In `+++`, the pairs beginning at zero and one overlap, but they represent different single moves and must both appear.
Advancing the scan by one position handles this naturally. By contrast, a string shorter than two characters or one
without `++` produces no states.

## Complexity detail
Let $n$ be the state length and $k$ the number of legal `++` pairs. Scanning takes $O(n)$ time, and materializing $k$
immutable strings of length $n$ takes $O(kn)$ time and output space. Since $k \le n - 1$, both are $O(n^2)$ in the
worst case. Checking a pair before slicing avoids paying that construction cost at non-moves.

## Alternatives and edge cases
- **Construct at every position:** is correct if non-moves are discarded afterward, but performs quadratic work even
  when only one pair is legal.
- **Overlapping pairs:** are distinct moves and must not be skipped after the first match.
- **No legal pair:** a state shorter than two symbols or one without `++` returns an empty list.
- **Ordering:** the candidate emits moves from left to right, while the source contract permits any order.
