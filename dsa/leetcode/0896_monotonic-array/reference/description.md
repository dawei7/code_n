## Description

An array is **monotonic** if it is either monotone increasing or monotone decreasing.

An array `nums` is monotone increasing if for all $i \le j$, $\text{nums}[i] \le \text{nums}[j]$. An array `nums` is monotone decreasing if for all $i \le j$, $\text{nums}[i] \ge \text{nums}[j]$.

Given an integer array `nums`, return `true`* if the given array is monotonic, or *`false`* otherwise*.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

- **Input:** `nums = [1,2,2,3]`
- **Output:** `true`
#### Example 2

- **Input:** `nums = [6,5,4,4]`
- **Output:** `true`
#### Example 3

- **Input:** `nums = [1,3,2]`
- **Output:** `false`
### Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $-10^{5} \le \text{nums}[i] \le 10^{5}$