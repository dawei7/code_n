## Description

A ball moves through a maze whose empty spaces are `0` and whose walls are `1`. From a stopped position, the ball
may begin rolling up, down, left, or right. It continues in that direction until the next step would hit a wall; only
after stopping may it choose another direction.

Given the $m \times n$ maze, `start = [startrow, startcol]`, and
`destination = [destinationrow, destinationcol]`, return whether the ball can stop exactly at `destination`. Passing
through that cell without stopping does not succeed. The maze border may be treated as surrounded by walls.
