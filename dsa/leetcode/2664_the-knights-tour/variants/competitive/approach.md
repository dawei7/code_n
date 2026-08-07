## General
### Beginner-Friendly Intuition & Strategy
The core task in **The Knight’s Tour** is to two positive integers `m` and `n` which are the height and width of a **0-indexed** 2D-array `board`, a pair of positive integers `(r, c)` which is the starting position of the knight on the board. A naive approach might try every possible digit or combination randomly, which leads to millions of redundant calculations. Instead, this solution uses **Backtracking (Recursive State Exploration)**. Imagine solving a maze: you make a tentative choice at an open cell, check if it obeys all constraints, and move deeper into the maze. If you ever hit a dead end, you **backtrack** (undo your last move by resetting the cell to empty) and try the next alternative. This guarantees finding a valid configuration while pruning invalid paths early.

### Step-by-Step Execution Guide
**Step 1: Setup & Initial State**  
We inspect the board/grid and locate the first empty spot (or decision point) that needs a valid assignment. We also define helper validation routines to quickly verify whether a candidate choice violates any row, column, or region constraints.  
**Step 2: Core Processing & Decisions**  
1. Scan for an empty cell (`'.'`).  
2. Iterate through all possible candidate choices (e.g. digits `'1'` through `'9'`).  
3. For each candidate, check if placing it is **valid** according to puzzle rules.  
4. If valid, place the candidate tentatively into the cell and recursively call `solver()` to attempt solving the rest of the board.  
5. If the recursive call returns `True`, the puzzle is solved!  
6. If the recursive call returns `False` (a dead end), **undo the placement** (reset cell to `'.'`) and try the next candidate digit.  
**Step 3: Completion & Result Return**  
Bitwise operators (`&`, `|`, `^`, `<<`, `>>`) allow ultra-fast bitmask updates for set operations in $O(1)$ hardware instructions.  
When processing finishes, the algorithm outputs the final validated solution.

### Why This Handles Edge Cases Gracefully
- **Empty / Null Inputs:** Early guard checks return empty results immediately without crashing.
- **No Solution / Unsolvable States:** If no candidate number works for a cell, the function returns `False`, triggering proper backtracking up the call stack until an alternative branch is explored.


## Complexity detail
- **Time Complexity**: $O(8^(mn))$ — Detailed Analysis: The time complexity corresponds directly to the total number of operations required by the step-by-step execution loop described above.
- **Space Complexity**: $O(mn)$ — Detailed Analysis: The space complexity reflects the auxiliary memory allocated for tracking structures, recursion stack depth, or hash maps during processing.
