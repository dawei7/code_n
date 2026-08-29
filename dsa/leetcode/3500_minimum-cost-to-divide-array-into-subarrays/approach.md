## General

**Express boundaries with prefix sums.** Let

$$
N_i=\sum_{h=0}^{i-1}\texttt{nums}[h],
\qquad
C_i=\sum_{h=0}^{i-1}\texttt{cost}[h],
$$

for boundaries $i=0..n$. A subarray $[i,j-1]$ has cost-sum $C_j-C_i$, while the problem's numeric prefix through its right endpoint is $N_j$.

The difficulty is the subarray order multiplier $k\cdot order$. The protected solution removes that extra DP dimension by considering a suffix partition and accounting for how adding a front subarray shifts all later orders.

**Define a suffix DP with local order numbers.** Let `dp[i]` be the minimum cost to partition suffix `i..n-1` when its first subarray is numbered one, its second two, and so on, while each subarray still uses the global numeric prefix $N_j$ from the problem.

Suppose the first suffix subarray ends at boundary $j>i$. Its own cost is

$$
(N_j+k)(C_j-C_i).
$$

The remaining partition begins at $j$. `dp[j]` numbers its first subarray as one, but in the combined partition that subarray must be number two, and every later one is also shifted upward by one. Increasing every remaining subarray's order by one adds $k$ times the total cost weights in suffix $j$:

$$
k(C_n-C_j).
$$

Therefore,

$$
dp[i]=\min_{j>i}
\left[
(N_j+k)(C_j-C_i)
+dp[j]
+k(C_n-C_j)
\right].
$$

For $i=0$, these local order numbers are exactly the original partition's global order numbers, so `dp[0]` is the requested answer.

**Turn each candidate boundary into a line.** Expand the recurrence around query coordinate $x=C_i$:

$$
dp[i]
=
\min_{j>i}
\left[
-(N_j+k)C_i
+dp[j]
+N_jC_j
+kC_n
\right].
$$

For each future boundary $j$, define a line

$$
y=m_jx+b_j,
$$

with

$$
m_j=-(N_j+k)
$$

and

$$
b_j=dp[j]+N_jC_j+kC_n.
$$

Querying the minimum line value at $x=C_i$ yields `dp[i]`.

The initial line represents boundary $j=n$. Here `dp[n]=0`, and the code's slope and intercept are

`-(prefix_nums + k)` and `prefix_nums * prefix_cost + k * total_cost`,

which match $N_n$ and $C_n$.

**Sweep boundaries from right to left.** `prefix_nums` and `prefix_cost` begin at totals $N_n,C_n$. At loop index `i`, subtracting `nums[i]` and `cost[i]` changes them to $N_i,C_i$. The hull is queried at `prefix_cost` to get `answer = dp[i]`. Then the line for boundary $i$ is added for earlier states.

This order guarantees that the hull contains exactly candidates $j>i$ when `dp[i]` is computed.

**Why a deque is enough for the convex hull.** All `nums` values are positive. As the reverse sweep moves $i$ left, $N_i$ strictly decreases, so slopes `-(N_i+k)` are inserted in monotone increasing order. All `cost` values are positive too, so query coordinates $C_i$ move monotonically downward.

With monotone slopes and monotone query coordinates, useful lines appear in deque order. Before a query, while the second front line is no worse than the first at current $x$, the first can never become useful again for later monotone queries and is removed.

When adding a line, the source compares cross-products of slopes and intercept differences. If the middle of the last two lines becomes obsolete before the new line, it is removed from the back. Cross multiplication avoids floating-point intersection calculations and precision errors.

Each line is appended once and removed at most once from each end, so all hull maintenance is linear across the sweep.

**Trace the meaning of one initial query.** If suffix $i..n-1$ is kept as one subarray, the $j=n$ line evaluated at $C_i$ gives

$$
(N_n+k)(C_n-C_i),
$$

the exact cost of that one-subarray suffix with order one. Other lines represent placing an earlier cut at some $j$ and using the already optimized suffix partition beyond it.

**Why the recurrence is correct.** Every suffix partition has a unique first ending boundary $j$. Its first subarray cost, optimal remainder cost, and necessary order-shift charge are exactly the three recurrence terms. Conversely, choosing any $j$ and an optimal `dp[j]` partition produces a valid suffix partition with correct orders. Minimizing over all $j$ is therefore exact. The line transformation is algebraic, and the monotone hull returns that same minimum, so the final `dp[0]` is optimal.

## Complexity detail

Computing total prefix values takes $O(n)$ through `sum`. The reverse loop processes $n$ boundaries. Every line enters the deque once; back-removal and front-removal can each occur only once per line over the whole algorithm. Hull work is amortized $O(1)$ per boundary, so total time is $O(n)$.

The deque can store up to $O(n)$ lines. All other state is scalar, giving $O(n)$ auxiliary space. These bounds match the manifest.

Cross-products and DP values can be large because they combine several prefix sums. Python integers preserve exact arithmetic; fixed-width implementations need sufficiently wide integer types.

## Alternatives and edge cases

- **Quadratic suffix DP:** Evaluating every next boundary $j$ for every $i$ directly costs $O(n^2)$ but follows the same recurrence.
- **DP by number of subarrays:** It adds an unnecessary order dimension; the suffix order-shift term absorbs that information.
- **Floating-point line intersections:** Precision loss can discard the wrong line. Cross-products keep comparisons exact.
- **Arbitrary line order:** A general Li Chao tree could handle it, but positive prefix sums provide monotone slopes and queries for a simpler deque.
- **One element:** The only boundary candidate is $j=n$, and the single-subarray cost is returned.
- **One subarray chosen:** The initial terminal line always represents this valid option.
- **Many cuts:** Each added boundary line represents all optimally partitioned suffixes beyond it.
- **Positive arrays:** Strictly positive `nums` and `cost` values are what guarantee monotonicity used by the deque.
- **Equal line values at a query:** The `>=` front comparison may discard the older line because the newer is at least as good now and for future query direction.
- **Obsolete middle line:** The back cross-product test removes it before it can corrupt later minima.
- **Order starts at one:** The recurrence's first suffix segment uses `+k`, and every prepended cut shifts later segments by another `k`.
- **Global numeric prefix:** $N_j$ includes values before suffix index $i$, exactly matching the problem's formula.
