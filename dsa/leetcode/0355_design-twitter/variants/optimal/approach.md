## General
Given Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the `10` most recent tweets in the user's news feed, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(1) / O(F + 10 \log F)$ — Operation count bound.
- **Space Complexity**: $O(U + E)$ — Auxiliary memory allocation bound.
