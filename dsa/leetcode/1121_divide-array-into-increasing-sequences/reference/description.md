### 1. Description

Given an integer array `nums` sorted in non-decreasing order and an integer `k`, return `true`* if this array can be divided into one or more disjoint increasing subsequences of length at least *`k`*, or *`false`* otherwise*.

### 2. Function Contract

**Inputs**

- `nums`: a nonempty integer array of length $n$, sorted in non-decreasing order.
- `k`: the minimum permitted length of every resulting subsequence.

A valid division assigns every array occurrence to exactly one subsequence. Each subsequence retains the original relative order of its selected occurrences, has strictly increasing values, and contains at least `k` elements.

**Return value**

- `true` exactly when a valid division exists; otherwise, `false`.

### 3. Examples

#### Example 1

- **Input:** `nums = [1,2,2,3,3,4,4], k = 3`
- **Output:** `true`
- **Explanation:** The array can be divided into two subsequences [1,2,3,4] and [2,3,4] with lengths at least 3 each.
#### Example 2

- **Input:** `nums = [5,6,6,7,8], k = 3`
- **Output:** `false`
- **Explanation:** There is no way to divide the array using the conditions required.

### 4. Constraints

- $1 \le k \le \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{5}$

- `nums` is sorted in non-decreasing order.