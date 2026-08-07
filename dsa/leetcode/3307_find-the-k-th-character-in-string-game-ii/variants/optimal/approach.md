## General
Given Alice and Bob are playing a game. Initially, Alice has a string $word = "a"$, the algorithm solves **Find the K-th Character in String Game II** directly. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(log k)$ — Operation count bound.
- **Space Complexity**: $O(1)$ — Auxiliary memory allocation bound.
