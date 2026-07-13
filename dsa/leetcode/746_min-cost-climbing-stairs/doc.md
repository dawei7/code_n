# Min Cost Climbing Stairs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 746 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/min-cost-climbing-stairs/) |

## Problem Description

### Goal

Given an integer array `cost`, `cost[i]` is the price paid when you step on stair `i`. After paying that cost, you may climb either one step or two steps.

You may begin on stair `0` or stair `1`. Return the minimum total cost needed to reach the top of the floor, which lies just beyond the final indexed stair. You do not pay a separate cost for the top itself, and you may choose different one- and two-step moves along the route.

### Function Contract

**Inputs**

- `cost`: a list of non-negative integers, where `cost[i]` is charged when stair `i` is used.

**Return value**

- The minimum cost of reaching the virtual top immediately after the array.

### Examples

**Example 1**

- Input: `cost = [10, 15, 20]`
- Output: `15`
- Explanation: Start on stair `1`, pay `15`, and jump two positions to the top.

**Example 2**

- Input: `cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]`
- Output: `6`
- Explanation: Choosing the inexpensive stairs avoids every cost of `100`.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Make the paid stair the dynamic-programming state**

Let `landing[i]` be the minimum total cost after landing on stair `i` and paying `cost[i]`. The previous paid stair can only be $i - 1$ or $i - 2$, so

`landing[i] = cost[i] + min(landing[i - 1], landing[i - 2])`.

Starting directly on stair `0` or stair `1` costs nothing before that stair is paid. Two initial zero states therefore model both allowed starting choices without a special recurrence. After all costs have been processed, the top is reachable from either of the final two stairs, so the answer is the smaller of their totals.

**Keep only the states that can still be used**

Each transition reads only the two preceding totals. Store them as `two_before` and `one_before`, compute the current total, and shift the pair forward. Older values can never influence a later choice and need not be retained.

Every route to a stair must arrive from one of its two legal predecessors. The recurrence takes the cheapest already-optimal route among exactly those possibilities and then adds the unavoidable current cost. Processing stairs from left to right consequently makes each stored total optimal, and the final minimum covers the only two legal jumps to the top.

#### Complexity detail

The algorithm performs one constant-time transition for each of the `n` costs, giving $O(n)$ time. It keeps two accumulated totals and one temporary value, giving $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Full dynamic-programming array:** Store every `landing[i]`; this uses the same recurrence and $O(n)$ time but consumes $O(n)$ auxiliary space unnecessarily.
- **Top-down recursion with memoization:** Cache the cheapest cost from each position; it is also $O(n)$ time and $O(n)$ space, with recursion overhead.
- **Unmemoized recursion:** Explore both jumps from every state; repeated subproblems make its running time exponential.
- **Exactly two stairs:** Either stair can be the starting point, so the smaller of the two costs is the answer.
- **Zero-cost stairs:** Zero values require no special handling and may form an entirely free route.
- **The top has no cost:** Return the cheaper way to move beyond the array; do not add another stair charge.

</details>
