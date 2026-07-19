## General
**Ignore fragment boundaries.** Treat each array as a lazy stream that yields the characters of its first fragment, then its second, and so on. Comparing streams directly captures the represented strings without allocating either concatenation.

**Compare aligned characters and exhaustion.** Advance both streams together. Every paired character must match, and both streams must end at the same moment. A mismatch proves inequality immediately; if one stream has an extra character after the other ends, the represented lengths differ and the result is also false.

**Why streaming is sufficient.** Concatenation preserves exactly the order in which the nested iteration yields characters. Fragment boundaries contribute no data, so equal-length streams with equal characters at every position are identical strings, while any unequal position or unequal exhaustion distinguishes them.

## Complexity detail
At most all $N$ input characters are examined once, for $O(N)$ time. Iterators and current positions use $O(1)$ auxiliary space; the output strings are never materialized.

## Alternatives and edge cases
- **Join and compare:** `"".join(word1) == "".join(word2)` is concise and $O(N)$ time, but allocates $O(N)$ additional string storage.
- **Manual fragment pointers:** Four indices tracking each array and offset provide the same $O(N)$ time and $O(1)$ space without iterator utilities.
- **Repeated concatenation:** Rebuilding a growing string after each fragment can copy prefixes repeatedly and cost $O(N^2)$.
- Equal fragment counts are neither necessary nor sufficient.
- A mismatch may occur exactly across different fragment boundaries.
- Identical prefixes with different total lengths are not equivalent.
- Single-fragment arrays reduce to ordinary string equality.
- Every fragment is nonempty, so no special empty-fragment skipping is required by the contract.
