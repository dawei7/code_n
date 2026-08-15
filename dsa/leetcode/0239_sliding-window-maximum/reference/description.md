### 1. Description

You are given an array of integers `nums`, there is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the `k` numbers in the window. Each time the sliding window moves right by one position.

Return *the max sliding window*.

### 2. Function Contract

**Inputs**

- `nums`: The nonempty integer array traversed by the window.
- `k`: The number of consecutive values visible in each window.

**Return value**

Return the maximum of each of the $\text{nums.length} - k + 1$ windows from left to right.

### 3. Examples

#### Example 1

- **Input:** `nums = [1,3,-1,-3,5,3,6,7], k = 3`
- **Output:** `[3,3,5,5,6,7]`
- **Explanation:** Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       **3**
1 [3  -1  -3] 5  3  6  7       **3**
1  3 [-1  -3  5] 3  6  7      ** 5**
1  3  -1 [-3  5  3] 6  7       **5**
1  3  -1  -3 [5  3  6] 7       **6**
1  3  -1  -3  5 [3  6  7]      **7**

#### Example 2

- **Input:** `nums = [1], k = 1`
- **Output:** `[1]`

### 4. Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $-10^{4} \le \text{nums}[i] \le 10^{4}$

- $1 \le k \le \text{nums.length}$
