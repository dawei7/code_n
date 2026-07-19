## General
**Use symmetry to target a non-negative distance**

Reflecting every chosen direction negates the final position without changing the move count. Work with `distance = abs(target)`.

**Characterize what a fixed number of moves can reach**

If all `m` moves point right, their sum is the triangular number $S = m(m + 1) / 2$. Reversing move `i` changes the total by `2i`. Therefore `distance` is reachable in `m` moves exactly when `S >= distance` and `S - distance` is even. The numbers `1` through `m` can form every subset sum from `0` through `S`, so an even excess can always be removed by reversing moves whose lengths sum to `(S - distance) / 2`.

**Jump directly to the first large enough triangular number**

Solve `m(m + 1) / 2 >= distance` using the integer square root of `1 + 8 * distance`, then correct upward by at most one step. If the excess is odd, add moves until its parity becomes even. At most two additional moves are needed: adding the next move toggles parity when that move is odd, and otherwise the following move toggles it.

The initial `m` is the smallest with enough total distance, and the parity loop chooses the first such `m` whose signed moves can equal the target. Every smaller count fails either the magnitude or parity condition, so the returned count is minimum.

## Complexity detail
On the word-RAM model for the bounded integer input, the integer-square-root calculation and at most three corrections use a constant number of operations, giving $O(1)$ time. Only a few integer variables are stored, giving $O(1)$ space.

## Alternatives and edge cases
- **Accumulate steps one by one:** Stop when the triangular sum is large enough with matching parity; this is simple and correct but takes $O(\sqrt{|target|})$ iterations.
- **Binary search for the first triangular bound:** This avoids the square-root formula but uses $O(\log |target|)$ time before the parity correction.
- **Breadth-first search over positions:** It explores many duplicate states and is unnecessary once magnitude and parity are recognized.
- **Negative target:** Absolute value is sufficient because every route can be reflected.
- **Target zero:** No move is needed, so return `0`.
- **Odd excess:** Reaching or passing the magnitude alone is insufficient; signed sums preserve the triangular sum's parity.
