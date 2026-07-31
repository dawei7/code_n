## General

**Use the bounded value as an index.** Allocate one weight slot for every
legal value from 0 through $V$. For every `[value, weight]` pair in both
arrays, add the weight to that value's slot. Since a slot represents exactly
one value, it becomes the required combined weight regardless of overlap.

**Emit in contract order.** Scan values from 1 through $V$ and append a pair
whenever its accumulated weight is positive. The scan order directly produces
ascending values, and positive input weights ensure a zero slot means the
value was absent.

Every input weight is added once to the unique slot for its value, so every
reported total is exact. The final scan visits every possible value exactly in
ascending order, proving both completeness and ordering.

## Complexity detail

Accumulating $n$ pairs and scanning the $V=1000$ value domain takes $O(n+V)$
time. The weight array uses $O(V)$ space; the returned pairs are required
output.

## Alternatives and edge cases

- **Hash map plus sorting:** Aggregate in a dictionary and sort its keys; this
  works for unbounded values but costs $O(n+u\log u)$ for $u$ distinct values.
- **Sort and merge both arrays:** Sorting each input followed by two pointers
  is correct but unnecessary with the small fixed domain.
- **Nested matching:** Searching the other array separately for every item can
  take $O(n^2)$ time.
- **Disjoint inputs:** Values present in only one array retain their original
  weights.
- **Input order:** The output must be ascending even when both inputs are not.
