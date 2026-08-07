## General
Given In LeetCode Store, there are `n` items to sell. Each item has a price. However, there are some special offers, and a special offer consists of one or more different kinds of items with a sale price, the algorithm executes a single-pass linear scan through input elements. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(SM \cdot \prod(needs_i + 1))$ — Operation count bound.
- **Space Complexity**: $O(M \cdot \prod(needs_i + 1))$ — Auxiliary memory allocation bound.
