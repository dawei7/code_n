## General
Given Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle, and the last position is connected ba..., the algorithm solves **Design Circular Queue** directly. It utilizes a double-ended queue (`deque`) to support dynamic $O(1)$ push and pop operations at both ends. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(Q)$ — Operation count bound.
- **Space Complexity**: $O(k)$ — Auxiliary memory allocation bound.
