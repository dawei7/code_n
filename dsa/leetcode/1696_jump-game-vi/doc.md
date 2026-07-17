# Jump Game VI

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1696 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Queue, Heap (Priority Queue), Monotonic Queue |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/jump-game-vi/) |

## Problem Description
### Goal

You begin at index `0` of the 0-indexed integer array `nums` and must reach index `n - 1`. From index `i`, one move may land at any index from `i + 1` through `min(n - 1, i + k)`, inclusive. Jumps only move forward and may use fewer than $k$ steps.

Your score is the sum of `nums[j]` over every visited index, including the starting and final positions. Values may be negative, so some losses can be unavoidable. Choose the sequence of legal jumps that reaches the last index with the maximum possible score, and return that score.

### Function Contract
**Inputs**

- `nums`: a list of $n$ integers, where $1 \le n \le 10^5$ and each value lies between $-10^4$ and $10^4$
- `k`: the inclusive maximum forward jump length, where $1 \le k \le 10^5$

**Return value**

The greatest score among all legal paths from index `0` to index `n - 1`.

### Examples
**Example 1**

- Input: `nums = [1, -1, -2, 4, -7, 3], k = 2`
- Output: `7`

Visiting values `[1, -1, 4, 3]` achieves the optimum.

**Example 2**

- Input: `nums = [10, -5, -2, 4, 0, 3], k = 3`
- Output: `17`

The path through values `[10, 4, 3]` skips the early negative positions.

**Example 3**

- Input: `nums = [1, -5, -20, 4, -1, 3, -6, -3], k = 2`
- Output: `0`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Express each landing through its best predecessor**

Let `best_score[i]` be the maximum score of a path that lands at index `i`. The start has `best_score[0] = nums[0]`. Any later index can be reached from the preceding window of at most $k$ positions, so

$$
\texttt{best\_score[i]} = \texttt{nums[i]} +
\max_{\max(0,i-k) \le j < i} \texttt{best\_score[j]}.
$$

The recurrence considers every legal final jump. Extending the optimal path to its chosen predecessor gives the candidate score, and no path reaching `i` can do better than the maximum predecessor state.

**Maintain the moving maximum in a decreasing deque**

Store candidate indices in decreasing order of their `best_score` values. Before evaluating index `i`, remove indices from the front while they are smaller than `i - k`, because they can no longer reach `i`. The front is then the highest-scoring legal predecessor and directly supplies the recurrence maximum.

After computing `best_score[i]`, remove indices from the back whose scores are no greater. The new index is both at least as valuable and remains eligible for every future window at least as long as those older indices, so a removed candidate can never become preferable later. Append `i` to restore decreasing score order.

Expiration preserves exactly the legal range, and domination removal preserves its maximum. By induction, every DP value is optimal; in particular, the final entry is the best score at the required destination.

#### Complexity detail

Each of the $n$ indices enters the deque once and can leave it once from either end, giving $O(n)$ total time. The DP array uses $O(n)$ space, and the deque contains at most $k+1$ indices, which is also $O(n)$ under the constraints.

#### Alternatives and edge cases

- **Scan all predecessors:** evaluating the recurrence by checking up to $k$ earlier scores per index is correct but takes $O(nk)$ time.
- **Max-heap:** a heap with lazy expiration yields $O(n \log n)$ time and $O(n)$ space but does not exploit monotonic window order as efficiently.
- **Segment tree:** range-maximum queries give $O(n \log n)$ time with more machinery than the deque requires.
- **Single element:** the start is already the destination, so return `nums[0]` even when it is negative.
- **Jump length one:** every index must be visited and the result is the sum of the entire array.
- **Large `k`:** the predecessor window may include all earlier indices, but visiting profitable intermediate positions can still beat a direct jump.
- **Equal predecessor scores:** keeping only the newer equal-scoring index is safe because it expires later.

</details>
