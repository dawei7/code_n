## General

**The robot's full state includes direction**

Knowing only the robot's cell is insufficient. From the same cell, facing right and facing down lead to different next actions.

The source represents a state as `(i,j,k)`, where `i,j` is the position and `k` is one of four direction indices. `dirs = (0,1,0,-1,0)` encodes right, down, left, and up as adjacent coordinate pairs.

A repeated full state means every future action will repeat forever, so simulation can stop.

**Mark directional states to detect the eventual cycle**

At the beginning of `dfs`, the source checks whether `(i,j,k)` is already in `vis`. If so, it returns without further recursion.

The room and direction choices are deterministic. Once the same position and facing direction recur, the robot will follow the identical infinite suffix of movements and turns. No new cell can be cleaned after that point.

There are at most four states per cell, so indefinite physical running becomes a finite state traversal.

**Count a cell only on its first visit**

The source adds `room[i][j] == 0` to `ans`. Python treats the Boolean as one for an uncleaned empty cell and zero otherwise.

It then writes `room[i][j] = -1`. Later visits to that cell do not increment the answer because negative one differs from zero.

Objects remain value one and are never entered. Thus the matrix itself doubles as the cleaned-cell marker.

**Move forward when possible**

For direction `k`, the prospective cell is

`x = i + dirs[k]` and `y = j + dirs[k+1]`.

The robot moves there when it is within row and column bounds and `room[x][y] != 1`. Both original empty cells zero and already cleaned cells negative one are traversable.

The recursive call keeps the same direction because the robot continues straight after a successful move.

**Turn clockwise when blocked**

If the forward square is outside the room or contains an object, the robot stays at `(i,j)` and calls `dfs(i,j,(k+1)%4)`.

The direction order right, down, left, up makes adding one a clockwise turn. Modulo four wraps up back to right.

Turning itself does not clean a new space, but it creates a different directional state at the same cell and must be recorded for correct cycle detection.

**Trace a trapped starting cell**

If objects or boundaries block every direction at `(0,0)`, the first call counts that cell and marks it cleaned.

Four blocked transitions rotate through directions one, two, three, and zero. When `(0,0,0)` is reached again, the visited-state check terminates simulation. The answer remains one.

**Why visited cells and visited states serve different purposes**

The negative-one cell marker answers, “Has this space already contributed to the clean count?”

The `vis` set answers, “Has the robot already been at this space facing this direction?” A cell may be revisited from several directions before behavior cycles, so using only one of these structures for both roles would be incorrect.

**Why the simulation counts exactly the cleaned spaces**

Every time the robot enters an originally empty cell for the first time, its matrix value is zero and the answer increases once. The cell is then marked, preventing duplicate counting.

The recursion implements exactly the deterministic forward-or-turn rule. It stops only at a repeated full state, after which the future trajectory is periodic and cannot reach an unvisited state or cell. Therefore every cell the infinite run ever visits has been counted exactly once.

**Mutation of the input matrix**

The exact source overwrites every cleaned zero with negative one. The returned count is correct, but the caller's `room` matrix no longer contains its original binary values.

A separate cleaned set would preserve the input but use additional storage; `vis` is needed either way for directional states.

**Recursion depth in Python**

Although the state space is finite, a path can visit many of the at most `4mn` states before repeating. With dimensions up to 300 by 300, recursive depth can greatly exceed Python's default recursion limit.

The algorithmic idea is linear, but an iterative loop is safer for the full constraint range. The exact protected source retains the recursive implementation.

## Complexity detail

Let $M$ and $N$ be room dimensions. At most $4MN$ position-direction states are entered, and each performs constant work. Time is $O(MN)$.

The visited set stores up to $4MN$ states, so explicit auxiliary space is $O(MN)$. Recursion can also grow to $O(MN)$ depth. The room matrix itself is reused for cleaned-cell marking rather than allocating another cell set.

## Alternatives and edge cases

- **Iterative simulation:** Use a loop until a state repeats, avoiding recursion-limit failure with the same $O(MN)$ bounds.
- **Separate cleaned set:** Preserves `room` but adds another $O(MN)$ structure.
- **Visited cell only:** Insufficient because direction changes future behavior.
- **Starting cell:** Always empty and is counted immediately.
- **Previously cleaned cell:** Remains traversable but contributes zero on revisit.
- **Object cell:** Never entered and remains value one.
- **Boundary:** Treated exactly like a blocked forward cell and causes a clockwise turn.
- **Four consecutive blocks:** Return to the same directional state and terminate.
- **Open rectangular room:** The robot may cycle around a boundary without cleaning every interior cell.
- **Repeated full state:** Proves the future is periodic.
- **Input mutation:** Cleaned spaces are changed from zero to negative one.
- **Recursion risk:** A long state path can raise `RecursionError` under default Python limits.
