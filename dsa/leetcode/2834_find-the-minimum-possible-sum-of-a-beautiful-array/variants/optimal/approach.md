## General

**Choose the smallest values that do not conflict.** A beautiful array contains distinct positive integers and cannot contain two different values summing to `target`. To minimize total sum, reason about positive integers in increasing order.

Let

$$
m=\left\lfloor\frac{\texttt{target}}{2}\right\rfloor.
$$

The first safe block is every value from one through $m$.

**Why the low block is internally valid.** Take two distinct values $a<b\le m$.

If target is even, target equals $2m$. The greatest possible sum of two distinct values at most $m$ is $m+(m-1)<2m$.

If target is odd, target equals $2m+1$. Even allowing the same upper value twice would produce only $2m$, and distinct values produce less.

Thus no two distinct values in one through $m$ sum to target. The special middle value when target is even is safe once because the forbidden condition uses distinct indices and the array values themselves are pairwise distinct; two copies of $m$ cannot appear.

**Why values after the low block must jump to target.** Consider a value $y$ with $m<y<\texttt{target}$. Its complement `target - y` is a positive integer at most $m$, so that complement belongs to the low block. Selecting $y$ would create a forbidden pair.

At `y = target`, the complement is zero, which cannot appear in a positive array. For every larger $y$, the complement is negative. Therefore, all values from target upward are mutually safe with the low block and with one another.

The lexicographically smallest feasible increasing sequence is consequently

$$
1,2,\ldots,m,\ \texttt{target},\texttt{target}+1,\ldots
$$

until $n$ values have been selected.

**Case one: the requested length fits in the low block.** If `n <= m`, the minimum array is simply one through `n`. Its sum is the arithmetic-series formula

$$
\frac{n(n+1)}{2}.
$$

The source writes this as `(1 + n) * n // 2` and reduces it modulo $10^9+7$.

**Case two: a high block is needed.** If `n > m`, take all $m$ low values and let `n - m` be the high-block length.

The low sum is

$$
\frac{m(m+1)}{2}.
$$

The high block starts at target and ends at

$$
\texttt{target}+(n-m)-1.
$$

An arithmetic progression with $n-m$ terms has sum

$$
\frac{\left(2\texttt{target}+n-m-1\right)(n-m)}{2}.
$$

The exact return expression adds those two formulas and applies the modulus.

**Why this sequence minimizes the sum.** Every complementary pair below target permits at most one member. Choosing its smaller member is never worse than choosing its larger member. The sequence one through $m$ makes all such smaller choices. Once they are fixed, every intervening value $m+1$ through target minus one is forbidden, and target is the smallest remaining legal value. All later legal choices are consecutive. Therefore, any different valid sorted array has a first position containing a larger value, which increases its total; the constructed sequence is minimum.

**Modulo is applied only after deriving the ordinary minimum.** The goal is to minimize the true integer sum, not its residue. The algorithm selects values using ordinary ordering and then reduces the exact arithmetic total for output. Attempting to optimize modulo values would be invalid.

**Large constraints motivate the formula.** `n` can be one billion, so explicitly constructing or looping over the array is impossible. The two-block structure lets the method use a fixed number of arithmetic operations.

**Relation to the smaller k-avoiding problem.** The underlying complement-pair reasoning is the same as in the length-fifty variant, but here the huge input bound requires summing implicit ranges rather than scanning candidates with a set.

## Complexity detail

The method performs a constant number of integer divisions, multiplications, additions, comparisons, and one modulo operation. In the usual word-RAM analysis for values bounded by the input constraints, time is $O(1)$ and auxiliary space is $O(1)$.

Python integers are arbitrary precision. If bit complexity is considered, arithmetic cost depends on the $O(\log n+\log\texttt{target})$ bit lengths of intermediate values. Competitive-programming complexity convention treats these bounded-width operations as constant here.

No array of length $n$ is created. The few scalar variables are the only storage, so the method remains usable at the one-billion limit.

The multiplication is performed before integer division, but one of consecutive factors is even, ensuring the arithmetic-series result is exact.

## Alternatives and edge cases

- **Greedy set scan:** Try positive integers in order and skip complements of selected values. It is intuitive and correct but takes $O(n+\texttt{target})$ time and $O(n)$ space, impossible for $n=10^9$.
- **Explicitly build the two blocks:** This takes $O(n)$ time and space merely to sum values whose formula is known.
- **`target = 1`:** `m = 0`, so the entire minimum array is the high block starting at one; the formula yields one through `n`.
- **`n <= m`:** No high values are needed, and the ordinary first $n$ positive integers are already beautiful.
- **Even target midpoint:** It may appear once because values are distinct; the forbidden pair cannot use the same index twice.
- **Odd target:** The low block stops at floor half, and every value through target minus one above that block conflicts with a chosen complement.
- **`n = 1`:** The minimum positive value one is always valid because no pair of distinct indices exists.
- **Large `n`:** Constant-space arithmetic avoids constructing the requested conceptual array.
- **Modulo timing:** Reduce the final exact sum, not individual choices made according to residue.
- **Distinctness:** Both arithmetic blocks contain consecutive nonoverlapping values, so no duplicates occur.
- **Positive values:** Starting the first block at one and the second at target respects positivity even when target is one.
