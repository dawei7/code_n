### 1. Description

Given an array `nums` of integers, return *the length of the longest arithmetic subsequence in* `nums`.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Note

that:

- A **subsequence** is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

- A sequence `seq` is arithmetic if $seq[i + 1] - \text{seq}[i]$ are all the same value (for $0 \le i < \text{seq.length} - 1$).

### 4. Examples

#### Example 1

- **Input:** `nums = [3,6,9,12]`
- **Output:** `4`
- **Explanation:** The whole array is an arithmetic sequence with steps of length = 3.
#### Example 2

- **Input:** `nums = [9,4,7,2,10]`
- **Output:** `3`
- **Explanation:** The longest arithmetic subsequence is [4,7,10].
#### Example 3

- **Input:** `nums = [20,1,15,3,10,5,8]`
- **Output:** `4`
- **Explanation:** The longest arithmetic subsequence is [20,15,10,5].

### 5. Constraints

- $2 \le \text{nums.length} \le 1000$

- $0 \le \text{nums}[i] \le 500$