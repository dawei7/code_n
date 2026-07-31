## Description

You receive two integer arrays, `nums1` and `nums2`, together with a sequence of queries. The values in `nums1` remain fixed, while range-addition queries change `nums2` as the sequence is processed.

Each query has one of two forms:

- `[1, x, y, val]` adds `val` to every element of the inclusive subarray `nums2[x..y]`.
- `[2, tot]` asks how many index pairs `(j, k)` satisfy `nums1[j] + nums2[k] == tot` using the current values of `nums2`.

Process the queries in their given order. Every pair of indices is counted separately, so equal values occurring at different positions contribute their full multiplicity. Return the answers to the type-2 queries in the same order in which those queries appear.
