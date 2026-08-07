## General
Given Design a search autocomplete system for a search engine. Users may input a sentence (at least one word and end with a special character `'#'`), the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(C + Q)$ — Operation count bound.
- **Space Complexity**: $O(C + Q)$ — Auxiliary memory allocation bound.
