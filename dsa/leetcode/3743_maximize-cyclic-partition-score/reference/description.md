## Description

You are given a cyclic integer array `nums` and an integer `k`.

Partition the cycle into at most `k` non-empty subarrays. Each part contains consecutive positions around the cycle, so one part may continue from the end of the displayed array back to its beginning. Together, the parts cover every array position exactly once.

The range of one subarray is its maximum value minus its minimum value. A partition's score is the sum of the ranges of all its parts.

Return the greatest score attainable by any valid cyclic partition.
