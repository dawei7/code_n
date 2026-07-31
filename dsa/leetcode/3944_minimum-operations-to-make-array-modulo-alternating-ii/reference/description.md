## Description

You receive an integer array `nums` and an integer modulus `k`. One operation changes any one array element by exactly `1`, either upward or downward.

The target is a **modulo alternating** array. There must be two distinct residues `x` and `y`, both in the range from `0` through `k - 1`, such that every element at an even index is congruent to `x` modulo `k` and every element at an odd index is congruent to `y` modulo `k`.

Choose the two residues and the individual element changes so that the total number of unit operations is as small as possible, and return that minimum.

