## Description

You are given an integer array `nums`. Split it into contiguous, non-empty subarrays so that every original element belongs to exactly one part. A split is valid only when, for each part, the greatest common divisor of that part's first and last elements is greater than $1$. Values between those endpoints do not affect whether the part is valid.

Return the minimum possible number of subarrays in a valid split. If no partition satisfies the endpoint condition for every part, return `-1`. The greatest common divisor of two integers is their largest shared positive divisor.
