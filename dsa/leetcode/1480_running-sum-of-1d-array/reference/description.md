## Description

Given an array `nums`. We define a running sum of an array as $\text{runningSum}[i] = sum(\text{nums}[0]…\text{nums}[i])$.

Return the running sum of `nums`.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

- **Input:** `nums = [1,2,3,4]`
- **Output:** `[1,3,6,10]`
- **Explanation:** Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
#### Example 2

- **Input:** `nums = [1,1,1,1,1]`
- **Output:** `[1,2,3,4,5]`
- **Explanation:** Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
#### Example 3

- **Input:** `nums = [3,1,2,10,1]`
- **Output:** `[3,4,6,16,17]`
### Constraints

- $1 \le \text{nums.length} \le 1000$

- $-10^{6} \le \text{nums}[i] \le 10^{6}$