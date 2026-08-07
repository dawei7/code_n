## General
Given You would like to make dessert and are preparing to buy the ingredients. You have `n` ice cream base flavors and `m` types of toppings to choose from. You must follow these rules when making your dessert:, the algorithm executes depth-first search (DFS) recursion to explore valid decision branches. It utilizes a hash set (`set`) to track unique elements and prevent duplicate processing in $O(1)$ time, a dynamic programming memoization table to cache intermediate subproblem states. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(n \cdot 3^m)$ — Operation count bound.
- **Space Complexity**: $O(3^m)$ — Auxiliary memory allocation bound.
