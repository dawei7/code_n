# Just One More Episode

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ONEMORE |
| Difficulty Rating | 320 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [ONEMORE](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/ONEMORE) |

---

## Problem Statement

Chef has to attend an exam that starts in $X$ minutes, but of course, watching shows takes priority.

Every episode of the show that Chef is watching, is $24$ minutes long.
If he starts watching a new episode now, will he finish watching it **strictly before** the exam starts?

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of one line of input, containing a single integer $X$ — the amount of time from now at which Chef's exam starts.

---

## Output Format

For each test case, output on a new line the answer — `YES` if Chef will finish his episode before the exam starts, and `NO` otherwise.

Each character of the output may be printed in either lowercase or uppercase, i.e, the string `Yes`, `YES`, `yes`, YeS` will all be treated as equivalent.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq X \leq 100$

---

## Examples

**Example 1**

**Input**

```text
4
30
23
60
24
```

**Output**

```text
Yes
No
Yes
No
```

**Explanation**

**Test case $1$:** Chef has $30$ minutes of free time, which is easily enough to finish watching a $24$-minute episode. Hence, the answer is `Yes`.

**Test case $2$:** Chef has $23$ minutes of free time, which is not enough to finish watching a $24$-minute episode. Hence, the answer is `No`.

**Test case $3$:** Chef has $60$ minutes of free time, which is easily enough to finish watching a $24$-minute episode. Hence, the answer is `Yes`.

**Test case $4$:** Chef has $24$ minutes of free time. He will finish watching the episode exactly when the exam starts, and not **strictly** before it. Hence, the answer is `No`.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
30
```

**Output for this case**

```text
Yes
```



#### Test case 2

**Input for this case**

```text
23
```

**Output for this case**

```text
No
```



#### Test case 3

**Input for this case**

```text
60
```

**Output for this case**

```text
Yes
```



#### Test case 4

**Input for this case**

```text
24
```

**Output for this case**

```text
No
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/ONEMORE)

[Contest: Division 1](https://www.codechef.com/START80A/problems/ONEMORE)

[Contest: Division 2](https://www.codechef.com/START80B/problems/ONEMORE)

[Contest: Division 3](https://www.codechef.com/START80C/problems/ONEMORE)

[Contest: Division 4](https://www.codechef.com/START80D/problems/ONEMORE)

***Author:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

***Testers:*** [wuhudsm](https://www.codechef.com/users/wuhudsm), [satyam_343](https://www.codechef.com/users/satyam_343)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef has X minutes of time before an exam, and wants to watch an episode that’s 24 minutes long. Can he finish it?

#
[](#explanation-5)EXPLANATION:

As per the problem statement, the answer is `Yes` if X \gt 24 and `No` otherwise.

This can be checked using a conditional statement.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    x = int(input())
    print('Yes' if x > 24 else 'No')
``

</details>
