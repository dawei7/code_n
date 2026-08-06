## Description

You are given an array `nums` consisting of non-negative integers. You are also given a `queries` array, where `queries[i] = [x_i, m_i]`.

The answer to the `i^th` query is the maximum bitwise `XOR` value of `x_i` and any element of `nums` that does not exceed `m_i`. In other words, the answer is `max(nums[j] XOR x_i)` for all `j` such that `nums[j] <= m_i`. If all elements in `nums` are larger than `m_i`, then the answer is `-1`.

Return *an integer array *`answer`* where *`answer.length == queries.length`* and *`answer[i]`* is the answer to the *`i^th`* query.*
