## Description

You are given an integer array `nums` of length `n`. Choose a split index `i` with `0 <= i < n - 1`, so both sides of the split are nonempty.

For that index, `prefixSum(i)` is `nums[0] + nums[1] + ... + nums[i]`, while `suffixMin(i)` is the minimum among `nums[i + 1], ..., nums[n - 1]`.

Define the split score by

$$
\operatorname{score}(i)=\operatorname{prefixSum}(i)-\operatorname{suffixMin}(i).
$$

Return the greatest score over all valid split indices.
