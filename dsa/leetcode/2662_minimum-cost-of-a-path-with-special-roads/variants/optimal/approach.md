## General
Given an array `start` where $start = [startX, startY]$ represents your initial position `(startX, startY)` in a 2D space. You are also given the array `target` where $target = [targetX, targetY]$ represents your target pos..., the algorithm executes a single-pass linear scan through input elements. It utilizes a hash set (`set`) to track unique elements and prevent duplicate processing in $O(1)$ time, a priority queue (`heapq`) to maintain dynamic minimum/maximum element ordering.

## Complexity detail
- **Time Complexity**: $O(r^2 log r)$ — Operation count bound.
- **Space Complexity**: $O(r^2)$ — Auxiliary memory allocation bound.
