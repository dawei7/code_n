## Description

Given an array `arr` of integers, check if there exist two indices `i` and `j` such that :

- $i \neq j$

- $0 \le i, j < \text{arr.length}$

- $\text{arr}[i] = 2 * \text{arr}[j]$
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

- **Input:** `arr = [10,2,5,3]`
- **Output:** `true`
- **Explanation:** For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]
#### Example 2

- **Input:** `arr = [3,1,7,11]`
- **Output:** `false`
- **Explanation:** There is no i and j that satisfy the conditions.
### Constraints

- $2 \le \text{arr.length} \le 500$

- $-10^{3} \le \text{arr}[i] \le 10^{3}$