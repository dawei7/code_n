## Description

Given an integer array `nums` of length $n$, construct a new array with one entry for every adjacent pair in `nums`.

For each index $i$ from $0$ through $n-2$, set `answer[i] = nums[i] | nums[i + 1]`, where `|` denotes bitwise OR. Return the resulting array of length $n-1$.

Consecutive output positions come from overlapping pairs: an interior value of `nums` participates once as the right member of a pair and once as the left member of the next pair. Each pair is evaluated independently, and its result remains in the same left-to-right order as that pair in the input.
