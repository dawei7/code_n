## Description

You are given an integer array `nums`.

An ordered index pair `(i,j)` is a **mirror pair** when $0\leq i<j<\texttt{nums.length}$ and reversing the decimal digits of `nums[i]` produces `nums[j]`. Any leading zeros created by the reversal are discarded; for example, `reverse(120) = 21`.

For every mirror pair, its absolute index distance is `abs(i - j)`. Return the smallest such distance across the array, or return `-1` when no mirror pair exists.
