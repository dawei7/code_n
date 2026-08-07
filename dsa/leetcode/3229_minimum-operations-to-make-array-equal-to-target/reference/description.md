## Description

You are given two positive integer arrays `nums` and `target`, of the same length.

In a single operation, you can select any subarray of `nums` and increment each element within that subarray by 1 or decrement each element within that subarray by 1.

Return the **minimum** number of operations required to make `nums` equal to the array `target`.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

<div class="example-block">
**Input:** nums = [3,5,1,2], target = [4,6,2,4]

**Output:** 2

**Explanation:**

We will perform the following operations to make `nums` equal to `target`:

- Increment `nums[0..3]` by 1, `nums = [4,6,2,3]`.

- Increment `nums[3..3]` by 1, `nums = [4,6,2,4]`.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [1,3,2], target = [2,1,4]

**Output:** 5

**Explanation:**

We will perform the following operations to make `nums` equal to `target`:

- Increment `nums[0..0]` by 1, `nums = [2,3,2]`.

- Decrement `nums[1..1]` by 1, `nums = [2,2,2]`.

- Decrement `nums[1..1]` by 1, `nums = [2,1,2]`.

- Increment `nums[2..2]` by 1, `nums = [2,1,3]`.

- Increment `nums[2..2]` by 1, `nums = [2,1,4]`.

</div>
### Constraints

- $1 \le \text{nums.length} = \text{target.length} \le 10^{5}$

- $1 \le \text{nums}[i], \text{target}[i] \le 10^{8}$