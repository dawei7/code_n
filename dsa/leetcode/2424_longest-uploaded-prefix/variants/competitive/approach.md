## General
Given a stream of `n` videos, each represented by a **distinct** number from `1` to `n` that you need to "upload" to a server. You need to implement a data structure that calculates the length of the **longest uploaded pref..., the algorithm solves **Longest Uploaded Prefix** directly. It utilizes a hash set (`set`) to track unique elements and prevent duplicate processing in $O(1)$ time.

## Complexity detail
- **Time Complexity**: $O(n + q)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
