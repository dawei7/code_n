## Description

You are given an integer array `nums` and two distinct integers, `target1` and `target2`.

A **partition** divides `nums` into one or more contiguous, non-empty blocks. The blocks must cover the entire array, and no two blocks may overlap.

The partition is **valid** when the bitwise XOR values of consecutive blocks alternate between `target1` and `target2`, beginning with `target1`. In particular, if the blocks are $b_1,b_2,b_3,\ldots$, then:

- `XOR(b1) = target1`
- `XOR(b2) = target2`, when a second block exists
- `XOR(b3) = target1`, with the same alternation continuing afterward

Return the number of valid partitions of `nums`, modulo $10^9+7$.
