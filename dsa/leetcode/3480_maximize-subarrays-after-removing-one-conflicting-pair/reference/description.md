## Description

You are given an integer `n` which represents an array `nums` containing the numbers from 1 to `n` in order. Additionally, you are given a 2D array `conflictingPairs`, where `conflictingPairs[i] = [a, b]` indicates that `a` and `b` form a conflicting pair.

Remove **exactly** one element from `conflictingPairs`. Afterward, count the number of <span data-keyword="subarray-nonempty">non-empty subarrays</span> of `nums` which do not contain both `a` and `b` for any remaining conflicting pair `[a, b]`.

Return the **maximum** number of subarrays possible after removing **exactly** one conflicting pair.
