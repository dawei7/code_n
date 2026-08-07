## General
Given The **median** is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values, the algorithm solves **Find Median from Data Stream** directly. It utilizes a priority queue (`heapq`) to maintain dynamic minimum/maximum element ordering. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(n \log n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
