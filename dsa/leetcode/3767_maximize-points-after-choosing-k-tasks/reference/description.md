## Description

You are given two integer arrays, `technique1` and `technique2`, of the same length $n$. The $n$ positions represent tasks that must all be completed.

- Completing task `i` with technique 1 earns `technique1[i]` points.
- Completing task `i` with technique 2 earns `technique2[i]` points.

An integer `k` specifies the minimum number of tasks that must use technique 1. Those tasks may occur at any indices; they are not required to be the first `k` tasks.

Every task beyond that mandatory minimum may use whichever technique is more beneficial. Return the maximum total number of points obtainable after assigning exactly one technique to every task while using technique 1 at least `k` times.
