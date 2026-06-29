# Treasure Hunting

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | N1 |
| Difficulty Rating | 1634 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Graphs |
| Official Link | [N1](https://www.codechef.com/practice/course/3to4stars/LP3TO403/problems/N1) |

---

## Problem Statement

Treasure Hunting is a great computer game that has attracted generations of Bytelandian children.
In the game, there is a maze divided into $N \times N$ squares.

- Dave starts in the top-left corner, which is square $(1,1)$, and needs to go to the bottom-right corner, which is square $(N,N)$.
- Some of the squares are blocked and some of the squares contain treasures.
- Dave needs to capture all the treasures in the maze before going to square $(N,N)$.
- In each second, Dave can go to one of its four adjacent squares (if the destination is not blocked).

Find the earliest time that Dave can reach the destination $(N,N)$ after collecting all the treasures in the maze.

---

## Input Format

- The first line contains $T$, the number of test cases. Then $T$ test cases follow.
- The first line of each testcase contains $N$, the size of the maze
- The $N$ following lines describe the maze. The meaning of the symbols is as follows:
   - '.' : an empty square
   - '*' : a treasure
   - '#' : a blocked square

---

## Output Format

For each test case, print in a single line the earliest time that Dave can reach the destination after collecting all the treasures. If Dave cannot reach the destination, print -1.

---

## Constraints

- $1 \leq T \leq 15$
- $1 \leq N \leq 13$
- The number of treasures in the maze does not exceed 13.
- Squares $(1,1)$ and $(N,N)$ are always empty.

---

## Examples

**Example 1**

**Input**

```text
4

3
...
.##
*#.

3
..*
...
...

3
..*
*..
...

4
....
.#.*
.#*.
**#.
```

**Output**

```text
-1
4
6
16
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Treasure Hunting](https://www.codechef.com/practice/course/3to4stars/LP3TO403/problems/N1)

### [](#problem-statement-1)Problem Statement

Treasure Hunting is a great computer game that has attracted generations of Bytelandian children.

In the game, there is a maze divided into N \times N squares.

- Dave starts in the top-left corner, which is square (1,1), and needs to go to the bottom-right corner, which is square (N,N).

- Some of the squares are blocked and some of the squares contain treasures.

- Dave needs to capture all the treasures in the maze before going to square (N,N).

- In each second, Dave can go to one of its four adjacent squares (if the destination is not blocked).

Find the earliest time that Dave can reach the destination (N,N) after collecting all the treasures in the maze.

### [](#approach-2)Approach

The approach starts by scanning the maze to find all treasure positions and storing their coordinates. Each treasure is represented by a unique bit in a binary bitmask to track the treasures Dave has collected. Once all treasures are located, a target bitmask is defined to represent the state where all treasures are collected.

The solution uses `Breadth-First Search` (BFS), starting from the `top-left` corner. BFS explores the maze level by level, ensuring the shortest path to collect all treasures and reach the destination. At each step, we check if Dave collects a treasure and update the bitmask accordingly. A `3D` visited array tracks each cell’s state to avoid reprocessing.

BFS continues until Dave reaches the bottom-right corner with all treasures collected, returning the time taken. If no valid path exists, the result is -1.

### [](#time-complexity-3)Time Complexity

The time complexity is O(N^2×2^T), where 𝑁 is the size of the maze and T is the number of treasures. This accounts for the BFS search across each cell with different treasure collection states.

### [](#space-complexity-4)Space Complexity

The space complexity is O(N^2×2^T ), for the 3D visited array to store each cell’s visited states and the BFS queue.

</details>
