# Chef Solves Sudoku

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | UELPQ01 |
| Difficulty Band | Recursion |
| Path | Data Structures and Algorithms |
| Lesson | Fundamentals of Recursion |
| Official Link | [UELPQ01](https://www.codechef.com/learn/course/recursion/LRECUR03/problems/UELPQ01) |

---

## Problem Statement

Chef has encountered a challenging Sudoku puzzle and wants to solve it by filling all the empty cells. Each digit from $1$ to $9$ must appear exactly once in every row, every column, and each of the nine $3 \times 3$ sub-boxes of the grid. \
The empty cells are represented by the character `'.'`. Chef wants to complete the puzzle so that it becomes a valid Sudoku configuration. Help Chef by writing a program that fills the empty cells following these strict Sudoku rules.

## Function Declaration

### Function Name
$solvePuzzle$ — This function solves a given Sudoku puzzle by filling the empty cells according to Sudoku rules.

### Parameters
- $sudokuBoard$ : A $9 \times 9$ 2D grid representing the Sudoku board.
  Each cell contains a digit character (`'1'`–`'9'`) or `'.'` indicating an empty cell.

### Return Value
- Returns `void`.
- The function updates the $\text{sudokuBoard  inPlace}$ to reflect the solved Sudoku puzzle.
- The modified board must be a valid completed Sudoku configuration.

## Constraints
- $1 \leq T \leq 10$
- The Sudoku board size is fixed at $9 \times 9$.
- Each $sudokuBoard[i][j]$ is either a digit character `'1'`–`'9'` or `'.'`.
- It is guaranteed that the input board has at least one valid solution.

*The input and output formats provided below are only for testing with custom inputs. You only need to complete the core logic function.*

---

## Input Format

- The first line contains a single integer $T$ — the number of test cases.
- For each test case:
  - The first line contains a single integer $N$, the size of the Sudoku board. It is guaranteed that $N = 9$.
  - The next $N$ lines represent the rows of the Sudoku board.
  - Each row is formatted as $N$ space-separated characters enclosed in square brackets [...].
- Each character is either a digit from `'1'` to `'9'` or `'.'`, where `'.'` denotes an empty cell.

---

## Output Format

- For each test case, print 9 lines representing the solved Sudoku board.
- Each line is a completed row enclosed in square brackets [...] containing 9 space-separated characters.
- The output board must be a valid Sudoku solution.

---

## Examples

**Example 1**

**Input**

```text
1
9
[5 3 . . 7 . . . .]
[6 . . 1 9 5 . . .]
[. 9 8 . . . . 6 .]
[8 . . . 6 . . . 3]
[4 . . 8 . 3 . . 1]
[7 . . . 2 . . . 6]
[. 6 . . . . 2 8 .]
[. . . 4 1 9 . . 5]
[. . . . 8 . . 7 9]
```

**Output**

```text
[5 3 4 6 7 8 9 1 2]
[6 7 2 1 9 5 3 4 8]
[1 9 8 3 4 2 5 6 7]
[8 5 9 7 6 1 4 2 3]
[4 2 6 8 5 3 7 9 1]
[7 1 3 9 2 4 8 5 6]
[9 6 1 5 3 7 2 8 4]
[2 8 7 4 1 9 6 3 5]
[3 4 5 2 8 6 1 7 9]
```

**Explanation**

- The given Sudoku board has empty cells represented by dots.
- Using Sudoku rules, each empty cell is filled with a digit 1-9 that doesn't repeat in its row, column, or 3x3 subgrid.
- The output shows the fully completed board where all constraints are satisfied, resulting in a unique valid solution.

**Example 2**

**Input**

```text
1
9
[. . . 2 6 . 7 . 1]
[6 8 . . 7 . . 9 .]
[1 9 . . . 4 5 . .]
[8 2 . 1 . . . 4 .]
[. . 4 6 . 2 9 . .]
[. 5 . . . 3 . 2 8]
[. . 9 3 . . . 7 4]
[. 4 . . 5 . . 3 6]
[7 . 3 . 1 8 . . .]
```

**Output**

```text
[4 3 5 2 6 9 7 8 1]
[6 8 2 5 7 1 4 9 3]
[1 9 7 8 3 4 5 6 2]
[8 2 6 1 9 5 3 4 7]
[3 7 4 6 8 2 9 1 5]
[9 5 1 7 4 3 6 2 8]
[5 1 9 3 2 6 8 7 4]
[2 4 8 9 5 7 1 3 6]
[7 6 3 4 1 8 2 5 9]
```

**Explanation**

- Filled empty cells by checking row, column, and 3x3 box constraints, starting with cells having fewest options.
- Used logical deductions and backtracking to place numbers ensuring no repetitions in rows, columns, or boxes.
- Completed the grid by systematically resolving each cell until the entire Sudoku was valid and solved.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## Problem Overview

You are given a partially filled 9×9 Sudoku grid.
Empty cells are denoted by `.`.

The objective is to fill the grid such that:

* Each row contains digits 1 to 9 exactly once
* Each column contains digits 1 to 9 exactly once
* Each 3×3 subgrid contains digits 1 to 9 exactly once

If a valid completion exists, output the solved Sudoku grid.

---

## Constraints and Observations

* The grid size is fixed (9×9)
* The problem is a classic **constraint satisfaction problem**
* A valid solution is guaranteed for standard Sudoku inputs
* Brute-force enumeration is infeasible due to exponential growth

---

## Approach 1: Naive Backtracking

### Idea

* Traverse the grid to find an empty cell
* Try placing digits 1 to 9
* For each digit, check if placement is valid:

  * Digit does not appear in the same row
  * Digit does not appear in the same column
  * Digit does not appear in the same 3×3 subgrid
* Recursively solve the rest of the grid
* If no digit fits, backtrack

### Validity Check

For every attempted placement:

* Scan 9 cells in the row
* Scan 9 cells in the column
* Scan 9 cells in the subgrid

### Time Complexity

* Worst case is exponential
* Each check costs linear time
* Performs poorly on hard Sudoku instances

### Verdict

* Simple and easy to implement
* Works for easy puzzles
* Leads to TLE for difficult or near-empty grids

---

## Approach 2: Backtracking with Bitmask Optimization

### Core Optimization

Instead of scanning rows, columns, and subgrids repeatedly, maintain:

* A bitmask for each row
* A bitmask for each column
* A bitmask for each 3×3 subgrid

Each bitmask tracks which digits are already used.

### How It Works

* Each digit 1–9 is mapped to a bit position
* Validity check becomes a constant-time bitwise operation
* When placing a digit:

  * Set the corresponding bits in row, column, and box
* When backtracking:

  * Unset the bits

### Advantages

* Validity checks become O(1)
* Massive reduction in redundant work
* Handles hard test cases efficiently

### Time Complexity

* Still exponential in theory
* Extremely fast in practice due to pruning

### Verdict

* Highly efficient
* Recommended baseline solution
* Passes all standard competitive programming constraints

---

## Approach 3: Backtracking with MRV Heuristic

### Idea

MRV (Minimum Remaining Values) heuristic:

* Instead of picking the first empty cell, choose the cell with the fewest valid options

### Why It Works

* Reduces branching factor early
* Forces difficult decisions first
* Avoids deep useless recursion paths

### Steps

1. For all empty cells, count how many digits can be placed
2. Select the cell with the minimum count
3. Try digits only for that cell

### Benefits

* Dramatically improves performance on hardest puzzles
* Often solves minimal-clue Sudokus very quickly

### Verdict

* Best possible backtracking strategy
* Slightly more complex to implement
* Ideal for production-level solvers

---

## Approach 4: Constraint Propagation (Advanced)

### Concept

Before guessing:

* Automatically fill cells with only one possible value
* Continuously propagate constraints

Examples:

* Single candidate rule
* Single position rule

### Usage

* Usually combined with backtracking
* Reduces recursion depth further

### Verdict

* Powerful but complex
* Used in professional Sudoku solvers
* Not mandatory for competitive programming

---

## Comparative Summary

| Approach               | Validity Check | Speed     | Complexity | Recommended |
| ---------------------- | -------------- | --------- | ---------- | ----------- |
| Naive Backtracking     | $O(N \cdot N^{N^2})$   | Slow      | Simple     | No          |
| Bitmask Backtracking   | $O(N^{N^2})$  | Fast      | Moderate   | Yes         |
| MRV + Bitmask          | $O(V^{N^2})$ (where $V < N$)  | Very fast | High       | Best        |
| Constraint Propagation | $O(N^2)$  | Fastest   | Advanced   | Optional    |

---

## Final Recommendation

For competitive programming and real-world use:

* Use **bitmask-based backtracking**
* Add **MRV heuristic** for best performance
* Avoid repeated row/column scans

This guarantees correctness, speed, and scalability.

---

## Key Takeaways

* Sudoku is a constraint satisfaction problem
* Pruning and constant-time checks are essential
* Algorithmic optimizations matter more than language choice
* A well-optimized backtracking solution easily passes all test cases

</details>
