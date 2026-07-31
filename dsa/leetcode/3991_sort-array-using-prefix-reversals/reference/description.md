## Description

You are given an integer array `nums` of length $n$. It is a permutation of every integer from $0$ through $n-1$, so its ascending target is exactly `[0, 1, ..., n - 1]`.

The array `pre` lists the distinct prefix lengths that may be used. In one operation, choose any `x` in `pre` and reverse the first `x` elements of `nums`; the suffix beginning at index `x` stays in place. For instance, reversing the first three elements of `[4, 1, 2, 3]` produces `[2, 1, 4, 3]`.

Return the minimum number of allowed prefix reversals needed to put `nums` in ascending order. Return `-1` when no sequence of the permitted operations can reach that order.
