## Description

You are given an integer array `nums` of length `n` and an integer `k`.

An index `i` is a **peak** if:

- $0 < i < n - 1$

- $\text{nums}[i] > nums[i - 1]$ and $\text{nums}[i] > nums[i + 1]$

A subarray `[l, r]` is **valid** if:

- It contains **exactly one** peak at index `i` from `nums`

- $i - l \le k$ and $r - i \le k$

Return an integer denoting the number of **valid subarrays** in `nums`.

A **subarray** is a contiguous **non-empty** sequence of elements within an array.
### Function Contract

**Inputs**

- `nums`: The integer array whose contiguous subarrays are counted.
- `k`: The maximum allowed distance from the unique contained peak to either selected endpoint.

Peak status is evaluated in the complete input array, not relative to a selected subarray. Therefore a length-one subarray containing a global peak contains exactly one peak even though that element has no neighbors inside the subarray.

Let $n=\lvert\texttt{nums}\rvert$.

**Return value**

Return the total number of index intervals `[l, r]` that contain exactly one original-array peak `i` and satisfy both distance bounds.

### Examples

#### Example 1

<div class="example-block">
**Input:** nums = [1,3,2], k = 1

**Output:** 4

**Explanation:**

- Index $i = 1$ is a peak because $\text{nums}[1] = 3$ is greater than $\text{nums}[0] = 1$ and $\text{nums}[2] = 2$.

- Any valid subarray must include index 1, and the distance from the peak to both ends of the subarray must not exceed $k = 1$.

- The valid subarrays are `[3]`, `[1, 3]`, `[3, 2]`, and `[1, 3, 2]`, so the answer is 4.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [7,8,9], k = 2

**Output:** 0

**Explanation:**

- There is no index `i` such that $\text{nums}[i]$ is greater than both $nums[i - 1]$ and $nums[i + 1]$.

- Therefore, the array contains no peak. Thus, the number of valid subarrays is 0.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [4,3,5,1], k = 2

**Output:** 6

**Explanation:**

- Index $i = 2$ is a peak because $\text{nums}[2] = 5$ is greater than $\text{nums}[1] = 3$ and $\text{nums}[3] = 1$.

- Any valid subarray must contain this peak, and the distance from the peak to both ends of the subarray must not exceed $k = 2$.

- The valid subarrays are `[5]`, `[3, 5]`, `[5, 1]`, `[3, 5, 1]`, `[4, 3, 5]`, and `[4, 3, 5, 1]`, so the answer is 6.

</div>
### Constraints

- $1 \le n = \text{nums.length} \le 10^{5}$

- $-10^{5} \le \text{nums}[i] \le 10^{5}$

- $1 \le k \le n$