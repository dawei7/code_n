## Description

You are given an integer `length` and an array `updates`, where each update has the form `[startIdx_i, endIdx_i, inc_i]`.

Begin with an array `arr` of `length` zeroes. For update $i$, add `inc_i` to every element from `arr[startIdx_i]` through `arr[endIdx_i]`, including both endpoints.

Return `arr` after every update has been applied.
