# Journey of the Knight

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | KNIGHT2 |
| Difficulty Rating | 1144 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [KNIGHT2](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/KNIGHT2) |

---

## Problem Statement

Chef has an $8 \times 8$ chessboard. He placed a knight on the square $(X_1, Y_1)$. Note that, the square at the intersection of the $i^{th}$ row and $j^{th}$ column is denoted by $(i, j)$.

Chef wants to determine whether the knight can end up at the square $(X_2, Y_2)$ in **exactly** $100$ moves or not.

For reference, a knight can move to a square which is:

- One square horizontally and two squares vertically away from the current square, or
- One square vertically and two squares horizontally away from the current square

A visual description of this may be found [here](https://en.wikipedia.org/wiki/Knight_(chess)#Movement).

---

## Input Format

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first and only line of each test case contains $4$ integers $X_1, Y_1, X_2, Y_2$ — where $(X_1, Y_1)$ denotes the starting square of the knight and $(X_2, Y_2)$ denotes the ending square of the knight.

---

## Output Format

For each test case, output `YES` if knight can move from $(X_1, Y_1)$ to $(X_2, Y_2)$ in **exactly** $100$ moves. Otherwise, output `NO`.

You may print each character of `YES` and `NO` in uppercase or lowercase (for example, `yes`, `yEs`, `Yes` will be considered identical).

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \le X_1, Y_1, X_2, Y_2 \le 8$

---

## Examples

**Example 1**

**Input**

```text
3
1 1 1 1
8 8 7 6
8 8 8 6
```

**Output**

```text
YES
NO
YES
```

**Explanation**

**Test Case 1:** Knight can first move to $(2, 3)$ and then back to $(1, 1)$. He can repeat this $50$ times and he will end up at $(1, 1)$ after $100$ moves.

**Test Case 2:** It can be proven that it is not possible for the knight to end at $(7, 6)$ after $100$ moves.

**Test Case 3:** Knight can first move to $(6, 7)$ and then to $(8, 6)$. After that, he can alternate between $(6, 7)$ and $(8, 6)$ for $49$ times and he will end up at $(8, 6)$ after $100$ moves.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 1 1 1
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
8 8 7 6
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
8 8 8 6
```

**Output for this case**

```text
YES
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest](https://www.codechef.com/JULY221/)

[Practice](https://www.codechef.com/problems/KNIGHT2)

**Setter:** [jeevanjyot](https://www.codechef.com/users/jeevanjyot)

**Testers:** [satyam_343](https://www.codechef.com/users/satyam_343), [rivalq](https://www.codechef.com/users/rivalq)

**Editorialist:** [hrishik85](https://www.codechef.com/users/hrishik85)

#
[](#difficulty-2)DIFFICULTY:

1144

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef has an 8 \times 8 chessboard. He placed a knight on the square (X_1, Y_1). Note that, the square at the intersection of the i^{th} row and j^{th} column is denoted by (i, j).

Chef wants to determine whether the knight can end up at the square (X_2, Y_2) in **exactly** 100 moves or not.

For reference, a knight can move to a square which is:

- One square horizontally and two squares vertically away from the current square, or

- One square vertically and two squares horizontally away from the current square

A visual description of this may be found [here](https://en.wikipedia.org/wiki/Knight_(chess)#Movement).

#
[](#explanation-5)EXPLANATION:

Chef has exactly 100 moves.

Important point to note here is that a knight can travel from one corner of the board at (1,1) to the opposite corner at (8,8) in 6 moves.

- In effect, 100 moves are large enough to have repetitive moves on the chess board.

- If a knight is on any position (X,Y) on an odd move, can it ever be on the same position on the 100^{th} move? Not possible.

In effect, the problem reduces to finding squares that the knight will reach on odd moves. Such squares can never be reached on the 100th move.

Given any (X_1, Y_1) and (X_2, Y_2), if ((X_2+Y_2)-(X_1+Y_1)) is divisible by 2, then the knight can reach (X_2, Y_2) on the 100^{th} move. Else it cannot.

#
[](#time-complexity-6)TIME COMPLEXITY:

Time complexity is O(1).

#
[](#solution-7)SOLUTION:

Editorialist's Solution
``t=int(input())
for _ in range(t):
    x1,y1,x2,y2=map(int,input().split())
    if ((x2+y2)-(x1+y1))%2==0:
        print('YES')
    else:
        print('NO')
``

</details>
