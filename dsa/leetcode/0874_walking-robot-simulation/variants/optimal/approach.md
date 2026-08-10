## General

The robot's future behavior is completely determined by three pieces of state: its current coordinate $(x,y)$, the direction it faces, and the next command. Because commands must be executed in order and obstacles can stop a movement partway through, direct simulation is the natural optimal approach.

The only potential performance trap is obstacle lookup. Before processing commands, the solution converts every obstacle coordinate into a tuple and stores the tuples in a set:

```text
s = {(x, y) for x, y in obstacles}
```

Membership testing such as `(nx, ny) in s` then takes $O(1)$ expected time. Scanning the whole obstacle list before every attempted unit step would be much slower.

**Encode four directions with one flat tuple.** The tuple `dirs = (0, 1, 0, -1, 0)` contains overlapping coordinate pairs:

- index 0 gives `(dirs[0], dirs[1]) = (0, 1)`, north;
- index 1 gives `(1, 0)`, east;
- index 2 gives `(0, -1)`, south;
- index 3 gives `(-1, 0)`, west.

The direction index `k` begins at zero because the robot initially faces north. A right turn advances one position around the cyclic order, so `k = (k + 1) % 4`. A left turn moves back one position, equivalently forward three positions, so `k = (k + 3) % 4`. Modulo four wraps the index after west or before north.

Turns change only `k`. They do not move the robot and therefore cannot change its distance from the origin.

**Movement must be simulated one unit at a time.** For a positive command `c`, the solution repeats up to `c` times. It first computes the proposed next coordinate:

```text
nx = x + dirs[k]
ny = y + dirs[k + 1]
```

If that coordinate is an obstacle, the loop breaks immediately. The robot remains at its current coordinate, which is the square adjacent to the obstacle, and processing continues with the next command. Otherwise, the proposed coordinate becomes the current coordinate.

It would be incorrect to jump directly by `c` units and test only the endpoint. An obstacle can lie anywhere between the start and endpoint. The command explicitly moves one unit at a time and stops at the first blocked next square.

**Update the maximum after every successful step.** At each visited coordinate, squared Euclidean distance is

$$
x^2+y^2.
$$

The solution computes `x * x + y * y` and maximizes `ans`. It does not take a square root because the requested result is already the squared distance. Avoiding the square root also keeps the computation exact and preserves distance order: for nonnegative distances, the point with the largest squared distance is also the point with the largest distance.

Updating after each unit step is the most direct way to satisfy “at any point in its path.” A later command may bring the robot closer to the origin, so returning only the final distance would be wrong. In a straight unobstructed segment, squared distance is not guaranteed to change monotonically if the robot travels toward and then past the origin, which further supports checking every reached point.

**Why the simulation exactly matches the rules.** Before the first command, $(x,y)=(0,0)$ and $k=0$, matching the initial state. Assume the stored state is correct before some command. For a turn, the modular update chooses exactly the direction 90 degrees left or right and preserves position. For a movement, each inner iteration tests precisely the next square in the current direction. A blocked square ends the command without entering it; a free square advances exactly one unit. By induction over the attempted units and then over commands, the stored state equals the robot's real state throughout the journey.

Because `ans` is compared with the squared distance after every successful move and begins at zero for the starting position, it is the maximum over all visited coordinates when simulation ends.

**Obstacle at the origin.** The robot starts at $(0,0)$ even if that coordinate is listed as blocked. The solution does not inspect the current square; it inspects only a proposed next square. Therefore it can move away from the origin normally. If it later attempts to return, $(0,0)$ is then the next proposed coordinate, membership succeeds, and movement stops just outside it. This exactly matches the special note.

For commands `[4,-1,4,-2,4]` with obstacle $(2,4)$, the robot first reaches $(0,4)$. After turning east, it enters $(1,4)$, then detects that $(2,4)$ is blocked and ends that movement command. Turning left faces north, and four more free steps reach $(1,8)$. The stored maximum becomes $1^2+8^2=65$.

## Complexity detail

Let $n$ be the number of commands, $b$ the number of obstacles, and

$$
S=\sum_{\substack{c\in\texttt{commands}\\c>0}} c
$$

be the total number of requested forward unit steps. Building the obstacle set takes $O(b)$ expected time. Each command is inspected once, and at most $S$ unit moves are attempted.

- **Time complexity:** $O(n+b+S)$ expected.
- **Space complexity:** $O(b)$ for the obstacle set. Direction and simulation state use constant space.

Because every positive command is at most 9, $S\le 9n$ and the time can also be simplified to $O(n+b)$ under the stated constraints. The manifest retains $S$ to describe the direct amount of simulated movement.

## Alternatives and edge cases

- **Scan all obstacles for every step:** This can cost $O(bS)$ and is unnecessary; the coordinate set gives expected constant-time membership.
- **Jump directly to a command endpoint:** This misses obstacles between the current position and endpoint and violates the one-unit-at-a-time rule.
- **Group obstacles by row and column:** Sorted coordinate maps plus binary search can jump across long distances efficiently in a generalized problem with huge commands. Here each command is at most nine, so unit simulation is simpler and already optimal.
- **Encode coordinates as one integer:** A collision-free numeric encoding can replace tuple keys. Python tuple hashing is direct and avoids choosing a multiplier based on coordinate bounds.
- **Final distance only:** The robot may later move closer to the origin, so the maximum must be maintained throughout the path.
- **Obstacle immediately ahead:** The inner loop breaks before changing `x` or `y`, and the rest of that movement command is discarded.
- **Multiple obstacles in one direction:** Only the first encountered one matters for that command; stepwise checking naturally finds it.
- **Repeated turns:** Modular direction updates handle any sequence of left and right commands without special cases.
- **Negative coordinates:** Tuple membership and squaring work identically in every quadrant.
- **Obstacle at the origin:** It is ignored while the robot initially occupies the origin but blocks a later attempted return because only next positions are tested.
- **No obstacles:** Every requested step succeeds, and the set remains empty.
- **Maximum at an intermediate step:** Updating after each successful unit captures a maximum that occurs before the end of a command or before later commands reverse direction.
- **Blocked movement and distance:** When the first attempted step is blocked, position and distance do not change, so no additional maximum update is needed.
- **Squared distance bound:** Python integers do not overflow, and the problem guarantees the returned answer is below $2^{31}$.
