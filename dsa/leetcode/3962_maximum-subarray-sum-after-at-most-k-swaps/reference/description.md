## Description

You are given an integer array `nums` and an integer `k`.

You are allowed to perform **at most** `k` swap operations on the array.

In one swap operation, you may choose any two indices `i` and `j` and swap $\text{nums}[i]$ and $\text{nums}[j]$.

Return an integer denoting the **maximum possible subarray sum** after performing the swaps.
### Function Contract

**Inputs**

- `nums`: A nonempty list of integers whose elements may be positive, zero, or negative.
- `k`: The maximum number of swaps allowed between pairs of distinct positions.

Let $n$ be the length of `nums`, and let $M$ be the number of distinct values in it.

**Return value**

Return the maximum possible sum of a nonempty contiguous subarray after performing at most `k` swaps. The result may be negative when every array value is negative.

### Examples

#### Example 1

<div class="example-block">
**Input:** nums = [1,-1,0,2], k = 1

**Output:** 3

**Explanation:**

- We can swap on indices 1 and 3, resulting in the array `[1, 2, 0, -1]`.

- The subarray `[1, 2]` has a sum of 3, which is the maximum possible subarray sum after at most $k = 1$​​​​​​​ swap.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [4,3,2,4], k = 2

**Output:** 13

**Explanation:**

The maximum possible subarray sum after at most $k = 2$ swaps is the sum of the entire array, which is 13.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [-1,-2], k = 0

**Output:** -1

**Explanation:**

- $k = 0$ swaps are allowed.

- The possible subarrays are `[-1]`, `[-2]`, and `[-1, -2]`, with sums -1, -2, and -3 respectively.

- Among these sums, the maximum is -1.

</div>
### Constraints

- $1 \le \text{nums.length} \le 1500$

- $-10^{5} \le \text{nums}[i] \le 10^{5}$

- $0 \le k \le \text{nums.length}$