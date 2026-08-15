### 1. Description

You are given a **0-indexed** array of integers `nums` of length `n`. You are initially positioned at index 0.

Each element $\text{nums}[i]$ represents the maximum length of a forward jump from index `i`. In other words, if you are at index `i`, you can jump to any index $(i + j)$ where:

- $0 \le j \le \text{nums}[i]$ and

- $i + j < n$

Return *the minimum number of jumps to reach index *$n - 1$. The test cases are generated such that you can reach index $n - 1$.

### 2. Function Contract

**Inputs**

- `nums`: The maximum forward-jump length available at each index.

**Return value**

Return the fewest jumps needed to travel from index `0` to the final index.

### 3. Examples

#### Example 1

- **Input:** `nums = [2,3,1,1,4]`
- **Output:** `2`
- **Explanation:** The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

#### Example 2

- **Input:** `nums = [2,3,0,1,4]`
- **Output:** `2`

### 4. Constraints

- $1 \le \text{nums.length} \le 10^{4}$

- $0 \le \text{nums}[i] \le 1000$

- It's guaranteed that you can reach $nums[n - 1]$.
