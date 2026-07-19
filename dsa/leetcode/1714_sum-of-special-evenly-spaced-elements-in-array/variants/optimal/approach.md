## General
**Separate small and large steps**

Choose $S=\lfloor\sqrt n\rfloor+1$ and group queries by their step `y`. When `y >= S`, one query visits at most $\lceil n/y\rceil=O(S)$ array positions, so summing its progression directly is already cheap.

When `y < S`, many queries could each visit nearly the whole array. For one such step, build a reverse dynamic-programming array:

`suffix[i] = nums[i] + suffix[i + y]`

whenever `i + y` is valid. Then every query with this step is answered in $O(1)$ by `suffix[x]`. Process all queries sharing that step, discard the temporary array, and continue with the next step.

**Why grouping preserves every progression**

For a fixed step, `suffix[i]` contains `nums[i]` and exactly the special sum starting one step later. Induction from the end of the array therefore shows that it contains every and only index in the progression `i, i + y, i + 2 * y, ...`.

Large-step queries enumerate that same progression explicitly. Grouping changes only the evaluation strategy; saved query indices restore the original output order. Applying the modulus during each DP addition and after direct accumulation preserves the required modular sum.

## Complexity detail
There are fewer than $S$ possible small steps, and each distinct small step costs $O(n)$ to preprocess, for $O(nS)$ total. Each large-step query visits $O(S)$ positions, for $O(qS)$ total. Grouping and answer placement add $O(q)$, giving $O((n+q)S)$ time.

The query groups and answers use $O(q)$ space. Only one length-$n$ small-step DP array exists at a time, so total space is $O(n+q)$ rather than $O(nS)$.

## Alternatives and edge cases
- **Traverse every query directly:** this is simple but repeated step-one queries take $O(nq)$ time.
- **Precompute every step in a permanent table:** it answers small-step queries quickly but consumes $O(nS)$ memory unnecessarily.
- **Prefix sums:** ordinary contiguous prefix sums cannot subtract an arithmetic progression with step greater than one.
- **Group without saved indices:** queries must still be returned in their original order, not grouped-step order.
- **Start at the last index:** every positive step selects exactly one value.
- **Step at least the remaining length:** only `nums[x]` contributes.
- **Repeated queries:** each receives the same numeric result at its own output position.
- **Zero values:** they contribute nothing but do not terminate the progression.
- **Large totals:** reduce modulo $10^9+7$ so intermediate DP values remain bounded.
