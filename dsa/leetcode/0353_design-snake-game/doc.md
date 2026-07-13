# Design Snake Game

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 353 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Design, Queue, Simulation |
| Official Link | [LeetCode](https://leetcode.com/problems/design-snake-game/) |

## Problem Description
### Goal
Simulate a snake beginning at the board's top-left cell on a `height x width` grid. Each `U`, `D`, `L`, or `R` move advances the head one cell. Food appears in the supplied order, and only the next food item can be consumed when the head reaches its coordinate.

Eating food increases the score and leaves the tail in place, growing the snake. Otherwise the tail advances, so moving into the cell it vacates is allowed. Moving outside the board or into any remaining body cell ends the game and returns `-1`; successful moves return the current score. Preserve all state across calls.

### Function Contract
**Inputs**

- `width`, `height`: board dimensions in columns and rows
- `food`: food coordinates `[row, column]` in consumption order
- `directions`: for the app adapter, the sequence of `"U"`, `"D"`, `"L"`, and `"R"` moves. Native LeetCode calls `move(direction)` individually.

**Return value**

- The app adapter returns the score after every move, or `-1` at the losing move. Native `move` returns that move's status directly.

### Examples
**Example 1**

- Input: `width = 3, height = 2, food = [[1,2],[0,1]], directions = ["R","D","R","U","L","U"]`
- Output: `[0, 0, 1, 1, 2, -1]`

**Example 2**

- Input: `width = 1, height = 1, food = [], directions = ["R"]`
- Output: `[-1]`

**Example 3**

- Input: `width = 2, height = 2, food = [[0,1]], directions = ["R","D","L","U"]`
- Output: `[1, 1, 1, 1]`

### Required Complexity

- **Time:** $O(q)$
- **Space:** $O(f)$

<details>
<summary>Approach</summary>

#### General

**Represent the body for both order and membership**

Two views of the body serve different operations. A deque stores cells from tail to head so the oldest cell can leave in constant time. A set stores the same cells for constant-time self-collision checks.

**Resolve each move in game order**

For each direction, compute the candidate head from the current head. A position outside the board loses immediately. Next determine whether the candidate equals the next unconsumed food coordinate.

**Remove a moving tail before checking collision**

If no food is eaten, remove the tail from both the deque and occupied set *before* testing the new head against the body. This ordering is essential: moving into the cell vacated by the tail on the same move is legal. If food is eaten, the tail stays and the food index advances. After the appropriate tail handling, an occupied candidate is a real self-collision; otherwise append it as the new head and return the number of foods consumed.

**Why both body views remain consistent**

The deque and set contain exactly the snake cells after every successful move. A normal move removes one tail and adds one head, preserving length; an eating move adds only the head, increasing length by one. The collision test considers precisely the cells that remain occupied after the simultaneous tail movement, so it rejects every and only illegal body collision.

#### Complexity detail

Every move performs constant-time deque and expected constant-time set operations, so `q` moves take $O(q)$ total time. The snake begins with one cell and grows once per consumed food, so the deque and set use $O(f)$ space, more precisely $O(f + 1)$.

#### Alternatives and edge cases

- **Body list only:** makes tail removal or collision membership $O(length)$ per move.
- **Full occupancy matrix:** gives constant-time membership but uses $O(width \cdot height)$ space even when the snake is short.
- Check wall coordinates before indexing the board.
- Food is consumed only in the supplied order.
- Moving into the departing tail cell is legal, while moving into any other body segment is not.
- After game over, later moves continue returning `-1` defensively.

</details>
