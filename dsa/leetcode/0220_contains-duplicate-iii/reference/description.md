## Description

You are given an integer array `nums` and two integers `indexDiff` and `valueDiff`.

Find whether a pair of indices `(i,j)` meets all three conditions:

- `i != j`
- $\lvert i-j \rvert \le \texttt{indexDiff}$
- $\lvert \texttt{nums[i]}-\texttt{nums[j]} \rvert \le \texttt{valueDiff}$

Return `true` if at least one such pair exists; otherwise return `false`.
