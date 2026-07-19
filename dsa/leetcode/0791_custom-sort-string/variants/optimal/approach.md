## General
**Count before ordering**

Build a frequency table for the `n` characters of `s`. Then scan the `m` characters of `order`; for each one, append all of its occurrences and remove that entry from the table.

**Append characters without a custom rank**

After the ordered scan, every remaining frequency belongs to a character absent from `order`. Append those occurrences in any deterministic order. Their positions do not affect the custom constraint.

Every input occurrence is recorded once. Ranked occurrences are emitted exactly when their character is visited in `order`, so any two ranked character classes appear in the required relative order. The remaining occurrences are precisely the unranked characters and may be appended freely. Thus the result is both a permutation of `s` and a valid custom ordering.

## Complexity detail
Counting `s`, scanning `order`, and emitting the `n` output characters takes $O(m + n)$ time. The frequency table stores `u` distinct characters from `s`, using $O(u)$ auxiliary space apart from the returned string.

## Alternatives and edge cases
- **Rank-key sorting:** Sort `s` by a map from ordered characters to ranks; this is concise but takes $O(n \log n)$ time.
- **Fixed alphabet counts:** With lowercase English letters, a 26-element array replaces the hash table while preserving linear time.
- **Selection sorting by custom rank:** Repeatedly searching the remaining suffix is correct but takes $O(n^2)$ time.
- **No ranked characters in `s`:** Any permutation is valid; returning `s` unchanged is sufficient.
- **Repeated characters:** Emit the complete frequency at its single ranked position.
- **Order characters absent from `s`:** They contribute nothing and do not affect the output.
- **Unranked characters:** They may appear before, between, or after ranked groups as long as multiplicities are preserved.
