## Description

You are given a 0-indexed array `nums` whose integers are all distinct. Construct a 0-indexed array `ans` of the same length.

For every index `i`, `ans[i]` is the greatest possible length of a contiguous subarray `nums[l..r]` whose maximum element is `nums[i]`. Because every value is unique, such a subarray necessarily contains index `i`. The one-element range `nums[i..i]` is always valid.

Return `ans`.
