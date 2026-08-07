## Description

Given an integer array `nums` of `2n` integers, group these integers into `n` pairs $(a_{1}, b_{1}), (a_{2}, b_{2}), ..., (a_{n}, b_{n})$ such that the sum of $min(a_{i}, b_{i})$ for all `i` is **maximized**. Return* the maximized sum*.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

- **Input:** `nums = [1,4,3,2]`
- **Output:** `4`
- **Explanation:** All possible pairings (ignoring the ordering of elements) are:
1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
So the maximum possible sum is 4.
#### Example 2

- **Input:** `nums = [6,2,6,5,1,2]`
- **Output:** `9`
- **Explanation:** The optimal pairing is (2, 1), (2, 5), (6, 6). min(2, 1) + min(2, 5) + min(6, 6) = 1 + 2 + 6 = 9.
### Constraints

- $1 \le n \le 10^{4}$

- $\text{nums.length} = 2 * n$

- $-10^{4} \le \text{nums}[i] \le 10^{4}$