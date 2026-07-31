## Description

You are given an integer array `nums` together with two integers `k` and `m`.
Examine every nonempty contiguous subarray of `nums` as a separate candidate.

A candidate qualifies only when two conditions hold at the same time. It must
contain exactly `k` distinct integers, and every distinct integer present in
that subarray must appear at least `m` times. A subarray with the right number
of distinct values is therefore still invalid if even one of their frequencies
is below the threshold.

Return the total number of qualifying subarrays. Intervals with different
boundaries are counted separately, even when their value sequences happen to
be equal.
