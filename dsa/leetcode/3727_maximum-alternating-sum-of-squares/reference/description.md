## Description

You are given an integer array `nums`. You may **rearrange the elements** in any order.

The **alternating score** of an array `arr` is defined as:

- $score = \text{arr}[0]^2 - \text{arr}[1]^2 + \text{arr}[2]^2 - \text{arr}[3]^2 + ...$

Return an integer denoting the **maximum possible alternating score** of `nums` after rearranging its elements.
### Function Contract

**Inputs**

- `nums`: The integer array whose elements may be placed in any order.

Let $n$ be the length of `nums`. An arrangement has $\lceil n/2 \rceil$ even-indexed terms that are added and $\lfloor n/2 \rfloor$ odd-indexed terms that are subtracted. Each term is squared before its sign in the alternating sum is applied, so an element's original sign does not change its contribution's magnitude.

**Return value**

Return the greatest integer score among all permutations of `nums`.

### Examples
#### Example 1

<div class="example-block">
**Input:** nums = [1,2,3]

**Output:** 12

**Explanation:**

A possible rearrangement for `nums` is `[2,1,3]`, which gives the maximum alternating score among all possible rearrangements.

The alternating score is calculated as:

$score = 2^{2} - 1^{2} + 3^{2} = 4 - 1 + 9 = 12$

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [1,-1,2,-2,3,-3]

**Output:** 16

**Explanation:**

A possible rearrangement for `nums` is `[-3,-1,-2,1,3,2]`, which gives the maximum alternating score among all possible rearrangements.

The alternating score is calculated as:

$score = (-3)^2 - (-1)^2 + (-2)^2 - (1)^2 + (3)^2 - (2)^2 = 9 - 1 + 4 - 1 + 9 - 4 = 16$

</div>
### Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $-4 * 10^{4} \le \text{nums}[i] \le 4 * 10^{4}$