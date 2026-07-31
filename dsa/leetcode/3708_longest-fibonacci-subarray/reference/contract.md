## Function Contract

**Inputs**

- `nums`: An array of $n$ positive integers.

A subarray `nums[left..right]` is contiguous. When it contains at least three values, each index $k$ with `left + 2 <= k <= right` must satisfy `nums[k] = nums[k - 1] + nums[k - 2]`.

**Return value**

Return the greatest length of any Fibonacci subarray in `nums`.
