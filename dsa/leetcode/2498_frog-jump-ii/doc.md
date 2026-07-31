# Frog Jump II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2498 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/frog-jump-ii/) |

## Problem Description

### Goal

The strictly increasing array `stones` gives stone positions along a river. A frog starts on the first stone, must reach the last stone, and must then return to the first. During this round trip, it may jump to any intermediate stone at most once.

The length of a jump between two stones is the absolute difference of their positions. The cost of the entire route is its longest single jump. Intermediate stones are available to divide the outward and return journeys into shorter jumps, but the two directions cannot reuse the same intermediate landing.

Return the smallest possible route cost. Although the contract does not require every intermediate stone to be visited, an optimal arrangement can distribute them between the two directions without increasing the maximum jump.

### Function Contract

**Inputs**

- `stones`: A strictly increasing list of stone positions with $2 \leq \lvert\texttt{stones}\rvert \leq 10^5$, `stones[0] = 0`, and every position between $0$ and $10^9$.

**Return value**

Return the minimum achievable value of the maximum jump length over a trip from the first stone to the last and back, with each intermediate stone used at most once.

### Examples

**Example 1**

- Input: `stones = [0, 2, 5, 6, 7]`
- Output: `5`
- Explanation: Alternating intermediate stones between the two directions achieves a longest jump of `5`, and no arrangement can make every required crossing shorter.

**Example 2**

- Input: `stones = [0, 3, 9]`
- Output: `9`
- Explanation: One direction may use the middle stone, but the other must jump directly between `0` and `9`.

**Example 3**

- Input: `stones = [0, 1]`
- Output: `1`
- Explanation: With only the endpoints, both directions use the same distance of `1`.
