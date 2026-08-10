## General

**Why the last index and common difference define a reusable state**

An arithmetic subsequence is determined incrementally. If a subsequence ends at index `k` and has common difference `d`, then a later value at index `i` can extend it exactly when

$$
\texttt{nums}[i]-\texttt{nums}[k]=d.
$$

The full list of earlier chosen indices is not needed to decide whether the extension is legal. Only its final index, its common difference, and its best length matter. This is the dynamic-programming compression used by the solution.

Define `f[i][d]` conceptually as the maximum length of an arithmetic subsequence whose last chosen element is `nums[i]` and whose common difference is `d`. The code cannot use a negative number directly as a list index for the intended mapping, so it stores the difference in an offset column.

**Why there are exactly 1001 difference columns**

Every value lies between zero and 500. Therefore, the smallest possible difference is `0 - 500 = -500`, and the largest is `500 - 0 = 500`. There are 1001 integers in that inclusive range.

For a real difference `d`, the code uses column

`j = d + 500`.

Difference `-500` maps to column zero, difference zero maps to column 500, and difference 500 maps to column 1000. The source constraints guarantee that `j` is always a valid column, so no dictionary or bounds condition is necessary.

**Why every table entry begins at one**

The table is initialized as `[[1] * 1001 for _ in range(n)]`. A single array element can be viewed as a length-one subsequence waiting to receive a second element. A one-element sequence has no meaningful common difference yet, but treating it as a length-one seed in every difference column makes the transition uniform.

When indices `k < i` form the first pair for difference `d`, `f[k][j]` may still be one. Adding one produces length two, which is exactly the pair `[nums[k], nums[i]]`. If a longer subsequence with difference `d` already ends at `k`, the same addition appends `nums[i]` to it.

This initialization eliminates a special branch such as “use two if no earlier state exists.”

**The transition**

The outer loop chooses the last index `i`, beginning at one because index zero has no predecessor. The inner loop tries every earlier index `k`.

For the pair `k, i`, the difference is computed and shifted:

`j = nums[i] - nums[k] + 500`.

Any arithmetic subsequence represented by `f[k][j]` already ends at `nums[k]` with the same real difference. Appending `nums[i]` preserves that difference, so its new length is `f[k][j] + 1`.

The assignment

`f[i][j] = max(f[i][j], f[k][j] + 1)`

keeps only the longest sequence ending at `i` with this difference. Several earlier indices can produce the same `j`. A shorter state is never more useful for a future extension than a longer state with the same endpoint index and difference, so discarding it is safe.

After each transition, `ans = max(ans, f[i][j])` records the best length formed anywhere so far.

**Why indices, not only values, are part of the state**

A subsequence must preserve array order. Two equal values at different positions are different choices because one may have useful elements after it that the other does not. Storing a state for each ending index guarantees that every extension uses `k < i` and therefore respects order automatically.

Combining all states only by ending value could accidentally use an occurrence that appears after the current element or reuse the same position. The row index prevents both errors.

**Trace an increasing example**

For `nums = [3, 6, 9, 12]`, the pair from index zero to index one has difference three, stored in column 503. Since `f[0][503]` is one, `f[1][503]` becomes two.

At index two, pairing with index one also has difference three. The state `f[1][503] = 2` extends to `f[2][503] = 3`, representing `[3, 6, 9]`. Pairing index zero directly with index two has difference six and creates a separate length-two state in column 506.

At index three, predecessor index two with difference three extends the length-three state to four. The method returns four. The difference-six pairs never interfere because they occupy a different column.

**Trace a negative difference**

For `[20, 1, 15, 3, 10, 5, 8]`, the desired sequence `20, 15, 10, 5` has difference `-5`, mapped to column 495.

When fifteen is processed, the pair with twenty creates length two in that column. Ten extends it to three, and five extends it to four. Elements between those chosen indices are simply ignored, which is permitted for a subsequence.

Negative differences need no separate logic. The offset changes only storage position; the transition still compares the true difference implied by the pair.

**Why the result cannot remain below two**

The input contains at least two values. On the first inner-loop iteration, `i = 1` and `k = 0`. The initialized predecessor state is one, so some `f[1][j]` becomes two and `ans` becomes two. Every pair of numbers is an arithmetic sequence of length two because there is only one adjacent difference to satisfy.

This explains why `ans` can safely begin at zero despite the mathematical lower bound of two.

**Why the dynamic program is correct**

Consider an optimal arithmetic subsequence ending at index `i` with difference `d`. If its length is two, its preceding index `k` forms a pair, and the transition from the initialized value one creates length two.

If its length is greater than two, remove its final element. What remains is an arithmetic subsequence ending at some `k < i` with the same difference `d`. By the time row `i` is processed, the loops have already computed the longest such state in `f[k][d]`. The transition from `k` therefore creates a sequence at least as long as the chosen optimal sequence.

Every transition is also valid: it appends a later index whose value difference equals the state's common difference. Thus the table never claims an impossible length. Induction over increasing ending indices proves that each state stores exactly the best valid length, and taking the maximum in `ans` yields the global optimum.

## Complexity detail

Let `N = len(nums)`. The nested loops examine every ordered index pair `k < i` exactly once. There are `N(N - 1) / 2` such pairs, and each transition is constant time. Total running time is `O(N^2)`, matching the manifest.

Let `D = 1001` be the fixed difference-domain width. The dense table contains `N \cdot D` integers, so its exact storage is `O(ND)`. Under the stated value constraint, `D` is fixed and this can be described more tightly as `O(N)` with a large constant.

The package records the conventional general dynamic-programming bound `O(N^2)`. That is a safe upper bound and matches a dictionary formulation in which an index may hold up to `O(N)` distinct observed differences. The exact bounded-domain allocation is more precise: `N` rows by 1001 columns. The scalar variables and answer add only `O(1)` space.

## Alternatives and edge cases

- **Dictionary per ending index:** Store only observed differences as `dp[i][d]`. This avoids allocating 1001 columns when few differences occur and naturally supports unbounded input values, while retaining `O(N^2)` worst-case states.
- **Brute-force starting pairs:** Choose two indices and scan the remaining suffix for expected values. Repeating that scan for every pair can require `O(N^3)` time.
- **Enumerate all subsequences:** There are exponentially many subsequences, making direct generation infeasible even before testing their differences.
- **Value-frequency reasoning:** Counts alone lose positional order. The valid sequence depends on indices increasing, so dynamic-programming states must preserve an ending position.
- **Zero difference:** Repeated equal values produce `d = 0` and use column 500. Each later equal occurrence extends the chain normally.
- **Negative difference:** Adding 500 maps it into the table without changing its meaning. No reverse traversal is required.
- **Maximum positive difference:** Pair zero followed by 500 maps to column 1000, the last valid entry.
- **Maximum negative difference:** Pair 500 followed by zero maps to column zero, the first valid entry.
- **Two elements:** The only pair creates length two, which is always a valid arithmetic subsequence.
- **All values equal:** Every pair uses difference zero, and the state extends until the answer equals `N`.
- **Already arithmetic array:** Each consecutive element extends the same difference state, so the whole array is recovered.
- **Noncontiguous optimum:** The loops consider every earlier predecessor, not only `i - 1`, so arbitrary deletions are naturally supported.
- **Multiple predecessors with one difference:** The `max` assignment is essential. It retains the longest chain and prevents a later, shorter predecessor from overwriting a better state.
- **Constraint-dependent table width:** If values were allowed outside zero through 500, the fixed offset could index outside the table. A dictionary would then be the appropriate generalization.
