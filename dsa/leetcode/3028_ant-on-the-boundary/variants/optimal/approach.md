## General

**Represent direction with the sign.** Treat the boundary as coordinate zero. A positive movement adds its magnitude to the current coordinate, and a negative movement already subtracts its magnitude. Therefore the ant's position after step `i` is exactly the prefix sum through `nums[i]`.

**Count only completed returns.** Update the running position once per list element, then increment the answer if it equals zero. Checking only after the addition matches the rule that crossing the boundary mid-movement does not count. It also excludes the initial position because no check occurs before the first movement.

After every processed prefix, `position` equals the ant's true signed displacement from the boundary. Consequently `position == 0` holds exactly for the completed movements that end on the boundary, so the accumulated count is correct.

## Complexity detail

The algorithm performs one addition and one comparison for each of the $N$ movements, giving $O(N)$ time. It stores only the current position and count, so auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Recompute each prefix:** Summing `nums[:i + 1]` after every step gives the same positions but costs $O(N^2)$ time.
- **Store all positions:** A prefix-sum array works but uses $O(N)$ space even though only the current sum and return count are needed.
- **Boundary crossing:** Moving from a positive coordinate to a negative one does not count unless the final coordinate is exactly zero.
- **Initial position:** The ant begins on the boundary, but that state is not counted because no movement has completed.
- **Repeated returns:** Each distinct completed movement ending at zero contributes one, even when the ant has returned before.
- **One movement:** A legal movement is nonzero, so an input of length one can never produce a return.
