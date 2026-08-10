## General

**Analyze the operation one bit at a time.** For one bit position, two selected numbers contain one of four bit pairs:

- `(0,0)` becomes `(0,0)` under AND and OR;
- `(0,1)` or `(1,0)` becomes `(0,1)`;
- `(1,1)` becomes `(1,1)`.

In every case, the total number of one-bits across the two numbers is unchanged. Therefore the operation can move an occurrence of a bit between array elements, but it cannot create or destroy occurrences. Each bit position has a conserved count.

The first loop records those resources. `cnt[i]` becomes the number of input values whose bit $i$ is set. Thirty-one positions are enough because `nums[i] <= 10^9 < 2^{30}`; the extra position is harmless.

**Why bits should be concentrated.** The objective uses squares. For nonnegative $a\ge b$ and a positive quantity $\delta$ that can be moved from $b$ to $a$,

$$
(a+\delta)^2+(b-\delta)^2-a^2-b^2
=2\delta(a-b)+2\delta^2\ge0.
$$

Concentrating value into an already larger selected number never decreases the square sum. The best arrangement therefore packs available bit occurrences together as much as possible instead of spreading them evenly.

**Build the largest possible selected number first.** For each of the `k` chosen numbers, the source starts `x = 0`. It scans every bit. If `cnt[i]` is positive, it places that bit into `x` with `x |= 1 << i` and consumes one occurrence with `cnt[i] -= 1`.

The first constructed number receives every bit that occurs at least once in the input. The second receives every bit that originally occurred at least twice, the third every bit occurring at least three times, and so on. Thus constructed values are non-increasing and their set bits are nested.

For a fixed bit, this assigns its occurrences to the earliest possible constructed numbers. Doing so simultaneously for every bit aligns high and low bit contributions on the same numbers, creating the concentration favored by convex squaring.

**Why the conserved counts are achievable.** The AND/OR operation moves bit occurrences toward the OR result while leaving their count fixed. Operations can be applied repeatedly to concentrate the occurrences of different bit positions into chosen array slots. Bits act independently under AND and OR, so the count profile represented by the greedy constructed values is reachable from some sequence of allowed operations. The algorithm needs only the maximum score, not the explicit operation sequence.

**A majorization view of correctness.** Sort any achievable chosen values descending. For any prefix of $t$ selected numbers, a bit occurring $c$ times can contribute to at most $\min(t,c)$ of them. The greedy construction attains that maximum for every bit and every prefix because the bit appears in exactly the first $\min(k,c)$ constructed numbers. Consequently, its prefix values are as concentrated as conservation permits. A convex function such as the square is maximized by this majorized arrangement.

**Trace the first example.** Values `2,6,5,8` have bit occurrences that allow the first constructed number to take bits forming fifteen. After those counts are decremented, remaining occurrences form six for the second number. Their squares sum to `225 + 36 = 261`.

**Modulo belongs after each square addition.** The mathematical score can be very large. The code calculates `x*x` with Python integers, adds it to `ans`, and reduces modulo $10^9+7$ every iteration. Modular reduction preserves the final required remainder and prevents `ans` itself from growing unnecessarily.

The greedy construction runs exactly `k` rounds. Bit occurrences left after that correspond to unselected array elements and do not contribute to the requested score.

## Complexity detail

Let $B=31$, or generally $B=O(\log V)$ for maximum value $V$. Counting scans $nB$ bit positions. Constructing `k` numbers scans $kB$. Total time is $O((n+k)\log V)$, which is $O(n\log V)$ because $k\le n$.

The count array has $B$ entries and all other state is scalar, so auxiliary space is $O(\log V)$, constant 31 words under the constraints. The result values are constructed one at a time rather than stored in a length-`k` array.

## Alternatives and edge cases

- **Simulate AND/OR operations:** Searching operation sequences is enormous and unnecessary because per-bit counts fully characterize the optimum.
- **Spread bits evenly:** Squaring is convex, so spreading conserved value loses the concentration benefit.
- **`k = 1`:** The selected value receives every bit that appears anywhere, equivalent to the OR of all inputs.
- **`k = n`:** Every conserved bit occurrence is consumed; the greedy still optimally arranges the entire array.
- **Bit appearing `c` times:** It is placed in exactly the first $\min(c,k)$ constructed values.
- **Duplicate input values:** They simply add bit occurrences and need no special handling.
- **Modulo:** Optimize the true integer square sum conceptually; reduce only the accumulated numerical result, not bit counts.
- **Fixed bit bound:** Thirty-one positions cover every legal positive input value.
