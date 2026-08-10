## General

**Group equal values before making decisions**

Choosing one occurrence of value `x` earns `x` points and deletes every occurrence of `x - 1` and `x + 1`. It does not delete other occurrences of `x`. Since all values are positive, once the decision is made to use value `x`, taking every occurrence of `x` is always beneficial: each adds points and creates no new forbidden value beyond the same two neighbors.

The exact solution therefore aggregates the total reward for each numeric value:

`total[x] = x * frequency(x)`.

It builds this array by adding `num` to `total[num]` for every input occurrence.

After aggregation, the problem becomes: choose numeric values so that no two chosen values are consecutive, maximizing the sum of their total rewards. This is the same decision structure as House Robber on a line of value positions.

**Why values, not input positions, form the line**

The deletion rule depends only on numeric adjacency. Input order has no meaning. Every 3 conflicts with every 2 and every 4, regardless of where those values occur in `nums`.

The `total` array places each possible value at its numeric index. Missing values simply have reward zero. Now conflicts occur only between neighboring array positions.

**Define the dynamic-programming state**

Let `dp[i]` be the maximum points obtainable using values from zero through `i`.

At value `i` there are two exhaustive choices:

- Skip value `i`. The best score remains `dp[i - 1]`.
- Take all copies of value `i`. Value `i - 1` must be excluded, so combine `total[i]` with `dp[i - 2]`.

The recurrence is

`dp[i] = max(dp[i - 1], dp[i - 2] + total[i])`.

This recurrence never needs the specific deletion sequence. Once a set of nonadjacent values is chosen, their occurrences can be taken in any compatible order.

**Compress the DP to two values**

The exact solution does not allocate a `dp` array because the next state needs only the previous two.

Before processing value `i >= 2`:

- `first` represents `dp[i - 2]`.
- `second` represents `dp[i - 1]`.

It computes

`cur = max(first + total[i], second)`,

then shifts `first = second` and `second = cur`. After the shift, the invariant is ready for the next numeric value.

**Base cases**

The array includes index zero even though inputs are positive. `total[0]` is zero, so

`first = total[0]`

represents `dp[0] = 0`.

For values zero and one, the best score is the larger of their totals:

`second = max(total[0], total[1])`.

Since the input is nonempty and every value is at least one, the maximum `mx` is at least one and index one always exists in `total`.

**Trace `[2, 2, 3, 3, 3, 4]`**

Aggregation gives:

- `total[2] = 4`
- `total[3] = 9`
- `total[4] = 4`

At value 2, taking it gives four and skipping gives zero, so the best becomes four.

At value 3, taking it combines nine with the best through value 1, producing nine. Skipping keeps four, so nine wins.

At value 4, taking it combines four with the best through value 2, producing eight. Skipping preserves nine, so the final answer is nine. This corresponds to taking all three copies of value 3.

**Trace nonadjacent values**

For `[2, 2, 5]`, missing totals at 3 and 4 are zero. The recurrence carries the score from value 2 across those gaps, then adds the reward at 5 because it does not conflict with 2. Both values are selected.

Iterating through zero-reward gaps costs time proportional to the maximum value, which is acceptable under the stated `10^4` bound.

**Why aggregation loses no optimal solution**

If an optimal sequence ever takes one copy of value `x`, adding every remaining copy of `x` increases its score and does not require deleting any additional numeric categories. Therefore an optimum either takes all copies of a value or none.

The only conflicts among these all-or-none value choices are between consecutive integers. The House Robber recurrence examines both possibilities at every value and combines a taken value with the optimal compatible prefix. By induction on `i`, `second` after processing `i` equals the maximum reward through that value. At `mx`, it covers every value in the input and is the required maximum.

## Complexity detail

Let `n` be the input length and `m = max(nums)`.

The first pass finds `m` in `O(n)` time. Allocating `total` costs `O(m)`, the second input pass aggregates rewards in `O(n)`, and the DP loop scans values through `m` in `O(m)`. Total time is `O(n + m)`.

The `total` array has `m + 1` integers, giving `O(m)` auxiliary space. The dynamic-programming state itself uses only `O(1)` space because it keeps two previous values.

The exact code initializes `mx` with negative infinity, but the nonempty-input guarantee ensures the first positive number replaces it before array allocation.

## Alternatives and edge cases

- **Hash totals plus sorted unique values:** Aggregate in a dictionary, sort only values that occur, and apply the recurrence carefully across consecutive versus gapped keys. This costs `O(u log u)` for `u` unique values and can be better when the maximum value is huge and sparse.

- **Full DP array:** Store `dp[i]` for every value. It makes state inspection easy but uses another `O(m)` array when only two prior states are needed.

- **Top-down memoization:** Recursively choose take or skip for each value. It uses `O(m)` cache and call-stack space and risks recursion-depth issues; the bottom-up loop is simpler.

- **Operate on input positions:** Input order is irrelevant, and duplicate values should be combined. A position-based robber recurrence would model the wrong adjacency.

- **Take only one duplicate:** Once a value is chosen, every same-valued occurrence should be taken because all give positive points and share the same neighbor restriction.

- **Only one distinct value:** Its entire aggregated total is selected.

- **Consecutive high rewards:** The recurrence compares taking the current total plus the compatible prefix against keeping the previous optimum.

- **Gaps between values:** Zero totals carry the previous best forward, allowing all profitable nonadjacent categories to combine.

- **Minimum value one:** The explicit base state at index one handles it safely.

- **Nonempty positive input:** These constraints justify indexing `total[1]` and avoid a separate empty-array return path.
