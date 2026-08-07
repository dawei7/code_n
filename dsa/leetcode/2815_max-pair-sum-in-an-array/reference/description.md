## Description

You are given an integer array `nums`. You have to find the **maximum** sum of a pair of numbers from `nums` such that the **largest digit **in both numbers is equal.

For example, 2373 is made up of three distinct digits: 2, 3, and 7, where 7 is the largest among them.

Return the **maximum** sum or -1 if no such pair exists.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

<div class="example-block">
**Input:** nums = [112,131,411]

**Output:** -1

**Explanation:**

Each numbers largest digit in order is [2,3,4].

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [2536,1613,3366,162]

**Output:** 5902

**Explanation:**

All the numbers have 6 as their largest digit, so the answer is 2536 + 3366 = 5902.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [51,71,17,24,42]

**Output:** 88

**Explanation:**

Each number's largest digit in order is [5,7,7,4,4].

So we have only two possible pairs, 71 + 17 = 88 and 24 + 42 = 66.

</div>
### Constraints

- $2 \le \text{nums.length} \le 100$

- $1 \le \text{nums}[i] \le 10^{4}$