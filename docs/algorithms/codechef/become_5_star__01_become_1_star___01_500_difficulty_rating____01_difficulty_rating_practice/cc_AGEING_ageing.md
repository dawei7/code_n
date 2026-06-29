# Ageing

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | AGEING |
| Difficulty Rating | 299 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [AGEING](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/AGEING) |

---

## Problem Statement

Chef's current age is $20$ years, while Chefina's current age is $10$ years.
Determine Chefina's age when Chef will be $X$ years old.

Note: Assume that Chef and Chefina were born on same day and same month (just different year).

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single integer $X$, the age of Chef.

---

## Output Format

For each test case, output Chefina's age when Chef will be $X$ years old.

---

## Constraints

- $1 \leq T \leq 25$
- $25 \leq X \leq 50$

---

## Examples

**Example 1**

**Input**

```text
4
25
36
50
44
```

**Output**

```text
15
26
40
34
```

**Explanation**

**Test case $1$:** Chefina is $10$ years old when Chef is $20$ years old. Thus, when Chef would be $25$, Chefina would be $15$.

**Test case $2$:** Chefina is $10$ years old when Chef is $20$ years old. Thus, when Chef would be $36$, Chefina would be $26$.

**Test case $3$:** Chefina is $10$ years old when Chef is $20$ years old. Thus, when Chef would be $50$, Chefina would be $40$.

**Test case $4$:** Chefina is $10$ years old when Chef is $20$ years old. Thus, when Chef would be $44$, Chefina would be $34$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
25
```

**Output for this case**

```text
15
```



#### Test case 2

**Input for this case**

```text
36
```

**Output for this case**

```text
26
```



#### Test case 3

**Input for this case**

```text
50
```

**Output for this case**

```text
40
```



#### Test case 4

**Input for this case**

```text
44
```

**Output for this case**

```text
34
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/AGEING)

[Contest: Division 1](https://www.codechef.com/START79A/problems/AGEING)

[Contest: Division 2](https://www.codechef.com/START79B/problems/AGEING)

[Contest: Division 3](https://www.codechef.com/START79C/problems/AGEING)

[Contest: Division 4](https://www.codechef.com/START79D/problems/AGEING)

***Author:*** [abhi_inav](https://www.codechef.com/users/abhi_inav)

***Testers:*** [tabr](https://www.codechef.com/users/tabr), [iceknight1093](https://www.codechef.com/users/iceknight1093)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef is now 20 years old, and Chefina is 10.

When Chef is X years old, how old will Chefina be?

#
[](#explanation-5)EXPLANATION:

Chefina is 10 years younger than Chef.

So, when Chef is X years old, Chefina will be X-10 years old.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    x = int(input())
    print(x - 10)
``

</details>
