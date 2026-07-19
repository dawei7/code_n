## General
**Reject amounts that cannot physically fit**

The two jugs can hold at most $x + y$ units in total. Any larger target is impossible regardless of the pouring sequence. A zero target is always achievable by leaving both jugs empty.

**Identify the indivisible volume unit**

Filling, emptying, and pouring can change the stored amounts only by combinations of the two capacities. Consequently every measurable total must be a multiple of $\gcd(x,y)$. Conversely, Bézout's identity shows that integer combinations of $x$ and $y$ produce every multiple of their greatest common divisor. Repeated legal pours realize those combinations while keeping each jug within its capacity.

Therefore, once the total-capacity check passes, the target is measurable exactly when it is divisible by $\gcd(x,y)$.

**Compute the divisor with Euclid's algorithm**

Repeatedly replace `(x,y)` with $(y, x \bmod y)$ until the second value becomes zero. Each replacement preserves the set of common divisors, and the final nonzero value is the greatest common divisor. Testing `target % gcd = 0` completes the decision without exploring individual jug states.

**Trace the classic capacities**

For capacities `3` and `5`, Euclid's algorithm gives gcd `1`, so every whole-number target up to `8`, including `4`, is measurable. Capacities `2` and `6` have gcd `2`, so target `5` is impossible.

## Complexity detail
Euclid's remainder sequence shrinks at least as quickly as consecutive Fibonacci numbers, requiring $O(\log \min(x,y))$ iterations. The algorithm stores only the two changing capacities and a few scalar values, using $O(1)$ space.

## Alternatives and edge cases
- **Breadth-first search over jug states:** directly models every operation but can visit $O(xy)$ states and is unnecessary for a reachability decision.
- **Depth-first state exploration:** has the same state-space cost and needs explicit cycle detection.
- **Subtractive GCD:** preserves correctness but may require linear time when capacities are consecutive.
- Target `0` is achievable even when both capacities are zero.
- A target greater than $x + y$ is impossible even when divisible by the gcd.
- If one jug has zero capacity, only zero and the other jug's full capacity are measurable.
- When both capacities are zero and the target is positive, the capacity check rejects it before any modulo operation.
