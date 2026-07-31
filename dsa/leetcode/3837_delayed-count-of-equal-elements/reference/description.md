## Description

You are given an integer array `nums` of length `n` together with a non-negative integer `k`.

For an index `i`, its **delayed count** is the number of later indices `j` that are more than `k` positions beyond `i` and hold the same value. In precise terms, a position contributes only when both `i + k < j <= n - 1` and `nums[j] == nums[i]` are true.

Return an array `ans` of length `n` in which `ans[i]` is the delayed count for index `i`.
