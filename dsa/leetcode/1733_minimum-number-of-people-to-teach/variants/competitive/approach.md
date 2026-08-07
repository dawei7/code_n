## General
Given On a social network consisting of `m` users and some friendships between users, two users can communicate with each other if they know a common language, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(S + C)$ — Operation count bound.
- **Space Complexity**: $O(S + m)$ — Auxiliary memory allocation bound.
