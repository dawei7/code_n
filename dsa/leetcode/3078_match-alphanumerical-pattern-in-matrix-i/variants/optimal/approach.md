## General
Given a 2D integer matrix `board` and a 2D character matrix `pattern`. Where $0 \le \text{board}[r][c] \le 9$ and each element of `pattern` is either a digit or a lowercase English letter, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(R C p q)$ — Operation count bound.
- **Space Complexity**: $O(1)$ — Auxiliary memory allocation bound.
