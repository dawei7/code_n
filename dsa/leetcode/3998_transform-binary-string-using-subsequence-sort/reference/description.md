## Description

You are given a binary string `s` and an array `strs`. Every string in `strs` has the same length as `s`; its characters may be `0`, `1`, or `?`. Each question mark must independently be replaced by either `0` or `1`.

The source string may be changed by repeating the following operation any number of times, including zero. Choose a subsequence of `s`, sort the selected binary characters into non-decreasing order, and write them back into the same selected positions. Characters outside those positions do not move.

For every pattern `strs[i]`, decide whether some replacement of all its question marks can be obtained from `s` through those subsequence-sorting operations. Return the decisions in a boolean array `ans`, preserving the order of `strs`.
