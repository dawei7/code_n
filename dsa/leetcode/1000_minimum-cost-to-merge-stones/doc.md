# Minimum Cost to Merge Stones

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1000 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/minimum-cost-to-merge-stones/) |

## Problem Description

### Goal

There are `n` piles of stones arranged in a row, and `stones[i]` gives the number of stones in the $i$th pile. One move must select exactly `k` consecutive piles and replace them with a single pile.

The cost of a move is the total number of stones in the selected piles. Return the minimum total cost required to reduce the entire row to one pile. If the fixed merge size makes that final state impossible, return `-1`.

### Function Contract

**Inputs**

- `stones`: a list of $N$ pile sizes, where $1\le N\le30$ and $1\le\texttt{stones[i]}\le100$.
- `k`: the exact number $K$ of consecutive piles merged per move, where $2\le K\le30$.

**Return value**

- The minimum total merge cost needed to leave one pile, or `-1` when no legal sequence can do so.

### Examples

**Example 1**

- Input: `stones = [3, 2, 4, 1], k = 2`
- Output: `20`
- Explanation: Merge the first pair for $5$, the last pair for $5$, then the two remaining piles for $10$.

**Example 2**

- Input: `stones = [3, 2, 4, 1], k = 3`
- Output: `-1`
- Explanation: One merge leaves two piles, which cannot be merged by an exactly-three operation.

**Example 3**

- Input: `stones = [3, 5, 1, 2, 6], k = 3`
- Output: `25`
- Explanation: Merge `[5, 1, 2]` for $8$, then merge the remaining three piles for $17$.

### Required Complexity

- **Time:** $O(N^3/(K-1))$
- **Space:** $O(N^2)$

<details>
<summary>Approach</summary>

#### General

**Reject impossible pile counts first:** Every move reduces the number of piles by exactly $K-1$. Starting with $N$ piles can reach one only when $N-1$ is divisible by $K-1$. This condition is also sufficient because interval merges can then be scheduled until one pile remains.

**Store the best cost for each interval:** Let `dp[left][right]` be the minimum cost to reduce that interval as far as its length permits. Split an interval after `middle`, combining the best left and right costs. Only split positions separated by $K-1$ need consideration, because the left part must be reducible to one pile before it can participate in the eventual merge.

When an interval length satisfies `(length - 1) % (k - 1) == 0`, its partial piles can be merged into one, so add the interval's total stone count. Prefix sums provide that total in constant time. Considering every legal final split covers every valid merge tree, and choosing the minimum yields the optimal cost.

#### Complexity detail

There are $O(N^2)$ intervals. Each examines at most $O(N/(K-1))$ legal split points, so time is $O(N^3/(K-1))$. The interval table and prefix sums use $O(N^2)$ space.

#### Alternatives and edge cases

- **Enumerate merge sequences:** Recursively trying every legal consecutive group is correct but can visit exponentially many pile configurations.
- **Three-dimensional pile-count DP:** Explicitly storing the cost to reduce each interval to every pile count is general but uses $O(N^2K)$ space.
- **One initial pile:** The answer is zero because no merge is required.
- **Merge size larger than the row:** More than one pile cannot be reduced when `k > n`.
- **Exact full-row merge:** When `k == n`, one move costs the sum of all piles.

</details>
