## Function Contract

**Inputs**

- `maze`: a rectangular binary matrix where `0` is an empty space and `1` is a wall
- `ball`: the ball's initial empty cell as `[row, column]`
- `hole`: the distinct empty cell that catches the ball as `[row, column]`

**Return value**

- Return the lexicographically smallest instruction string among all routes with minimum traveled distance, or
  `"impossible"` if the hole is unreachable.

Each instruction character commits the ball to a complete roll. A wall normally ends that roll, but encountering
the hole ends the entire route immediately. The instruction alphabet is `u` for up, `d` for down, `l` for left, and
`r` for right.
