## Description

You are given an integer array `nums` and a window length `k`. Consider every contiguous subarray of exactly `k` elements, from left to right.

For each window, find the minimum length of one contiguous segment whose elements can be sorted so that the entire window becomes non-decreasing. Sorting may change only the chosen segment. If a window is already non-decreasing, its answer is zero.

Return the answers for all windows in their original order. The result therefore contains exactly $n-k+1$ values, where $n=\lvert\texttt{nums}\rvert$.
