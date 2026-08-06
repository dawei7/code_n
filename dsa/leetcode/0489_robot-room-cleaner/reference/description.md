## Description

A robot is located in a room represented internally by an $m \times n$ binary grid. A `0` is a wall, and a `1` is
an empty cell. The robot begins on an empty cell, but neither the room layout nor its absolute starting position is
available to the solution.

Control the robot through its movement and cleaning interface so that it cleans every empty cell in the room. It can
move one cell forward, turn left or right by $90$ degrees, and clean its current cell. If it attempts to move into a
wall, its bumper detects the obstacle, `move()` reports failure, and the robot remains where it is.
