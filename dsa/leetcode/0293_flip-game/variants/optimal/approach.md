## General
**A move is determined by one index**

There is no game-tree search in this problem: only the immediate next states are requested. A legal move is completely identified by the left index `i` of an adjacent `++` pair. Scan those possible starts from left to right.

Only after confirming a pair is legal, construct
`currentState[:i] + "--" + currentState[i+2:]`. This changes exactly two symbols and preserves every other position. Since every legal move has one such left index, the scan produces all and only the requested states.

**Overlap is intentional**

In `+++`, the pairs beginning at zero and one overlap, but they represent different single moves and must both appear. Advancing the scan by one position handles this naturally. By contrast, a string shorter than two characters or one without `++` produces no states.

## Complexity detail
There are at most $n - 1$ moves, and each returned immutable string has length `n`. Merely materializing the worst-case answer therefore needs $O(n^2)$ time and space. Building strings at every index before checking legality wastes that cost on non-moves; checking first keeps sparse-output inputs efficient.

## Alternatives and edge cases
- Constructing a candidate at every index is correct but performs quadratic work even when only one pair is legal.
- Overlapping pairs are distinct moves and must not be skipped after the first match.
- Inputs shorter than two characters, or inputs with no `++`, return an empty list.
