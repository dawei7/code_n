## General
Given an array `start` where $start = [startX, startY]$ represents your initial position `(startX, startY)` in a 2D space. You are also given the array `target` where $target = [targetX, targetY]$ represents your target pos..., the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, a hash set (`set`) to track unique elements and prevent duplicate processing in $O(1)$ time, a priority queue (`heapq`) to maintain dynamic minimum/maximum element ordering. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(r^2 log r)$ — Operation count bound.
- **Space Complexity**: $O(r^2)$ — Auxiliary memory allocation bound.
