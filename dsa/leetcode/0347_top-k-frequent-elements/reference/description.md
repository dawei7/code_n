## Description

Given an integer array `nums` and an integer `k`, return *the* `k` *most frequent elements*. You may return the answer in **any order**.
### Function Contract

**Inputs**

- `nums`: The nonempty integer array whose distinct-value frequencies are measured.
- `k`: The number of most-frequent values to return.

**Return value**

Return the unique set of `k` most-frequent values as an array in any order.

### Examples
#### Example 1

<div class="example-block">
**Input:** nums = [1,1,1,2,2,3], k = 2

**Output:** [1,2]

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [1], k = 1

**Output:** [1]

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [1,2,1,2,1,2,3,1,3,2], k = 2

**Output:** [1,2]

</div>
### Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $-10^{4} \le \text{nums}[i] \le 10^{4}$

- `k` is in the range `[1, the number of unique elements in the array]`.

- It is **guaranteed** that the answer is **unique**.

**Follow up:** Your algorithm's time complexity must be better than `O(n log n)`, where n is the array's size.