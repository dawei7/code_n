## General

**Define a subsequence by its last index and change budget**

A good subsequence counts transitions where adjacent selected values differ. Let

`f[i][h]`

be the maximum length of a subsequence ending at original index $i$ with at most $h$ unequal adjacent transitions.

Every state starts at 1 because `nums[i]` alone is a valid subsequence with zero changes.

To extend from earlier index $j<i$:

- if `nums[j] == nums[i]`, appending creates no new unequal transition, so candidate is `f[j][h] + 1`;
- if values differ and $h>0$, appending consumes one allowed change, so candidate is `f[j][h-1] + 1`.

The nested loops inspect every possible predecessor, so the maximum transition yields the best subsequence ending at $i$.

**Why “at most h” works**

States do not require exactly $h$ changes. A one-element subsequence initializes every budget layer to one, and equal-value extensions stay within the same layer. A solution using fewer changes remains available in larger budget states through their own transitions.

The requested answer is therefore the maximum `f[i][k]` over endpoints.

**Subsequence order**

Only $j<i$ is considered, so selected indices remain increasing. Values between $j$ and $i$ may be skipped, which is exactly subsequence behavior rather than subarray behavior.

For `nums = [1,2,1,1,3]` and $k=2$, a path selecting values `[1,2,1,1]` has changes 1→2 and 2→1, then an equal transition. The recurrence charges budgets exactly that way.

When $k=0$, only equal-value transitions are available. The DP reduces to finding the maximum frequency of one value while respecting order, which is simply its count.

**A small table trace**

For prefix values `[1,2,1]` with budget one, the state ending at the third value considers both earlier indices. Extending the first 1 uses `f[0][1] + 1` because values match. Extending value 2 uses `f[1][0] + 1` because the final transition differs and consumes the one change. Taking the larger candidate captures whichever history uses the budget best.

Several earlier positions can have the same value but different best lengths. The quadratic loop compares all of them and retains the best implicitly. An optimized algorithm may aggregate by value, but this exact table stores each endpoint separately.

Although the source does not explicitly copy `f[i][h-1]` into `f[i][h]`, any lower-budget subsequence is also valid under the looser budget and its transition chain is recreated in the higher layer.


Consider an optimal subsequence represented by `f[i][h]`. If it has one element, initialization covers it. Otherwise, let $j$ be its penultimate selected index. If values match, removing $i$ leaves a valid state `f[j][h]`; if they differ, it leaves `f[j][h-1]`. The recurrence considers that $j$ and can reconstruct the optimal length.

Conversely, every transition appends a later index and charges exactly zero or one change according to value equality. Every constructed candidate is valid. Taking maxima makes each state exact by induction on $i$.

**Exact implementation details**

The source writes `for j, y in enumerate(nums[:i])`. The slice contains exactly indices below $i$, so `j` remains the original index. However, a new prefix list is allocated for every $(i,h)$ iteration. An index loop over `range(i)` would avoid this repeated copying.

The manifest describes an optimized per-value state updated in $O(nk)$. The exact source is the straightforward predecessor DP and must be explained with its quadratic scan.

## Complexity detail

There are $n(k+1)$ states. Each state scans up to $i=O(n)$ predecessors, so time is $O(n^2k)$.

The repeated `nums[:i]` slices also copy $O(i)$ references and do not change the asymptotic time. Peak temporary slice space is $O(n)$.

The table `f` stores $n(k+1)$ integers, using $O(nk)$ space. It dominates the temporary slice, so auxiliary space is $O(nk)$.

This contradicts the manifest's $O(nk)$ time claim, which belongs to the optimized value-aggregate method used conceptually by ID 3177.

Input is not mutated.

## Alternatives and edge cases

- **Per-value best maps:** Store the best length ending in each value for every budget, avoiding all predecessor scans.
- **Top-two global endings:** Needed to efficiently choose a different ending value; ID 3177 implements this.
- **Index loop instead of slicing:** Preserves $O(n^2k)$ time but avoids repeated temporary lists.
- **k equals zero:** Only equal values may be adjacent in the selected sequence.
- **k at least length minus one:** Every subsequence, including the whole array, is allowed.
- **All values equal:** Full array is valid for every budget.
- **All values distinct:** A length $\ell$ subsequence needs $\ell-1$ changes.
- **One element:** Every state remains one and answer is one.
- **Repeated nonadjacent values:** They can be selected together without a change when adjacent in the subsequence.
- **At most versus exactly:** Unused budget is allowed.
- **Endpoint maximum:** Optimal subsequence may end anywhere, so `ans` checks every $i$.
- **Manifest mismatch:** The source is quadratic in $n$ despite the optimized summary.
