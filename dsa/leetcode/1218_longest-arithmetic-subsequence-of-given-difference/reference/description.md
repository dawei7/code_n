### 1. Description

Given an integer array `arr` and an integer `difference`, return the length of the longest subsequence in `arr` which is an arithmetic sequence such that the difference between adjacent elements in the subsequence equals `difference`.

A **subsequence** is a sequence that can be derived from `arr` by deleting some or no elements without changing the order of the remaining elements.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** `arr = [1,2,3,4], difference = 1`
- **Output:** `4`
- **Explanation:** The longest arithmetic subsequence is [1,2,3,4].
#### Example 2

- **Input:** `arr = [1,3,5,7], difference = 1`
- **Output:** `1`
- **Explanation:** The longest arithmetic subsequence is any single element.
#### Example 3

- **Input:** `arr = [1,5,7,8,5,3,4,2,1], difference = -2`
- **Output:** `4`
- **Explanation:** The longest arithmetic subsequence is [7,5,3,1].

### 4. Constraints

- $1 \le \text{arr.length} \le 10^{5}$

- $-10^{4} \le \text{arr}[i], difference \le 10^{4}$