## General

**Use the output matrix as both result and visited record**

The method first creates an `m x n` matrix filled with `-1`. This value has two roles:

- it is the required value for cells left over after the linked list ends;
- it marks cells that have not yet received a list value.

This dual use is safe because every linked-list value lies between zero and 1000. A written cell can never still contain `-1`, so testing `ans[x][y] == -1` accurately means “unvisited.”

The starting position is `(0, 0)`, the top-left corner required by the statement. The direction index `k` starts at zero, which represents movement to the right.

**Encode the four clockwise directions compactly**

The tuple

`dirs = (0, 1, 0, -1, 0)`

stores overlapping row-column pairs:

- `k = 0` uses `(dirs[0], dirs[1]) = (0, 1)` for right;
- `k = 1` uses `(1, 0)` for down;
- `k = 2` uses `(0, -1)` for left;
- `k = 3` uses `(-1, 0)` for up.

Updating `k = (k + 1) % 4` rotates clockwise through right, down, left, and up, then returns to right.

This representation avoids a separate list of four coordinate pairs while expressing the same movement pattern.

**Write one list node before deciding the next position**

At the top of each outer iteration, `ans[i][j] = head.val` places the current node's value into the current spiral cell. The local `head` reference then advances to `head.next`.

If that was the last list node, `head` becomes `None` and the method breaks immediately. This timing is important. There is no need to find a next empty cell when no value remains, and if the list exactly fills the matrix there may be no such cell.

The original linked-list nodes are not changed. Only the local pointer moves; no `next` field is reassigned.

**Turn until the next step is legal**

If another node remains, the inner loop proposes

`x = i + dirs[k]` and `y = j + dirs[k + 1]`.

The proposal is valid only when it lies inside all four boundaries and the target cell still equals `-1`. If valid, `i, j` move there and the inner loop ends so the next outer iteration writes the next list value.

If the proposal is outside the matrix or already filled, `k` rotates clockwise and tries again. Filled cells act as the inner walls of completed spiral layers, while bounds act as the outer walls.

The source uses a loop rather than assuming exactly one turn. In normal rectangular spiral traversal, one clockwise turn is usually enough at a corner, but repeated checking is robust and directly expresses “keep turning until a valid unfilled neighbor appears.”

**Why a next cell exists whenever another node remains**

The list length is at most `m \cdot n`. If `head` is not `None` after writing one value, fewer than the list's total nodes have been placed, and therefore fewer than `m \cdot n` cells have been filled. At least one unfilled cell remains.

The clockwise wall-following traversal visits rectangular perimeter layers without jumping or isolating an unvisited region. Starting from the top-left and turning whenever it meets a boundary or visited cell creates the standard spiral Hamiltonian order of all matrix cells. Consequently, the next cell in that order is an adjacent unfilled neighbor in one of the four directions, and the inner loop will find it.

**Why values appear in the required spiral order**

Initially, the state is at the first spiral coordinate and points right. While the next coordinate in the current direction is inside and unvisited, movement continues along the current side of the active perimeter. At the side's end, the invalid proposal triggers one clockwise turn onto the next side.

After a complete perimeter is written, attempting to revisit it is rejected by the `-1` test, causing movement into the next inner perimeter. This repeats until the list ends or all cells are filled.

Exactly one list node is consumed per written cell, and cells are never revisited because movement accepts only `-1` targets. Thus linked-list order is preserved along the unique generated spiral. Any cells not reached before the list ends retain their initialized `-1` values.

**Single-row and single-column matrices need no special cases**

For one row, movement continues right until the list ends or the boundary is reached. If nodes remain after the final column, that would contradict the length bound. For one column, the first attempted right move is out of bounds, so the direction rotates down and traversal proceeds.

The same bounds and visited checks also handle thin remaining inner layers.

## Complexity detail

Let `L` be the linked-list length, with `1 <= L <= mn`. Initializing the output matrix takes `O(mn)` time. The outer loop writes exactly `L` nodes. Each movement considers a constant number of four possible directions, so filling costs `O(L)` and total time is `O(mn + L) = O(mn)`.

The matrix itself contains `mn` required output entries. Excluding this output, the method stores only coordinates, a direction index, a five-number direction tuple, and the moving list pointer, so auxiliary space is `O(1)`. Including required output storage, total newly allocated space is `O(mn)`.

No separate visited matrix is needed because `-1` is outside the valid node-value range and already fills the output.

## Alternatives and edge cases

- **Four shrinking boundaries:** Maintain top, bottom, left, and right limits and traverse each side while consuming nodes. This avoids visited checks and is equally `O(mn)`, but must stop carefully in the middle of a side when the list ends.
- **Separate visited matrix:** It makes visitation explicit but duplicates `O(mn)` storage. The output sentinel already provides the needed state.
- **Generate all spiral coordinates first:** Store an `mn` coordinate sequence and pair it with list nodes. This adds linear auxiliary memory without simplifying the actual writes enough to justify it.
- **Assume every invalid move needs exactly one turn:** Usually true for the standard spiral, but the inner loop safely checks until it finds a valid direction and is easier to reason about at narrow final layers.
- **Use zero as the unfilled marker:** Zero is a valid node value, so the algorithm could mistake a written zero for an empty cell and revisit it. `-1` is safe under the constraints.
- **List shorter than the matrix:** The break occurs immediately after the final write, and all untouched cells remain `-1`.
- **List exactly fills the matrix:** The last-node check breaks before searching for a nonexistent empty neighbor.
- **One cell:** The first node is written at `(0,0)` and must be the last because list length cannot exceed one.
- **One row:** The traversal moves right; no special boundary variables are needed.
- **One column:** The initial right proposal fails, direction turns down, and values fill top to bottom.
- **Repeated node values:** Visitation depends on whether a cell is `-1`, not on uniqueness, so duplicates cause no ambiguity.
- **Node value `0`:** It correctly marks the cell as filled because zero differs from `-1`.
- **Head guarantee:** The list contains at least one node, so dereferencing `head.val` in the first iteration is safe.
- **Local pointer advancement:** The method changes which node `head` refers to but does not mutate the linked list's structure or values.
- **Direction tuple indexing:** `k` stays in zero through three, so `k + 1` stays within the five-element tuple.
