## Description

You are given an integer array `nums` of length `n`. For each index `i`, consider the suffix made from every element positioned strictly to its right: `nums[i + 1]` through `nums[n - 1]`.

An index is **dominant** when its value is strictly greater than the arithmetic average of that entire right-hand suffix. Here, an average is the sum of the suffix values divided by the number of values in the suffix.

Return the number of indices that satisfy this dominance condition.

