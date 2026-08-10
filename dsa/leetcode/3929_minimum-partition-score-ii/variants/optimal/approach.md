## General

A straightforward dynamic program would choose every cut position for every number of parts. With up to $5\cdot10^4$ elements, an $O(kN^2)$ or even $O(N^2)$ method is far too slow. The source combines two optimizations:

1. a penalty transforms “exactly `k` parts” into a one-dimensional dynamic program that chooses its own number of parts;
2. a monotone convex hull trick evaluates that dynamic program in linear time for one penalty.

Binary search then finds the penalty associated with exactly the requested part count.

**Double the score to keep every calculation integral**

For a subarray whose element sum is $s$, its value is

$$
T(s)=\frac{s(s+1)}{2}.
$$

The source works with twice the score:

$$
2T(s)=s^2+s.
$$

This avoids fractions throughout the dynamic program. The final line divides by two after recovering the unpenalized doubled score. That division is exact because $s(s+1)$ is always even.

Let $P_i$ be the sum of the first $i$ values, with $P_0=0$. Because all input numbers are positive, the prefixes are strictly increasing. If the final segment starts after position $j$ and ends at $i$, its sum is $P_i-P_j$, so its doubled contribution is

$$
(P_i-P_j)^2+(P_i-P_j).
$$

**Temporarily charge a penalty per part**

For an integer penalty $\lambda$, `run(penalty)` minimizes

$$
\text{doubled partition score}+\lambda\cdot\text{number of parts}
$$

without requiring a fixed part count. It returns both the minimum penalized cost and the number of parts used by its chosen optimum.

Let $F_i$ be the best penalized cost for the first $i$ elements. Trying a previous cut $j<i$ gives

$$
F_i=
\min_{0\le j<i}
\left[
F_j+(P_i-P_j)^2+(P_i-P_j)+\lambda
\right].
$$

Expanding the square and grouping everything that depends on $i$ outside the choice gives

$$
F_i=P_i^2+P_i+\lambda+
\min_{j<i}
\left[
(-2P_j)P_i+
\left(F_j+P_j^2-P_j\right)
\right].
$$

For every possible cut $j$, the bracketed expression is a line evaluated at $x=P_i$:

$$
m_jx+b_j,
$$

with slope $m_j=-2P_j$ and intercept $b_j=F_j+P_j^2-P_j$. This is exactly what the arrays `slopes` and `intercepts` store.

The initial line represents the empty prefix $j=0$: its slope, intercept, penalized cost, and part count are all zero. Selecting it makes the first segment begin at index zero.

**Querying the best previous cut**

At the current positive prefix `prefix`, the source compares the line at `head` with the next line. If the next value is smaller, the current head can never become best again for later, even larger prefix sums, so `head` advances.

When the two values are equal, the source advances only if the next line's stored partition uses more parts. After adding the new final segment, both candidates' counts increase by one, so this comparison makes `run` prefer the larger number of parts among equal-cost penalized solutions. That tie rule is important to locating the correct boundary during penalty binary search.

Once the best line is at `head`, the source computes

`cost = prefix * prefix + prefix + line_value + penalty`.

The new partition count is the chosen prefix partition's count plus one. The new state then becomes a line for future endpoints:

- `new_slope = -2 * prefix`;
- `new_intercept = cost + prefix * prefix - prefix`;
- its stored count is the newly computed number of parts.

These expressions are the direct substitutions of $P_i$ and $F_i$ into the line formula above.

**Maintaining the lower convex hull**

Positive array values make prefix sums strictly increase. Consequently, newly inserted slopes $-2P_i$ are strictly decreasing, and query coordinates $P_i$ are strictly increasing. This monotonicity permits an array-backed deque instead of a general-purpose line container.

Before adding a new line, the source checks the last two retained lines and the candidate. If their intersection order would make the middle line permanently useless, it decreases `tail` and removes that line. The products named `left` and `right` compare intersection positions by cross multiplication. No floating-point division is used, so very large integer coefficients cannot introduce rounding errors.

Each line is inserted once, removed from the back at most once, and passed by `head` at most once. A complete `run` is therefore linear despite the nested-looking `while` loops.

The `slopes`, `intercepts`, and `counts` arrays are allocated once outside `run` and reused. Each invocation rebuilds the active prefix of the hull from index zero.

**Why changing the penalty controls the part count**

At penalty zero, splitting any segment with positive sums $a$ and $b$ changes its doubled quadratic contribution from

