## General

**The operations preserve one of two cyclic orientations.** Let $L$ denote one left rotation and $R$ denote reversal. Repeated rotations produce only rotations of the current array. Reversal switches to the reversed orientation, and another reversal switches back; algebraically, $RLR=L^{-1}$. Consequently, every reachable state is either a rotation of `nums` or a rotation of `reversed(nums)`.

The increasing target can therefore be reached only when `nums` is one of these two forms:

- **cyclically increasing:** every circular successor satisfies `next == (current + 1) % n`;
- **cyclically decreasing:** every circular successor satisfies `next == (current - 1) % n`.

If neither circular condition holds, no allowed operation can repair the internal cyclic order, so return `-1`.

**Derive the minimum for a cyclically increasing permutation.** Let $i$ be the index of zero. Rotating left $i$ times moves zero to the front and sorts the array, costing $i$. A pair of reversals can implement rotation in the opposite direction: reverse, rotate left $n-i$ times, and reverse again, costing $n-i+2$. Every sequence ending in the increasing orientation has an even number of reversals and reduces to one of these two rotation directions, so the minimum is

$$
\min(i,\ n-i+2).
$$

**Derive the minimum for a cyclically decreasing permutation.** Sorting must change orientation, so an odd number of reversals is necessary. One canonical route reverses first and then rotates left $n-i-1$ times, costing $n-i$. The other rotates left $i+1$ times and then reverses, costing $i+2$. Any additional pair of reversals merely chooses the opposite rotation direction without improving these normal forms. Thus the minimum is

$$
\min(n-i,\ i+2).
$$

The single-element and length-two overlaps are handled by the same formulas; testing the increasing orientation first still returns the true minimum.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. Finding zero and checking at most two circular orientations each take $O(n)$ time. The algorithm stores only indices and Boolean results, so it uses $O(1)$ auxiliary space.

For scaling evidence, the three benchmark tiers use cyclically increasing permutations of lengths $64$, $256$, and $1024$, with zero halfway through the array. The required orientation scan remains linear. An explicit breadth-first search stores and constructs $O(n)$ full-array states of length $n$, taking $O(n^2)$ time and space on these reachable inputs while still completing under the legal source constraints.

## Alternatives and edge cases

- **BFS over compressed `(orientation, shift)` states:** This has only $2n$ states and can be made $O(n)$, but deriving the two closed-form costs is simpler and avoids a queue.
- **BFS over full arrays:** It is a useful small-permutation oracle and always returns the exact distance, but copying and hashing $O(n)$ arrays across $O(n)$ states costs $O(n^2)$ time and space.
- **Check only the location of zero:** Zero determines the cost only after cyclic orientation is verified; an arbitrary permutation with zero in the same position may be unreachable.
- **Already sorted:** Zero is at index zero in a cyclically increasing array, so the answer is zero.
- **Single element:** `[0]` satisfies both orientations, and the increasing formula returns zero.
- **Length two:** Increasing and decreasing cyclic order coincide modulo two; either valid formula gives the same minimum.
- **Nearly sorted but wrong cyclic order:** Even one adjacent relationship outside the two permitted orientations makes the target unreachable.
