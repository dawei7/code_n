## Description

A ball moves through a rectangular maze whose empty spaces are `0` and whose walls are `1`. From a stopped
position, the ball may begin rolling up, down, left, or right. It continues in that direction until the next step
would hit a wall; only after stopping may it choose another direction. The maze border may be treated as surrounded
by walls.

Given the $m \times n$ maze, `start = [startrow, startcol]`, and
`destination = [destinationrow, destinationcol]`, return the shortest distance that lets the ball stop exactly at
`destination`. Passing through that cell without stopping does not succeed. Return `-1` if no sequence of complete
rolls can stop there.

Distance is the number of empty spaces crossed after leaving `start`, with the destination cell included in the
count.
