## Description

You are given two integer arrays, `nums1` and `nums0`, with the same length. Index $i$ describes one binary segment: it contains `nums1[i]` consecutive `1` bits followed by `nums0[i]` consecutive `0` bits. Every described segment is non-empty.

The segments may be rearranged in any order, but the bits within an individual segment must stay in that prescribed one-run-then-zero-run form. Concatenate all segments after choosing an order. Among every possible ordering, maximize the integer represented by the resulting binary string.

Return that maximum integer modulo $10^9+7$. The ordering must maximize the full binary value itself; applying the modulus is only the final numeric representation step.
