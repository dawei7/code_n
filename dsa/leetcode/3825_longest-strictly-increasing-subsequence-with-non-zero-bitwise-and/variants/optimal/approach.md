## General

A bitwise AND is non-zero exactly when at least one bit remains set in the result. A bit remains set after AND-ing a subsequence precisely when that bit is set in every selected value. Therefore every valid subsequence shares some bit position, and every subsequence whose values share a set bit automatically has non-zero AND.

Fix one bit. Ignore every array value that does not contain that bit, without changing the order of the remaining values. The best valid subsequence sharing this bit is now exactly the ordinary longest strictly increasing subsequence of the filtered sequence.

Maintain one patience-sorting `tails` list for each of the $B$ bit positions. For every `value` in original array order, update only the lists for bits set in `value`. Within one list, binary-search with `bisect_left` for the first tail greater than or equal to `value`:

- if no such tail exists, append `value` and extend that bit's LIS;
- otherwise, replace the tail at that position with `value`, preserving the best—smallest—tail for a subsequence of that length.

Using the first tail greater than or equal to `value` prevents equal values from extending a subsequence, which enforces strict increase. The length of each bit's tails list is its filtered sequence's LIS length; the answer is the greatest such length.

To see that this maximum is exact, take any valid subsequence. Its AND contains some set bit, so every selected value appears in that bit's filtered sequence. Its length cannot exceed the LIS computed for that bit. Conversely, every subsequence represented by a bit's LIS is strictly increasing, retains original order, and has that bit set in every value, so its AND is non-zero. The maximum over all bits is therefore both an upper and a lower bound on the required answer.

## Complexity detail

Each of the $N$ values can update at most $B$ bit-specific tails lists. Every update performs a binary search in a list of length at most $N$, taking $O(\log N)$ time. Total time is $O(NB\log N)$.

The combined tails lists can contain at most $N$ entries for each of $B$ bits, so the conservative auxiliary-space bound is $O(NB)$. Here $B = 30$ under the source value limit, making it a small fixed factor.

The benchmark defines size as $N$ and uses an increasing sequence in which every value shares the lowest bit. The optimal method updates logarithmic tails structures, while the slower control performs quadratic LIS transitions within each bit-filtered sequence.

## Alternatives and edge cases

- **Quadratic dynamic programming per bit:** Compare each eligible value with all earlier eligible values. This is correct but costs $O(BN^2)$ time in the worst case.
- **One ordinary LIS over all values:** Its longest result may have AND zero because increasing order alone does not guarantee a common set bit.
- **Track every reachable AND value:** Dynamic programming over subsequence AND states can be correct, but coupling those states with increasing-value ordering is more complicated than the common-bit decomposition.
- **All zeros:** Zero has no set bits, so it updates no tails list and the correct result is `0`.
- **One nonzero value:** Its set bits each receive a length-one LIS, making the answer `1`.
- **Duplicate values:** `bisect_left` replaces an existing tail instead of extending it, preserving strict rather than non-decreasing order.
- **Disjoint powers of two:** No two values share a bit, so only length-one subsequences can have non-zero AND.
- **Highest permitted bit:** Values up to $10^9$ may use bit position $29$; all 30 positions from $0$ through $29$ must be represented.
- **Subsequence gaps:** Filtering and patience sorting preserve original relative order, so selected values need not be adjacent.
