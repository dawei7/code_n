## Description

Given a circular integer array `nums` (i.e., the next element of $nums[\text{nums.length} - 1]$ is $\text{nums}[0]$), return *the **next greater number** for every element in* `nums`.

The **next greater number** of a number `x` is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return `-1` for this number.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

- **Input:** `nums = [1,2,1]`
- **Output:** `[2,-1,2]`
- **Explanation:** The first 1's next greater number is 2;
The number 2 can't find next greater number.
The second 1's next greater number needs to search circularly, which is also 2.
#### Example 2

- **Input:** `nums = [1,2,3,4,3]`
- **Output:** `[2,3,4,-1,4]`
### Constraints

- $1 \le \text{nums.length} \le 10^{4}$

- $-10^{9} \le \text{nums}[i] \le 10^{9}$