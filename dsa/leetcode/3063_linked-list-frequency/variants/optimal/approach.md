## General

**Count without losing value identity.** Traverse the input list once and maintain a hash table from each encountered node value to its current occurrence count. After any processed prefix, the entry for a value equals exactly how many nodes in that prefix contain it: the first occurrence creates an entry of one, and every later occurrence increments that same entry.

**Turn counts into nodes.** Once the traversal ends, the table contains one final frequency for each of the $k$ distinct values. Create a dummy output node and keep a tail pointer. For every stored frequency, append one new node and move the tail forward. The problem permits any output order, so the hash table's iteration order does not carry semantic meaning.

The counting invariant proves that each appended value is the true frequency of one distinct input value. Every table entry is appended exactly once, and no node is appended for anything outside the table. The returned list therefore has exactly $k$ nodes and contains precisely the required frequency multiset.

## Complexity detail

Let $n$ be the input length and $k$ the number of distinct values. With expected $O(1)$ hash-table operations, counting costs $O(n)$ time; building the output costs $O(k)$, so total time is $O(n+k)=O(n)$. The table stores $k$ entries and the returned list has $k$ nodes, giving $O(k)$ space including the output, with $O(k)$ auxiliary storage for the table.

## Alternatives and edge cases

- **Fixed frequency array:** Since values are bounded by $10^5$, an indexed array can replace the hash table, but it consumes space for the entire value domain even when $k$ is small and must scan or separately track used indices.
- **Sort copied values:** Copying and sorting the list values groups equal elements, but raises the running time to $O(n \log n)$ and still needs linear storage.
- **Repeated rescans:** Counting one chosen value per pass avoids a hash table but can require $O(nk)$ time.
- **Output order:** Cases must compare the multiset of frequency values, because any permutation of the result is valid.
- **Duplicate frequencies:** Different input values may occur equally often; the output must retain one frequency node for each of them rather than deduplicating equal counts.
- **Single distinct value:** The result contains one node whose value is the full input length.
- **All values distinct:** The result contains $n$ separate nodes, each holding `1`.
