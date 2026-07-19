## General
**Pair positions from opposite ends**

Reversal pairs positions that are equally far from opposite ends. Keep `left` at the beginning and `right` at the end. While `left < right`, swap `s[left]` with `s[right]`, then move both pointers inward.

**Why each swap finalizes two positions**

After each swap, the prefix before `left` and the suffix after `right` are already in their final reversed positions. The untouched middle still contains exactly the remaining original characters, so pairing its outermost two positions extends both finalized regions without disturbing earlier work. When the pointers meet or cross, every position has been finalized; a middle character in an odd-length array correctly remains where it is.

**Trace an odd-length array**

For `["h", "e", "l", "l", "o"]`, the first swap places `o` and `h`, the second places the two `l`/`e` endpoints of the remaining middle, and the center `l` needs no move.

## Complexity detail
There are $\left\lfloor n / 2 \right\rfloor$ swaps, so the running time is $O(n)$. Only two indices and a constant-size temporary value used by the swap are needed, giving $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Slice reversal or a new reversed list:** takes $O(n)$ time but allocates $O(n)$ extra storage and violates the in-place requirement.
- **Repeated front insertion:** can take $O(n^2)$ because every insertion shifts existing list elements.
- An empty list and a one-character list require no swaps.
- Duplicate characters do not change the pairing rule because positions, not character identities, determine the reversal.
