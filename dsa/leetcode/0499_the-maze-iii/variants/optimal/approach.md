## General
Given There is a ball in a `maze` with empty spaces (represented as `0`) and walls (represented as `1`). The ball can go through the empty spaces by rolling **up, down, left or right**, but it won't stop rolling until hitti..., the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window. It utilizes a double-ended queue (`deque`) to support dynamic $O(1)$ push and pop operations at both ends.

## Complexity detail
- **Time Complexity**: $O(rows \cdot cols \cdot p \log(rows \cdot cols))$ — Operation count bound.
- **Space Complexity**: $O(rows \cdot cols \cdot p)$ — Auxiliary memory allocation bound.
