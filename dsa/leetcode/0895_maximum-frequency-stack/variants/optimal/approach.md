## General

Every pop must rank currently stored elements by two criteria:

1. Higher current frequency wins.
2. Among equal frequencies, the occurrence pushed most recently wins.

The exact solution stores one heap entry for every pushed occurrence. Each entry is a triple

```text
(-frequency_at_this_push, -timestamp, value)
```

Python's heap removes the lexicographically smallest tuple. Negating frequency makes a larger frequency numerically smaller, so it receives higher priority. If frequencies tie, negating the timestamp makes the later push smaller and therefore higher priority.

**Track the frequency reached by each occurrence.** `cnt[val]` is incremented before the entry is inserted. If value 5 is pushed for the first, second, and third times, its three entries carry frequency ranks 1, 2, and 3. These ranks describe nested occurrences: the third-frequency entry is the occurrence that made 5 appear three times.

On pop, the heap returns the occurrence with the greatest stored rank and newest timestamp among that rank. The solution extracts its value and decrements `cnt[val]`.

**Why old entries do not become invalid after a pop.** Suppose value 5 currently has frequency three. Its remaining heap entries include ranks 1, 2, and 3. Popping its rank-3 entry reduces the actual frequency to two. The greatest remaining entry for 5 is exactly its rank-2 entry, so the heap's historical rank now equals its new current frequency.

In general, pushes create ranks $1,2,\ldots,f$ for a value. Pops always remove the highest remaining rank for whichever value wins. Therefore the remaining ranks are always $1,2,\ldots,\text{cnt[val]}$. There is no stale entry with a rank greater than the value's current frequency.

This property is what allows the heap to store frequency at push time rather than updating every existing entry when a count changes.

**Why timestamp resolves stack recency correctly.** Each push increments `ts`, so timestamps are strictly increasing across all values. For values tied at the maximum frequency $f$, their rank-$f$ entries were created on the pushes that most recently brought each value to frequency $f$. The later of those occurrences is also the one closest to the top among candidates at frequency $f$, so the negative timestamp selects the required value.

After a pop, lower-rank entries retain their original timestamps. Those timestamps correctly describe where the remaining occurrences sat in push order.

**Example trace.** Push sequence `5,7,5,7,4,5` creates:

- 5 with frequency ranks 1, 2, and 3;
- 7 with ranks 1 and 2;
- 4 with rank 1.

The rank-3 entry for 5 has top priority and is popped first. Now 5 and 7 each have highest remaining rank 2. The rank-2 push of 7 occurred later than the rank-2 push of 5, so 7 is popped next. The next maximum is rank 2 for 5, so 5 follows. All remaining values have rank 1, and 4 has the latest timestamp, so it is returned next.
At every moment, the highest remaining rank for each value equals its current frequency. The heap's first tuple coordinate therefore chooses a value of maximum current frequency. Among entries with that rank, its second coordinate chooses the most recent push. That is exactly the specification. Removing the selected entry and decrementing its count restores the rank invariant for the next operation.

The structure stores all active occurrences, not merely one entry per distinct value. This makes pop simple because the next historical frequency level is already in the heap.

## Complexity detail

Let $q$ be the number of elements currently stored, bounded by the number of operations.

- **`push` time:** $O(\log q)$ for `heappush`.
- **`pop` time:** $O(\log q)$ for `heappop`.
- **Space complexity:** $O(q)$ for one heap entry per active pushed occurrence and frequency counts for distinct values.

The local manifest's $O(1)$ operation claim belongs to the editorial's stack-of-stacks design, not this heap implementation. The exact code performs logarithmic heap operations and should be documented accordingly.

## Alternatives and edge cases

- **Stacks grouped by frequency:** Map each value to its count, keep a stack for each frequency, and track the maximum frequency. Push and pop are both $O(1)$ and this is the method matching the manifest.
- **Scan the entire logical stack on every pop:** It can find frequency and recency but costs $O(q)$ or worse per operation.
- **Heap with only current value frequency:** Updating priorities for all older occurrences is awkward. The rank-per-occurrence representation avoids decrease-key operations.
- **One distinct value:** Its rank increases on each push and decreases through successive pops, so every pop returns it.
- **All values distinct:** Every rank is one, so negative timestamps make behavior identical to an ordinary stack.
- **Equal maximum frequencies:** The later rank-reaching occurrence wins through `-timestamp`.
- **Repeated pop after a winner:** Its next lower-rank entry remains and competes using the value's newly reduced frequency.
- **Large values:** Values are tuple payloads and dictionary keys; their magnitude does not affect ordering criteria.
- **Nonempty-pop guarantee:** The code does not check an empty heap because the contract guarantees at least one stored element before pop.
- **Timestamp uniqueness:** Incrementing before every push ensures no two entries need a further recency tie-breaker.
- **Frequency count after pop:** Decrementing exactly once matches removal of one occurrence; zero-count dictionary entries are harmless.
- **Manifest mismatch:** Describing this exact heap code as $O(1)$ per operation would be incorrect even though another optimal design achieves it.
