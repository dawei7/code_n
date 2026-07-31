## Description

You are given an integer array `nums` of length $n$ and a non-negative threshold `k`. Each index $i$ has an instability score obtained from two inclusive ranges: the prefix ending at $i$ and the suffix beginning at $i$.

Take the largest value in `nums[0..i]` and subtract the smallest value in `nums[i..n - 1]`:

$$
\max(\texttt{nums}[0..i])-\min(\texttt{nums}[i..n-1]).
$$

Index $i$ is stable when this difference is at most `k`. Return the smallest stable index. If every index has an instability score greater than `k`, return `-1`.
