## Description

You are given a sorted integer array `arr` containing `1` and **prime** numbers, where all the integers of `arr` are unique. You are also given an integer `k`.

For every `i` and `j` where $0 \le i < j < \text{arr.length}$, we consider the fraction $\text{arr}[i] / \text{arr}[j]$.

Return *the* $$k^{\text{th}}$$*smallest fraction considered*. Return your answer as an array of integers of size `2`, where$\text{answer}[0] = \text{arr}[i]$and$\text{answer}[1] = \text{arr}[j]$.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

- **Input:** `arr = [1,2,3,5], k = 3`
- **Output:** `[2,5]`
- **Explanation:** The fractions to be considered in sorted order are:
1/5, 1/3, 2/5, 1/2, 3/5, and 2/3.
The third fraction is 2/5.
#### Example 2

- **Input:** `arr = [1,7], k = 1`
- **Output:** `[1,7]`
### Constraints

- $2 \le \text{arr.length} \le 1000$

- $1 \le \text{arr}[i] \le 3 * 10^{4}$

- $\text{arr}[0] = 1$

- $\text{arr}[i]$ is a **prime** number for `i > 0`.

- All the numbers of `arr` are **unique** and sorted in **strictly increasing** order.

- $1 \le k \le \text{arr.length} * (\text{arr.length} - 1) / 2$

**Follow up:** Can you solve the problem with better than $O(n^{2})$ complexity?