# Rat In Maze

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | RATMAZE |
| Difficulty Band | Recursion |
| Path | Data Structures and Algorithms |
| Lesson | Fundamentals of Recursion |
| Official Link | [RATMAZE](https://www.codechef.com/learn/course/recursion/LRECUR03/problems/RATMAZE) |

---

## Problem Statement

A rat is placed at the top-left corner of an **n × n** grid (cell **(0, 0)**) and wants to reach the bottom-right corner **(n−1, n−1)**.
Some cells are blocked and cannot be visited.

The rat may move in **four directions**:

* **U** → Up
* **D** → Down
* **L** → Left
* **R** → Right

A cell with value $1$ is open; a cell with value $0$ is blocked.
The rat **cannot visit any cell more than once** in a single path.
If the starting cell is blocked, no movement is possible.

Your task is to return **all distinct valid paths** from start to destination, using the movement characters `'U', 'D', 'L', 'R'`.
If no valid path exists, return **an empty list**.

## **Function Declaration**

### **Function Name**

$findAllPaths$ – This function computes all possible valid paths the rat can take from the start cell to the destination cell.

### **Parameters**

* $n$ : Integer representing the dimension of the grid $(n * n)$.
* $grid$ : A 2D vector/list of integers containing only $0$ and $1$, where

  * $1$ → the cell is open
  * $0$ → the cell is blocked

### **Return Value**

* Returns a array, where each string represents a valid movement sequence.
* Returns an **empty vector/list** if no path exists.

## **Constraints**

* $1 \leq T \leq 10$
* $2 \leq n \leq 5$
* $grid[i][j] \in {0, 1}$
* The rat cannot revisit any cell in the same path.
* The rat may move only in **U, D, L, R** directions.

---

## Input Format

* The first line contains an integer $T$ — the number of test cases.
* For each test case:

  * The first line contains a single integer $n$.
  * The next $n$ lines contain $n$ integers each, describing the grid.

---

## Output Format

* For each test case:

  * Print all valid paths in **lexicographical order**.
  * If no path exists, print $-1$.

---

## Constraints

1 <= T <= 100

1 <= n, m <= 100

0 <= maze[i][j] <= 1

---

## Examples

**Example 1**

**Input**

```text
1
4
1 1 1 1
0 1 1 1
0 0 1 0
1 1 1 1
```

**Output**

```text
[ "RDRDDR", "RRDDDR", "RRRDLDDR" ]
```

**Example 2**

**Input**

```text
1
2
1 0
0 1
```

**Output**

```text
-1
```

**Explanation**

No valid path exists, so output is `-1`.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## **1. Problem Summary**

You are given an `n × n` grid where each cell contains either:

* `1` → open cell (the rat can move here)
* `0` → blocked cell (the rat cannot enter)

The rat starts at cell `(0, 0)` and wants to reach `(n − 1, n − 1)`.

The allowed movements are:

* Up (`U`)
* Down (`D`)
* Left (`L`)
* Right (`R`)

The objective is to generate all possible valid paths as strings of movement characters, ensuring that:

1. No cell is visited more than once in a single path.
2. You only step on open cells (`1`).
3. If there is no valid path, the output should reflect that.

Since `n ≤ 5`, the grid is small enough for an exhaustive search.

---

## **2. Key Observations**

1. At each cell, the rat can attempt to move in four directions.
2. Re-visiting cells must be avoided to prevent infinite loops.
3. This is a classical backtracking problem, where decisions are made step-by-step and reversed when needed.
4. All valid paths need to be collected, not just one.

---

## **3. Why Backtracking Works**

Backtracking systematically explores every valid movement by:

1. Marking the current cell as visited.
2. Attempting all possible moves from this cell.
3. For each valid direction:

   * Add the move to the current path.
   * Recurse into the next cell.
   * Remove the move when returning (undo the choice).
4. Unmarking the cell before returning.

Since `n` is small, the number of possible paths is manageable, making backtracking ideal.

---

## **4. Validity Conditions for Movement**

For a move from `(x, y)` to `(nx, ny)` to be valid:

* `nx` and `ny` must be inside grid boundaries
* The target cell must contain `1`
* The cell must not have been visited in the current path

These conditions prevent invalid paths and infinite loops.

---

## **5. Search Order**

A common directional order used is:

1. Down (`D`)
2. Left (`L`)
3. Right (`R`)
4. Up (`U`)

This order impacts the sequence in which paths are discovered but does not affect correctness.

---

## **6. Handling Special Cases**

1. **Start cell blocked**
   If `(0, 0)` is `0`, no paths exist.

2. **End cell blocked**
   If `(n−1, n−1)` is `0`, no path can reach the destination.

3. **Surrounded start or dead-end corridors**
   Backtracking naturally handles these by exploring all avenues and discarding invalid paths.

4. **Large number of valid paths**
   Backtracking collects all of them before completing.

---

## **7. Time and Space Complexity**

### **Time Complexity**

In the worst case, the rat can move in 4 directions from each cell.

Maximum cells = `25` (when `n = 5`)

Worst-case complexity is:

`O(4^(n*n))`, but effective branching reduces quickly due to visited checks.

With constraints, this is acceptable.

### **Space Complexity**

* Visited array: `O(n²)`
* Recursion depth: up to `n²`
* Output storage depends on number of paths

---

## **8. Approach Summary**

1. Initialize a visited structure.
2. Begin DFS from `(0, 0)` with an empty path string.
3. At each step:

   * If destination reached, store the path.
   * Otherwise, try moving in four directions.
4. Backtrack by unmarking cells and removing moves.
5. Return all collected paths.

</details>
