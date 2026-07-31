## Description

You are given a circular integer array `nums` of length $n$. An index $i$ is a **peak** when its value is strictly greater than both circular neighbors. Its previous neighbor is index $i-1$ when $i>0$ and index $n-1$ otherwise; its next neighbor is index $i+1$ when $i<n-1$ and index $0$ otherwise.

An operation chooses any index and increases its value by exactly $1$, and operations may be repeated. Find the minimum total number of operations needed for the resulting circular array to contain at least `k` peaks. Return $-1$ when no array obtainable through such increases can have that many peaks.
