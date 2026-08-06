## Description

The **median** of an ordered list with an odd number of integers is its middle value. For example, the median of
`[2, 3, 4]` is `3`. An even-length list has two central values, so its median is their arithmetic mean; the median of
`[1, 2, 3, 4]` is `(2 + 3) / 2 = 2.5`.

Given an integer array `nums` and an integer `k`, consider a window containing exactly `k` consecutive elements. The
window starts at the left end of the array and advances one position at a time until it reaches the right end. At
each position, only the values within that window participate in its median.

Return the medians of all window positions in their original left-to-right order. A reported value is accepted when
it differs from the exact median by at most $10^{-5}$.
