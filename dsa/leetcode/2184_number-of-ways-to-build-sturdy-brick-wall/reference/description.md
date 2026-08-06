## Description

Build a wall with `height` rows, each exactly `width` units long. Every
available brick is one unit high and has a width listed in the unique array
`bricks`. Each brick type has an unlimited supply, but bricks cannot be
rotated.

Within a row, adjacent bricks create vertical joints at their meeting
positions. The wall is sturdy only when two adjacent rows have no joint at the
same interior position; their shared boundaries at the two ends are allowed.
Count all sturdy walls and return the result modulo $10^9+7$.
