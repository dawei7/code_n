## General
**Represent the four headings:** Encode north, east, south, and west cyclically and associate them with displacement vectors $(0,1)$, $(1,0)$, $(0,-1)$, and $(-1,0)$. A `"G"` instruction adds the current vector to the coordinates. Turning left or right changes only the direction index modulo four.

**Inspect one complete instruction cycle:** Simulate `instructions` once from the initial state. The resulting position is the displacement contributed by one cycle, while the resulting heading tells how that displacement will be rotated during later cycles.

**Classify the repeated transformation:** If the robot returns to $(0,0)$ after one cycle, every repetition begins at that point up to its heading and the path is bounded. If it ends with a heading other than north, repeating the sequence rotates the cycle displacement. A quarter-turn has order four and a half-turn has order two, so the rotated displacement vectors cancel after at most four cycles; the robot returns to the origin and repeats a finite route.

The only unbounded case is therefore a nonzero final displacement while still facing north. Then every cycle has the same orientation and adds the same nonzero displacement vector, so the robot's distance from the origin grows without limit. Thus the path is bounded exactly when the final position is the origin or the final heading is not north.

## Complexity detail
The simulation visits each of the $M$ instructions once, taking $O(M)$ time. It stores two coordinates, one direction index, and a fixed four-entry direction table, so its space usage is $O(1)$.

## Alternatives and edge cases
- **Simulate four cycles:** Four repetitions restore any heading and reveal whether the robot returns to the origin. This remains $O(M)$ time but performs unnecessary repeated work.
- **Simulate until a state repeats:** Tracking every position and direction can detect a cycle, but unbounded paths never repeat and require an arbitrary stopping rule.
- **Repeat a full simulation for every character:** Recomputing the same one-cycle state $M$ times remains correct but takes $O(M^2)$ time.
- **Turns only:** A string containing no `"G"` never leaves the origin and is bounded regardless of its final heading.
- **Return to the origin:** A zero one-cycle displacement is sufficient even when the final direction differs from north.
- **Same heading with displacement:** Ending north away from the origin is always unbounded; the displacement need not itself point north.
- **Single instruction:** `"G"` is unbounded, whereas `"L"` and `"R"` are bounded.
