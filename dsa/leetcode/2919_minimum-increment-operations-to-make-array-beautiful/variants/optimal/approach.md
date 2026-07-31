## General

**Reduce the condition to length-three windows.** If every contiguous window
of exactly three elements contains a value at least `k`, then every longer
subarray also contains such a window and therefore has a qualifying maximum.
Conversely, length-three subarrays are explicitly required. The task is thus
to choose positions that hit every length-three window. Choosing position $i$
costs $\max(0,\texttt{k}-\texttt{nums[i]})$ increments; a value already at
the threshold has cost zero.

**Track the latest chosen position.** Let `dp[i]` be the minimum cost of a
valid selection ending with position $i$ chosen. Consecutive chosen positions
may be at most three indices apart, or an uncovered length-three window would
lie between them. Therefore

$$
\texttt{dp[i]} =
\max(0,\texttt{k}-\texttt{nums[i]})
+ \min(\texttt{dp[i-1]},\texttt{dp[i-2]},\texttt{dp[i-3]}).
$$

Three virtual zero-cost states before the array initialize the first three
positions. The same gap argument shows that every transition preserves
coverage and that any valid selection must use one of those three predecessor
states, so the recurrence loses no optimum. At the end, the final chosen
position must lie among the last three indices; taking the minimum of their
states covers the suffix and yields the global optimum. Only those three
values are needed while scanning.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. Each position performs a constant amount
of work, giving $O(n)$ time. The rolling three-state dynamic program uses
$O(1)$ auxiliary space.

## Alternatives and edge cases

- **Enumerate raised-position subsets:** Testing all $2^n$ choices can find the optimum but is exponential.
- **Full dynamic-programming array:** Storing every `dp[i]` value uses the same recurrence and $O(n)$ time, but consumes $O(n)$ space when only three predecessors are needed.
- **Greedily raise the cheapest value in each window:** Overlapping windows make local choices interact, so a cheapest current choice can prevent a cheaper global placement pattern.
- **Values already at least `k`:** They are valid zero-cost chosen positions and naturally reset the maximum allowed gap.
- **Threshold zero:** Every non-negative input value already qualifies, so the answer is zero.
- **Exactly three elements:** At least one position must qualify; the answer is the smallest individual raising cost.
- **Large increment totals:** The optimum can exceed 32-bit signed range, so fixed-width implementations need 64-bit dynamic-programming totals.

