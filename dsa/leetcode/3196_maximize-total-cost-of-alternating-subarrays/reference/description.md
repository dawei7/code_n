## Description

You are given an integer array `nums` with length `n`.

The **cost** of a <span data-keyword="subarray-nonempty">subarray</span> `nums[l..r]`, where `0 <= l <= r < n`, is defined as:

`cost(l, r) = nums[l] - nums[l + 1] + ... + nums[r] * (−1)^r − l`

Your task is to **split** `nums` into subarrays such that the **total** **cost** of the subarrays is **maximized**, ensuring each element belongs to **exactly one** subarray.

Formally, if `nums` is split into `k` subarrays, where `k > 1`, at indices `i_1, i_2, ..., i_k − 1`, where `0 <= i_1 < i_2 < ... < i_k - 1 < n - 1`, then the total cost will be:

`cost(0, i_1) + cost(i_1 + 1, i_2) + ... + cost(i_k − 1 + 1, n − 1)`

Return an integer denoting the *maximum total cost* of the subarrays after splitting the array optimally.

**Note:** If `nums` is not split into subarrays, i.e. `k = 1`, the total cost is simply `cost(0, n - 1)`.
