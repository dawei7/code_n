### 1. Description

Given an array of integers arr, find the sum of `min(b)`, where `b` ranges over every (contiguous) subarray of `arr`. Since the answer may be large, return the answer **modulo** $10^{9} + 7$.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** `arr = [3,1,2,4]`
- **Output:** `17`
- **Explanation:**
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.
#### Example 2

- **Input:** `arr = [11,81,94,43,3]`
- **Output:** `444`

### 4. Constraints

- $1 \le \text{arr.length} \le 3 * 10^{4}$

- $1 \le \text{arr}[i] \le 3 * 10^{4}$