## Description

You are given an integer array `nums`.

A subarray `nums[l..r]` is **alternating** if one of the following holds:

- $\text{nums}[l] < nums[l + 1] > nums[l + 2] < nums[l + 3] > ...$

- $\text{nums}[l] > nums[l + 1] < nums[l + 2] > nums[l + 3] < ...$

In other words, if we compare adjacent elements in the subarray, then the comparisons alternate between **strictly** greater and **strictly** smaller.

You can remove **at most one** element from `nums`. Then, you select an alternating subarray from `nums`.

Return an integer denoting the **maximum** **length** of the alternating subarray you can select.

A subarray of length 1 is considered alternating.
### Function Contract

**Inputs**

- `nums`: The integer array from which at most one element may be removed.

Let $N = \lvert\texttt{nums}\rvert$.

The selected elements must form one contiguous subarray after the optional removal. Adjacent values in that subarray must be unequal, and successive comparison directions must alternate. A one-element selection is valid even though it has no adjacent comparison.

**Return value**

Return the maximum length of an alternating subarray obtainable after removing zero or one element from `nums`.

### Examples
#### Example 1

<div class="example-block">
**Input:** nums = [2,1,3,2]

**Output:** 4

**Explanation:**

- Choose not to remove elements.

- Select the entire array `[<u>**2, 1, 3, 2**</u>]`, which is alternating because `2 > 1 < 3 > 2`.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [3,2,1,2,3,2,1]

**Output:** 4

**Explanation:**

- Choose to remove $\text{nums}[3]$ i.e., `[3, 2, 1, <u>**2**</u>, 3, 2, 1]`. The array becomes `[3, 2, 1, 3, 2, 1]`.

- Select the subarray `[3, **<u>2, 1, 3, 2</u>**, 1]`.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [100000,100000]

**Output:** 1

**Explanation:**

- Choose not to remove elements.

- Select the subarray `[100000, <u>**100000**</u>]`.

</div>
### Constraints

- $2 \le \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{5}$