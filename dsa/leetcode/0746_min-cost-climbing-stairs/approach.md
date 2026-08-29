## General

**Define the cost from the step where payment occurs**

You may begin on step zero or step one. Whenever you stand on an indexed step and use it to climb, you pay that step’s cost, then move one or two positions forward. The top is the position just beyond the final array index and has no cost.

The exact solution defines `dfs(i)` as the minimum additional cost needed when the next step to pay is index `i`.

If `i >= len(cost)`, the climber has reached or passed the top. No more indexed step is used, so `dfs(i) = 0`.

Otherwise, paying `cost[i]` is unavoidable from this state. After payment, choose the cheaper continuation between one step and two:

`dfs(i) = cost[i] + min(dfs(i + 1), dfs(i + 2))`.

**Why starting choice is outside the recurrence**

The rules allow the first paid step to be either index zero or index one. These are two possible initial states, so the final result is

`min(dfs(0), dfs(1))`.

Starting at index one does not mean paying index zero, and the separate calls model that directly.

**Why moving past the final index is safe**

From the final indexed step, a two-step move may land one position beyond the conceptual top. The base condition uses `i >= len(cost)` rather than equality so both reaching exactly the top and stepping beyond it terminate with zero additional cost.

This matches the abstract staircase: after the last paid step, either allowed climb that clears the indexed steps reaches the floor above.

**Memoization prevents exponential repetition**

Without caching, `dfs(i)` calls two later states, which call overlapping later states again. The resulting recursion tree contains exponentially many repeated subproblems.

The `@cache` decorator stores the result for each index. The first call to `dfs(i)` computes it; all later calls return the stored value. There are only linearly many relevant indices, so the recursion becomes dynamic programming.

**Trace `[10, 15, 20]`**

From index 2, pay 20 and then reach the top, so `dfs(2) = 20`.

From index 1, pay 15 and choose between `dfs(2) = 20` and `dfs(3) = 0`. A two-step climb reaches the top, giving `dfs(1) = 15`.

From index 0, pay 10 and choose between costs from indices 1 and 2, giving `10 + min(15, 20) = 25`.

The final minimum between starts is 15.

**Why local cheapest next step is not enough**

Choosing the immediately cheaper of `cost[i + 1]` and `cost[i + 2]` can be misleading because those positions lead to different future possibilities. The recurrence compares `dfs(i + 1)` and `dfs(i + 2)`, which include the complete optimal remaining cost, not only one visible step.

**Why the two recursive choices are sufficient**

From any in-range index `i`, every legal route must pay `cost[i]` and then make exactly one of two moves. After moving to `i + 1` or `i + 2`, the best remaining route is independent of how `i` was reached and is exactly the corresponding DFS value.

Taking the smaller continuation therefore gives the optimum for state `i`. The base state correctly charges nothing after the top. Induction backward over indices proves every cached state correct, and taking the minimum of the two legal starting states yields the global minimum.

## Complexity detail

Let `n` be the number of cost entries. Memoization computes each in-range state at most once. Each performs constant work and refers to two later states, so time complexity is `O(n)`.

The cache stores `O(n)` state results, and recursive calls can reach `O(n)` depth through successive one-step moves. The exact implementation therefore uses `O(n)` auxiliary space.

This differs from the `O(1)` space achievable with bottom-up rolling variables. The stored source is top-down and cached, so it should not be described as constant-space.

## Alternatives and edge cases

- **Bottom-up with two variables:** Let the state be minimum cost to reach each position and retain only the previous two values. This gives `O(n)` time and `O(1)` auxiliary space.

- **Full bottom-up DP array:** It avoids recursion and stores the cost to reach every step, using `O(n)` space.

- **Uncached recursion:** It follows the same recurrence but repeats states exponentially and is unsuitable for large `n`.

- **Greedy next-step choice:** The cheapest immediate step may lead to a more expensive suffix. Compare complete optimal suffix costs instead.

- **Exactly two steps:** The answer is the smaller of the two costs because the climber may start on either and then leave the staircase.

- **Zero-cost steps:** They work naturally; the recurrence may choose them without any special condition.

- **Jump beyond the last index:** The `i >= n` base case returns zero for either top-reaching landing.

- **Input remains unchanged:** The method reads costs and stores results separately.

- **Recursion depth:** With at most 1000 steps, the recursive structure is linear; an iterative version avoids interpreter recursion-limit concerns entirely.
