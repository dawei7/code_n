# Magnetic Force Between Two Balls

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1552 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/magnetic-force-between-two-balls/) |

## Problem Description
### Goal
Baskets are placed at distinct integer coordinates listed in `position`. You must put exactly one ball into each of `m` chosen baskets. For any two balls, their magnetic force is defined as the absolute difference between their basket coordinates.

Choose the baskets so that the minimum force among every pair of placed balls is as large as possible. Return that greatest achievable minimum distance. The positions may arrive in any order and can be spread over a large coordinate range.

### Function Contract
**Inputs**

- `position`: $n$ distinct basket coordinates, where $2 \le n \le 10^5$ and $1 \le \texttt{position[i]} \le 10^9$.
- `m`: the number of balls, where $2 \le m \le n$.
- Let $R = \max(\texttt{position}) - \min(\texttt{position})$.

**Return value**

The maximum possible value of the minimum pairwise distance between the $m$ selected basket coordinates.

### Examples
**Example 1**

- Input: `position = [1, 2, 3, 4, 7], m = 3`
- Output: `3`
- Explanation: Choosing positions one, four, and seven makes the minimum pairwise distance three.

**Example 2**

- Input: `position = [5, 4, 3, 2, 1, 1000000000], m = 2`
- Output: `999999999`
- Explanation: With two balls, choosing the two extreme positions maximizes their distance.

**Example 3**

- Input: `position = [1, 2, 8, 12, 17], m = 3`
- Output: `7`
- Explanation: Positions one, eight, and seventeen have adjacent gaps seven and nine.

### Required Complexity

- **Time:** $O(n \log n+n \log R)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Convert a candidate distance into a feasibility question**

Sort the basket coordinates. For a proposed minimum distance `distance`, place the first ball at the leftmost basket, then scan from left to right and place each next ball at the earliest coordinate at least `distance` beyond the previous placement.

This greedy placement leaves every subsequent ball as much remaining space as possible. If any placement with the candidate distance can fit $m$ balls, replacing its first position by the leftmost basket and each later position by the greedy earliest feasible basket never moves a ball rightward. The greedy scan therefore also fits $m$ balls. Conversely, every greedy placement directly satisfies the distance requirement.

**Exploit monotonic feasibility**

If a distance is feasible, every smaller nonnegative distance is feasible. If it is infeasible, every larger distance is infeasible. Binary-search this monotone boundary between one and the span divided by $m-1$, which is an upper bound because $m-1$ gaps must fit inside the full span.

When the midpoint is feasible, search above it; otherwise search below it. At termination, the last feasible value is the largest achievable minimum force.

#### Complexity detail

Sorting a copied list of $n$ coordinates costs $O(n \log n)$ time and $O(n)$ space for the copy. Each feasibility scan costs $O(n)$ and binary search performs $O(\log R)$ scans, giving $O(n \log n+n \log R)$ total time. Beyond the sorted copy, the scan and search use $O(1)$ state.

#### Alternatives and edge cases

- **Try every integer distance:** reuse the greedy feasibility test but check distances one by one, which can take $O(nR)$ time.
- **Enumerate basket subsets:** examining all choices of $m$ baskets is combinatorial.
- **Dynamic programming over coordinates:** possible state formulations are much heavier than the monotone feasibility search.
- With $m=2$, the answer is the distance between the extreme baskets.
- With $m=n$, every basket is used and the answer is the smallest adjacent sorted gap.
- Input order has no effect after sorting.
- Large unused gaps can dominate the answer even when many baskets are clustered elsewhere.
- The upper-bound division by $m-1$ is safe because the selected positions create exactly $m-1$ adjacent gaps.

</details>
