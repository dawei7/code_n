## Description

You are given an integer array `nums`. Its **strength** is the bitwise OR of all its elements.

A nonempty subsequence is **effective** when removing the selected occurrences makes the strength of the elements that remain strictly smaller than the original strength. Subsequences are determined by their chosen indices, so equal values taken from different positions represent different choices.

Count every effective subsequence and return the total modulo $10^9+7$.

The bitwise OR of an empty array is defined to be `0`; consequently, removing every element is evaluated using that value.
