## Description

You are given an integer array ​​​​​​​`nums`.

Define a **frequency balance subarray** as follows:

- If the subarray contains only one distinct value, it is frequency balanced.

- Otherwise, there must exist a positive integer `f` such that every distinct value in the subarray occurs either `f` or $2 * f$ times, and both frequencies occur among the distinct values.

Return an integer denoting the length of the **longest** frequency balance subarray.
### Function Contract

**Inputs**

- `nums`: The integer array in which nonempty contiguous subarrays are examined.

Values are compared by equality, and their magnitudes do not affect the balance rule.

**Return value**

Return the maximum length of a frequency balanced subarray. At least one single-element subarray exists, so the result is always positive.

### Examples

#### Example 1

<div class="example-block">
**Input:** nums = [1,2,2,1,2,3,3,3]

**Output:** 5

**Explanation:**

- The longest frequency balance subarray is `[2, 1, 2, 3, 3]`.

- The elements that appear most frequently are 2 and 3, both appearing twice.

- The remaining element 1 appears once, meeting the requirements.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [5,5,5,5]

**Output:** 4

**Explanation:**

- The longest frequency balance subarray is `[5, 5, 5, 5]`.

- The element that appears most frequently is 5.

- There are no other elements meeting the requirements.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [1,2,3,4]

**Output:** 1

**Explanation:**

Since all elements appear only once, the length of the longest frequency balance subarray is 1.

</div>
### Constraints

- $1 \le \text{nums.length} \le 10^​​​​​​​3$

- $1 \le \text{nums}[i] \le 10^​​​​​​​9$