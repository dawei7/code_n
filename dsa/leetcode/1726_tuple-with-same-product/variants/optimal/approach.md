## General
Given an array `nums` of **distinct** positive integers, return *the number of tuples *`(a, b, c, d)`* such that *$a * b = c * d$* where *`a`*, *`b`*, *`c`*, and *`d`* are elements of *`nums`*, and *$a \neq b \neq c \neq d$*.*, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(n^2)$ — Operation count bound.
- **Space Complexity**: $O(n^2)$ — Auxiliary memory allocation bound.
