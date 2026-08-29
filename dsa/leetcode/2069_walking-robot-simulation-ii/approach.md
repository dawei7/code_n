## General

**The robot always follows the perimeter**

Starting at the bottom-left corner facing east, the robot moves along the bottom edge, then the right edge, then the top edge, then the left edge, and repeats.

It never enters an interior cell because a turn occurs only when forward movement would leave the rectangle. The complete state can therefore be represented by one distance around this perimeter cycle.

**Measure the side lengths in steps**

`mx = width - 1` is the number of horizontal steps between the left and right edges. `my = height - 1` is the vertical step count.

One full circuit uses

`p = 2 * mx + 2 * my`

steps. With width and height at least two, this perimeter length is positive.

**Accumulate steps modulo the perimeter**

`cur` is the robot's distance along the cycle from the origin. `step(num)` performs

`cur = (cur + num) % p`.

Moving a full multiple of the perimeter returns to the same cell and post-movement direction, so discarding whole cycles is valid. Each call takes constant time even when `num` is large.

Successive calls compose naturally because each begins from the current cycle distance.

**Map the first segment to the bottom edge**

For `0 <= d <= mx`, the robot is at `[d,0]`.

At distance zero this is the origin. At distance `mx` it is the bottom-right corner. The direction after reaching that corner is still east, because the robot turns only when it attempts the next step.

**Map the second segment to the right edge**

For `mx < d <= mx+my`, the robot has completed the bottom edge and moved upward by `d-mx` steps.

Its position is `[mx,d-mx]` and its direction is north.

The strict lower bound prevents the bottom-right corner from being assigned to the north segment before the robot has attempted another step.

**Map the top and left segments**

For `mx+my < d <= 2*mx+my`, the robot moves west along the top edge. The horizontal coordinate decreases by the distance beyond the top-right corner.

Remaining cycle positions lie on the left edge moving south, with position

`[0, my - (d - (2*mx+my))]`.

The cycle never stores `d=p` because modulo converts it to zero.

**Handle direction at the origin carefully**

Before any movement, the robot is at the origin facing east. After one or more complete perimeter circuits, it is again at the origin but its last successful step was south, so it faces south.

Position alone cannot distinguish these states. Boolean `moved` begins false and becomes true on every `step` call.

`getDir` returns east when movement has never occurred. Otherwise, distance zero falls through to the south case, giving the correct post-cycle direction.

**Why corners belong to the incoming side**

At bottom-right after exactly `mx` steps, the last move was east. The turn north happens only as part of the next requested step.

The same rule makes the top-right corner north-facing and the top-left corner west-facing. The interval boundaries in `getDir` encode these incoming directions exactly.

Direction describes where the robot is currently facing after completing the requested steps, not the direction it would use after resolving a future blocked attempt. At a corner, no turn has occurred until another step is requested. This timing is why assigning the corner to the outgoing side too early would be incorrect.

**Trace a full cycle**

If `num=p` on the first movement call, `cur` returns to zero and `moved` becomes true. `getPos` returns `[0,0]` while `getDir` returns south.

This differs intentionally from a newly constructed robot, which has the same position but faces east.

**Why the arithmetic simulation is correct**

Each integer cycle distance corresponds to exactly one successful perimeter step state. The four position formulas partition all distances from zero through `p-1` without gaps.

Adding requested steps modulo `p` reaches the same state as performing each forward move and boundary turn individually. The moved flag resolves the only duplicate-position direction ambiguity at the initial origin.

The accessors do not advance or turn the robot. Repeated `getPos` or `getDir` calls return the same state until `step` changes `cur`. This matches the class contract that the robot stops and waits after each movement instruction.

**Why modulo preserves direction as well as position**

After a full perimeter circuit, every side and corner transition has occurred once, and the robot returns to the origin from the north while moving south. Beginning another circuit requires the same next blocked attempt and eastward movement as before.

Thus states after positive movement repeat with period `p`, including direction. The special unmoved state is the only exception and is handled separately.

## Complexity detail

Construction stores five scalar fields and runs in $O(1)$ time. Each `step`, `getPos`, and `getDir` call performs a fixed number of arithmetic operations and comparisons, so each is $O(1)$.

Across $Q$ calls, total time is $O(Q)$. The object uses $O(1)$ space; unlike a precomputed-cycle solution, it stores no perimeter array.

## Alternatives and edge cases

- **Precompute every perimeter state:** Makes queries constant time but uses $O(width+height)$ space.
- **Simulate one step at a time:** Can cost $O(num)$ per call and is unnecessary.
- **No movement yet:** Origin direction is east.
- **Complete positive cycle:** Origin direction is south.
- **Bottom-right corner:** Faces east until another step triggers the turn.
- **Top-right corner:** Faces north.
- **Top-left corner:** Faces west.
- **Large `num`:** Modulo removes complete circuits safely.
- **Several step calls:** Modular distances accumulate exactly.
- **Minimum two-by-two grid:** All four perimeter cells and corner directions remain covered.
- **Position return:** A new two-element list is produced each time.
- **No interior cells:** Boundary-turn rules keep the robot on the perimeter forever.
