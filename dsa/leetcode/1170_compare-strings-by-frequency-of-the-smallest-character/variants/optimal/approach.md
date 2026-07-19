## General
**Compute each frequency in one scan.** Track the smallest character seen and how many times it has appeared. A smaller character resets the count to one; an equal character increments it. This produces $f(s)$ without separately calling `min` and `count`.

**Exploit the length bound.** Every string has length at most `10`, so every frequency is an integer from `1` through `10`. Count how many words have each possible frequency in an 11-slot bucket array. Then sweep frequencies downward to precompute `greater[k]`, the number of words whose frequency is strictly greater than $k$.

**Answer each query directly.** Compute `frequency(query)` and append `greater[frequency(query)]`. The suffix counts already exclude equal-frequency words, exactly matching the strict inequality. Each word and query is scanned once, and query order is unchanged.

## Complexity detail
All string scans examine $S$ characters. Building the suffix counts touches only the fixed 10-frequency domain, so total time is $O(S)$. The two fixed-size arrays use $O(1)$ auxiliary space; the required result array is output storage.

## Alternatives and edge cases
- **Sort word frequencies and binary search:** This is correct in $O(S+w\log w+q\log w)$ time, but the fixed frequency range permits direct counting.
- **Compare every query with every word:** This takes $O(qw)$ comparisons after frequency calculation and scales quadratically when both arrays grow.
- **Equal frequencies:** A word counts only when its frequency is strictly greater, not equal.
- **One-character string:** Its smallest character occurs once, so its frequency is `1`.
- **All characters equal:** The frequency is the full string length, up to `10`.
- **Smallest character not first:** The scan must reset when a later, lexicographically smaller character appears.
