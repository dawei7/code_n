## General
**Encode direction and obstacles for constant-time updates**

Store the four direction vectors in clockwise order: north, east, south, and west. A right turn increments the direction index modulo four, while a left turn decrements it modulo four. Convert every obstacle pair to a tuple in a hash set so each proposed point can be checked in expected constant time.

**Simulate every unit because every intermediate point matters**

For a positive command, compute the next point one unit in the current direction. If it belongs to the obstacle set, stop processing that command; otherwise, assign the new coordinates and update the maximum with $x^2+y^2$. Checking one unit at a time is necessary both because an obstacle can interrupt a longer command and because the requested maximum may occur before the final command.

The maintained coordinates are exactly the robot's position after each processed instruction: turns change only the direction, successful unit moves enter the requested adjacent point, and a blocked candidate ends that movement command without changing position. Since the squared distance is inspected after every reachable point, the recorded maximum is precisely the required result. Keeping `(0, 0)` in the obstacle set naturally permits the initial state but blocks any later proposed move into it.

## Complexity detail
Building the obstacle set takes $O(b)$ time and space. The command loop handles $n$ instructions and attempts at most $S$ unit moves, each with expected $O(1)$ hash lookup, for $O(n+b+S)$ total time. Apart from the obstacle set and a constant amount of simulation state, no additional storage is needed, so auxiliary space is $O(b)$.

## Alternatives and edge cases
- **Scan the obstacle array for every step:** This preserves the simulation but can take $O(Sb)$ time; hashing removes the repeated linear membership search.
- **Jump directly by each positive command:** A direct endpoint update can pass through an obstacle and therefore violates the one-unit-at-a-time rule.
- **Group obstacles by row or column:** Sorted coordinate maps can jump to the nearest blocker and may reduce work for very large command distances, but commands here are at most `9` and the extra machinery is unnecessary.
- **Obstacle at the origin:** Starting on `(0, 0)` is allowed, but after leaving, a proposed return to that point is blocked.
- **Blocked first unit:** The robot does not move for the remainder of that positive command and proceeds to the following instruction.
- **Turns only:** The position never changes, so the answer remains `0`.
- **Path returns toward the origin:** The answer is a maximum over the whole path and must not be replaced by the final squared distance.
