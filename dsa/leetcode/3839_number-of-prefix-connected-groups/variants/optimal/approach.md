## General

**A prefix identifies an entire connected group**

Ignore every word shorter than `k`. For each remaining word, extract its first `k` characters and increment that prefix's frequency in a hash map. After all words have been processed, count the map entries whose frequency is at least two.

Prefix connectivity is equality of the length-`k` prefix, so it is reflexive across an index's own prefix, symmetric, and transitive. Consequently, all eligible indices with one prefix form exactly one maximal group, and indices with different prefixes cannot share a group. Counting a map key once when its frequency reaches at least two therefore counts each valid connected group once, regardless of how many pairs or words it contains.

Duplicate strings need no special treatment: separate array positions cause separate frequency increments. Conversely, skipping a word before slicing ensures that a short word cannot be mistaken for a valid shorter prefix.

## Complexity detail

Let $N$ be the number of words and $K$ the requested prefix length. Constructing and hashing one eligible prefix takes $O(K)$ time, so the expected time complexity is $O(N K)$. At most $N$ distinct prefixes of length $K$ are stored, giving $O(N K)$ space in the worst case. Hash-table qualifications belong to these expected bounds.

The benchmark fixes $K=16$ and defines size as $N K$, the total length of the compared prefixes. The accepted frequency map and an independent pair-of-sets formulation grow linearly in this size. A correct all-pairs comparison introduces another factor of $N$.

## Alternatives and edge cases

- **Seen and repeated sets:** Put a prefix in `seen` on its first occurrence and in `repeated` on later occurrences; the size of `repeated` is the answer. This has the same expected asymptotic bounds.
- **Sort valid prefixes:** After extracting every eligible prefix, sorting makes equal prefixes contiguous. It is correct but adds an $O(N\log N)$ comparison factor.
- **Pairwise comparison:** Compare every pair of eligible words and store each matching prefix once. This returns the right number of groups but takes $O(N^2K)$ time.
- **Short words:** Length less than `k` means no valid comparison prefix, so the word must be ignored completely.
- **Duplicate strings:** Equal strings at different indices increase the same prefix frequency and can form a group by themselves.
- **Groups, not pairs:** A prefix occurring four times contributes one group, not six index pairs.
- **Singleton prefixes:** A prefix seen exactly once never contributes to the answer.
