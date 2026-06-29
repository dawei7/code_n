# X Jumps

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | XJUMP |
| Difficulty Rating | 686 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [XJUMP](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/XJUMP) |

---

## Problem Statement

Chef is currently standing at stair $0$ and he wants to reach stair numbered $X$.

Chef can climb either $Y$ steps or $1$ step in one move.
Find the **minimum** number of moves required by him to reach **exactly** the stair numbered $X$.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single line of input containing two space separated integers $X$ and $Y$ denoting the number of stair Chef wants to reach and the number of stairs he can climb in one move.

---

## Output Format

For each test case, output the **minimum** number of moves required by him to reach **exactly** the stair numbered $X$.

---

## Constraints

- $1 \leq T \leq 500$
- $1 \leq X, Y \leq 100$

---

## Examples

**Example 1**

**Input**

```text
4
4 2
8 3
3 4
2 1
```

**Output**

```text
2
4
3
2
```

**Explanation**

**Test case $1$:** Chef can make $2$ moves and climb $2$ steps in each move to reach stair numbered $4$.

**Test case $2$:** Chef can make a minimum of $4$ moves. He can climb $3$ steps in $2$ of those moves and $1$ step each in remaining $2$ moves to reach stair numbered $8$.

**Test case $3$:** Chef can make $3$ moves and climb $1$ step in each move to reach stair numbered $3$.

**Test case $4$:** Chef can make $2$ moves and climb $1$ step in each move to reach stair numbered $2$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4 2
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
8 3
```

**Output for this case**

```text
4
```



#### Test case 3

**Input for this case**

```text
3 4
```

**Output for this case**

```text
3
```



#### Test case 4

**Input for this case**

```text
2 1
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

[Practice](https://www.codechef.com/problems/XJUMP)

[Contest: Division 1](https://www.codechef.com/START62A/problems/XJUMP)

[Contest: Division 2](https://www.codechef.com/START62B/problems/XJUMP)

[Contest: Division 3](https://www.codechef.com/START62C/problems/XJUMP)

[Contest: Division 4](https://www.codechef.com/START62D/problems/XJUMP)

***Author:*** [Tejas Pandey](https://www.codechef.com/users/tejas10p)

***Testers:*** [Nishank Suresh](https://www.codechef.com/users/iceknight1093), [Takuki Kurokawa](https://www.codechef.com/users/tabr)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

686

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef can climb either Y stairs or 1 stair in a single move. What’s the minimum number of moves to reach stair X?

#
[](#explanation-5)EXPLANATION:

If possible, it’s better to use one move to climb Y stairs rather than 1, since Y \geq 1.

That gives an easy greedy strategy.

- Let C denote the current stair Chef is on.

- If C+Y \leq X, use one move to climb Y stairs.

- Otherwise, climb one stair.

Directly implementing this using a loop is enough to get AC.

Thinking a little more should also give you a simple formula for the answer:

\left\lfloor \frac{X}{Y} \right\rfloor + (X\bmod Y)

where (X\bmod Y) is the remainder when X is divided by Y, represented by `X % Y` in most languages.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    x, y = map(int, input().split())
    print(x//y + x%y)
``

</details>
