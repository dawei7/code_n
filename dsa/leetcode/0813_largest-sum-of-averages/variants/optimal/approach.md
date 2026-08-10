## General

**Why dynamic programming is needed**

The array must be divided into adjacent, nonempty groups that together use every element. A score is the sum of the groups' averages. A locally attractive cut is not necessarily part of the best complete partition: making one group look better changes which elements remain for every later group. We therefore need to compare all possible first cuts while reusing answers for the repeated suffix problems they create.

The exact solution defines `dfs(i, k)` for a suffix beginning at index `i` with `k` groups available. From that state, it chooses where the first group ends, adds that group's average, and asks the same function to partition the remaining suffix with one fewer group.

**Why “at most” becomes exactly `k` here**

The problem permits at most `k` groups, but every `nums[i]` is positive. Splitting one nonempty group into two nonempty adjacent groups cannot reduce the score.

Suppose the two new groups have positive averages `a` and `b`. The average of their combined group is a weighted average of `a` and `b`, so it is no greater than `max(a,b)`. Because both values are positive,

$$
a+b>\max(a,b).
$$

Thus, the sum of the two separate averages is strictly greater than the old combined average. As long as a group contains at least two elements, adding a cut improves the score. Since `k <= n`, any partition using fewer than `k` groups can be refined until it uses exactly `k` nonempty groups, improving the result at each step.

This positivity argument is why the implementation can search for exactly `k` groups even though the wording says “at most.” It would not be valid if negative values were allowed.

**Prefix sums make each group average constant-time**

The list

`s = list(accumulate(nums, initial=0))`

builds prefix sums with `s[0] = 0` and

$$
s[j]=\sum_{p=0}^{j-1}\texttt{nums}[p].
$$

Therefore, the sum of the half-open subarray `nums[i:j]` is `s[j] - s[i]`, and its average is

$$
\frac{s[j]-s[i]}{j-i}.
$$

Without prefix sums, calculating each candidate average by scanning `nums[i:j]` would add another linear factor. With prefix sums, every candidate average takes constant time.

**The recursive state and its base cases**

The call `dfs(i, k)` returns the best score obtainable from `nums[i:]` when the recurrence is to form `k` groups.

If `i == n`, no numbers remain, so the function returns 0. This also protects the recursion from trying to divide an empty suffix.

If `k == 1`, every remaining number must belong to the final group. There is no cut left to choose, so the only possible score is the suffix average:

$$
\frac{s[n]-s[i]}{n-i}.
$$

This base case is essential. It guarantees that a completed feasible branch consumes the entire remaining suffix rather than leaving elements unused.

**Trying every first boundary**

When more than one group remains, the first group must contain at least `nums[i]` and must end before index `n` so that something remains for later groups. The loop

`for j in range(i + 1, n)`

tries every such end boundary. For each `j`, the candidate score is

$$
\frac{s[j]-s[i]}{j-i}+\operatorname{dfs}(j,k-1).
$$

The first term scores `nums[i:j]`. The recursive term supplies the best score for the suffix beginning at `j`. Taking the maximum over all boundaries selects the best first cut together with the best completion after that cut.

The implementation initializes `ans` to zero. Some calls can have more requested groups than remaining elements; such an infeasible call has no loop candidate and returns zero. Those branches cannot become the global optimum under the positive-input contract. If an overlong first group leaves too few elements, splitting that positive prefix into the extra needed groups and retaining the remaining positive elements produces a feasible partition with a strictly larger sum of averages. Hence, a feasible exactly-`k` branch dominates every incomplete branch from the initial valid state.

A more defensive formulation could restrict `j` so at least `k - 1` elements remain. The exact code relies on positivity instead, and its returned maximum is still correct.

**Why caching changes the cost completely**

Different earlier cut choices can request the same suffix index and remaining group count. For example, many paths may eventually ask for `dfs(4, 2)`. The `@cache` decorator computes each pair `(i, k)` once and reuses its result thereafter.

