## Description

You are given an integer array `nums` of length $N$. For each possible window
length $L$ from 1 through $N$, consider every contiguous subarray containing
exactly $L$ elements. Find the minimum value within each such subarray, then
take the maximum among those minima.

Return all $N$ query answers in one array. Position `i` corresponds to window
length $i+1$, so `answer[i]` is the greatest minimum obtainable from any
subarray of that length.
