# Disabled King

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DISABLEDKING |
| Difficulty Rating | 1237 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [DISABLEDKING](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/DISABLEDKING) |

---

## Problem Statement

Chef loves Chess and has thus invented a new piece named "Disabled King".

Let's denote the cell at the intersection of the $i$-th column from the left and $j$-th row from the top by $(i, j)$.

If he is currently in cell $(x,y)$, the disabled king can move to the following positions in one move (provided that he remains in the chessboard):

- $(x,y+1)$
- $(x,y-1)$
- $(x+1,y+1)$
- $(x+1,y-1)$
- $(x-1,y+1)$
- $(x-1,y-1)$

In short, the Disabled King cannot move horizontally.

In an $N \times N$ chessboard, the Disabled King is currently situated at the top-left corner (cell $(1, 1)$) and wants to reach the top-right corner (cell $(N, 1)$). Determine the minimum number of moves in which the task can be accomplished.

---

## Input Format

- The first line will contain $T$, the number of test cases. Then the test cases follow.
- Each test case contains a single integer $N$ in a separate line.

---

## Output Format

Output the minimum number of moves to get from the top-left cell to the top-right one.

---

## Constraints

- $1 \leq T \leq 500$
- $2 \leq N \leq 500$

---

## Examples

**Example 1**

**Input**

```text
2
2
3
```

**Output**

```text
2
2
```

**Explanation**

**Test case 1:**

Initially chef is at $(1, 1)$. He cannot directly move to $(2, 1)$ as the disabled king cannot move horizontally. So he needs at least $2$ moves to reach $(2, 1)$. And that can be achieved by first moving to $(1, 2)$ and then moving to $(2, 1)$ from there.

**Test case 2:**

Clearly we cannot reach $(3, 1)$ from $(1, 1)$ in just one move. We require at least $2$ moves. And this can be achieved by first moving to $(2, 2)$ and then moving to $(3, 1)$ from there.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
3
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest - Division 3](https://www.codechef.com/COOK135C/problems/DISABLEDKING)

[Contest - Division 2](https://www.codechef.com/COOK135B/problems/DISABLEDKING)

[Contest - Division 1](https://www.codechef.com/COOK135A/problems/DISABLEDKING)

#
[](#difficulty-2)DIFFICULTY:

CAKEWALK

#
[](#problem-3)PROBLEM:

Given a chess board of size N\times N. A ‘disabled’ king is initially at cell (1,1). In one move, the king can move from cell (x,y) to any of the following cells (provided they are within the board):

- (x, y + 1)

- (x, y - 1)

- (x + 1, y + 1)

- (x + 1, y - 1)

- (x - 1, y + 1)

- (x - 1, y - 1)

Determine the minimum moves required to reach cell (N,1).

#
[](#explanation-4)EXPLANATION:

**Observation:** The minimum moves required is always \ge N-1.

Proof

In one move, the king can travel atmost 1 step to the right. The destination cell is exactly N-1 steps to the right of the initial cell.

Thus, the minimum moves required is always \ge N-1.

There are now two cases:

-
N is odd: The minimum number of moves required is N-1, which can be achieved as follows:

(1,1)\to(2,2)\to(3,1)\to(4,2)\to\dots\to(N,1)

-
N is even: Here, it isn’t hard to conclude that it is impossible to reach the destination cell using only N-1 moves. However, it can be done in N moves, in the following fashion:

(1,1)\to(2,2)\to(3,1)\to(4,2)\to\dots\to(N,2)\to(N,1)

Therefore, output

-
N-1 when N is odd, and

-
N otherwise.

#
[](#time-complexity-5)TIME COMPLEXITY:

O(1)

per test case.

#
[](#solutions-6)SOLUTIONS:

Editorialist’s solution can be found [here](https://www.codechef.com/viewsolution/54153326)

***Experimental:** For evaluation purposes, please rate the editorial (1 being poor and 5 excellent)*

- 1

- 2

- 3

- 4

- 5

0
voters

</details>
