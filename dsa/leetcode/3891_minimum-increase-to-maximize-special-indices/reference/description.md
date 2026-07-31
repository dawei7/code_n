## Description

You are given an integer array `nums` of length $n$. Only an interior index $i$, where $0<i<n-1$, can be **special**. It is special exactly when `nums[i]` is strictly greater than both immediate neighbors, `nums[i - 1]` and `nums[i + 1]`.

In one operation, choose any array index and increase its value by $1$. The optimization has two priorities: first make the number of special indices as large as possible, and then, among all ways to attain that maximum, use as few operations as possible. Return that minimum operation count. A cheaper result with fewer special indices does not satisfy the first priority.
