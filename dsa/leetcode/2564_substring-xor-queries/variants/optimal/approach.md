## General

**Reduce each equation to one target.** XOR is its own inverse, so `val ^ first == second` holds exactly when `val == first ^ second`. The queries therefore ask only where particular non-negative binary values occur in `s`. Precomputing each useful value once avoids rescanning the string for every query.

**Only 30 bits can matter.** Both integers in a query are at most $10^9$, so their XOR is smaller than $2^{30}$. A positive target's shortest binary representation consequently has at most 30 bits. For each starting index containing `1`, extend the substring at most 30 positions, update its value by shifting left and adding the next bit, and record its endpoints only if that value has not appeared before.

The scan processes starting indices from left to right and, for a fixed start, ending indices from left to right. The first stored occurrence of a value is thus shortest among occurrences at that start; because a positive binary value cannot have a shortest representation beginning with zero, the first globally stored occurrence also has the smallest possible `left`. A start containing `0` needs special handling: its one-character substring is the unique shortest representation of zero, and longer substrings beginning there cannot improve any positive value because their leading zero is removable.

After preprocessing, look up `first ^ second` for every query. A stored pair is the required shortest, leftmost occurrence by the scan argument above; a missing key proves that no relevant substring has that decimal value.

## Complexity detail

Let $n$ be the length of `s` and $q$ the number of queries. At most 30 characters are inspected from each starting position, so preprocessing takes $O(30n) = O(n)$ time. The $q$ hash lookups take $O(q)$ expected time, for $O(n + q)$ total expected time. At most $30n + 1$ values are stored, which is $O(n)$ auxiliary space; the returned $O(q)$ answer list is output space.

## Alternatives and edge cases

- **Search separately for every query:** Converting each XOR target to binary and searching `s` is simple and naturally finds its leftmost shortest representation, but repeated searches cost $O(nq)$ time.
- **Enumerate all substring lengths:** Considering substrings longer than 30 characters creates unnecessary quadratic work; no query can require a positive value with more than 30 significant bits.
- **Zero target:** The shortest representation is a single `0`, so the first zero in `s` must be stored as `[left, left]`.
- **Leading zeroes:** A substring such as `"011"` has the same value as `"11"` but is longer, so it can never win the primary length tie-break.
- **Repeated values:** Keeping the first stored endpoints preserves the smallest `left` among equally short representations.
- **Missing target:** If preprocessing never records `first ^ second`, the answer for that query is `[-1, -1]`.
- **Repeated queries:** Each repeated target is answered independently from the same immutable lookup table.
