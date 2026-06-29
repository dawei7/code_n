# Nearest Exit

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | NEARESTEXIT |
| Difficulty Rating | 585 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [NEARESTEXIT](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/NEARESTEXIT) |

---

## Problem Statement

There are two exits in a bus with $100$ seats:
- First exit is located beside seat number $1$.
- Second exit is located beside seat number $100$.

Seats are arranged in a straight line from $1$ to $100$ with equal spacing between any $2$ adjacent seats.

A passenger prefers to choose the nearest exit while leaving the bus.

Determine the exit taken by passenger sitting on seat $X$.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists a single integer $X$, denoting the seat number.

---

## Output Format

For each test case, output `LEFT` if the passenger chooses the exit beside seat $1$, `RIGHT` otherwise.

You may print each character of the string in uppercase or lowercase (for example, the strings `LEFT`, `lEft`, `left`, and `lEFT` will all be treated as identical).

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq X \leq 100$

---

## Examples

**Example 1**

**Input**

```text
6
1
50
100
30
51
73
```

**Output**

```text
LEFT
LEFT
RIGHT
LEFT
RIGHT
RIGHT
```

**Explanation**

**Test case $1$:** The exit is located beside seat $1$. Hence, the passenger can take this exit without moving to any other seat.

**Test case $2$:** To take exit at seat $1$, the passenger needs to move $49$ seats. However, to take the exit at seat $100$, the passenger needs to move $50$ seats. Thus, exit at seat $1$ is closer.

**Test case $3$:** The exit is located beside seat $100$. Hence, the passenger can take this exit without moving to any other seat.

**Test case $4$:** To take exit at seat $1$, the passenger needs to move $29$ seats. However, to take the exit at seat $100$, the passenger needs to move $70$ seats. Thus, exit at seat $1$ is closer.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1
```

**Output for this case**

```text
LEFT
```



#### Test case 2

**Input for this case**

```text
50
```

**Output for this case**

```text
LEFT
```



#### Test case 3

**Input for this case**

```text
100
```

**Output for this case**

```text
RIGHT
```



#### Test case 4

**Input for this case**

```text
30
```

**Output for this case**

```text
LEFT
```



#### Test case 5

**Input for this case**

```text
51
```

**Output for this case**

```text
RIGHT
```



#### Test case 6

**Input for this case**

```text
73
```

**Output for this case**

```text
RIGHT
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/NEARESTEXIT)

[Contest: Division 1](https://www.codechef.com/START56A/problems/NEARESTEXIT)

[Contest: Division 2](https://www.codechef.com/START56B/problems/NEARESTEXIT)

[Contest: Division 3](https://www.codechef.com/START56C/problems/NEARESTEXIT)

[Contest: Division 4](https://www.codechef.com/START56D/problems/NEARESTEXIT)

***Author:*** [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_25dec)

***Testers:*** [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_25dec), [Jatin Garg](https://www.codechef.com/users/rivalq)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

387

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

In a bus with 100 seats, a passenger will always choose to exit from the side closest to their seat. The left exit is beside seat 1 and the right exit is beside seat 100.

Which exit will a passenger at seat X choose?

#
[](#explanation-5)EXPLANATION

The left exit is closer to seats 1, 2, \ldots, 50, and the right exit is closer to the other seats.

So, the solution is to print “Left” if X \leq 50 and “Right” otherwise.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    x = int(input())
    print('Left' if x <= 50 else 'Right')
``

</details>
