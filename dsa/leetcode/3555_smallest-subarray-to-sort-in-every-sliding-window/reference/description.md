### 1. Description

You are given an integer array `nums` and an integer `k`.

For each contiguous subarray of length `k`, determine the **minimum** length of a continuous segment that must be sorted so that the entire window becomes **non‑decreasing**; if the window is already sorted, its required length is zero.

Return an array of length $n − k + 1$ where each element corresponds to the answer for its window.

### 2. Function Contract

- Refer to method signature.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** nums = [1,3,2,4,5], k = 3

**Output:** [2,2,0]

**Explanation:**

- $nums[0...2] = [1, 3, 2]$. Sort `[3, 2]` to get `[1, 2, 3]`, the answer is 2.

- $nums[1...3] = [3, 2, 4]$. Sort `[3, 2]` to get `[2, 3, 4]`, the answer is 2.

- $nums[2...4] = [2, 4, 5]$ is already sorted, so the answer is 0.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [5,4,3,2,1], k = 4

**Output:** [4,4]

**Explanation:**

- $nums[0...3] = [5, 4, 3, 2]$. The whole subarray must be sorted, so the answer is 4.

- $nums[1...4] = [4, 3, 2, 1]$. The whole subarray must be sorted, so the answer is 4.

</div>

### 4. Constraints

- $1 \le \text{nums.length} \le 1000$

- $1 \le k \le \text{nums.length}$

- $1 \le \text{nums}[i] \le 10^{6}$