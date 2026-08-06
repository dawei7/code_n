## Description

You are given an array of strings `words`. Find all **shortest common supersequences (SCS)** of `<font face="monospace">words</font>` that are not <span data-keyword="permutation-string">permutations</span> of each other.

A **shortest common supersequence** is a string of **minimum** length that contains each string in `words` as a <span data-keyword="subsequence-string-nonempty">subsequence</span>.

Return a 2D array of integers `freqs` that represent all the SCSs. Each `freqs[i]` is an array of size 26, representing the frequency of each letter in the lowercase English alphabet for a single SCS. You may return the frequency arrays in any order.
