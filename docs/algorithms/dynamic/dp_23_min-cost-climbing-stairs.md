# Min Cost Climbing Stairs

| | |
|---|---|
| **ID** | `dp_23` |
| **Category** | dynamic |
| **Complexity (required)** | $O(N)$ Time, $O(1)$ Space |
| **Difficulty** | 2/10 |
| **Interview relevance** | 9/10 |
| **LeetCode Equivalent** | [Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/) |

## Problem statement

You are given an integer array `cost` where `cost[i]` is the cost of `i`-th step on a staircase. Once you pay the cost, you can either climb one or two steps.
You can either start from the step with index 0, or the step with index 1.
Return the minimum cost to reach the top of the floor (which is index `N`, strictly outside the array).

**Input:** An integer array `cost`.
**Output:** An integer representing the minimum cost.

## When to use it

- The weighted/cost-based variant of `dp_02 - Climbing Stairs`.
- An absolutely perfect introductory problem for teaching minimization transitions in 1D arrays.

## Approach

**1. Define the State:**
Let `dp[i]` be the minimum total cost to *reach* step `i`.
*(Note: To "reach the top of the floor", we need to reach step `N`, which is one index past the end of the `cost` array).*

**2. Find the Base Cases:**
The problem states we can start at step 0 or step 1 for free. We only pay the cost when we *leave* the step.
Therefore, the cost to *reach* step 0 is 0. The cost to *reach* step 1 is 0.
`dp[0] = 0`, `dp[1] = 0`.

**3. Find the Transition (The recurrence relation):**
How could we possibly arrive at step `i`?
- We could have come from step `i-1`. To do that, we had to reach step `i-1` (which cost `dp[i-1]`), and then we had to pay the toll to leave step `i-1` (which is `cost[i-1]`).
- We could have come from step `i-2`. To do that, we had to reach step `i-2` (which cost `dp[i-2]`), and then pay the toll `cost[i-2]`.

We want the absolute minimum!
`dp[i] = min( dp[i-1] + cost[i-1], dp[i-2] + cost[i-2] )`

**4. Optimize Space:**
Notice that `dp[i]` only relies on the previous two steps (`dp[i-1]` and `dp[i-2]`). Just like Fibonacci, we can discard the $O(N)$ array and just use two sliding variables!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for dp_23: Min Cost Climbing Stairs.

Minimum cost to reach the top of a staircase where you
may climb 1 or 2 steps at a time. cost[i] is the cost of
step i. dp[i] = cost[i] + min(dp[i-1], dp[i-2]). The
answer is min(dp[n-1], dp[n-2]).
"""


def solve(cost, n):
    if n == 0:
        return 0
    if n == 1:
        return cost[0]
    prev2 = cost[0]
    prev1 = cost[1]
    for i in range(2, n):
        cur = cost[i] + min(prev1, prev2)
        prev2, prev1 = prev1, cur
    return min(prev1, prev2)
```

</details>

## Walk-through

`cost = [10, 15, 20]`. N = 3.
Initialize `prev2 = 0`, `prev1 = 0`.

1. **i = 2 (reaching step 2):**
   - From step 1: `prev1 + cost[1]` = 0 + 15 = 15.
   - From step 0: `prev2 + cost[0]` = 0 + 10 = 10.
   - `current_cost = min(15, 10) = 10`.
   - Shift: `prev2 = 0`, `prev1 = 10`.
2. **i = 3 (reaching the top, N):**
   - From step 2: `prev1 + cost[2]` = 10 + 20 = 30.
   - From step 1: `prev2 + cost[1]` = 0 + 15 = 15.
   - `current_cost = min(30, 15) = 15`.
   - Shift: `prev2 = 10`, `prev1 = 15`.

Result `prev1` is 15. ✓ (The path is: Start at index 1, pay 15, jump 2 steps to the top).

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N)$ | $O(1)$ |
| **Average** | $O(N)$ | $O(1)$ |
| **Worst** | $O(N)$ | $O(1)$ |

The loop iterates strictly N-1 times. The math inside the loop is $O(1)$. Total time is $O(N)$.
Space complexity is strictly $O(1)$ because we only use two integer variables instead of an array.

## Variants & optimizations

- **Mutating the Input Array:** You can actually solve this by mutating the `cost` array in place! Loop from `i=2` to `N-1`: `cost[i] += min(cost[i-1], cost[i-2])`. Then return `min(cost[N-1], cost[N-2])`. This is also $O(1)$ space, but avoids extra variables. However, mutating input parameters is generally considered bad practice in production engineering.

## Real-world applications

- **Network Routing Protocols:** A vastly simplified 1D version of calculating the path of least resistance/latency for a packet traversing a linear sequence of routers where hopping skips a node.

## Related algorithms in cOde(n)

- **[dp_02 - Climbing Stairs](dp_02_climbing-stairs.md)** — The unweighted, combinatorial variant.
- **[dp_11 - House Robber](dp_11_house-robber.md)** — Another 1D DP that uses the identical `prev1`/`prev2` space optimization.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
