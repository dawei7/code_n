## Description

You are given an integer array `nums` of length $n$ and a positive integer `p`. A subsequence is good when it is non-empty, uses strictly fewer than $n$ elements, and the greatest common divisor (GCD) of all its selected values is exactly `p`.

You are also given a sequence of point updates. Each query `[ind_i, val_i]` replaces `nums[ind_i]` with `val_i`; the change remains in effect for all later queries.

After applying each update, determine whether the current array contains at least one good subsequence. Return the number of queries whose resulting array satisfies that condition. For two integers $a$ and $b$, $gcd(a,b)$ denotes their greatest common divisor.
