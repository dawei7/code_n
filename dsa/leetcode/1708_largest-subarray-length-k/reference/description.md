## Description

An array $A$ is larger than an array $B$ (of the same length) if for the first index $i$ where $A[i] \neq B[i]$, $A[i] > B[i]$.

For example, `[1,3,2,4]` is larger than `[1,2,4,3]` because the first index they differ at is index 1, and $3 > 2$.

You are given an integer array `nums` of **distinct** integers and an integer `k`. Return *the largest subarray of `nums` of length `k`*.

A **subarray** is a contiguous part of an array.
