## General
**Keep one pointer in each array.** At any step, inspect `arr1[i]`, `arr2[j]`, and `arr3[k]`. If all three values are equal, that value belongs to the intersection. Append it and advance every pointer; strict increase guarantees it cannot occur again.

**Discard values that cannot catch up.** Otherwise, let $M$ be the maximum of the three pointed values. Any pointer currently below $M$ cannot form a common value at its present position because at least one other array has already advanced beyond it. Advance each such pointer. Moving all smaller pointers is safe and avoids wasting iterations on values that are already impossible.

**Preserve sorted output automatically.** Pointers only move forward, and each emitted value is greater than the previous emitted value. If any pointer reaches its array's end, no later triple exists because every intersection value needs one remaining element from each array.

## Complexity detail
Pointer `i` advances at most $n_1$ times, `j` at most $n_2$ times, and `k` at most $n_3$ times. Total time is $O(n_1+n_2+n_3)$. Apart from the returned array, the three pointers and current maximum use $O(1)$ space.

## Alternatives and edge cases
- **Hash-set intersection:** Converting arrays to sets is concise and expected-linear, but uses $O(n_1+n_2+n_3)$ additional space and requires sorting the result if order is not preserved.
- **Binary search from one array:** Searching every `arr1` value in the other two arrays takes $O(n_1(\log n_2+\log n_3))$ time.
- **Linear membership scans:** Testing every first-array value by scanning the other arrays from the beginning can take $O(n_1(n_2+n_3))$ time.
- **No common value:** One pointer reaches the end without an emission, yielding `[]`.
- **All values common:** Each comparison matches and all pointers advance together.
- **Unequal lengths:** The algorithm stops when the shortest exhausted path makes another triple impossible.
- **Strict increase:** No duplicate suppression is needed in either the inputs or output.
