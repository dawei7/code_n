## Description

Given an array of integers `nums` and a positive integer `k`, check whether it is possible to divide this array into sets of `k` consecutive numbers.

Return `true` *if it is possible*.** **Otherwise, return `false`.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

- **Input:** `nums = [1,2,3,3,4,4,5,6], k = 4`
- **Output:** `true`
- **Explanation:** Array can be divided into [1,2,3,4] and [3,4,5,6].
#### Example 2

- **Input:** `nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3`
- **Output:** `true`
- **Explanation:** Array can be divided into [1,2,3] , [2,3,4] , [3,4,5] and [9,10,11].
#### Example 3

- **Input:** `nums = [1,2,3,4], k = 3`
- **Output:** `false`
- **Explanation:** Each array should be divided in subarrays of size 3.
### Constraints

- $1 \le k \le \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{9}$

**Note:** This question is the same as 846: <a href="https://leetcode.com/problems/hand-of-straights/" target="_blank">https://leetcode.com/problems/hand-of-straights/</a>