Without caching, the recursion enumerates partitions through an exponentially branching tree. With caching, it evaluates a polynomial number of distinct states, while still trying all possible next boundaries within each state.

**Example structure**

For `nums = [9,1,2,3,9]` and `k = 3`, the initial state `dfs(0, 3)` tries first groups such as `[9]`, `[9,1]`, and `[9,1,2]`. If it chooses `[9]`, the next state determines the best two-group partition of `[1,2,3,9]`. That state can choose `[1,2,3]` followed by `[9]`, giving

$$
9+\frac{1+2+3}{3}+9=20.
$$

Every other legal pair of cut positions is represented by exactly one chain of boundary choices. Because the recurrence takes the maximum, the returned `dfs(0, k)` is the best complete partition.

**Why the recurrence is correct**

Any feasible partition of `nums[i:]` into `k` groups has one uniquely determined first boundary `j`. Its score equals the average of `nums[i:j]` plus the score of its remaining `k-1` groups. By definition, `dfs(j, k-1)` is at least as good as that particular remaining partition, so the recurrence considers a candidate at least as large as every feasible solution.

Conversely, every feasible candidate chosen by the recurrence combines one nonempty first group with a recursively valid partition of the remaining suffix, so it describes an allowed partition. The base case consumes the full suffix as the last group. Therefore, the maximum is neither below nor above the true optimum; it is exactly the optimum.

## Complexity detail

Let `n` be the array length. There are at most `O(kn)` distinct state pairs `(i, k)` reachable by the memoized recursion. A state may try `O(n)` boundary positions `j`, and each candidate uses constant-time prefix-sum arithmetic. The time complexity is therefore

$$
O(k\cdot n^2).
$$

The prefix-sum list uses `O(n)` space. The cache for this exact top-down implementation can hold `O(kn)` floating-point results, and the recursion stack reaches depth at most `O(k)`. Consequently, the exact implementation's auxiliary space is `O(kn)`, dominated by the cache.

The manifest lists `O(n)` space, which is attainable by the editorial's in-place bottom-up layering because it retains only one one-dimensional DP array. The protected optimal source shown here is top-down and cached, so `O(kn)` is the precise storage bound for the code being explained. The algorithmic recurrence and `O(k n^2)` time are the same in both organizations.

## Alternatives and edge cases

- **Bottom-up one-dimensional DP:** Initialize each suffix with its one-group average, then add partition layers while updating a length-`n` array. This realizes `O(n)` auxiliary space but requires careful update ordering so values from the previous layer are not overwritten before use.

- **Uncached recursion:** It expresses the same first-cut recurrence but recalculates suffix states for many different cut sequences, causing exponential work.

- **Recompute each subarray sum:** Summing `nums[i:j]` inside the boundary loop adds an avoidable factor. Prefix sums make every average query constant-time.

- **Greedy isolation of large values:** Making a large number a singleton can be attractive, but it may force poor groupings elsewhere. Only the DP accounts for the complete downstream effect of every cut.

- **`k = 1`:** The whole array is the only group, so the answer is its average. The base case returns it directly.

- **`k = n`:** Every element can be its own group, and the score is the sum of all values. The recurrence has a feasible chain of one-element groups.

- **All values are positive:** This guarantee is what makes exactly `k` groups optimal. With zero or negative values, adding a cut would require a new proof and could fail to improve the score.

- **Non-integer result:** Python's `/` performs floating-point division, preserving fractional averages as required.

- **Adjacent and exhaustive groups:** Every boundary `j` advances from `i`, and the last-group base case uses the entire suffix, so groups never overlap, never reorder elements, and never omit elements on a feasible branch.

- **Infeasible internal state:** A state with too many groups for its remaining elements returns zero because its loop is empty. Positivity ensures such an incomplete candidate cannot beat a feasible exactly-`k` partition from the valid initial call.

- **Numerical tolerance:** The algorithm performs ordinary floating-point additions and divisions. The bounded input size and accepted `10^{-6}` error make this appropriate.
