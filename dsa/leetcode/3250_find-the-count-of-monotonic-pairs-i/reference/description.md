### 1. Description

You are given an array of **positive** integers `nums` of length `n`.

We call a pair of **non-negative** integer arrays `(arr1, arr2)` **monotonic** if:

- The lengths of both arrays are `n`.

- `arr1` is monotonically **non-decreasing**, in other words, $\text{arr1}[0] \le \text{arr1}[1] \le ... \le arr1[n - 1]$.

- `arr2` is monotonically **non-increasing**, in other words, $\text{arr2}[0] \ge \text{arr2}[1] \ge ... \ge arr2[n - 1]$.

- $\text{arr1}[i] + \text{arr2}[i] = \text{nums}[i]$ for all $0 \le i \le n - 1$.

Return the count of **monotonic** pairs.

Since the answer may be very large, return it **modulo** $10^{9} + 7$.

### 2. Function Contract

**Inputs**

- `nums`: Input parameter (`List[int]`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** nums = [2,3,2]

- **Output:** 4

- **Explanation:** The good pairs are:

- $([0, 1, 1], [2, 2, 1])$

- $([0, 1, 2], [2, 2, 0])$

- $([0, 2, 2], [2, 1, 0])$

- $([1, 2, 2], [1, 1, 0])$

#### Example 2

- **Input:** nums = [5,5,5,5]

- **Output:** 126

### 4. Constraints

- $1 \le n = \text{nums.length} \le 2000$

- $1 \le \text{nums}[i] \le 50$
