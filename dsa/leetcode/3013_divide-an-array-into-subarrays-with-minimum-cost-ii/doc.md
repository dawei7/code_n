# Divide an Array Into Subarrays With Minimum Cost II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3013 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Sliding Window, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-ii/) |

## Problem Description

### Goal

You are given a 0-indexed integer array `nums` of length $N$ and positive integers `k` and `dist`. The cost of a nonempty array is its first value.

Divide `nums` into exactly `k` disjoint contiguous subarrays that together preserve the entire array. If their starting indices are

$$
0 = i_0 < i_1 < cdots < i_{k-1} < N,
$$

then the start of the last subarray must be no more than `dist` positions after the start of the second subarray:

$$
i_{k-1} - i_1 \le \texttt{dist}.
$$

Return the minimum possible sum of the `k` subarray costs, namely

$$
\texttt{nums}[0] + \sum_{j=1}^{k-1} \texttt{nums}[i_j].
$$

### Function Contract

**Inputs**

- `nums`: A list of $N$ positive integers whose order must be preserved.
- `k`: The exact number of nonempty contiguous subarrays in the partition.
- `dist`: The maximum allowed difference between $i_{k-1}$ and $i_1$.

The source constraints guarantee $3 \le N \le 10^5$, $1 \le \texttt{nums}[i] \le 10^9$, $3 \le \texttt{k} \le N$, and $k-2 \le \texttt{dist} \le N-2$.

**Return value**

- The minimum possible sum of the first elements of all `k` subarrays.

### Examples

#### Example 1

- **Input:** `nums = [1, 3, 2, 6, 4, 2]`, `k = 3`, `dist = 3`
- **Output:** `5`
- **Explanation:** Starts at indices $0$, $2$, and $5$ form `[1, 3]`, `[2, 6, 4]`, and `[2]`. Their cost is $1+2+2=5$, and $5-2=3$ satisfies the distance limit.

#### Example 2

- **Input:** `nums = [10, 1, 2, 2, 2, 1]`, `k = 4`, `dist = 3`
- **Output:** `15`
- **Explanation:** Starts at indices $0$, $1$, $2$, and $3$ cost $10+1+2+2=15$. Choosing the final value at index $5$ together with index $1$ would span $4$ positions and is therefore invalid.

#### Example 3

- **Input:** `nums = [10, 8, 18, 9]`, `k = 3`, `dist = 1`
- **Output:** `36`
- **Explanation:** The only two additional starts that fit the optimal legal span are indices $1$ and $2$, giving $10+8+18=36$.
