## General

**Inspect the lowest unresolved bit.** For the current positive value, let $p$ be its lowest set bit. Every bit below $p$ is zero, so adding or subtracting $p$ changes the lowest unresolved part of the binary representation without disturbing any lower position.

If the bit worth $2p$ is zero, subtract $p$. This clears an isolated lowest set bit in one operation. Adding $p$ would instead move that contribution upward and cannot use fewer operations than clearing it immediately.

If the bit worth $2p$ is also one, add $p$. The carry clears both set positions and continues through any longer adjacent run of ones. Subtracting $p$ would only clear the first bit and leave the rest of the run to be handled later. For a run of exactly two ones the choices tie; for a longer run, carrying toward the next power of two is strictly better.

After either choice, the lowest unresolved set bit moves to a higher position. Repeating the rule constructs the non-adjacent signed-binary representation of `n`: each operation contributes one positive or negative power of two, and no two chosen nonzero digits are adjacent. Replacing any adjacent signed digits by their carried equivalent never increases their count, so this representation has the minimum possible number of nonzero terms. Its number of terms is exactly the minimum number of allowed operations.

## Complexity detail

Each iteration moves the lowest unresolved set bit to a higher binary position, and at most one final carry can create a new leading bit. There are $O(\log n)$ bit positions, so the algorithm takes $O(\log n)$ time. It stores only the current value, its lowest set bit, and the operation count, using $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Breadth-first search:** Treating integers as graph vertices and additions or subtractions as edges finds a shortest path, but exploring a range proportional to `n` costs far more time and memory than the bitwise greedy rule.
- **Memoized recurrence:** Trying both directions around a nearby power of two can be made correct, but it introduces recursion and cached states that the local signed-bit decision avoids.
- **Exact powers of two:** The lowest set bit equals the entire value, so one subtraction reaches zero.
- **Shifted runs of ones:** The adjacency test must compare $p$ and $2p$, not only the two least significant absolute positions; for example, `28` has the decisive run beginning at the $4$ bit.
- **Two adjacent ones:** Addition and subtraction can tie, as for `3`; choosing the carry remains optimal and keeps the rule uniform.
- **Temporary growth:** Adding the lowest set bit may increase the value or create a new leading bit, which is permitted by the contract and can reduce the total operation count.
