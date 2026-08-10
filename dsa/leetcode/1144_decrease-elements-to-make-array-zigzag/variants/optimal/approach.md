## General

**There are only two possible zigzag orientations**

A zigzag array must alternate strict comparisons. Once the role of index zero is chosen, every other role is forced:

- even indices are valleys and odd indices are peaks, giving `A[0] < A[1] > A[2] < ...`;
- odd indices are valleys and even indices are peaks, giving `A[0] > A[1] < A[2] > ...`.

The solution computes the cost of both orientations in `ans[0]` and `ans[1]`, then returns the smaller cost. In the outer iteration `i = 0`, it visits even indices and makes them valleys. In `i = 1`, it visits odd indices and makes them valleys.

This valley-centered view is especially appropriate because the only allowed operation decreases values. A peak cannot be repaired by increasing it, but a violated comparison can always be repaired by decreasing the neighboring valley. Once every chosen valley is strictly below its existing neighbors, those neighbors automatically serve as peaks relative to it.

**Compute the exact reduction needed for one valley**

Suppose `j` is intended to be a valley. If a left neighbor exists, strict inequality requires

`new_value < nums[j - 1]`.

Because values are integers, the largest legal final value is `nums[j - 1] - 1`. If the current value is already smaller, no move is needed. Otherwise, the number of unit decrements needed is

`nums[j] - nums[j - 1] + 1`.

The same reasoning for the right neighbor gives `nums[j] - nums[j + 1] + 1`. The code starts `d` at zero so a negative requirement does not create a negative cost.

If both neighbors exist, the valley must be below both. Its largest legal value is one less than the smaller neighbor. Equivalently, it must be reduced by the larger of the two individual requirements. That is why the code repeatedly applies `max` to `d`. Adding the two reductions would be wrong: one reduction changes the single valley value and can satisfy both comparisons simultaneously.

For example, if a candidate valley has value seven with neighbors five and three, the left condition needs three decrements, while the right condition needs five. Reducing the value by five changes it to two, which is below both neighbors. Eight moves are not necessary.

**Why valley costs can be added independently**

All selected valleys have the same index parity, so no two selected valleys are adjacent. Decreasing one valley cannot change another selected valley's own value. They may share a peak between them, but neither operation decreases that shared peak. Lowering either adjacent valley only makes the peak comparisons easier to satisfy.

Therefore, the minimum reduction calculated for each chosen valley remains valid when all other chosen valleys are reduced. There is no conflict and no need for a dynamic program. The total minimum cost for one orientation is simply the sum of its independent valley costs.

It is also important that the calculation always compares against the original `nums` values. The algorithm does not modify the array while evaluating an orientation. This is safe because only valley positions would be changed, while the neighbors of a valley are peak positions and remain untouched in that orientation. Original neighbor values are exactly their final values.

**Why checking both orientations is sufficient and optimal**

Every valid zigzag array has exactly one of the two alternating orientations. For a fixed orientation, every valley has an independent upper bound imposed by its existing neighbor or neighbors. The computed `d` is the smallest decrement that meets all of those bounds, so summing it gives the least cost for that orientation.

Any transformation producing that orientation must spend at least that many moves on each valley: stopping at a larger value would leave at least one strict inequality false. The constructed reductions achieve all inequalities at exactly the summed cost. Thus `ans[i]` is optimal for its orientation.

Taking `min(ans)` then chooses the cheaper of the only two possible zigzag forms, proving global optimality.

For `[1, 2, 3]`, making even indices valleys requires no reduction at index zero and two decrements at index two, changing three to one. Making the odd index a valley requires reducing two below both one and three, which takes two decrements and changes it to zero. Both orientations cost two, so the answer is two.

## Complexity detail

Let `n` be the array length. Each orientation visits approximately half the indices, and the two passes together perform constant work for `n` positions. The time complexity is `O(n)`.

The solution stores two totals, the length, loop indices, and one local reduction value. It does not allocate storage proportional to the input and does not modify or copy `nums`. The auxiliary space complexity is `O(1)`.

The numeric move total can be larger than an individual array value, but it remains a single integer and does not affect the asymptotic space bound.

## Alternatives and edge cases

- **Modify a copy for each orientation:** This can work, but copying and mutating arrays uses `O(n)` extra space. Independent cost calculation obtains the same result without constructing the final arrays.
- **Greedily repair comparisons from left to right:** A local change can commit to one orientation implicitly or alter a value needed by the next comparison. Evaluating the two valley parities directly avoids that ambiguity.
- **Add left and right reductions:** Both constraints apply to the same valley value. The larger required reduction satisfies both, so summing them overcounts moves.
- **Try to increase peaks:** Increasing is not an allowed move. Decreasing the alternating valley positions is sufficient to establish every strict comparison.
- **Length one:** There are no adjacent comparisons, so the array is already zigzag. Each orientation has zero cost and the method returns zero.
- **Length two:** Either endpoint can be chosen as the valley. The algorithm evaluates both directions and performs the smaller necessary decrease.
- **Equal neighbors or equal adjacent values:** Zigzag inequalities are strict. The `+ 1` ensures the lowered valley becomes strictly smaller rather than merely equal.
- **A valley already below both neighbors:** Both computed requirements are nonpositive, `d` remains zero, and no unnecessary move is counted.
- **Boundary valleys:** Index zero has only a right constraint and index `n - 1` has only a left constraint. The boundary checks apply exactly the existing comparison.
- **Shared peak:** Two same-parity valleys may border the same peak. Lowering either one only strengthens its comparison with that peak, so their costs remain independent.
