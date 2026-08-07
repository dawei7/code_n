## Description

Given a binary array `nums` and an integer `goal`, return *the number of non-empty **subarrays** with a sum* `goal`.

A **subarray** is a contiguous part of the array.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

- **Input:** `nums = [1,0,1,0,1], goal = 2`
- **Output:** `4`
- **Explanation:** The 4 subarrays are bolded and underlined below:
[<u>**1,0,1**</u>,0,1]
[<u>**1,0,1,0**</u>,1]
[1,<u>**0,1,0,1**</u>]
[1,0,<u>**1,0,1**</u>]
#### Example 2

- **Input:** `nums = [0,0,0,0,0], goal = 0`
- **Output:** `15`
### Constraints

- $1 \le \text{nums.length} \le 3 * 10^{4}$

- $\text{nums}[i]$ is either `0` or `1`.

- $0 \le goal \le \text{nums.length}$