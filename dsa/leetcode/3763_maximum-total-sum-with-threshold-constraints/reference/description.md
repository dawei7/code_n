## Description

You are given integer arrays `nums` and `threshold`, both of length $n$. Begin with `step = 1` and a running total of zero.

Repeat the following process:

- Choose an unused index `i` satisfying `threshold[i] <= step`. If no such index exists, the process stops.
- Add `nums[i]` to the running total, mark `i` as used, and increase `step` by one.

Choose indices optimally and return the maximum total sum obtainable before the process ends.
