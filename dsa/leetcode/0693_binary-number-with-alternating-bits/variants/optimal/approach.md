## General
**Compare neighboring bits directly**

The least-significant bit gives the first value to remember. Shift `n` right once, then repeatedly extract the new least-significant bit with $n \mathbin{\&} 1$. This new bit was immediately beside the remembered bit in the original representation.

**Stop at the first violation**

If the two bits are equal, that adjacent pair disproves alternation, so return `false`. Otherwise remember the current bit, shift again, and continue toward the most-significant bit.

**Why completing the scan is sufficient**

Every shift exposes exactly one previously unchecked adjacent pair. Returning early is therefore justified by a concrete equal pair. If the loop finishes, every adjacent pair in the representation has been checked and each differed, which is precisely the required condition.

## Complexity detail
A positive integer has $floor(log2(n)) + 1$ significant bits. The scan performs constant work per bit, so it takes $O(\log n)$ time and stores only the current and previous bits, using $O(1)$ extra space.

## Alternatives and edge cases
- **XOR consecutive shifts:** let `mask = n ^ (n >> 1)`; alternating bits make `mask` a run of `1` bits, testable with `mask & (mask + 1) = 0`. This is compact but less direct to derive.
- **Binary-string scan:** convert `n` to text and compare neighboring characters; it is also $O(\log n)$ time but allocates $O(\log n)$ space.
- A one-bit value such as `1` has no adjacent pair and is therefore alternating.
- Leading zeros are not part of the ordinary binary representation and must not be inspected.
- Equal bits anywhere in the representation are sufficient to return `false`, including at either end.
