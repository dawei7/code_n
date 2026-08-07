### 1. Description

You are given a **0-indexed** integer array `nums` of length `n`. You are initially standing at index `0`. You can jump from index `i` to index `j` where `i < j` if:

- $\text{nums}[i] \le \text{nums}[j]$ and $\text{nums}[k] < \text{nums}[i]$ for all indexes `k` in the range `i < k < j`, or

- $\text{nums}[i] > \text{nums}[j]$ and $\text{nums}[k] \ge \text{nums}[i]$ for all indexes `k` in the range `i < k < j`.

You are also given an integer array `costs` of length `n` where $\text{costs}[i]$ denotes the cost of jumping **to** index `i`.

Return *the **minimum** cost to jump to the index *$n - 1$.

### 2. Function Contract

**Inputs**

- `nums`: List of $n$ integers ($1 \le n \le 10^5$), where $0 \le \text{nums}[i] \le 10^5$.
- `costs`: List of $n$ integers ($1 \le n \le 10^5$), where $0 \le \text{costs}[i] \le 10^5$.

**Return value**

Return an integer representing the minimum total landing cost to reach index $n-1$ starting from index $0$. Return 0 if $n = 1$.

### 3. Examples

#### Example 1

- **Input:** `nums = [3,2,4,4,1], costs = [3,7,6,4,2]`
- **Output:** `8`
- **Explanation:** You start at index 0.
- Jump to index 2 with a cost of costs[2] = 6.
- Jump to index 4 with a cost of costs[4] = 2.
The total cost is 8. It can be proven that 8 is the minimum cost needed.
Two other possible paths are from index 0 -> 1 -> 4 and index 0 -> 2 -> 3 -> 4.
These have a total cost of 9 and 12, respectively.
#### Example 2

- **Input:** `nums = [0,1,2], costs = [1,1,1]`
- **Output:** `2`
- **Explanation:** Start at index 0.
- Jump to index 1 with a cost of costs[1] = 1.
- Jump to index 2 with a cost of costs[2] = 1.
The total cost is 2. Note that you cannot jump directly from index 0 to index 2 because nums[0] <= nums[1].

### 4. Constraints

- $n = \text{nums.length} = \text{costs.length}$

- $1 \le n \le 10^{5}$

- $0 \le \text{nums}[i], \text{costs}[i] \le 10^{5}$