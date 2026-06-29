# Chefland Games

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHEFGAMES |
| Difficulty Rating | 550 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [CHEFGAMES](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/CHEFGAMES) |

---

## Problem Statement

In Chefland, a tennis game involves $4$ referees.
Each referee has to point out whether he considers the ball to be inside limits or outside limits. The ball is considered to be `IN` if and only if **all** the referees agree that it was inside limits.

Given the decision of the $4$ referees, help Chef determine whether the ball is considered inside limits or not.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single line of input containing $4$ integers $R_1, R_2, R_3, R_4$ denoting the decision of the respective referees.

Here $R$ can be either $0$ or $1$ where $0$ would denote that the referee considered the ball to be inside limits whereas $1$ denotes that they consider it to be outside limits.

---

## Output Format

For each test case, output `IN` if the ball is considered to be inside limits by all referees and `OUT` otherwise.

The checker is case-insensitive so answers like `in`, `In`, and `IN` would be considered the same.

---

## Constraints

- $1 \leq T \leq 20$
- $0 \leq R_1, R_2, R_3, R_4 \leq 1$

---

## Examples

**Example 1**

**Input**

```text
4
1 1 0 0
0 0 0 0
0 0 0 1
1 1 1 1
```

**Output**

```text
OUT
IN
OUT
OUT
```

**Explanation**

**Test case $1$:** Referees $1$ and $2$ do not consider the ball to be `IN`. Thus, the ball is `OUT`.

**Test case $2$:** All referees consider the ball to be `IN`. Thus, the ball is `IN`.

**Test case $3$:** Referee $4$ does not consider the ball to be `IN`. Thus, the ball is `OUT`.

**Test case $4$:** No referee considers the ball to be `IN`. Thus, the ball is `OUT`.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 1 0 0
```

**Output for this case**

```text
OUT
```



#### Test case 2

**Input for this case**

```text
0 0 0 0
```

**Output for this case**

```text
IN
```



#### Test case 3

**Input for this case**

```text
0 0 0 1
```

**Output for this case**

```text
OUT
```



#### Test case 4

**Input for this case**

```text
1 1 1 1
```

**Output for this case**

```text
OUT
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/CHEFGAMES)

[Contest: Division 1](https://www.codechef.com/START56A/problems/CHEFGAMES)

[Contest: Division 2](https://www.codechef.com/START56B/problems/CHEFGAMES)

[Contest: Division 3](https://www.codechef.com/START56C/problems/CHEFGAMES)

[Contest: Division 4](https://www.codechef.com/START56D/problems/CHEFGAMES)

***Author:*** [Tejas Pandey](https://www.codechef.com/users/tejas10p)

***Testers:*** [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_25dec), [Jatin Garg](https://www.codechef.com/users/rivalq)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

365

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Given the decisions of four referees as to whether a ball was in or out, decide whether the ball was indeed in or not. It is considered to be in if and only if all 4 referees say that it is in.

#
[](#explanation-5)EXPLANATION

Simply check if all 4 numbers given in the input are 0 or not. If they are, print “In”, otherwise print “Out”.

This check can be done in several ways, for example:

- Apply an if condition to each input integer

- Or, find the sum of all 4 numbers and check if this is zero

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    print('In' if sum(map(int, input().split())) == 0 else 'Out')
``

</details>
