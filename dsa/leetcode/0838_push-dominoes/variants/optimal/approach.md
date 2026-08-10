## General

**Model time explicitly with a multi-source breadth-first search**

Every initially pushed domino begins falling at time zero. Its force moves one position per second in its direction. Because all initial pushes act simultaneously, the natural simulation starts from all `L` and `R` positions at once and expands them in increasing time order.

The queue `q` contains domino indices whose arriving forces are ready to process. Array `time` records the earliest second at which any force reaches each index; `-1` means no force has arrived.

Dictionary `force` stores the force or forces arriving at an index at that earliest time.

**Initialize every source**

For each non-dot character:

- append its index to `q`;
- set `time[i] = 0`;
- append `L` or `R` to `force[i]`.

All source indices enter the queue before propagation begins. This is what makes the search multi-source and preserves simultaneity.

The answer list starts as all dots. A position changes only when exactly one earliest force controls it.

**Process only an unopposed force**

When index `i` is removed from the queue, the code checks `len(force[i]) == 1`.

If exactly one force arrived at the earliest time, the domino falls in that direction. The code writes that character into `ans[i]` and computes the next index:

- `i-1` for `L`;
- `i+1` for `R`.

If two opposite forces arrived simultaneously, the length is two. The domino remains upright because forces balance, and it does not propagate either force farther. Leaving `ans[i]` as `.` and skipping expansion models both effects.

**Record the first arrival**

Suppose the force at `i` arrived at time `t = time[i]` and moves toward in-bounds neighbor `j`.

If `time[j] == -1`, no force has reached `j` yet. The algorithm:

- records arrival time `t+1`;
- appends the force direction;
- enqueues `j`.

This first arrival may eventually make `j` fall unless an opposing force reaches it at the same time.

**Combine equal-time arrivals**

If `time[j] == t+1`, another path has already scheduled a force for exactly the same second. The new force is appended to `force[j]`.

BFS queue order guarantees that all positions at time `t` are processed before a time-`t+1` position is popped. Therefore, every equal-time force is collected before `j` makes its falling decision.

If `time[j] < t+1`, an earlier force already reached and determined `j`. The later force has no effect and is ignored, matching the rule that a falling or fallen domino receives no additional effective force.

**Why same-direction duplicate arrivals are not a problem**

On a one-dimensional line, an `L` force can reach a position only from its right, and an `R` force only from its left. Two distinct sources cannot send the same direction into one position at the same earliest time along different paths because there is only one path from each side. A two-force list therefore represents the meaningful collision of opposite directions.

**Trace a collision**

Consider `"R...L"`. At time zero, the endpoints are sources.

- At time one, the R force reaches index 1 and the L force reaches index 3.
- At time two, both try to reach index 2.

The first processed parent schedules index 2 at time two. The second sees the same scheduled time and appends its opposite force. When index 2 is popped, its force list has length two, so it remains upright and sends nothing onward. The final pattern is `"RR.LL"`.

For `"R..L"`, the two middle positions are reached at time one from opposite sides but at different indices. They fall toward each other, yielding `"RRLL"`. There is no single central domino on which the forces can balance.

**Why barriers emerge naturally**

In `"R.L"`, the initially pushed L at the right and R at the left both reach the middle dot simultaneously, so it stays upright. In `"RR.L"`, the already pushed R immediately before the dot is falling right, while L is on the far side of an existing dot pattern; timing and earliest-arrival rules determine whether a collision occurs.

An initially pushed domino already has time zero. A later incoming force has a larger arrival time and is ignored, implementing the statement that a falling domino does not gain a new effect from another falling domino.

**Why the final state is correct**

BFS processes forces in nondecreasing arrival time. The first arrival time at a domino is therefore minimal. A unique force at that time makes the domino fall and sends the same force one step onward one second later. Opposite forces at that same minimal time cancel and stop.

Later forces cannot change a domino already falling or fallen. These are exactly the physical rules in the statement. Because every in-bounds propagation is scheduled and every source starts at time zero, the joined answer represents the final state of the entire line.

## Complexity detail

Let `n = len(dominoes)`. Each index is enqueued at most once, when its earliest arrival time is assigned. Processing an index and checking or appending forces takes constant time. Propagation examines at most one neighbor because a force moves in only one direction. Total time is `O(n)`.

The queue, `time` array, `ans` list, and force dictionary collectively store `O(n)` information. Each position receives at most the relevant earliest forces, bounded by a constant. Total space is `O(n)`.

Joining the `ans` list into the returned immutable string also takes `O(n)` time and creates an `O(n)` result.

## Alternatives and edge cases

- **Segment analysis between non-dot symbols:** Add virtual boundary symbols and resolve `L...L`, `R...R`, `L...R`, and `R...L` intervals directly. It is also linear and uses less explicit simulation state.

- **Net-force accumulation:** Sweep left-to-right for R influence and right-to-left for L influence, then compare magnitudes. This is linear but encodes timing less directly.

- **Second-by-second whole-string simulation:** Repeatedly updating all positions can require `O(n^2)` time before a long chain settles.

- **All dots:** The source queue is empty, so every answer position stays upright.

- **All initially pushed:** Each source has time zero and retains its given direction.

- **One domino:** It stays dot if unpushed or preserves its initial L/R state.

- **Force leaving the line:** The bounds check discards it, as there is no domino beyond the edge.

- **Simultaneous opposite arrivals:** Both are stored at the same earliest time, the domino remains dot, and propagation stops.

- **Later opposite arrival:** It is ignored because the domino was already reached earlier.

- **Outward-facing pair `L...R`:** Forces move away from the middle interval, so its dots remain upright.

- **Inward-facing pair `R...L` with odd gap:** The center receives equal-time forces and remains upright.

- **Inward-facing pair with even gap:** No single center exists; the left half falls right and the right half falls left.

- **Input immutability:** The source string is read, while all simulation state lives in new arrays and collections.
