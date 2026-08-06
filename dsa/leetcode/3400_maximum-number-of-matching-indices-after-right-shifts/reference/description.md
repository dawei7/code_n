## Description

You are given integer arrays `nums1` and `nums2` with the same length $n$. An index matches when the values at that position in the two arrays are equal.

You may right-shift `nums1` any number of times. One right shift moves every element formerly at index $i$ to index $(i+1)\bmod n$, so the final element wraps around to index zero. Among all possible circular alignments of `nums1` against the unchanged `nums2`, return the largest number of matching indices.
