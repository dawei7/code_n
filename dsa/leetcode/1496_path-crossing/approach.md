## General

**Representing the walk with coordinates**

The walk begins at the origin. The stored solution uses two integers, `i` and `j`, to represent the current grid location. Here `i` acts like a row coordinate and `j` like a column coordinate:

- North decreases `i` by one.
- South increases `i` by one.
- East increases `j` by one.
- West decreases `j` by one.

Using north as negative rather than positive does not change the geometry. It merely chooses screen-style row coordinates instead of a conventional upward-positive Cartesian y-axis. Opposite directions still cancel each other, every instruction moves exactly one unit, and equal coordinate pairs still mean equal physical locations.

The code uses Python structural pattern matching to translate each path character into one coordinate update. The input contract guarantees that every character is one of the four listed directions, so no default case is needed.

**Why a set detects crossing**

The set `vis` contains every coordinate occupied so far. It is initialized as `{(0, 0)}` before any instruction is processed because the starting location counts as visited. This detail is essential: a path that leaves the origin and later returns to it crosses itself even if no post-move location was repeated before that return.

After applying one movement, the code checks `if (i, j) in vis`. If the pair is present, the walk has arrived at a location occupied at an earlier time, which is exactly the definition of crossing in this problem. It returns true immediately because later instructions cannot undo the fact that a crossing already occurred.

If the new coordinate has not appeared, `vis.add((i, j))` records it before the next move. When the loop completes without a repeated pair, the method returns false.

Python tuples are immutable and hashable, so a coordinate tuple can be stored directly in a set. The set compares both components, distinguishing positions that share only one coordinate.

**The invariant after every instruction**

After processing any prefix of the path without returning, two facts hold:

1. `(i, j)` is the location reached by executing exactly that prefix.
2. `vis` contains precisely the origin and every location reached after each move in that prefix, with no duplicates.

Both facts are true before the loop: the empty prefix ends at the origin and the set contains only the origin. For the next character, the matching case applies the correct unit displacement, so the coordinate becomes the endpoint of the extended prefix.

If that endpoint is already in `vis`, the algorithm correctly reports a crossing. Otherwise, inserting it preserves the exact visited-location set and its uniqueness. This induction covers the entire path.

**Why repeated coordinates are enough**

The path consists of horizontal or vertical unit segments whose endpoints have integer coordinates. Under the problem's definition, crossing means being at a previously visited location at some time. Each discrete instruction takes the walker from one lattice point to an adjacent lattice point, and every location at an instruction boundary is checked.

Two such unit grid edges cannot create an unnoticed proper crossing halfway through both edges: a horizontal unit segment and a vertical unit segment intersect, if at all, at an integer endpoint. Retracing an edge in reverse also first arrives at a previously visited endpoint. Therefore, checking the sequence of reached coordinate points captures every crossing relevant to this unit-step walk.

For `NESWW`, the coordinates evolve from the origin to north, then northeast, then southeast, then east of the origin, and finally back to the origin. Because the origin was inserted before the loop, the final membership test returns true.

**Why no full path geometry is stored**

The answer depends only on whether a location has appeared, not on when it appeared or which direction first reached it. A hash set is therefore sufficient. A list would preserve unnecessary order and require a linear search for every new coordinate.

The source does not modify `path` and stores no per-step direction history. Its state is exactly the current coordinate plus the membership set.

## Complexity detail

Let $N$ be the path length. Each character is processed once. Direction matching, integer updates, tuple construction, expected set membership, and expected set insertion take constant time, giving expected $O(N)$ total time.

If the path never crosses, it visits $N+1$ distinct coordinates including the origin, so the set uses $O(N)$ space. If a crossing occurs early, the method returns with less storage, but worst-case space remains $O(N)$.

Hash-set operations are expected constant time. A theoretical adversarial collision model can worsen lookup behavior, but coordinate tuples of bounded integers use Python's normal hashing and the standard analysis is appropriate. Coordinate magnitude is at most $N$ in either direction.

## Alternatives and edge cases

- **List of visited coordinates:** It is correct but membership is linear, causing $O(N^2)$ worst-case time.
- **Boolean grid:** An offset grid can give direct lookup, but a square covering all possible coordinates consumes $O(N^2)$ space even though the path visits only $O(N)$ locations.
- **Complex-number coordinates:** Directions can be mapped to complex displacements and positions stored in a set. It is concise but may be less beginner-friendly than integer pairs.
- **Return to origin:** This is detected only because the origin is inserted before processing the first move.
- **Immediate reversal:** Paths such as `NS` revisit the origin on the second step and return true.
- **Repeated edge:** Traversing an old edge in reverse necessarily revisits its endpoint, so the set detects it.
- **Straight path:** Every coordinate is new, and the method returns false after the loop.
- **North sign convention:** Decreasing the first coordinate is arbitrary but consistent; crossing detection depends on equality, not orientation.
- **Single instruction:** It reaches one new neighboring point and cannot cross under the valid-direction contract.
- **Invalid direction character:** The match would make no movement and could cause a false repeat, but such characters are explicitly excluded.
- **Python version:** The `match` statement requires Python 3.10 or newer.
