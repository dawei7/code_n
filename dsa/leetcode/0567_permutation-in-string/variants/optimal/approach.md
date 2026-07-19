## General
**A permutation is a frequency match**

Order inside the candidate substring does not matter. Because the inputs contain only lowercase English letters, represent `s1` and a window of `s2` with two fixed arrays of 26 counts.

**Use exactly the target length**

Only a substring of length `m = len(s1)` can contain the same multiset. Build the first window of that length, then move it one position at a time by removing its left character and adding the new right character.

**Track matching frequency slots**

Count how many of the 26 window frequencies currently equal their target frequencies. Before changing a letter count, remove its equality contribution; after the change, add the contribution back if equality was restored. All 26 slots matching means the current window is a permutation.

**Reject an impossible length immediately**

If `s1` is longer than `s2`, no complete target-length window exists.

**Why a match count of 26 is exact**

The window and target always describe strings of the same length. When all 26 per-letter counts agree, the two strings contain identical character multisets, so one is a permutation of the other. Conversely, any permutation substring has identical counts in every slot and will make the match count 26 when its window is examined.

## Complexity detail
Building the target and first-window counts takes $O(m)$ time. Each of the remaining $n - m$ slides performs two constant-time updates, so total time is $O(m + n)$. Two 26-entry arrays use $O(1)$ space.

## Alternatives and edge cases
- **Compare both 26-entry arrays after every slide:** is also linear because the alphabet size is constant, though it performs more fixed work per window.
- **Sort every substring:** is correct but costs $O((n - m + 1) m \log m)$ time.
- **Recount every window:** avoids sorting but still takes $O(nm)$ time.
- **Target longer than search text:** returns `False` immediately.
- **Equal strings:** the first window matches.
- **Repeated letters:** exact multiplicities, not only character membership, determine a permutation.
- **Match at the final window:** the entering and leaving updates must occur before the last equality check.
