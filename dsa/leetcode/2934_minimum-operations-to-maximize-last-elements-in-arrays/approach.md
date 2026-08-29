## General

At each index we may either keep the pair `(nums1[i], nums2[i])` or swap it. The final elements must be maxima of their respective arrays.

The pair at the last index has only two possible orientations:

1. Leave it unchanged, making bounds `x = nums1[-1]` and `y = nums2[-1]`.
2. Swap it, making bounds `x = nums2[-1]` and `y = nums1[-1]`, at a cost of one operation.

Once these final bounds are fixed, decisions at all earlier indices are independent. Every resulting first-array value must be at most $x$, and every second-array value at most $y$.

**Helper for fixed final bounds**

`f(x, y)` scans each earlier pair $(a,b)$.

If `a <= x and b <= y`, its current orientation already fits. The source continues without increasing the count. Even if swapping would also fit, leaving it is always at least as good because we minimize operations.

If the current orientation does not fit, the only remaining choice is to swap. After swapping, $b$ goes to the first array and $a$ to the second, so feasibility requires

$$
b\le x\quad\text{and}\quad a\le y.
$$

The code writes the same test as `a <= y and b <= x`. If it fails, neither orientation works for this pair, so the entire fixed-bound scenario is impossible and `f` returns `-1`. If it succeeds, the swap is forced and `cnt` increases.

Because an operation affects only one index, taking every locally forced swap and no optional swaps gives the minimum count for the fixed final orientation.

**Evaluate both last-index orientations**

The source computes

- `a = f(nums1[-1], nums2[-1])` for no final swap;
- `b = f(nums2[-1], nums1[-1])` for a final swap.

Scenario `a` has no extra cost. Scenario `b` costs `b + 1` because index $n-1$ itself is swapped. The answer is `min(a, b + 1)` when feasible.

The expression first checks `a + b == -2`. Helper results are either `-1` or nonnegative, so this equality means both scenarios are impossible. In fact feasibility is symmetric here: an earlier unordered pair can fit within endpoint values in some orientation for one final ordering if and only if it can fit for the other, though the number of required swaps can differ. Thus legal executions do not have only one helper equal to `-1`, and the final minimum is safe.

**Why checking bounds makes the last elements maxima**

If every earlier element of the first array is at most $x$ and its last element equals $x$, that last element is a maximum, with ties allowed. The same holds for $y$ in the second array. No comparison among earlier positions is otherwise needed.

Conversely, any successful operation sequence chooses one of the two orientations for the final pair. Under that orientation, each earlier pair must use an orientation satisfying exactly the helper's inequalities. Therefore the corresponding helper considers every successful sequence and chooses its fewest swaps.

For each fixed orientation, local decisions cannot conflict: swapping index $i$ changes no value at another index and does not alter the fixed last bounds. This proves the greedy count inside `f` is globally optimal for that scenario, and comparing the two scenarios is exhaustive.

## Complexity detail

Each helper call scans $n-1$ pairs, and it is called twice. Time complexity is $O(n)$.

The manifest claims $O(1)$ auxiliary space, which would be true for an index-based loop. The exact Python source uses `nums1[:-1]` and `nums2[:-1]` inside each helper call. These slices allocate two new lists containing $n-1$ elements, so actual peak auxiliary space is $O(n)$. The second call occurs after the first returns, so the two calls' slices do not accumulate beyond the same asymptotic peak.

## Alternatives and edge cases

- **Try all swap subsets:** There are $2^n$ possibilities. Fixing the final orientation makes each earlier choice independent.
- **Check only the original last pair:** The optimal solution may require swapping the final index, so both orientations are mandatory.
- **Swap an already fitting pair:** It cannot lower the operation count and may violate bounds; the helper correctly leaves it unchanged.
- **Neither orientation fits an earlier pair:** The fixed scenario is impossible immediately.
- **Ties with the final value:** Allowed because the condition says the last element equals a maximum, not that it is uniquely greatest.
- **Length one:** Both last elements are automatically maxima. Helpers scan empty slices; the no-swap scenario costs zero.
- **Both orientations feasible locally:** Keeping the pair costs zero and is optimal for that fixed endpoint orientation.
- **Only both global scenarios impossible:** The helper feasibility sets are symmetric under exchanging endpoint bounds, so `a+b==-2` detects impossibility.
- **Slicing overhead:** Replacing slices with `for i in range(n-1)` would restore $O(1)$ auxiliary space without changing logic.
- **Large values:** Only comparisons and counts are used, so Python integer size creates no overflow concern.
