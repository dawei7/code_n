## General
Given You have a video sharing platform where users can upload and delete videos. Each `video` is a **string** of digits, where the $$i^{\text{th}}$$ digit of the string represents the content of the video at minute `i`. Fo..., the algorithm solves **Design Video Sharing Platform** directly. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, a priority queue (`heapq`) to maintain dynamic minimum/maximum element ordering.

## Complexity detail
- **Time Complexity**: $O(Q log Q + C)$ — Operation count bound.
- **Space Complexity**: $O(U + Q)$ — Auxiliary memory allocation bound.
