# Search Word

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DSAPROB8 |
| Difficulty Band | Recursion |
| Path | Data Structures and Algorithms |
| Lesson | Fundamentals of Recursion |
| Official Link | [DSAPROB8](https://www.codechef.com/learn/course/recursion/LRECUR03/problems/DSAPROB8) |

---

## Problem Statement

Given a $R$ x$C$ grid of lowercase characters and a string $s$, check if $s$ is present in the grid. The string can be constructed from letters of sequentially adjacent cells, where **adjacent** cells are those horizontally or vertically neighbouring. The same letter cell may not be used more than once.

---

## Input Format

- The first line contains two integers $R$ $and$ $C$.
- The next $R$ lines contain $C$ space-separated lowercase characters representing the grid.
- The last line contains the string $s$.

---

## Output Format

Output true if the string s exists in the grid, otherwise output false.

---

## Constraints

- $ 1 \leq R, C \leq 6 $
- The size of the string $s$ will not exceed $R * C$

---

## Examples

**Example 1**

**Input**

```text
3 4
a b c e
s f c s
a d e e
abcced
```

**Output**

```text
true
```

**Explanation**

The string "abcced" can be found by moving right from (1,1) to (1,2) to (1,3) and then down to (2,3) and again down to (3,3) and then left to (3,2).

**Example 2**

**Input**

```text
3 4
a b c e
s f c s
a d e e
see
```

**Output**

```text
true
```

**Explanation**

The string "see" can be found by moving down from (2,4) to (3,4) and then left to (3,3).

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problme [Link](https://www.codechef.com/learn/course/recursion/LRECUR03/problems/DSAPROB8)

#### [](#problem-statement-1)Problem Statement:

You are given a `R x C` grid of lowercase characters and a string `s`. The task is to check if the string `s` can be found in the grid by sequentially connecting adjacent cells. A cell is considered adjacent if it is horizontally or vertically neighboring. The same cell may not be used more than once in the construction of the string.

#### [](#approach-2)Approach:

To solve this problem, we can use **Depth-First Search (DFS)**. The idea is to start from each cell in the grid and try to construct the string `s` by exploring adjacent cells in the grid. We recursively explore all possible paths in the grid that can form the string. If we find such a path, the function returns `true`. Otherwise, after exploring all possibilities, the function returns `false`.

### [](#detailed-explanation-3)Detailed Explanation:

-

**DFS Traversal**:

- We define a DFS function that takes the current position in the grid `(i, j)`, the current index `k` of the string `s`, and the grid itself.

- If `k` equals the length of the string, it means we’ve successfully found the string in the grid, so we return `true`.

- If the current position `(i, j)` is out of bounds or the character at `board[i][j]` does not match `s[k]`, return `false`.

-

**Marking Cells as Visited**:

- To avoid using the same cell more than once, we temporarily mark the current cell as visited by replacing its value with a special marker (e.g., `#`).

- After exploring all possible paths from the current cell, restore its original value.

-

**Exploring All Directions**:

- From the current cell, we recursively explore the four possible directions (up, down, left, right) to see if we can continue forming the string.

-

**Initial Search**:

- The search begins from each cell in the grid. If we find a path that successfully forms the string, we return `true`. If after checking all cells the string is not found, we return `false`.

### [](#example-4)Example:

Consider the grid:

``A B C E
S F C S
A D E E
``

and the word `ABCCED`.

Starting from `A` at `(0, 0)`:

- Move right to `B`, then to `C`, then right again to `C`, then down to `E`, and finally down to `D`. The word `ABCCED` is found.

### [](#complexity-5)Complexity:

-

**Time Complexity**: The time complexity is `O(R * C * 4^L)`, where `R` and `C` are the dimensions of the grid, and `L` is the length of the word. In the worst case, we explore up to four directions for each character in the word, but the actual complexity is often much lower due to early termination.

-

**Space Complexity**: The space complexity is `O(L)` due to the recursive call stack, where `L` is the length of the word.

</details>
