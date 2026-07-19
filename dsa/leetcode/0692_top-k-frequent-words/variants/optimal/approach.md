## General
**Count each distinct word once**

Build a frequency map in one pass. The remaining task is to retain the best `k` among `U` distinct candidates according to higher frequency first and, on a tie, lexicographically smaller word first.

**Keep the worst retained candidate at the heap root**

Use a min-heap of at most `k` entries. Lower frequency is worse. For equal frequency, a lexicographically larger word is worse and must compare smaller in the heap key. Encode that reverse lexical ordering with negated character codes plus a terminator that also reverses prefix ordering. When a new candidate is better than the root, replace the root.

**Sort only the retained words for output order**

The heap identifies the correct set but not presentation order. Sort its at most `k` words by `(-frequency, word)` before returning them.

**Why no discarded word belongs in the answer**

After each distinct word is processed, the heap contains the best `k` candidates seen so far: an unfilled heap accepts the candidate, and a full heap replaces exactly its current worst member only when the newcomer ranks better. Induction preserves the top-`k` set. The final sort applies the contract's exact total order to that set.

## Complexity detail
Counting `N` words takes $O(N)$ time. Each of `U` distinct words performs an $O(\log K)$ heap operation in the worst case, and sorting the retained entries takes $O(K \log K)$; because $U \le N$ and $K \le U$, this is $O(N \log K)$ overall. The frequency map and heap use $O(U)$ space.

## Alternatives and edge cases
- **Sort all distinct words:** sort frequency-map keys by `(-count, word)`; it is concise and takes $O(U \log U)$ time.
- **Frequency buckets:** group words by count and lexically sort within buckets; it can avoid a global frequency sort but still must order tied words.
- **Repeated best selection:** scan all remaining words once for every output position; it is correct but can take $O(KU)$ time.
- Lexicographic order is ascending only within equal-frequency groups.
- A word appears once in the result regardless of how many input occurrences it has.
- When $k = U$, every distinct word is returned in full ranking order.
