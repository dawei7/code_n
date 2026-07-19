## General
**Scan bits from least significant to most significant**

Maintain the current bit position, the position of the most recently encountered `1`, and the largest gap seen. At each step, test the low bit with `n & 1`, then shift the remaining value right by one position.

When the current bit is `1` and a previous set-bit position exists, their difference is the gap between consecutive `1` bits: no other set bit has been encountered between them. Update the maximum and replace the previous position with the current one. Zero bits change neither stored position.

Every adjacent pair is considered exactly when its later `1` is encountered. Non-adjacent pairs are never compared because the stored position is always overwritten by the latest `1`. Thus the maximum recorded difference is precisely the longest binary gap; if no comparison occurs, the initialized result `0` is correct.

## Complexity detail
Right shifts remove one bit per iteration, so the loop runs $L=O(\log n)$ times. The current position, previous set-bit position, maximum gap, and shifting value use a fixed number of integers, giving $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Convert to a binary string:** Scanning characters is correct and still linear in $L$, but it allocates $O(L)$ additional storage.
- **Store every set-bit position:** Consecutive differences can then be computed, but the position list uses unnecessary $O(L)$ space.
- **Compare every pair of set bits:** Filtering for consecutive positions remains correct but raises the worst-case work to $O(L^2)$.
- **One set bit:** Powers of two have no pair and return `0`.
- **Consecutive set bits:** With no zero between them, their distance is `1`.
- **Several set bits:** Only consecutive entries in bit-position order are adjacent; a farther pair separated by another `1` is invalid.
- **Leading zeros:** They are not part of the standard binary representation and cannot create or enlarge a gap.
