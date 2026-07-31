## General

For one positive value $x$, repeatedly subtracting `k` requires exactly

$$
\left\lceil\frac{x}{k}\right\rceil
$$

operations. Fewer subtractions leave the value positive; that many make it zero or negative. Since an operation changes only its selected index, the minimum count for the whole array is therefore

$$
\texttt{nonPositive(nums, k)}
= \sum_{x \in \texttt{nums}} \left\lceil\frac{x}{k}\right\rceil.
$$

Evaluate each ceiling with integer arithmetic as `(x + k - 1) // k`. While summing, stop as soon as the count exceeds $k^2$, because the remaining positive elements cannot restore feasibility.

The feasibility predicate compares this sum with $k^2$. When `k` increases, every ceiling term stays the same or decreases, while $k^2$ strictly increases. Thus feasibility is monotone: all values before one boundary fail, and that boundary and every larger value pass.

Binary-search the first feasible value in $[1,H]`. This interval always contains an answer. At `k = H`, we have $k \ge V$, so every array element needs at most one operation and the total is at most $N$. We also have $k \ge \lceil\sqrt N\rceil$, so $N \le k^2$; consequently `H` is feasible.

During binary search, a feasible middle value remains a possible minimum, so move the upper boundary to it. An infeasible middle value and everything smaller can be discarded, so move the lower boundary above it. When both boundaries meet, every smaller value has been excluded and the retained value is feasible, making it exactly the minimum required `k`.

## Complexity detail

One feasibility check scans at most $N$ elements and takes $O(N)$ time. Binary search performs $O(\log H)$ checks, so total time is $O(N\log H)$. The running sum, bounds, and loop variables use $O(1)$ auxiliary space.

The benchmark defines size as $N$ and fills the array with the maximum legal value. The binary-search range stays bounded by $H$, while a slower control tests every candidate `k` from `1` upward and rescans the array, adding a growing factor to its runtime.

## Alternatives and edge cases

- **Try `k = 1, 2, 3, ...`:** This finds the same first feasible value but costs $O(NK)$ when the answer is $K$, instead of exploiting monotonicity.
- **Simulate every subtraction:** Repeatedly changing each value reproduces the operation definition but can perform far more work than the constant-time ceiling formula.
- **Fixed upper bound `10^5`:** It is legal and feasible under the source constraints, but $H$ gives a tighter problem-derived interval.
- **Ceiling division:** Floor division alone undercounts any value not divisible by `k`; a positive remainder still requires one final subtraction.
- **Exact budget equality:** The condition uses “at most,” so a count equal to $k^2$ is feasible.
- **Overshooting zero:** A final subtraction may make an element negative; it need not land exactly on zero.
- **Many small values:** The answer can exceed $V$ because even one operation per element may require $k^2 \ge N$; the $\lceil\sqrt N\rceil$ part of $H$ covers this case.
- **Large products:** Implementations in fixed-width languages should compute the sum and $k^2$ with a wide enough integer type.
- **Early termination:** Once the accumulated count exceeds $k^2$, returning false is safe and avoids unnecessary terms.
