## Description

You are given an integer array `nums` of length $n$. It is a permutation of every integer from $1$ through $n$. You are also given `sequences`, whose rows are subsequences of `nums`.

A supersequence for `sequences` contains every row of `sequences` as a subsequence. Among all such sequences, a shortest supersequence has the minimum possible length, and more than one shortest supersequence may exist. Determine whether `nums` is both shortest and the only shortest supersequence.

For example, `sequences = [[1,2],[1,3]]` permits the two shortest supersequences `[1,2,3]` and `[1,3,2]`. By contrast, `sequences = [[1,2],[1,3],[1,2,3]]` has `[1,2,3]` as its only shortest supersequence. Although `[1,2,3,4]` also contains all three rows as subsequences, its extra value means it is not shortest.

Return `true` exactly when `nums` is the unique shortest supersequence; otherwise, return `false`.

A subsequence is obtained from another sequence by deleting zero or more elements without changing the relative order of the elements that remain.
