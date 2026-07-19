## General
**Partition values around the median**

Use in-place quickselect to find the median value. The eventual odd positions must receive values greater than the median first, even positions receive values smaller than the median last, and copies equal to the median fill the remaining gaps. A three-way Dutch-national-flag partition can establish exactly those groups in one pass.

Quickselect uses the same three-way partition on the ordinary index range and continues only in the region containing the middle rank. Choosing a median-of-three pivot gives stable practical behavior; its expected running time is linear while retaining constant auxiliary storage.

**Virtual indices visit peaks before valleys**

Ordinary partition order would group large and small values contiguously. Instead, map logical partition position `i` to physical index $(1 + 2 \cdot i) \bmod (n | 1)$. This visits all odd indices first, followed by the even indices in a wraparound order.

Run three-way partitioning through that mapping. Values larger than the median move to the front of virtual order—the physical odd peak positions. Values smaller than the median move to its back—the physical even valley positions. Median copies remain between them and separate repeated extremes.

**The virtual partition implies every strict inequality**

After partitioning, every odd slot is drawn from the high side whenever needed, and every adjacent even slot is drawn from the low or median side. Reversing the effective halves through virtual order prevents equal duplicated values from being placed against each other in the dangerous middle boundary.

Because the problem guarantees that a strict arrangement exists, no value occurs too often to overwhelm all positions of one parity. The high/median/low placement therefore yields `even < odd` on the left of each peak and `odd > even` on its right. Only swaps are performed, so the result preserves the original multiset exactly.

## Complexity detail
Quickselect takes expected $O(n)$ time, and the virtual-index three-way partition takes $O(n)$ time. Both operate through indices and swaps, using $O(1)$ auxiliary space. A deterministic poor pivot sequence can make this quickselect implementation $O(n^2)$ in the worst case.

## Alternatives and edge cases
- **Sort and reverse-interleave two halves:** is simpler and correct in $O(n \log n)$ time with $O(n)$ copied storage.
- **Sort and alternate adjacent values directly:** can place equal median copies next to one another and violate strictness.
- **Validate against one expected array:** is incorrect because many different permutations satisfy the contract; validation must check both the multiset and every strict inequality.
- Two elements are valid when ordered low then high. Heavy duplication is the central edge case and is handled by the median group plus virtual indexing.
