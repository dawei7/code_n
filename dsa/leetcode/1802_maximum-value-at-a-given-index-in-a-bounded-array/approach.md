## General

**For a proposed peak, make every other position as small as possible**

Suppose `nums[index]` is fixed to a candidate value $x$. To decide whether $x$ is feasible, construct the minimum-sum array having that peak.

Moving one position away from the peak, a value can decrease by at most one because adjacent absolute differences must be at most one. To minimize the sum, decrease by exactly one at every step until reaching the positive lower bound 1, then remain at 1.

Thus a side of the array looks like

$$
x-1,\ x-2,\ x-3,\ldots,1,1,\ldots
$$

on the left, and similarly on the right. Any other valid array with the same peak has values at least as large position by position, so this profile gives the exact minimum sum required for $x$.

**Sum one descending side in constant time**

The helper named `sum(x, cnt)` computes the minimum total for `cnt` consecutive positions whose first value may be $x$ and then decreases by one toward the floor 1.

If `x >= cnt`, the sequence never reaches zero within those positions. Its terms are

$$
x,\ x-1,\ldots,x-\texttt{cnt}+1,
$$

and its arithmetic-series sum is

$$
\frac{(x+x-\texttt{cnt}+1)\cdot\texttt{cnt}}{2}.
$$

If `x < cnt`, the positive descending part has terms $x,x-1,\ldots,1$ and sum $x(x+1)/2$. The remaining `cnt - x` positions must be ones. The helper returns

$$
\frac{x(x+1)}{2}+\texttt{cnt}-x.
$$

The source shadows Python's built-in `sum` name only inside `maxValue`. Calls in this scope intentionally refer to the helper.

**Assemble the whole minimum profile without double-counting the peak**

For candidate peak `mid`:

- there are `index` positions strictly left of the peak, beginning with allowed value `mid - 1`, so their minimum total is `sum(mid - 1, index)`;
- there are `n - index` positions from the peak through the right edge, beginning with `mid`, so their minimum total is `sum(mid, n - index)`.

The left call excludes the peak and the right call includes it, so the two values add to the whole array exactly once.

The candidate is feasible precisely when this minimum required total is no greater than `maxSum`. If even the cheapest valid profile costs too much, no array with that peak can work. If it fits, unused budget causes no problem because the sum only needs to be at most `maxSum`.

**Why feasibility is monotone**

If peak value $x$ is feasible, every smaller positive peak is feasible: lowering the peak and rebuilding its minimum profile cannot increase the required sum. Conversely, once a candidate is too large, every greater peak requires at least as much total.

The feasible peak values therefore form a prefix of integers beginning at one. This monotonicity permits binary search for the last feasible value.

**Upper-mid binary search**

The search starts with `left = 1` and `right = maxSum`. One is always feasible because $n\leq\texttt{maxSum}$ and an all-ones array costs $n$. No individual value can exceed the total budget, so `maxSum` is a safe upper bound.

While the bounds differ, the solution computes

`mid = (left + right + 1) >> 1`.

Right shift by one performs integer division by two here. Adding one chooses the upper middle. If `mid` is feasible, `left = mid` keeps it and searches larger values. Otherwise, `right = mid - 1` discards it and everything larger. The upper middle prevents an infinite loop when only two candidates remain.

When the bounds meet, `left` is the largest feasible peak.

**Following the first example**

For `n = 4`, `index = 2`, and proposed peak 2, the two left positions have a minimum total of two and may be `[1,1]`. The peak-plus-right side contributes `[2,1]` with total three. Minimum total five fits within six, so peak 2 is feasible.

For peak 3, the left side must be `[1,2]` and the peak-right side is `[3,2]`, totaling eight. That exceeds six, so 3 is infeasible. Binary search consequently returns 2.

**Why the returned value is correct**

The helper exactly sums the pointwise-smallest valid array for each proposed peak. Its comparison therefore classifies feasibility without false positives or false negatives. Feasibility is monotone, and the binary search preserves the invariant that the answer lies within its bounds while retaining feasible `left`. At termination, no greater feasible value exists, so the returned peak is maximal.

## Complexity detail

The search interval has size at most `maxSum` and is halved each iteration. Each feasibility test uses a constant number of arithmetic operations, so time complexity is $O(\log\texttt{maxSum})$, matching the manifest.

The helper, bounds, midpoint, and parameters use only scalar storage. Auxiliary space is $O(1)$.

In a fixed-width language, arithmetic-series products can approach values beyond 32-bit range and should use 64-bit integers. Python integers grow automatically.

## Alternatives and edge cases

- **Build the array for every candidate:** A feasibility test would cost $O(n)$ instead of constant time, making binary search $O(n\log\texttt{maxSum})$.
- **Increment the peak one by one:** It can require up to `maxSum` trials; binary search exploits monotonicity.
- **Closed-form inversion:** Piecewise quadratic formulas can derive the answer but create more boundary cases than binary search.
- **Peak at index zero:** The left count is zero, and the helper's arithmetic correctly contributes zero.
- **Peak at the last index:** The right call contains only the peak, while the left call covers all earlier positions.
- **Single-element array:** The feasibility sum is exactly the candidate, so the answer is `maxSum`.
- **Descent reaches one:** Remaining farther positions stay at one because values must remain positive.
- **Descent does not reach one:** The helper uses only the truncated arithmetic sequence.
- **Unused budget:** Feasibility requires sum at most `maxSum`, not exactly equal.
- **All-ones baseline:** The constraint $n\leq\texttt{maxSum}$ guarantees at least one feasible array.
- **Upper midpoint:** It is required when assigning `left = mid` on feasible candidates.
- **Adjacent difference:** The minimal profile decreases by one, never by more.
- **Helper name shadowing:** It intentionally hides the built-in only inside this method.
- **Input scalars:** No input collection exists to mutate.
