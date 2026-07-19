## General
**Represent every rotation as a circular window**

Any sequence of type-1 operations selects a cyclic rotation of `s`. View the characters through virtual indices from $0$ to $2N-1$, reading position $i$ as the original character at index $i \bmod N$. Every rotation is then a contiguous window of length $N$ in this virtual doubled sequence; no doubled string needs to be stored.

There are only two alternating patterns at those virtual indices: one expects `0` at even indices and `1` at odd indices, while the other expects the opposite. For a fixed window, the number of mismatches against a pattern is exactly the number of type-2 flips required to realize it.

**Slide both mismatch counts**

Scan the virtual indices while maintaining the mismatch totals for both patterns. Add the entering character's mismatch. Once the window would exceed length $N$, subtract the outgoing character's mismatch. For each full-length window, minimize the answer with both totals.

Every possible cyclic rotation appears as one such window, and every alternating binary string must match one of the two patterns. The mismatch total is both necessary—each wrong position must be flipped—and sufficient—flipping exactly those positions produces the pattern. Taking the minimum across all windows and both patterns therefore gives the optimal number of paid operations.

## Complexity detail
The scan processes $2N$ virtual positions, doing constant work at each, so it takes $O(N)$ time. It stores two mismatch counters, window indices, and the current minimum. Characters are read from the original string with modular indices, so the auxiliary-space bound is $O(1)$ rather than $O(N)$.

## Alternatives and edge cases
- **Materialize `s + s`:** The same sliding-window reasoning is simpler to visualize with a doubled string and still takes $O(N)$ time, but it uses $O(N)$ auxiliary space.
- **Check every rotation independently:** Comparing all $N$ rotations with both alternating patterns is correct but takes $O(N^2)$ time.
- **Single character:** It is already alternating, so no flip is needed.
- **Odd length:** Moving one character across the boundary changes its parity, so different rotations can have different costs.
- **Even length:** A rotation may swap which of the two patterns is named first, but both mismatch totals are always considered.
- **Free rotations:** Type-1 operations are never added to the answer; only type-2 flips are counted.
