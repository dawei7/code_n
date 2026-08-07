## Description

Given an integer array `nums` and an integer `k`, return `true` *if there are two **distinct indices** *`i`* and *`j`* in the array such that *$\text{nums}[i] = \text{nums}[j]$* and *$abs(i - j) \le k$.
### Function Contract

**Inputs**

- `nums`: The integer array in which equal values are sought.
- `k`: The maximum permitted absolute distance between their indices.

**Return value**

Return `true` if equal values occur at distinct indices at most `k` positions apart; otherwise return `false`.

### Examples

#### Example 1

- **Input:** `nums = [1,2,3,1], k = 3`
- **Output:** `true`
#### Example 2

- **Input:** `nums = [1,0,1,1], k = 1`
- **Output:** `true`
#### Example 3

- **Input:** `nums = [1,2,3,1,2,3], k = 2`
- **Output:** `false`
### Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $-10^{9} \le \text{nums}[i] \le 10^{9}$

- $0 \le k \le 10^{5}$