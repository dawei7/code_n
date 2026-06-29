# Maximum Submissions

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MAXIMUMSUBS |
| Difficulty Rating | 435 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [MAXIMUMSUBS](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/MAXIMUMSUBS) |

---

## Problem Statement

A participant can make $1$ submission every $30$ seconds. If a contest lasts for $X$ minutes, what is the maximum number of submissions that the participant can make during it?

It is also given that the participant cannot make any submission in the last $5$ seconds of the contest.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single integer $X$, denoting the number of minutes.

---

## Output Format

For each test case, output the maximum number of submissions a participant can make in $X$ minutes.

---

## Constraints

- $1 \leq T \leq 30$
- $1 \leq X \leq 30$

---

## Examples

**Example 1**

**Input**

```text
4
1
2
3
4
```

**Output**

```text
2
4
6
8
```

**Explanation**

**Test case $1$:** The contest lasts for $1$ minute, which is $60$ seconds. A participant can make $2$ submissions during this time — for example, in the $5$-th second and in the $48$-th second. Making $3$ or more submissions is impossible.

**Test case $2$:** The contest lasts for $2$ minutes, which is $120$ seconds. A participant can make $4$ submissions during this time.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
2
```

**Output for this case**

```text
4
```



#### Test case 3

**Input for this case**

```text
3
```

**Output for this case**

```text
6
```



#### Test case 4

**Input for this case**

```text
4
```

**Output for this case**

```text
8
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/MAXIMUMSUBS)

[Contest: Division 1](https://www.codechef.com/AUG221A/problems/MAXIMUMSUBS)

[Contest: Division 2](https://www.codechef.com/AUG221B/problems/MAXIMUMSUBS)

[Contest: Division 3](https://www.codechef.com/AUG221C/problems/MAXIMUMSUBS)

[Contest: Division 4](https://www.codechef.com/AUG221D/problems/MAXIMUMSUBS)

***Author:*** [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_25dec)

***Testers:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093), [Nishant Shah](https://www.codechef.com/users/nishant403)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

435

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

How many submissions can a participant make in X minutes, if they can make 1 submission every 30 seconds?

#
[](#explanation-5)EXPLANATION:

Every minute is 60 seconds, so there are 60\cdot X seconds in total.

Since one submission can be made every 30 seconds, a total of 60\cdot X / 30 = 2\cdot X submissions can be made.

Thus, the solution is to read X and print 2\cdot X.

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(1) per test case.

#
[](#code-7)CODE:

Editorialist's Code (Python)
``for _ in range(int(input())):
    print(2*int(input()))
``

</details>
