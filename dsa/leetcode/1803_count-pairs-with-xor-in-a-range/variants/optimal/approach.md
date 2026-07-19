## General
**Turn the inclusive interval into two prefixes**

Let $F(L)$ count pairs whose XOR is strictly less than $L$. The requested inclusive count is $F(\texttt{high}+1)-F(\texttt{low})$. It is therefore enough to answer one strict upper-bound query.

**Compare XOR prefixes inside a binary trie**

Scan bits from most significant to least significant while comparing `value XOR previous` with limit $L$. If the current limit bit is zero, the XOR bit must also be zero to keep the prefix tied. If the limit bit is one, choosing XOR bit zero makes the result permanently smaller, so every value in that trie branch can be added immediately; choosing XOR bit one keeps the prefix tied and continues the search.

Trie nodes store how many previously inserted values pass through them. At each bit, XOR zero follows the child equal to the current value bit, while XOR one follows the opposite child.

**Insert only after querying**

For each array value, first count compatible values already in the trie and only then insert the current value. The trie therefore contains exactly the indices smaller than the current index. Every valid pair is counted when its right endpoint is processed, and no pair is counted twice.

The bit-prefix decisions enumerate exactly the prior values whose XOR is below the limit. Subtracting the two strict-prefix counts preserves precisely the inclusive interval, proving the final result.

## Complexity detail
Each of the $n$ values performs two trie queries and two insertions across $B=15$ bits, taking $O(nB)$ time. At most $O(nB)$ trie nodes are created, so auxiliary space is $O(nB)$.

## Alternatives and edge cases
- **All index pairs:** Directly testing every XOR is simple and correct but takes $O(n^2)$ time.
- **Frequency table over the entire value domain:** Convolution-style approaches are possible because values are bounded, but they add substantial machinery and do not naturally enforce incremental pair counting.
- **Inclusive upper bound:** Query strict inequality with `high + 1`; querying `high` would omit pairs equal to the upper boundary.
- **Equal values:** Their XOR is zero, which is below every legal positive `low`, but the duplicate indices must still be represented independently in trie counts.
- **Exact lower bound:** Subtract only XOR values strictly below `low`, leaving values equal to `low` included.
- **Single element:** No pair exists, so both prefix counts are zero.
- **Repeated trie path:** Store a count at every node so duplicate values contribute their full multiplicity.
