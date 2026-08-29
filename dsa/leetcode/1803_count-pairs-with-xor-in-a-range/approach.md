## General

**Convert an inclusive range into two strict-prefix counts**

Define $F(L)$ for the current number $x$ as the number of earlier values $y$ satisfying

$$
x\mathbin{\mathrm{XOR}}y<L.
$$

Then XOR values in the inclusive interval `[low, high]` are counted by

$$
F(\texttt{high}+1)-F(\texttt{low}).
$$

The first term includes all values at most `high`, while the second removes all values below `low`. The solution implements $F$ with a binary trie.

**Store previous numbers as bit paths**

Each `Trie` node has two children, for bit zero and bit one, plus `cnt`. Insertion processes bit positions 15 down through 0.

At each bit, the path follows the bit of the inserted number, creating a child when needed. After entering that child, its `cnt` increases. Thus `cnt` records how many inserted numbers share the prefix ending at that node.

Sixteen positions are sufficient for the valid domain. Input numbers and limits are below the represented $2^{16}$ range, and the extra leading bits are harmless zeros when smaller.

**Count XOR values strictly below a limit**

Binary numbers are ordered by their most significant differing bit. During `search(x, limit)`, `node` represents inserted numbers whose XOR prefix with $x$ is still equal to the limit's prefix.

Let `v` be the current bit of $x$.

If the current limit bit is zero, the XOR bit must also be zero to remain below or equal to the prefix. Choosing XOR bit one would make the result larger at the first differing position. To produce XOR zero, the stored number's bit must equal `v`, so the search continues to `children[v]`.

If the limit bit is one, there are two possibilities:

- choose XOR bit zero by taking stored bit `v`; the resulting prefix becomes strictly smaller than the limit, so every number under `children[v]` is valid and its `cnt` is added immediately;
- choose XOR bit one by taking stored bit `v ^ 1`; the prefix remains equal, so search continues down that child.

If the required continuation node is missing, no further equal-prefix number exists and the accumulated count can be returned early.

After all bits, paths exactly equal to `limit` have not been added, which is correct because the query is strict `< limit`.

**Count each unordered pair exactly once**

The outer loop handles numbers from left to right. For current `x`, both searches occur before `x` is inserted. The trie therefore contains exactly the elements at earlier indices.

Every counted pair has earlier index $i$ and current index $j$, so $i<j$. It is counted when $j$ is processed, never earlier and never again. Searching before insertion also prevents pairing an element with itself.

After adding the range count for `x`, `tree.insert(x)` makes it available to later positions.

**Following a small query**

Suppose a search reaches a bit where the limit has one. All stored values producing XOR zero at that bit are now guaranteed smaller, regardless of their lower bits, so adding the entire matching-child count is safe. Values producing XOR one remain tied at this bit and must be examined at lower positions.

This prefix decision is the binary analogue of counting decimal numbers below a bound digit by digit: once a prefix becomes smaller, every suffix is allowed.

For `nums = [1,4,2,7]`, the first number finds no prior partners and is inserted. Each later number queries prior values for XOR below 7 and below 2; their difference counts XOR from 2 through 6. Across the scan, all six unordered pairs satisfy the range and are accumulated once.

**Why the trie search is correct**

At every bit, the search partitions equal-prefix candidates according to whether their XOR bit makes the result smaller than the limit or keeps it equal. A branch that becomes smaller is counted in full; a branch that would become larger is discarded; the unique equal branch continues. This maintains the invariant that `ans` contains exactly all already-proven smaller values while `node` contains precisely the still-equal candidates.

Therefore `search(x, L)` returns exactly the number of inserted $y$ with `x ^ y < L`. Subtracting the two strict-prefix counts gives the requested inclusive range, and processing only previous numbers gives exactly the valid index pairs.

## Complexity detail

Let $n$ be the number of values and $B=16$ the processed bit width. Each number performs two searches and one insertion, each visiting at most $B$ nodes. Total time is $O(nB)$, matching the manifest; with fixed constraints this is linear in $n$.

Each inserted value creates at most $B$ new trie nodes. Total auxiliary space is $O(nB)$ in the worst case, also matching the manifest. Shared prefixes often reduce the actual node count.

Counts and the final answer can be as large as $n(n-1)/2$, which Python represents exactly.

## Alternatives and edge cases

- **Check every pair:** Direct XOR testing takes $O(n^2)$ time and is too slow for 20,000 values.
- **Frequency table over the bounded domain:** Iterating all possible partners per number can depend on the full value range; the trie uses only $B$ prefix decisions.
- **Count `<= limit` directly:** It is possible but introduces equality handling; strict `<` naturally yields `F(high + 1) - F(low)`.
- **Insert before searching:** That would allow the current element to pair with itself and violate $i<j$.
- **Duplicate values:** Their XOR is zero. The trie stores multiplicities in `cnt` even though the stated `low >= 1` excludes such pairs.
- **Lower boundary:** `search(x, low)` removes XOR values strictly below `low`, leaving equality included.
- **Upper boundary:** `search(x, high + 1)` includes XOR exactly equal to `high`.
- **Missing trie branch:** Returning the accumulated count is correct because no equal-prefix candidates remain.
- **Empty trie:** Both searches return zero for the first number.
- **Leading zero bits:** Processing all 16 positions preserves comparisons and does not change XOR values.
- **Node counts:** They count inserted occurrences, not merely distinct numbers, so index-pair multiplicity is correct.
- **Bitwise precedence:** Parenthesized conceptual expressions clarify that shifts, masks, and XOR choose individual bits.
- **No modulo:** The problem requests the exact pair count.
- **Input preservation:** Numbers are inserted into a separate trie and `nums` is never modified.
