### 1. Description

You are given a **0-indexed** integer array `nums`. For each index `i` ($1 \le i \le \text{nums.length} - 2$) the **beauty** of $\text{nums}[i]$ equals:

- `2`, if $\text{nums}[j] < \text{nums}[i] < \text{nums}[k]$, for **all** $0 \le j < i$ and for **all** $i < k \le \text{nums.length} - 1$.

- `1`, if $nums[i - 1] < \text{nums}[i] < nums[i + 1]$, and the previous condition is not satisfied.

- `0`, if none of the previous conditions holds.

Return* the **sum of beauty** of all *$\text{nums}[i]$* where *$1 \le i \le \text{nums.length} - 2$.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** `nums = [1,2,3]`
- **Output:** `2`
- **Explanation:** For each index i in the range 1 <= i <= 1:
- The beauty of nums[1] equals 2.
#### Example 2

- **Input:** `nums = [2,4,6,4]`
- **Output:** `1`
- **Explanation:** For each index i in the range 1 <= i <= 2:
- The beauty of nums[1] equals 1.
- The beauty of nums[2] equals 0.
#### Example 3

- **Input:** `nums = [3,2,1]`
- **Output:** `0`
- **Explanation:** For each index i in the range 1 <= i <= 1:
- The beauty of nums[1] equals 0.

### 4. Constraints

- $3 \le \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{5}$