$$
(a+b)^2+(a+b)
$$

to

$$
a^2+a+b^2+b,
$$

a reduction of $2ab>0$. Therefore the optimum uses all $N$ singleton parts.

As $\lambda$ increases, every additional part becomes more expensive. The optimal chosen part count can only stay the same or decrease. This monotone response is what binary search uses.

The source searches the largest penalty for which `run` still returns at least `k` parts. The upper bound `total * total` is sufficient: the entire possible improvement in the squared portion from splitting is smaller than or equal to the one-segment square, while every extra segment at that penalty pays another full `total²`. Thus the chosen solution has been driven down to one part by the high end.

If `run(middle)` uses at least `k` parts, the boundary is at `middle` or above, so `low` moves up. Otherwise the penalty is already too large and `high` moves below it.

**Recovering the exact unpenalized answer**

Let $A_c$ be the minimum doubled score using exactly $c$ parts. The segment cost has the required convex/Monge structure, so the optimal values $A_c$ have diminishing improvements as the number of parts grows. Adding $\lambda c$ places a line of slope $c$ over each exact-count optimum. At the boundary penalty, a supporting line touches the exact-count curve at `k`, possibly along a tie spanning several counts.

The query tie rule chooses the larger count in such a tie. Selecting the largest integer penalty with a returned count of at least `k` positions the search on the correct side of that supporting line. Even when `run(low)` returns a count greater than `k`, the tied marginal improvement makes the interpolated value for `k` equal to

$$
A_k=\text{penalized\_cost}-\texttt{low}\cdot k.
$$

The source then divides this doubled value by two. This penalty-recovery technique is often called Lagrangian relaxation or the “aliens trick”; the convex hull handles positions within one run, while the penalty handles the number of parts across runs.

## Complexity detail

Let $N$ be the array length and $S$ its total sum. One `run` processes all $N$ prefixes. Because each hull line advances past the head or leaves the tail at most once, its time is $O(N)$ and its three arrays use $O(N)$ space.

Binary search examines integer penalties from zero through $S^2$, requiring $O(\log(S^2+1))=O(\log S)$ runs. The final call at `low` adds one more linear pass. Total time is $O(N\log S)$ and additional space is $O(N)$, matching the manifest.

All hull comparisons use integer multiplication. Python's unbounded integers prevent fixed-width overflow, though arithmetic on larger integers naturally has a bit-level cost not shown in the usual RAM-model bound.

## Alternatives and edge cases

- **Dynamic programming over cuts and part counts:** The direct recurrence is easy to derive but costs $O(kN^2)$ time, which is infeasible for $N=5\cdot10^4$.
- **One-dimensional dynamic programming without a hull:** A fixed penalty removes the explicit part dimension, but trying every prior cut still costs $O(N^2)$ per run. The line expansion is what makes each run linear.
- **Floating-point intersection coordinates:** Division can round incorrectly for large prefixes and costs. Cross multiplication preserves exact hull decisions.
- **Binary search without a deterministic tie rule:** At a penalty where different part counts have equal cost, arbitrary choices can put the returned count on the wrong side of the boundary. Preferring more parts makes the search convention consistent.
- **Forget to double the score:** Using `s * (s + 1) // 2` inside the line algebra complicates coefficients and can invite premature integer division. The source keeps the exact doubled objective until the final return.
- **Exactly one part:** A sufficiently large penalty selects one segment; subtracting `low * 1` recovers the value of the whole array.
- **Exactly `N` parts:** At zero penalty, positivity makes every beneficial split strict, so all singleton parts are selected and the requested score is recovered.
- **All values positive:** Strictly increasing prefix sums give strictly decreasing line slopes. Zero or negative elements would invalidate the monotone-hull assumptions used by this implementation.
- **Equal penalized line values:** The source chooses the candidate carrying more prefix parts, then adds one. This is deliberate boundary behavior, not an arbitrary optimization detail.
- **Large prefix sums:** Products such as `prefix * prefix` and cross products can exceed 64-bit limits in some languages. Python evaluates them exactly.
- **Reused hull arrays:** Every `run` resets `head`, `tail`, and line zero before scanning, so data left beyond the new tail from an earlier binary-search call is inactive and harmless.
- **No empty subarrays:** A line for prefix $j$ is inserted only after processing that prefix and is queried only by later, larger prefixes. Hence every chosen final segment contains at least one element.
