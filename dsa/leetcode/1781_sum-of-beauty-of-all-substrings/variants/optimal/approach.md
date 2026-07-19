## General
**Reuse counts for a fixed starting index**

Choose a substring start `i` and initialize 26 zero frequencies. Extend the end index from `i` to the end of `s`, incrementing only the newly included character. The frequency array then describes `s[i:end + 1]` without recounting its earlier characters.

**Compute beauty over present letters**

After every extension, the maximum of the 26 counters is the largest character frequency. For the minimum, inspect only positive counters; including zeros would incorrectly give every substring containing fewer than 26 distinct letters an inflated beauty. Add `maximum - minimum` to the running total.

**Why every substring contributes exactly once**

Each nonempty substring has one unique pair of start and end indices. The outer loop chooses that start and the inner extension reaches that end once, so its frequency state and beauty are added exactly once. No non-contiguous sequence is considered because the inner loop only appends adjacent characters.

## Complexity detail
There are $n(n+1)/2$ substrings. Updating one counter and scanning the fixed 26-letter alphabet are constant-time operations, so total time is $O(n^2)$. The 26 counters and scalar total use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Recount every substring:** Construct a frequency map from each slice independently. It is straightforward but can take $O(n^3)$ time.
- **Prefix count arrays:** Store 26 prefix frequencies and subtract two rows for each substring. This also takes $O(n^2)$ time but uses $O(26n)$ space and still scans the alphabet per substring.
- A one-character substring always has beauty zero.
- A substring containing several characters can still have beauty zero when all positive frequencies match.
- Zero-frequency letters must never determine the minimum.
- Repeated occurrences at the extension boundary update only one counter.
