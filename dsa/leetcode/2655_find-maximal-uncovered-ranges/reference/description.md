## Description

An abstract 0-indexed array `nums` has length `n`. You are given `ranges`, a list of inclusive index intervals; intervals may overlap, and every index contained in at least one interval is covered. The actual values of `nums` are irrelevant because only its index domain $[0,n-1]$ matters.

Partition every uncovered index into maximal contiguous uncovered ranges. Each uncovered index must occur in exactly one returned interval, and no two returned intervals may be adjacent, since adjacent uncovered intervals would form one larger maximal interval. Return these inclusive pairs in ascending order of their starting indices.
