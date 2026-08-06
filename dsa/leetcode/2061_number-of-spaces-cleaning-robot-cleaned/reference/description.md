## Description

A binary matrix represents a room: `0` is an empty space and `1` is an object. The upper-left space is always empty. A cleaning robot starts there facing right, and its starting space and every empty space it visits become clean.

The robot repeatedly attempts to move one cell straight ahead. If the next cell is outside the room or contains an object, it stays in place and turns $90^\circ$ clockwise; otherwise it advances without changing direction. The robot runs indefinitely. Return the number of distinct spaces it eventually cleans.
