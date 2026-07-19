## General
**Record only positions that a swap must repair**

Scan the strings together and record the ordered character pair `(s1[i], s2[i])` whenever the characters differ. A swap changes at most two positions, so more than two mismatches makes the answer immediately `false`.

**Classify the possible mismatch counts**

Zero mismatches means the strings are already equal, which is valid because the operation count is at most one. Exactly one mismatch cannot work: swapping two positions preserves each string's character multiset and cannot change only one position. More than two mismatches also cannot work.

The only nontrivial case therefore has exactly two mismatches.

**Require the two character pairs to cross-match**

Suppose the mismatches are `(a, b)` and `(c, d)`. Swapping the two positions in `s1` repairs both precisely when `a = d` and `c = b`. Equivalently, the second ordered pair must be the reverse of the first.

If this cross-match holds, performing that swap produces equality. If it does not, neither swapping those positions nor any positions that already match can repair both mismatches. These cases exhaust every possible one-swap outcome.

## Complexity detail
The scan compares at most $n$ character pairs, taking $O(n)$ time. At most two mismatch pairs are retained, so auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Try every swap:** Constructing and testing every index pair is correct but takes at least $O(n^2)$ candidate swaps and may copy strings repeatedly.
- **Sort both strings first:** Equal character multisets are necessary for a repair, but four or more misplaced characters can share a multiset and still require several swaps.
- **Frequency counting plus mismatch count:** This is correct, but the two ordered mismatch pairs already verify both multiplicity and placement.
- **Already equal:** Return `true` without requiring an actual swap; choosing the same index would also leave a string unchanged.
- **One mismatch:** A swap cannot alter only one position, so the result is `false`.
- **Repeated characters:** They do not change the cross-pair criterion.
- **Adjacent or distant indices:** Distance is irrelevant; any two indices in one string may be swapped.
- **Swap either string:** The cross-match condition is symmetric, so checking one direction is sufficient.
