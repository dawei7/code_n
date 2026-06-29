# Reach on Time

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TIMELY |
| Difficulty Rating | 279 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [TIMELY](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/TIMELY) |

---

## Problem Statement

Chef has recently moved into an apartment. It takes $30$ minutes for Chef to reach office from the apartment.

Chef left for the office $X$ minutes before Chef was supposed to reach. Determine whether or not Chef will be able to reach on time.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single integer $X$.

---

## Output Format

For each test case, output `YES` if Chef will reach on time, `NO` otherwise.

The output is case-insensitive. Thus, the strings `YES`, `yes`, `yeS`, and `Yes` are all considered the same.

---

## Constraints

- $1 \leq T \leq 60$
- $1 \leq X \leq 60$

---

## Examples

**Example 1**

**Input**

```text
6
30
60
14
29
31
42
```

**Output**

```text
YES
YES
NO
NO
YES
YES
```

**Explanation**

**Test case 1:** Chef leaves $30$ minutes before he is supposed to reach, so he will reach the office exactly on time since it takes $30$ minutes to commute.

**Test case 2:** Chef will reach $30$ minutes early.

**Test case 3:** Chef will reach 16 minutes late.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
30
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
60
```

**Output for this case**

```text
YES
```



#### Test case 3

**Input for this case**

```text
14
```

**Output for this case**

```text
NO
```



#### Test case 4

**Input for this case**

```text
29
```

**Output for this case**

```text
NO
```



#### Test case 5

**Input for this case**

```text
31
```

**Output for this case**

```text
YES
```



#### Test case 6

**Input for this case**

```text
42
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

[Practice](https://www.codechef.com/problems/TIMELY)

[Contest: Division 1](https://www.codechef.com/START61A/problems/TIMELY)

[Contest: Division 2](https://www.codechef.com/START61B/problems/TIMELY)

[Contest: Division 3](https://www.codechef.com/START61C/problems/TIMELY)

[Contest: Division 4](https://www.codechef.com/START61D/problems/TIMELY)

***Author:*** [Jeevan Jyot Singh](https://www.codechef.com/users/jeevanjyot)

***Testers:*** [Tejas Pandey](https://www.codechef.com/users/tejas10p), [Hriday](https://www.codechef.com/users/the_hyp0cr1t3)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef needs 30 minutes to reach his office from home. He left with X minutes left. Will Chef reach on time?

#
[](#explanation-5)EXPLANATION:

Chef needs at least 30 minutes of time to reach the office. Thus, the answer is “Yes” if X \geq 30 and “No” otherwise. This can be checked using an `if` condition.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    print('Yes' if int(input()) >= 30 else 'No')
``

</details>
