## Description

A ball moves through a rectangular maze whose empty spaces are `0` and whose walls are `1`. From a stopped
position, the ball may begin rolling up, down, left, or right. It continues in that direction until the next step
would hit a wall. After stopping, it may choose a direction different from the direction of its preceding roll. The
maze border may be treated as surrounded by walls.

One empty space is a hole. If a roll reaches the hole, the ball falls into it immediately instead of continuing to
the wall that would otherwise stop the roll.

Given the maze, the ball's initial position, and the hole's position, return the instructions for reaching the hole
with minimum traveled distance. An instruction uses `u`, `d`, `l`, or `r` for each chosen rolling direction. Distance
counts the empty spaces crossed after leaving the initial position and includes the hole. If several instruction
strings attain the same minimum distance, choose the lexicographically smallest one. Return `"impossible"` when no
sequence of rolls reaches the hole.
