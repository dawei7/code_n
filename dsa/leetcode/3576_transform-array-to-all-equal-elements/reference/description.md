## Description

You are given an integer array `nums` of size `n` containing only `1` and `-1`, and an integer `k`.

You can perform the following operation at most `k` times:

- Choose an index `i` ($0 \le i < n - 1$), and **multiply** both $\text{nums}[i]$ and $nums[i + 1]$ by `-1`.

**Note** that you can choose the same index `i` more than once in **different** operations.

Return `true` if it is possible to make all elements of the array **equal** after at most `k` operations, and `false` otherwise.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

<div class="example-block">
**Input:** nums = [1,-1,1,-1,1], k = 3

**Output:** true

**Explanation:**

We can make all elements in the array equal in 2 operations as follows:

- Choose index $i = 1$, and multiply both $\text{nums}[1]$ and $\text{nums}[2]$ by -1. Now `nums = [1,1,-1,-1,1]`.

- Choose index $i = 2$, and multiply both $\text{nums}[2]$ and $\text{nums}[3]$ by -1. Now `nums = [1,1,1,1,1]`.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [-1,-1,-1,1,1,1], k = 5

**Output:** false

**Explanation:**

It is not possible to make all array elements equal in at most 5 operations.

</div>
### Constraints

- $1 \le n = \text{nums.length} \le 10^{5}$

- $\text{nums}[i]$ is either -1 or 1.

- $1 \le k \le n$