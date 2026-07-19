## General
**Turn query limits into a monotone insertion frontier**

Sort `nums` in ascending order. Attach each query's original index and sort the queries by `m`. While processing a query, insert every not-yet-inserted number whose value is at most its limit. Because later limits never decrease, inserted values remain eligible and each number enters the data structure once.

If no number has been inserted, store `-1`. Otherwise the structure contains exactly all values eligible for the current query, independent of the queries' original order. Write the computed result back at the saved index to restore that order.

**Maximize XOR from the most significant bit**

Store inserted values in a binary trie with one level for each of the $B$ bit positions. To query `x`, start at its most significant bit. An XOR bit becomes `1` when the chosen number's bit differs from `x`, so prefer the opposite-bit child whenever it exists. If it does not, follow the same-bit child and accept a zero at that result position.

This greedy choice is final at each level: a `1` at a more significant XOR position outweighs every possible combination of lower bits. After choosing the best available prefix, the trie node restricts the remaining candidates to exactly those with that prefix. Repeating down all levels therefore yields the maximum XOR among all inserted numbers.

The offline limit sweep and trie invariant combine cleanly: the trie controls eligibility, and the bitwise walk controls maximization. Neither concern is approximated.

## Complexity detail
Sorting numbers and indexed queries takes $O((n + q)\log(n + q))$ time. Each of the $n$ insertions and $q$ trie queries visits exactly $B$ levels, adding $O((n + q)B)$. At most $nB + 1$ trie nodes and $q$ indexed queries or answers are stored, for $O(nB + q)$ space.

## Alternatives and edge cases
- **Scan every eligible number per query:** direct maximization is correct but takes $O(nq)$ time when every query admits the whole array.
- **Build a fresh trie per query:** this repeats insertions and can also take $O(nqB)$ time.
- **One trie without limit metadata:** inserting every number answers unconstrained XOR but may select a value greater than the query's `m`.
- **Persistent tries by sorted prefix:** versioning one trie per insertion also answers limits efficiently, but uses a more complex persistent structure.
- **No eligible value:** return `-1`, not zero, even when `x ^ 0` would otherwise be meaningful.
- **Limit equality:** values exactly equal to `m` must be inserted before answering that query.
- **Zero:** its all-zero bit path is valid and may be the only eligible choice.
- **Duplicate values and queries:** duplicates do not change a maximum, but processing them must preserve every query output position.
- **Bit width:** include every bit needed for values up to $10^9$; omitting the highest bit can reverse the greedy result.
