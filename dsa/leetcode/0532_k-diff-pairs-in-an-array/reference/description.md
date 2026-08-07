## Description

Given an array of integers `nums` and an integer `k`, return *the number of **unique** k-diff pairs in the array*.

A **k-diff** pair is an integer pair $(\text{nums}[i], \text{nums}[j])$, where the following are true:

- $0 \le i, j < \text{nums.length}$

- $i \neq j$

- $|\text{nums}[i] - \text{nums}[j]| = k$

**Notice** that `|val|` denotes the absolute value of `val`.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

- **Input:** `nums = [3,1,4,1,5], k = 2`
- **Output:** `2`
- **Explanation:** There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of **unique** pairs.
#### Example 2

- **Input:** `nums = [1,2,3,4,5], k = 1`
- **Output:** `4`
- **Explanation:** There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
#### Example 3

- **Input:** `nums = [1,3,1,5,4], k = 0`
- **Output:** `1`
- **Explanation:** There is one 0-diff pair in the array, (1, 1).
### Constraints

- $1 \le \text{nums.length} \le 10^{4}$

- $-10^{7} \le \text{nums}[i] \le 10^{7}$

- $0 \le k \le 10^{7}$