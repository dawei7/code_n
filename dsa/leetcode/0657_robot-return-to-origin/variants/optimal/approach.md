## General

**Track net displacement**

The robot begins at coordinate `(0, 0)`. Every command changes exactly one coordinate by one unit:

- `U` adds one to the vertical coordinate `y`;
- `D` subtracts one from `y`;
- `L` subtracts one from the horizontal coordinate `x`;
- `R` adds one to `x`.

The final position is obtained by accumulating all these changes. The robot returns to the origin exactly when both final coordinates are zero.

**Why two counters contain all necessary state**

The plane position after any prefix of moves is fully described by its horizontal and vertical displacement from the start. We do not need to remember the entire path, visited points, the direction the robot faces, or the order in which canceling moves occurred.

For example, `U` followed by `D` changes `y` by plus one and then minus one, for net zero. Those commands cancel even if many horizontal moves occur between them. Similarly, every `L` can be canceled by some `R` regardless of their positions in the string.

The task asks only where the robot ends, not whether it revisits the origin earlier or what route it draws.

**Simulate each command**

The exact implementation initializes `x = y = 0` and scans `moves` once. Python's `match` statement selects the update corresponding to the current character.

Only one branch executes for each command. Because the contract guarantees that every character is one of `U`, `D`, `L`, or `R`, no default branch is required.

After the scan, the condition `x == 0 and y == 0` checks both independent axes. Testing only one coordinate would be insufficient: `LRU` has horizontal displacement zero but ends one unit above the origin.

**Coordinate orientation is a convention**

The exact source treats up as positive `y` and down as negative `y`. Some coordinate systems reverse that convention, especially screen coordinates. Either convention is correct as long as `U` and `D` use opposite changes of the same magnitude.

The result depends on cancellation, not on which direction is named positive. Horizontal movement similarly uses right as positive and left as negative.

**A prefix invariant**

After processing the first `i` commands:

- `x` equals the number of `R` commands in that prefix minus the number of `L` commands;
- `y` equals the number of `U` commands in that prefix minus the number of `D` commands.

This is true before any command because all four counts are zero. Processing one new command adjusts exactly the corresponding counter by one, so the statement remains true for the next prefix.

At the end of the string, the invariant describes the complete net displacement. The origin is reached exactly when right and left counts match and up and down counts match, which is equivalent to `x = 0` and `y = 0`.

**Walk through two examples**

For `moves = "UD"`:

- start at `(0, 0)`;
- `U` changes the position to `(0, 1)`;
- `D` changes it back to `(0, 0)`.

Both counters are zero, so the method returns `True`.

For `moves = "LL"`:

- the first `L` makes `x = -1`;
- the second makes `x = -2`;
- `y` remains zero.

The horizontal coordinate is not zero, so the method returns `False`.

For a mixed string such as `"URDL"`, the temporary route visits several positions, but the four updates sum to zero on each axis. The algorithm correctly cares only about the final counters.

**Why the method is correct**

Every legal move has exactly the coordinate effect encoded by its branch. Addition of displacement vectors is associative, so accumulating them in sequence produces the same final displacement as physically simulating the robot.

The robot starts at the origin. A final displacement of zero on both axes means its final coordinate is the origin. If either coordinate is nonzero, the final point differs from the origin on that axis. Therefore, the final Boolean condition is both necessary and sufficient.

**Why facing direction is absent**

The note says commands are absolute: `R` always means movement to the right of the plane, not “turn right relative to where the robot faces.” There is no rotation command or orientation-dependent movement. Adding an orientation state would solve a different problem and could produce incorrect interpretations.

## Complexity detail

Let `N` be the number of move characters.

The loop examines each character exactly once and performs one constant-time integer update, so running time is `O(N)`.

Only `x`, `y`, and the current character are stored. Their count does not grow with the input, giving `O(1)` auxiliary space. The input string is read directly and no character list or path history is created.

Coordinate magnitudes are at most `N`. Python integers handle them automatically; under the given constraints they also fit easily within ordinary fixed-width integer types.

## Alternatives and edge cases

- **Compare character counts:** Return whether `moves.count("U") == moves.count("D")` and `moves.count("L") == moves.count("R")`. It is correct but may scan the string four times; the coordinate simulation is one pass.

- **Use a frequency map:** Count all four commands, then compare opposites. This takes `O(N)` time but introduces a data structure when two counters suffice.

- **Store every visited coordinate:** This uses `O(N)` space and is necessary only for questions about intersections or revisits, not the final position.

- **Use complex numbers:** Map horizontal moves to plus or minus one and vertical moves to plus or minus the imaginary unit. Summing them is concise but less approachable than explicit coordinates.

- **Only vertical moves:** Equal numbers of `U` and `D` return to the origin; otherwise `y` reveals the imbalance.

- **Only horizontal moves:** Equal numbers of `L` and `R` are required.

- **Balanced counts in a different order:** `"UUDD"` and `"UDUD"` both return because only total displacement matters.

- **One move:** Any single legal command leaves one coordinate at plus or minus one, so the answer is `False`.

- **Temporary return before the end:** A prefix may reach the origin and later leave it. The check must occur after every command has been processed.

- **One coordinate canceled:** Returning requires both conditions. Horizontal cancellation alone or vertical cancellation alone is not enough.

- **Invalid character:** The source contract excludes it. The exact `match` has no default action, so an invalid character would be silently ignored; production code with untrusted input should reject it.

- **Empty string:** The formal constraint requires at least one move. If called with an empty string anyway, both counters stay zero and the implementation returns `True`, which is mathematically consistent with making no movement.

- **Screen-coordinate convention:** Reversing the signs for up and down would not affect the final origin test as long as they remain opposites.
