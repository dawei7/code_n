# Audible Range

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | AUDIBLE |
| Difficulty Rating | 279 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [AUDIBLE](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/AUDIBLE) |

---

## Problem Statement

Chef's dog *binary* hears frequencies starting from $67$ Hertz to $45000$ Hertz (both inclusive).

If Chef's commands have a frequency of $X$ Hertz, find whether *binary* can hear them or not.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single integer $X$ - the frequency of Chef's commands in Hertz.

---

## Output Format

For each test case, output on a new line `YES`, if *binary* can hear Chef's commands. Otherwise, print `NO`.

The output is case-insensitive. Thus, the strings `YES`, `yes`, `yeS`, and `Yes` are all considered the same.

---

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq X \leq 10^6$

---

## Examples

**Example 1**

**Input**

```text
5
42
67
402
45000
45005
```

**Output**

```text
NO
YES
YES
YES
NO
```

**Explanation**

**Test case $1$:** Chef's command has a frequency of $42$ Hertz which is less than $67$. Thus, it would not be audible to *binary*.

**Test case $2$:** Chef's command has a frequency of $67$ Hertz which lies in the range $[67, 45000]$. Thus, it would be audible to *binary*.

**Test case $3$:** Chef's command has a frequency of $402$ Hertz which lies in the range $[67, 45000]$. Thus, it would be audible to *binary*.

**Test case $4$:** Chef's command has a frequency of $45000$ Hertz which lies in the range $[67, 45000]$. Thus, it would be audible to *binary*.

**Test case $5$:** Chef's command has a frequency of $45005$ Hertz which is greater than $45000$. Thus, it would not be audible to *binary*.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
42
```

**Output for this case**

```text
NO
```



#### Test case 2

**Input for this case**

```text
67
```

**Output for this case**

```text
YES
```



#### Test case 3

**Input for this case**

```text
402
```

**Output for this case**

```text
YES
```



#### Test case 4

**Input for this case**

```text
45000
```

**Output for this case**

```text
YES
```



#### Test case 5

**Input for this case**

```text
45005
```

**Output for this case**

```text
NO
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/AUDIBLE)

[Contest: Division 1](https://www.codechef.com/START59A/problems/AUDIBLE)

[Contest: Division 2](https://www.codechef.com/START59B/problems/AUDIBLE)

[Contest: Division 3](https://www.codechef.com/START59C/problems/AUDIBLE)

[Contest: Division 4](https://www.codechef.com/START59D/problems/AUDIBLE)

***Author:*** [Kanhaiya Mohan](https://www.codechef.com/users/notsoloud)

***Tester:*** [Takuki Kurokawa](https://www.codechef.com/users/tabr)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef’s dog *binary* hears frequencies starting from 67 Hertz to 45000 Hertz (both inclusive).

If Chef’s commands have a frequency of X Hertz, find whether *binary* can hear them or not.

#
[](#explanation-5)EXPLANATION:

This is a direct application of `if` conditions: print “Yes” if X \geq 67 and X \leq 45000, and “No” otherwise.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    print('yes' if 67 <= int(input()) <= 45000 else 'no')
``

</details>
