## Description

Arrange the integers from `1` through `n` in increasing order from left to right.

Repeatedly sweep across the current sequence, retaining the first integer encountered and deleting every second integer after it. The first sweep starts at the left end. The next sweep starts at the right end, and the direction continues to alternate between left-to-right and right-to-left.

Continue until the sequence contains exactly one integer, then return that integer.
