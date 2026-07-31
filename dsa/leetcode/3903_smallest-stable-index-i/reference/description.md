## Description

You are given an integer array `nums` of length $n$ and a non-negative threshold `k`. Every index $i$ splits the information used by its instability score into an inclusive prefix and an inclusive suffix.

The prefix component is the largest value among `nums[0]` through `nums[i]`. The suffix component is the smallest value among `nums[i]` through `nums[n - 1]`. Their difference is the instability score:

$$
\max(\texttt{nums}[0..i])-\min(\texttt{nums}[i..n-1]).
$$

An index is stable when this score is at most `k`. Return the smallest stable index, or return `-1` if every index has a score greater than `k`.
