## General
Given You have a video sharing platform where users can upload and delete videos. Each `video` is a **string** of digits, where the $$i^{\text{th}}$$ digit of the string represents the content of the video at minute `i`. Fo..., the algorithm executes a single-pass linear scan through input elements. It utilizes a priority queue (`heapq`) to maintain dynamic minimum/maximum element ordering.

## Complexity detail
- **Time Complexity**: $O(Q log Q + C)$ — Operation count bound.
- **Space Complexity**: $O(U + Q)$ — Auxiliary memory allocation bound.
