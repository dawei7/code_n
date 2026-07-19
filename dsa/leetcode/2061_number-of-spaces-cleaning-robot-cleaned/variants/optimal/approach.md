## General
**Direction is part of the deterministic state**

Represent direction by an index into right, down, left, and up step vectors. From `(row, column, direction)`, the rules determine exactly one next state: turn clockwise in place when blocked, or move forward otherwise. A repeated complete state therefore proves that every future state will repeat as well.

**Separating visited states from cleaned cells**

Maintain one set of complete states for cycle detection and another set of positions for the answer. At each new state, add the current position to the cleaned set, then apply the movement rule. Stop when the current state has already appeared and return the number of cleaned positions.

There are only four possible directions per cell. The simulation follows the unique path through this finite state graph until it repeats; every state before that repetition is exactly the nonrepeating prefix and cycle the robot reaches. Consequently, every position the infinite run can visit has already been recorded.

## Complexity detail
At most $4mn$ complete states exist, and each simulation step performs constant work, giving $O(mn)$ time. The state and cleaned-position sets contain at most $4mn$ and $mn$ entries, respectively, for $O(mn)$ space.

## Alternatives and edge cases
- **Mutate the room to mark cells:** This can count cleaned positions, but position-only marks cannot detect a motion cycle because revisiting a cell from another direction may lead elsewhere.
- **List-based state history:** Linear search detects the same repeated state correctly but can require $O((mn)^2)$ time.
- Turning does not clean a new cell, though it creates a different state at the same position.
- An open room does not imply every cell is cleaned; an empty square room leaves interior cells untouched.
- A one-cell room cycles through four directions and cleans exactly one space.
