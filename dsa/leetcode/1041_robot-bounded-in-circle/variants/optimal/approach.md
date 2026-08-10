## General

**One execution tells us the repeated behavior**

The instruction string repeats forever, but it is unnecessary to simulate forever. After one complete execution, only two facts matter:

- The robot's displacement from where that execution began.
- The direction the robot now faces relative to its starting direction.

If the displacement is zero, the robot is back at the same position after one cycle. Repeating the same finite path remains bounded, regardless of its ending direction.

If the displacement is nonzero but the ending direction has rotated, later cycles rotate that displacement. The rotated vectors cancel after at most four repetitions.

The only unbounded case is nonzero displacement while still facing the original direction. Every repetition then adds the same translation and carries the robot farther away along a straight sequence of cycle endpoints.

**Direction encoding in the exact solution**

The code uses:

- `k = 0` for north.
- `k = 1` for west.
- `k = 2` for south.
- `k = 3` for east.

This order moves counterclockwise as the index increases.

A left turn therefore uses `k = (k + 1) % 4`. From north it goes to west, and from east index three it wraps to north.

A right turn is one step clockwise, equivalent to three steps counterclockwise, so it uses `k = (k + 3) % 4`. Modulo keeps the direction inside zero through three.

The encoding differs from the common north-east-south-west order, but it is internally consistent.

**Count movement by direction instead of storing coordinates**

`dist` contains four counters. Each `G` increments `dist[k]` for the direction currently faced.

After the whole string:

- Net vertical displacement is `dist[0] - dist[2]` because north and south oppose each other.
- Net horizontal displacement is `dist[3] - dist[1]` because east and west oppose each other.

The robot returns to the starting position exactly when north steps equal south steps and west steps equal east steps:

`dist[0] == dist[2] and dist[1] == dist[3]`.

Actual `x` and `y` coordinates are unnecessary because only a zero-versus-nonzero displacement test is needed.

**Why an origin return is bounded**

If opposite-direction counts balance, one instruction cycle ends at the position where it began. During that cycle, the robot visits only finitely many points.

The next repetition may begin with a different orientation, but it still traces a rotated version of a finite path from the same cycle endpoint. There are only four possible orientations. The union of at most four rotated finite paths fits inside some circle.

In fact, even without analyzing orientation, the repeated cycle endpoints remain at the same location whenever the net displacement for the executed orientation is zero. Rotation preserves a zero vector.

**Why a changed direction is bounded**

Suppose one cycle causes displacement vector `v` and rotates orientation by 90, 180, or 270 degrees.

If the rotation is 180 degrees, the second cycle contributes rotated displacement `-v`. The two cycle displacements sum to zero, so the robot returns to its cycle-start position after two repetitions.

If the rotation is 90 or 270 degrees, four repetitions contribute the four quarter-turn rotations of `v`. Their sum is zero:

$$
v+R(v)+R^2(v)+R^3(v)=0.
$$

After at most four cycles, both position and orientation repeat. The entire future trajectory is periodic and therefore bounded.

This is why `k != 0` alone is enough, even when the first cycle ends far from the origin.

**Why unchanged direction plus displacement diverges**

If `k == 0`, the robot ends facing north, its original orientation. Every later cycle is executed in exactly the same global orientation and contributes the same displacement vector `v`.

After `q` cycles, the endpoint is `qv`. If `v` is nonzero, its distance from the origin grows proportionally with `q`. No fixed circle can contain all endpoints, so the trajectory is unbounded.

The return condition rejects exactly this case: opposite step counts do not balance, and `k` remains zero.

**Trace `"GGLLGG"`**

Start with `k = 0`, north. Two `G` instructions make `dist[0] = 2`.

Two left turns change `k` from zero to one and then two, so the robot faces south.

The final two `G` instructions make `dist[2] = 2`. North and south counts are equal; east and west counts are both zero. The displacement is zero, so the method returns true even though final direction `k = 2` also independently indicates boundedness.

**Trace `"GG"`**

Both moves are north. `dist[0] = 2` while `dist[2] = 0`, so displacement is nonzero. There is no turn, so `k = 0`.

Both boundedness conditions fail. Every repetition moves two more units north, and the method returns false.

**Trace `"GL"`**

The `G` contributes one north step. The left turn changes `k` to one, meaning west. The first-cycle displacement is nonzero, but the final direction is not north.

Repeating the instructions rotates the step direction through west, south, and east. Four moves form a square and return to the origin. `k != 0` correctly returns true after examining only the first cycle.

**Why turns do not enter `dist`**

Turning changes orientation but not position. Recording only `G` counts is sufficient for displacement, while `k` separately remembers net rotation. These two pieces form a complete summary of the one-cycle transformation.


The method returns true if the one-cycle displacement is zero or the one-cycle rotation is nonzero. In the first case, cycle positions repeat. In the second, rotated displacements cancel within at most four cycles. Both yield a periodic bounded trajectory.

If it returns false, displacement is nonzero and rotation is zero. Identical nonzero translations accumulate forever, so the robot escapes every circle. The condition is therefore necessary and sufficient.

## Complexity detail

Let `M = len(instructions)`. The loop reads every instruction once and performs constant work. Time complexity is `O(M)`, matching the manifest.

The four-element `dist` list and direction index `k` have fixed size independent of `M`. Auxiliary space is `O(1)`.

No repeated-cycle simulation or trajectory history is stored. The proof compresses infinite behavior into one pass and five integers.

## Alternatives and edge cases

- **Track explicit coordinates:** Use a four-direction vector array and update `x` and `y` on each `G`. This is equally correct; the exact solution's opposite-direction counts encode only the zero-displacement information needed.
- **Simulate four cycles:** After four repetitions, any changed orientation returns to north, and a bounded path returns to its starting state. This works in `O(M)` time with a larger constant but is unnecessary.
- **Search for repeated states indefinitely:** Position is unbounded in the false case, so open-ended simulation has no useful stopping rule. The one-cycle theorem supplies one.
- **Only `G` instructions:** Final direction remains north. The nonzero north displacement makes every nonempty such string unbounded.
- **Only turns:** All distance counters remain zero, so the robot stays at the origin and returns true.
- **Net rotation 180 degrees:** Two cycle displacement vectors cancel, so boundedness is detected by `k != 0`.
- **Net rotation 90 or 270 degrees:** Four rotated displacement vectors cancel.
- **Return to origin facing north:** The first condition returns true; every repetition traces exactly the same path.
- **Return to origin facing another direction:** It is still bounded, and both conditions may be true.
- **Nonzero displacement facing north:** This is the unique false case and causes linear drift.
- **Different direction index conventions:** North-east-south-west would use different left and right updates. The exact counter interpretation must stay aligned with north-west-south-east.
- **Modulo wraparound:** Four left or four right turns restore `k = 0`, correctly representing a full rotation.
- **Finite within-cycle excursions:** Even if one cycle travels far before returning or rotating, the instruction string has finite length. Periodic repetition still fits inside a sufficiently large circle.
