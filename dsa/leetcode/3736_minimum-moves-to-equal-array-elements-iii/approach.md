## General

**The common final value cannot be below the current maximum**

Only increments are allowed. If

$$
M=\max(\texttt{nums}),
$$

then an element already equal to `M` can never be decreased. Therefore any common final value `T` must satisfy `T >= M`.

Choosing `T=M` is feasible: increase every smaller value until it reaches the maximum and leave maximum elements unchanged. Choosing any larger target adds `T-M` extra increments to every one of the `n` elements, so it can never improve the total. The unique best target value is therefore the existing maximum.

This is the central reason the problem is simpler than variants that permit both increments and decrements. With two-way movement, a median can be optimal. With increases only, the largest current value is an unavoidable lower bound and is itself reachable.

**Sum each element's deficit**

An element `nums[i]` needs exactly

$$
M-\texttt{nums}[i]
$$

moves to reach `M`. It cannot use fewer because each move changes it by only one, and that many increments directly achieve the target.

Summing gives

$$
\sum_{i=0}^{n-1}(M-\texttt{nums}[i]).
$$

Distribute the sum:

$$
\sum_{i=0}^{n-1}M-\sum_{i=0}^{n-1}\texttt{nums}[i]
=nM-S,
$$

where `S = sum(nums)`.

The exact source computes `n`, `mx`, and `s`, then returns `mx * n - s`. This compact formula is exactly the sum of individual deficits; it is not an approximation.

Notice that maximum-valued elements are included correctly even though they are not handled by a branch. Each contributes `M` to `nM` and the same `M` to `S`, so its net deficit is zero. Every smaller element contributes precisely the missing difference.

For `[2,1,3]`, `M=3` and `S=6`. The result is `3*3-6=3`, corresponding to one move for two, two moves for one, and zero for three.

For `[4,4,5]`, the result is `5*3-13=2`. Both fours receive one increment.

**Why operations on different elements do not interact**

Each move changes only one selected element. Increasing one value neither helps nor obstructs another value's progress. Once the final target is fixed at `M`, the minimum cost is therefore the sum of independent per-index minimum costs.

The order of moves is irrelevant. One may finish an element completely before touching the next or interleave increments arbitrarily; the total number remains the same.

**A lower bound that the construction attains**

Every valid solution must end at some `T >= M`. Its cost is

$$
\sum_i(T-\texttt{nums}[i])=nT-S.
$$

Because `n` is positive, this expression strictly increases as `T` increases. Its minimum allowed argument is `T=M`, giving `nM-S`.

The direct strategy of raising every element to `M` uses exactly that many moves, so the lower bound is attainable. This proves both minimality and feasibility.

**Why no simulation is needed**

Individual increments could number in the thousands even under the small constraints, and in a generalized version far more. The deficit formula counts them algebraically. The source needs only two aggregate facts about the array: its maximum and its sum.

Although Python's `max` and `sum` make separate passes, both are linear and simple. A single manual pass could compute them together but would not change asymptotic complexity or the mathematical method.

## Complexity detail

Let `n` be the array length. `max(nums)` scans all elements in $O(n)$ time, and `sum(nums)` performs another $O(n)$ scan. Constantly many linear passes remain $O(n)$ total time.

The method stores only `n`, `mx`, `s`, and the returned arithmetic value, so auxiliary space is $O(1)$. It does not copy or modify the input.

The largest stated answer is small, but in a broader implementation `nM-S` should use a sufficiently wide integer type. Python integers expand automatically.

## Alternatives and edge cases

- **Simulate one increment at a time:** This produces the correct result but its running time depends on the numerical answer rather than just `n`. Algebraic deficits avoid all simulation.
- **Sort the array:** The maximum would then be at the end, but sorting costs $O(n\log n)$ and is unnecessary because order has no role.
- **Raise values to the average:** The average may be below the maximum and therefore unreachable without decreasing a maximum element.
- **Use the median:** A median minimizes absolute deviations when both increases and decreases are allowed. It is not valid under increase-only operations.
- **Choose a value above the maximum:** Every extra unit raises all `n` elements and adds `n` moves, so it is strictly worse.
- **All elements already equal:** `S=nM`, and the formula returns zero.
- **Single element:** It is already equal to every element in the array, so the result is zero.
- **Several maximum elements:** Their deficits are zero; only smaller elements contribute.
- **One very small element:** Its complete difference to `M` appears directly in `nM-S`.
- **Input order:** Reordering does not affect maximum, sum, or required moves.
- **Positive-value guarantee:** The proof actually works for arbitrary integers as long as increments are the only operation, but no extra handling is needed.
- **No input mutation:** Unlike a sorting approach, the aggregation leaves `nums` unchanged.
