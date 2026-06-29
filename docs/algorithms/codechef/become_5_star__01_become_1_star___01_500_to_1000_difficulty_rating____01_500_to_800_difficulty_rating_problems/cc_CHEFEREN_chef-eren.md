# Chef Eren

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHEFEREN |
| Difficulty Rating | 706 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [CHEFEREN](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/CHEFEREN) |

---

## Problem Statement

Chef is a very big fan of Eren Yeager.

In the last season of Attack on Titan, there were $N$ episodes numbered from $1$ to $N$.
Each even indexed episode was $A$ minutes long and each odd indexed episode was $B$ minutes long.

Calculate the total duration (in minutes) of the last season.

---

## Input Format

- The first line of input contains a single integer $T$, the number of test cases.
- The first and only line of each test case contains three integers $N$, $A,$ and $B$, the number of episodes and the durations of each even-indexed and odd-indexed episodes respectively in minutes.

---

## Output Format

For each test case, print a single integer on a new line, the total duration of the last season in minutes.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 60$
- $1 \leq A, B \leq 60$

---

## Examples

**Example 1**

**Input**

```text
3
1 2 2
2 3 4
4 20 30
```

**Output**

```text
2
7
100
```

**Explanation**

**Test case $1$:** There is only one episode, so there is $1$ odd-indexed episode, and $0$ even-indexed episode. The total duration of the season $= 0\cdot A + 1\cdot B = 0\cdot 2 + 1\cdot 2 = 2$.

**Test case $2$:** There are two episodes with indices $\{1, 2\}$. Thus, there is $1$ odd-indexed episode $(\{1\})$, and $1$ even-indexed episode $(\{2\})$. The total duration of the season $= 1\cdot A + 1\cdot B = 1\cdot 3 + 1\cdot 4 = 7$.

**Test case $3$**: There are four episodes with indices $\{1, 2, 3, 4\}$. Thus, there are $2$ odd-indexed episodes $(\{1, 3\})$, and $2$ even-indexed episodes $(\{2, 4\})$. The total duration of the season $= 2\cdot A + 2\cdot B = 2\cdot 20 + 2\cdot 30 = 100$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 2 2
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
2 3 4
```

**Output for this case**

```text
7
```



#### Test case 3

**Input for this case**

```text
4 20 30
```

**Output for this case**

```text
100
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/CHEFEREN)

[Contest: Division 1](https://www.codechef.com/START83A/problems/CHEFEREN)

[Contest: Division 2](https://www.codechef.com/START83B/problems/CHEFEREN)

[Contest: Division 3](https://www.codechef.com/START83C/problems/CHEFEREN)

[Contest: Division 4](https://www.codechef.com/START83D/problems/CHEFEREN)

***Author:*** [pd_codes](https://www.codechef.com/users/pd_codes)

***Tester:*** [yash_daga](https://www.codechef.com/users/yash_daga)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

There are N episodes, numbered starting from 1.

The even-numbered episodes are A minutes long each, while the odd-numbered ones are B minutes long.

How many minutes will it take to watch all N episodes?

#
[](#explanation-5)EXPLANATION:

Since the constraints are small, it’s possible to simply run a loop from 1 to N and add either A or B to the answer, depending on whether the current episode is odd- or even-numbered.

There’s also a solution in \mathcal{O}(1) by noting that the number of even episodes is exactly \lfloor \frac N2 \rfloor and the number of odd episodes is \lceil \frac N2 \rceil. Hence the answer is

A\left\lfloor \frac N2 \right\rfloor + B\left\lceil \frac N2 \right \rceil

where \lfloor \ \rfloor and \lceil \ \rceil denote the floor and ceiling functions, respectively.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    n, a, b = map(int, input().split())
    print(a*(n//2) + b*(n - n//2))
``

</details>
