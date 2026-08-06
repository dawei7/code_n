## Description

Several pistons move vertically between positions `0` and `height`. The current position of a piston is also the area beneath it. `positions[i]` gives its initial position, while `directions[i]` is `U` for upward motion or `D` for downward motion.

During every second, each piston moves one unit in its current direction. Reaching either endpoint reverses its direction for subsequent motion, so every piston repeatedly travels from bottom to top and back. Endpoint directions are interpreted through this immediate reflection: a piston at an endpoint next moves into the valid interval.

At any integer time, the total occupied area is the sum of all piston positions. Return the greatest total that occurs over the continuing periodic motion, including the initial state.
