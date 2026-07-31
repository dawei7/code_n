## Description

Given an integer array `nums`, partition it from left to right by repeatedly removing a nonempty prefix. If the chosen prefix has length `k`, compute the prefix's MEX, append that value to `result`, and then continue with the unremoved suffix. The process ends only after every element has been removed.

The MEX of an array is the smallest non-negative integer absent from that array. For example, a collection containing `0` and `1` but not `2` has MEX $2$, while any collection without `0` has MEX $0$.

Among every result array obtainable by choosing the prefix lengths, return the lexicographically maximum one. At the first position where two arrays differ, the array with the larger value is greater. If every position up to the length of the shorter array agrees, the longer array is greater.
