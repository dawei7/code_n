## General
Given a string `text`. We want to display `text` on a screen of width `w` and height `h`. You can choose any font size from array `fonts`, which contains the available font sizes **in ascending order**, the algorithm executes binary search over the search space to achieve logarithmic reduction. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(n+\sigma\log f)$ — Operation count bound.
- **Space Complexity**: $O(\sigma)$ — Auxiliary memory allocation bound.
