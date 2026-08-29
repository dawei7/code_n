## General

**Use a different structure for each statistic.** No single ordering answers FIFO removal, mean, median, and mode equally well. The exact source maintains several synchronized views:

- `q`, a `deque`, preserves insertion order;
- `s` stores the running sum;
- `cnt` maps each value to its current frequency;
- `sl` is a sorted multiset of every live occurrence;
- `sl2` is a sorted collection of one `(number, frequency)` record per value ever encountered.

Every update changes all relevant views before returning, so each query can read an already prepared answer.

**Append and update the mean state.** `addNumber(number)` appends to the right of `q` and adds the value to `s`. Because removals always target the earliest insertion, a deque provides constant-time append and left-pop behavior.

The floored mean is then `s // len(q)`. All numbers are positive, so Python floor division agrees with ordinary truncation downward. The contract guarantees the tracker is nonempty when queried, avoiding division by zero.

**Maintain all live values in sorted order for the median.** `sl.add(number)` inserts another occurrence rather than collapsing duplicates. On removal, `sl.remove(number)` deletes exactly one occurrence.

For size $N$, the requested median is the larger middle value when $N$ is even. Zero-based index `N // 2` selects:

- the unique middle for odd $N$;
- the right-hand, larger middle for even $N$.

Thus `self.sl[len(self.q) // 2]` implements the problem's exact convention.

**Order mode records by frequency descending and value ascending.** `sl2` is created with key

`lambda x: (-x[1], x[0])`.

Its tuple is `(number, frequency)`. Negating frequency makes larger counts sort first. Using the number as the second key makes the smallest value come first among equal maximum frequencies. Therefore `sl2[0][0]` is the required mode.

**Replace, rather than duplicate, a value's frequency record.** Before incrementing a frequency, `addNumber` discards tuple `(number, old_count)` from `sl2`. It increments `cnt[number]` and inserts the new tuple. This preserves exactly one current record for that numeric value.

Removal performs the symmetric sequence: discard the old tuple, decrement the count, and add the updated tuple.

**Why zero-frequency records do not break the mode.** When the last live copy of a value is removed, the source inserts `(number,0)` instead of deleting the value completely. At least one live element exists whenever `getMode` is called, and every positive frequency sorts before every zero frequency because `-positive < 0`. A dead record can therefore never become the reported mode while the tracker is nonempty.

If the same value is added later, the zero-frequency tuple is discarded before its count returns to one. These retained records do increase storage to the number of distinct values ever added, which is still bounded by the total call count.

**Trace the first sequence.** After adding 4, 4, 2, 3, the deque contains insertion order `[4,4,2,3]`, the sum is 13, and the sorted multiset is `[2,3,4,4]`. Mean is `13 // 4 = 3`; upper median index two gives 4; frequency record for 4 sorts first with count two.

Removing the earliest 4 pops the deque's left side, deletes one 4 from `sl`, subtracts four from `s`, and changes 4's mode record from count two to one. Values 2, 3, and 4 now tie, so ascending numeric tie-breaking reports 2.

**All synchronized invariants survive each operation.** Addition inserts one occurrence everywhere and increases exactly one frequency. FIFO removal identifies one value through `q` and removes that same occurrence from every other view. Induction over operations shows `s` equals the live sum, `sl` equals the sorted live multiset, and `sl2` ranks current counts. Each getter consequently returns the required statistic.

**The manifest names the wrong implementation family.** Its summary mentions lazy dual median heaps and a lazy frequency heap. The exact source uses `SortedList` twice and performs eager record replacement. The asymptotic aggregate bounds are similar, but the data flow, dependencies, and per-query mechanics are different.

## Complexity detail

Let $N$ be the current number of live elements and $D$ the number of distinct values ever added. Deque and sum changes are $O(1)$. `SortedList` insertion/removal and `SortedList` keyed record replacement are approximately $O(\log N)$ or $O(\log D)$ search with block-list update costs as provided by `sortedcontainers`. Median/mode indexing is efficient but should not be described as heap-top access.

Across $q$ total calls, the intended bound is $O(q\log q)$ time and $O(q)$ space. The deque and occurrence multiset can hold $O(q)$ live items, while counts and zero-frequency records can hold $O(q)$ distinct historical values.

## Alternatives and edge cases

- **Two median heaps:** They can maintain the upper median with lazy deletion, but FIFO removal requires careful delayed-count bookkeeping.
- **Frequency heap for mode:** It can use lazy stale entries; the exact source instead eagerly replaces one keyed tuple.
- **Re-sort on every getter:** It simplifies updates but makes statistics queries $O(N\log N)$.
- **Single live element:** It is simultaneously the mean, median, and mode.
- **Even live count:** Index `N//2` deliberately selects the larger middle.
- **Mode tie:** The keyed ordering returns the smallest tied value.
- **Duplicate values:** `sl` stores every occurrence, while `sl2` stores one frequency record.
- **Value removed to zero count:** Its record remains but sorts after every live value.
- **Re-adding a dead value:** The old zero tuple is discarded and replaced cleanly.
- **FIFO versus smallest removal:** `q.popleft()` removes earliest insertion, unrelated to sorted order.
- **Nonempty-operation guarantee:** It makes `popleft`, division, median indexing, and mode indexing safe.
- **Positive-number constraint:** It makes `//` match the intended floored mean without negative-rounding ambiguity.
- **Third-party dependency:** `SortedList` comes from `sortedcontainers` and is not a Python built-in.
- **Required imports:** `deque`, `defaultdict`, and `SortedList` must be supplied.
- **Manifest discrepancy:** There are no heaps or lazy deletion in the exact Optimal file.
