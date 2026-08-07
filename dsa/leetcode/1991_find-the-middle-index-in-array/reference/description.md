## Description

Given a **0-indexed** integer array `nums`, find the **leftmost** `middleIndex` (i.e., the smallest amongst all the possible ones).

A `middleIndex` is an index where $\text{nums}[0] + \text{nums}[1] + ... + nums[middleIndex-1] = nums[middleIndex+1] + nums[middleIndex+2] + ... + nums[\text{nums.length}-1]$.

If $middleIndex = 0$, the left side sum is considered to be `0`. Similarly, if $middleIndex = \text{nums.length} - 1$, the right side sum is considered to be `0`.

Return *the **leftmost** *`middleIndex`* that satisfies the condition, or *`-1`* if there is no such index*.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

- **Input:** `nums = [2,3,-1,<u>8</u>,4]`
- **Output:** `3`
- **Explanation:** The sum of the numbers before index 3 is: 2 + 3 + -1 = 4
The sum of the numbers after index 3 is: 4 = 4
#### Example 2

- **Input:** `nums = [1,-1,<u>4</u>]`
- **Output:** `2`
- **Explanation:** The sum of the numbers before index 2 is: 1 + -1 = 0
The sum of the numbers after index 2 is: 0
#### Example 3

- **Input:** `nums = [2,5]`
- **Output:** `-1`
- **Explanation:** There is no valid middleIndex.
### Constraints

- $1 \le \text{nums.length} \le 100$

- $-1000 \le \text{nums}[i] \le 1000$

**Note:** This question is the same as 724: <a href="https://leetcode.com/problems/find-pivot-index/" target="_blank">https://leetcode.com/problems/find-pivot-index/</a>