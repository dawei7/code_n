## Description

You are given a **0-indexed** array `nums` consisting of positive integers.

You can do the following operation on the array **any** number of times:

- Choose an index `i` such that $0 \le i < \text{nums.length} - 1$ and $\text{nums}[i] \le nums[i + 1]$. Replace the element $nums[i + 1]$ with $\text{nums}[i] + nums[i + 1]$ and delete the element $\text{nums}[i]$ from the array.

Return *the value of the **largest** element that you can possibly obtain in the final array.*
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

- **Input:** `nums = [2,3,7,9,3]`
- **Output:** `21`
- **Explanation:** We can apply the following operations on the array:
- Choose i = 0. The resulting array will be nums = [<u>5</u>,7,9,3].
- Choose i = 1. The resulting array will be nums = [5,<u>16</u>,3].
- Choose i = 0. The resulting array will be nums = [<u>21</u>,3].
The largest element in the final array is 21. It can be shown that we cannot obtain a larger element.
#### Example 2

- **Input:** `nums = [5,3,3]`
- **Output:** `11`
- **Explanation:** We can do the following operations on the array:
- Choose i = 1. The resulting array will be nums = [5,<u>6</u>].
- Choose i = 0. The resulting array will be nums = [<u>11</u>].
There is only one element in the final array, which is 11.
### Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{6}$