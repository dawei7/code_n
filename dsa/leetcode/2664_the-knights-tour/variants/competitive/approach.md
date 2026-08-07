## General
### Beginner-Friendly Intuition & Strategy
The core task in **The Knight’s Tour** is to two positive integers `m` and `n` which are the height and width of a **0-indexed** 2D-array `board`, a pair of positive integers `(r, c)` which is the starting position of the knight on the board. A naive approach might try every possible digit or combination randomly, which leads to millions of redundant calculations. Instead, this solution uses **Backtracking (Recursive State Exploration)**. Imagine solving a maze: you make a tentative choice at an open cell, check if it obeys all constraints, and move deeper into the maze. If you ever hit a dead end, you **backtrack** (undo your last move by resetting the state) and try the next alternative. This guarantees finding a valid configuration while pruning invalid paths early.

### Step-by-Step Execution Guide
**Step 1: Setup & Base Cases**  
We inspect the board/grid and locate the first empty spot or decision point that needs a valid assignment, establishing helper validation routines.  
**Step 2: Core Processing & Traversal**  
1. Scan for an empty cell (`'.'`).  
2. Iterate through candidate choices (`'1'` to `'9'`).  
3. For each candidate, verify validity.  
4. If valid, place tentatively and recursively call `solver()`.  
5. If recursive call returns `True`, puzzle is solved!  
6. If it returns `False`, reset cell to `'.'`.  
**Step 3: Completion & Return**  
Bitwise operators (`&`, `|`, `^`, `<<`, `>>`) allow ultra-fast bitmask updates in $O(1)$ hardware instructions.  
When processing finishes, the algorithm outputs the final validated solution.

### Why This Handles Edge Cases Gracefully
- **Empty / Null Inputs:** Early guard checks return empty results immediately without crashing.


## Complexity detail
- **Time Complexity**: $O(8^(mn))$ — Detailed Analysis: The time complexity corresponds directly to the total number of operations required by the step-by-step execution loop described above.
- **Space Complexity**: $O(mn)$ — Detailed Analysis: The space complexity reflects the auxiliary memory allocated for tracking structures, recursion stack depth, or hash maps during processing.
