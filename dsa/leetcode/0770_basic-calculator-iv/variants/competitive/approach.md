## General
Given an expression such as $expression = "e + 8 - a + 5"$ and an evaluation map such as `{"e": 1}` (given in terms of $evalvars = ["e"]$ and $evalints = [1]$), return a list of tokens representing the simplified expression..., the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(p \log p)$ — Operation count bound.
- **Space Complexity**: $O(p)$ — Auxiliary memory allocation bound.
