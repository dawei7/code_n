## General

**Replace smash order with two signed groups**

Smashing weights `x <= y` replaces them with `y - x`, an absolute difference. Repeating differences ultimately gives the absolute value of a signed sum of the original stones: each original weight contributes with either a positive or negative sign.

Group positive-sign stones into set `A` and negative-sign stones into set `B`. If their sums are `a` and `b`, the final weight is

$$
\lvert a-b\rvert.
$$

Conversely, the arbitrary choice of smash pairs lets the difference process realize this two-group cancellation interpretation. The optimization is therefore to divide all weights into two groups whose sums are as close as possible.

This is a partition problem rather than a greedy “smash the largest” simulation. Unlike the preceding Last Stone Weight problem, here the pair choices are under our control and must be optimized globally.

**Use the total sum**

Let `s = sum(stones)`. If one group's sum is `a`, the other is `s - a`, and their difference is

$$
\lvert(s-a)-a\rvert=\lvert s-2a\rvert.
$$

The two groups are interchangeable. It is sufficient to search for a subset sum `a` no larger than `\lfloor s/2\rfloor`. Within that range, `s - 2a` decreases as `a` grows.

Therefore, the goal becomes:

Find the largest subset sum that does not exceed half of the total.

The code sets capacity `n = s >> 1`. Right shift divides the nonnegative total by two and takes the floor.

**Define the knapsack table**

`m` is the number of stones. `dp[i][j]` stores the largest total weight no greater than capacity `j` that can be formed using only the first `i` stones.

The table has `m + 1` rows and `n + 1` columns. Row zero contains all zeroes because no positive sum can be formed without stones. Capacity zero also stays zero.

This is a zero-or-one knapsack: each stone may enter the chosen subset once or not at all.

**Exclude or include the current stone**

For row `i`, the current weight is `stones[i - 1]`.

First, `dp[i][j] = dp[i - 1][j]` copies the best result that excludes the current stone.

If the weight fits within capacity `j`, inclusion is possible. The remaining capacity is `j - stones[i - 1]`. The best earlier subset for that capacity is `dp[i - 1][j - stones[i - 1]]`, so the inclusion candidate is:

`dp[i - 1][j - stones[i - 1]] + stones[i - 1]`.

The maximum of exclusion and inclusion becomes `dp[i][j]`.

Using the previous row for the inclusion state is essential. It prevents the current stone from being selected repeatedly.

**Why maximize only the half-capacity cell**

The final cell `dp[-1][-1]` is the largest subset sum `a` at most `\lfloor s/2\rfloor` using every available stone.

The return expression `s - 2 * dp[-1][-1]` is nonnegative because `a` does not exceed half. It equals the absolute difference between the selected subset and its complement.

There is no need to reconstruct which stones were chosen because the problem asks only for the minimum remaining weight.

**Trace the first example**

For `[2,7,4,1,8,1]`, total sum is 23 and half capacity is 11.

The table can form subset sum 11, for example with stones seven and four. The complementary group sums to 12.

The minimum difference is `23 - 2 * 11 = 1`, which is the returned last stone weight.

No subset can give zero because an odd total cannot be split into two equal integer sums.

**Even and odd totals**

If `s` is even and subset sum `s/2` is achievable, the two groups cancel completely and the answer is zero.

If `s` is odd, exact equality is impossible. The best answer is at least one, and finding the closest lower-half sum gives that minimum or a larger unavoidable difference.

**Why a greedy choice is unsafe**

Always smashing the two heaviest stones fixes one particular sequence, not necessarily the best sequence. Likewise, placing each next stone into the currently lighter group can make locally balanced choices that block a better final partition.

The DP remembers the best attainable sum for every capacity and prefix, retaining combinations that greedy balancing might discard.


For state `dp[i][j]`, an optimal subset either excludes stone `i - 1` or includes it. The exclude branch is exactly `dp[i - 1][j]`. In the include branch, removing the current stone leaves an optimal subset of earlier stones within reduced capacity, represented by `dp[i - 1][j - weight]`.

The recurrence takes the better exhaustive case. Induction over rows proves every table entry is exact.

The signed-group transformation then proves that the largest attainable half-sum minimizes `s - 2a`, so the returned value is the smallest possible final stone.

**Why every stone is assigned**

The selected subset is one sign group. Every stone not selected automatically belongs to the complement. No stone is discarded from the mathematical partition; physical destruction during smashes represents cancellation between the two groups.

## Complexity detail

Let `M` be the number of stones and `S` their total weight. The capacity is `\lfloor S/2\rfloor`, which is `O(S)`.

The nested loops fill `O(MS)` states, each in constant time. Exact time complexity is `O(MS)`, matching the manifest.

The protected source allocates a full `(M + 1) \times (\lfloor S/2\rfloor + 1)` table, so its actual auxiliary space is `O(MS)`.

The manifest lists the optimized `O(S)` space target. That is achieved by using one capacity array and iterating capacities downward for each stone. The exact two-dimensional source favors transparent recurrence reconstruction over that compression.

## Alternatives and edge cases

- **One-dimensional knapsack:** Keep `dp[j]` and update `j` from half-sum down to the stone's weight. Descending order prevents reuse and reaches the manifest's `O(S)` space.
- **Reachable-sums set:** Start with `{0}` and add `x + weight` for existing sums up to half. It is concise but can allocate many set objects and has similar pseudo-polynomial behavior.
- **Bitset subset sum:** Shift a bitset by each weight and OR it into the state. This is compact and fast in languages with efficient wide integers or bitsets.
- **Enumerate all two-group assignments:** There are `2^M` sign choices, infeasible compared with the pseudo-polynomial DP.
- **Greedy heaviest smash:** It solves the fixed-rule Last Stone Weight problem but not this minimum-over-all-pairings problem.
- **Single stone:** Capacity is below its weight, best subset sum is zero, and the stone's full weight is returned.
- **Two equal stones:** Half-sum equals one stone, producing answer zero.
- **Two unequal stones:** The smaller fits nearest to half, and the result is their difference.
- **Odd total:** Zero is impossible; the formula naturally returns an odd positive difference.
- **Even total without a half subset:** The answer remains positive because no exact partition exists.
- **Repeated weights:** Rows represent distinct stones, so equal numeric values can each be selected once.
- **Capacity loop includes zero:** It preserves the empty subset base state and simplifies indexing.
- **Previous-row inclusion:** Referencing `i - 1` is what enforces zero-or-one selection in the full table.
- **Pseudo-polynomial bound:** `O(MS)` depends on total numeric weight, not only input count. It is practical because there are at most 30 stones of weight at most 100.
- **Space-bound discrepancy:** The exact code is two-dimensional; claiming `O(S)` requires the one-row rewrite.
