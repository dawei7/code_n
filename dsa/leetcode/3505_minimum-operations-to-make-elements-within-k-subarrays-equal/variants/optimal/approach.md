## General

For a fixed length-$x$ window, changing every value to a target $v$ costs the sum of absolute deviations from $v$. This convex quantity is minimized by any median. Therefore, first compute an independent equalization cost $C[i]$ for every window `nums[i:i + x]`, then solve only the non-overlapping selection problem.

Coordinate-compress all values. Maintain the current window in two Fenwick trees: one stores occurrence counts and the other stores value sums. The count tree locates the lower median by order statistic. If the median is $v$, and the two trees report counts $c_L,c_R$ and sums $S_L,S_R$ at or below and strictly above $v$, respectively, then

$$
C[i] = vc_L-S_L + S_R-vc_R.
$$

Sliding one position removes the outgoing value and inserts the incoming value in both trees, so every window cost follows from logarithmic updates, prefix sums, and one order-statistic search. Duplicate and negative values require no special handling because compression preserves order while the sum tree preserves original magnitudes.

Now process how many windows have been selected. Let `previous[p]` be the minimum cost of choosing one fewer window entirely inside the prefix `nums[:p]`. For the current layer, the optimum for a prefix of length $p$ either skips its final element or takes the length-$x$ window ending there:

$$
\texttt{current[p]} = \min\bigl(\texttt{current[p-1]},
\texttt{previous[p-x]} + C[p-x]\bigr).
$$

The second transition jumps back by exactly $x$, which guarantees non-overlap while still allowing adjacent windows. Initialize the zero-window layer to zero for every prefix and repeat the layer $k$ times.

Although the contract asks for at least $k$ windows, all window costs are nonnegative. From any feasible choice of more than $k$ windows, removing extras cannot increase its cost, so an optimum exists with exactly $k$. The final DP layer therefore returns the requested minimum.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. Sorting the distinct values and computing compressed indices takes $O(n\log n)$ time. Each of $O(n)$ sliding positions performs $O(\log n)$ Fenwick work, and the $k$ dynamic-programming layers each scan $n$ prefixes. Total time is $O(n\log n+nk)$.

The compressed values, two trees, window costs, and two DP rows use $O(n)$ space. The benchmark grows $n$ with $x=n/4$ and fixed $k=2$. It contrasts the Fenwick window maintenance with a correct method that sorts and rescans every window independently, requiring superlinear work per collection of windows.

## Alternatives and edge cases

- **Sort every window:** Rebuilding a sorted length-$x$ slice and summing its deviations is correct, but costs $O(nx\log x)$ for all overlapping windows.
- **Two heaps with lazy deletion:** Balanced lower and upper heaps can maintain the median and both-side sums in $O(\log x)$ per slide, matching the main time class but requiring careful delayed removals and rebalancing.
- **Full two-dimensional DP:** Storing all $k(n+1)$ states is unnecessary because a layer depends only on the preceding layer and its own previous prefix.
- **Greedy cheapest windows:** Taking windows solely by individual cost can block a slightly more expensive early choice that permits a better collection later; the prefix DP accounts for this interaction.
- **Even window length:** Any value between the two central sorted elements is optimal; choosing the lower median gives the same total cost.
- **Duplicate medians:** The count and sum split includes every copy at or below the selected median, and zero-distance copies contribute nothing.
- **Negative values:** Compression affects only ranks, while all cost arithmetic uses the signed originals.
- **Adjacent windows:** A transition from prefix `p - x` permits the preceding chosen window to end exactly where the new one begins.
- **Already uniform windows:** Their zero costs are valid DP candidates and may make the global optimum zero.
- **Large answers:** Values span two million and many elements may move, so fixed-width implementations need 64-bit arithmetic.
