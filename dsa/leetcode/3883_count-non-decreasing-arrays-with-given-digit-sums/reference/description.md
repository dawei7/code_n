## Description

You are given an integer array `digitSum` of length $n$. Count the distinct integer arrays `arr` of the same length that meet all of the following conditions:

- Every value lies in the inclusive range from `0` through `5000`.
- `arr` is non-decreasing, so each value is at least the value immediately before it.
- For every index `i`, the decimal digits of `arr[i]` add up to `digitSum[i]`.

Return the number of valid arrays modulo $10^9+7$.
