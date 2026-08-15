### 1. Description

You are given a **0-indexed** integer array `nums` of size `n` and a positive integer `k`.

We call an index `i` in the range $k \le i < n - k$ **good** if the following conditions are satisfied:

- The `k` elements that are just **before** the index `i` are in **non-increasing** order.

- The `k` elements that are just **after** the index `i` are in **non-decreasing** order.

Return *an array of all good indices sorted in **increasing** order*.

### 2. Function Contract

**Inputs**

- `nums`: Input parameter (`List[int]`).
- `k`: Input parameter (`int`).

**Return value**

- Returns `List[int]`.

### 3. Examples

#### Example 1

- **Input:** `nums = [2,1,1,1,3,4,1], k = 2`
- **Output:** `[2,3]`
- **Explanation:** There are two good indices in the array:
- Index 2. The subarray [2,1] is in non-increasing order, and the subarray [1,3] is in non-decreasing order.
- Index 3. The subarray [1,1] is in non-increasing order, and the subarray [3,4] is in non-decreasing order.
Note that the index 4 is not good because [4,1] is not non-decreasing.

#### Example 2

- **Input:** `nums = [2,1,1,2], k = 2`
- **Output:** `[]`
- **Explanation:** There are no good indices in this array.

### 4. Constraints

- $n = \text{nums.length}$

- $3 \le n \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{6}$

- $1 \le k \le n / 2$
