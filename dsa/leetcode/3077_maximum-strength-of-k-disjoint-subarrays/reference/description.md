## Description

You are given an array of integers `nums` with length `n`, and a positive **odd** integer `k`.

Select exactly **`k`** disjoint subarrays **$\text{sub}_{1}, \text{sub}_{2}, ..., \text{sub}_{k}$** from `nums` such that the last element of $\text{sub}_{i}$ appears before the first element of `sub_{i+1}` for all $1 \le i \le k-1$. The goal is to maximize their combined strength.

The strength of the selected subarrays is defined as:

$strength = k * sum(\text{sub}_{1})- (k - 1) * sum(\text{sub}_{2}) + (k - 2) * sum(\text{sub}_{3}) - ... - 2 * sum(sub_{k-1}) + sum(\text{sub}_{k})$

where **$sum(\text{sub}_{i})$** is the sum of the elements in the `i`-th subarray.

Return the **maximum** possible strength that can be obtained from selecting exactly **`k`** disjoint subarrays from `nums`.

**Note** that the chosen subarrays **don't** need to cover the entire array.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

**Input:** nums = [1,2,3,-1,2], k = 3

**Output:** 22

**Explanation:**

The best possible way to select 3 subarrays is: nums[0..2], nums[3..3], and nums[4..4]. The strength is calculated as follows:

$strength = 3 * (1 + 2 + 3) - 2 * (-1) + 2 = 22$
#### Example 2

**Input:** nums = [12,-2,-2,-2,-2], k = 5

**Output:** 64

**Explanation:**

The only possible way to select 5 disjoint subarrays is: nums[0..0], nums[1..1], nums[2..2], nums[3..3], and nums[4..4]. The strength is calculated as follows:

$strength = 5 * 12 - 4 * (-2) + 3 * (-2) - 2 * (-2) + (-2) = 64$
#### Example 3

**Input:** nums = [-1,-2,-3], k = 1

**Output:** -1

**Explanation:**

The best possible way to select 1 subarray is: nums[0..0]. The strength is -1.
### Constraints

- $1 \le n \le 10^{4}$

- $-10^{9} \le \text{nums}[i] \le 10^{9}$

- $1 \le k \le n$

- $1 \le n * k \le 10^{6}$

- `k` is odd.