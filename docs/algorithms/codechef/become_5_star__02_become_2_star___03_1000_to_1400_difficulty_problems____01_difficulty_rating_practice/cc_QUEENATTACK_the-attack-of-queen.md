# The Attack of Queen

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | QUEENATTACK |
| Difficulty Rating | 1076 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [QUEENATTACK](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/QUEENATTACK) |

---

## Problem Statement

Chef has started developing interest in playing chess, and was learning how the [Queen](https://en.wikipedia.org/wiki/Queen_(chess)) moves.

Chef has an empty $N \times N$ chessboard. He places a Queen at $(X, Y)$ and wonders - What are the number of cells that are under attack by the Queen?

**Notes:**
- The top-left cell is $(1, 1)$, the top-right cell is $(1, N)$, the bottom-left cell is $(N,1)$ and the bottom-right cell is $(N, N)$.
- The Queen can be moved any number of unoccupied cells in a straight line vertically, horizontally, or diagonally.
- The cell on which the Queen is present, is **not** said to be under attack by the Queen.

---

## Input Format

- The first line contains a single integer $T$ - the number of test cases. Then the test cases follow.
- The first and only line of each test case contains three integers $N$, $X$ and $Y$, as described in the problem statement.

---

## Output Format

For each test case, output in a single line, the total number of cells that are under attack by the Queen.

---

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq N \leq 10^6$
- $1 \leq X, Y \leq N$

---

## Examples

**Example 1**

**Input**

```text
5
1 1 1
3 2 2
3 2 1
2 2 2
150 62 41
```

**Output**

```text
0
8
6
3
527
```

**Explanation**

**Test case 1:** The only cell on the board is $(1,1)$. Since Queen stands on this cell, it is not under attack.

**Test case 2:** The Queen can attack the following cells: $\{(1, 1), (1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2), (3, 3)\}$.

**Test case 3:** The Queen can attack the following cells: $\{(1, 1), (1, 2), (2, 2), (2, 3), (3, 1), (3, 2)\}$.

**Test case 4:** The Queen can attack the following cells: $\{(1, 1), (1, 2), (2, 1)\}$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 1 1
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
3 2 2
```

**Output for this case**

```text
8
```



#### Test case 3

**Input for this case**

```text
3 2 1
```

**Output for this case**

```text
6
```



#### Test case 4

**Input for this case**

```text
2 2 2
```

**Output for this case**

```text
3
```



#### Test case 5

**Input for this case**

```text
150 62 41
```

**Output for this case**

```text
527
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/QUEENATTACK)

[Contest: Division 1](https://www.codechef.com/MAY221A/problems/QUEENATTACK)

[Contest: Division 2](https://www.codechef.com/MAY221B/problems/QUEENATTACK)

[Contest: Division 3](https://www.codechef.com/MAY221C/problems/QUEENATTACK)

[Contest: Division 4](https://www.codechef.com/MAY221D/problems/QUEENATTACK)

***Author:*** [Lavish Gupta](https://www.codechef.com/users/lavish_adm)

***Testers:*** [Satyam](https://www.codechef.com/users/satyam_343), [Abhinav Sharma](https://www.codechef.com/users/inov_360)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

To be calculated

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

A queen is placed at cell (X, Y) on a N\times N chessboard. How many cells does it attack?

#
[](#explanation-5)EXPLANATION:

Let’s separately count the squares that are under attack horizontally, vertically, and diagonally. Our answer is the sum of these squares.

-
**Horizontally**: The queen can move any number of squares horizontally. So, every square in its row is under attack, apart from the one it’s standing on. This gives us N-1 squares.

-
**Vertically**: The exact same reasoning as the horizontal case gives us N-1 more squares in this case as well.

-
**Diagonally**: There are two diagonals to consider, so once again we count them separately and add up.

- One diagonal consists of all squares (A, B) such that A+B = X+Y. A little experimenting on paper should show you that the number of squares on this diagonal is the difference between N+1 and X+Y, i.e, |(N+1) - (X+Y)|. Subtract one from this to account for the square the queen is standing on.

- The other diagonal consists of all squares (A, B) such that A - B = X - Y. Once again, a little experimenting will show that the number of squares on this diagonal is N - |X - Y|, from which we subtract one.

Add up the answers to these four cases to obtain the final answer.

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(1) per test.

#
[](#code-7)CODE:

Python
``for _ in range(int(input())):
	n, x, y = map(int, input().split())
	ans = 2*n # row + column
	ans += n - abs(x - y) # diagonal 1
	ans += n - abs(n+1 - (x + y)) # diagonal 2
	print(ans - 4)
``

</details>
