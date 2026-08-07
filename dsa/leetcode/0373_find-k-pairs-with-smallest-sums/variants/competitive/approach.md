## General
Given two integer arrays `nums1` and `nums2` sorted in **non-decreasing order** and an integer `k`, the algorithm executes a single-pass linear scan through input elements. It utilizes a double-ended queue (`deque`) to support dynamic $O(1)$ push and pop operations at both ends, a priority queue (`heapq`) to maintain dynamic minimum/maximum element ordering. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(k \log \min(k,m))$ — Operation count bound.
- **Space Complexity**: $O(\min(k,m))$ — Auxiliary memory allocation bound.
