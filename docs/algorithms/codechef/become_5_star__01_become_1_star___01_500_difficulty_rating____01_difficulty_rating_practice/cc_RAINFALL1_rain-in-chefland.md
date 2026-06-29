# Rain in Chefland

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | RAINFALL1 |
| Difficulty Rating | 328 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [RAINFALL1](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/RAINFALL1) |

---

## Problem Statement

In Chefland, precipitation is measured using a rain gauge in millimetre per hour.

Chef categorises rainfall as:
- `LIGHT`, if rainfall is less than $3$ millimetre per hour.
- `MODERATE`, if rainfall is greater than equal to $3$ millimetre per hour and less than $7$ millimetre per hour.
- `HEAVY` if rainfall is greater than equal to $7$ millimetre per hour.

Given that it rains at $X$ millimetre per hour on a day, find whether the rain is `LIGHT`,` MODERATE`, or `HEAVY`.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single integer $X$ — the rate of rainfall in millimetre per hour.

---

## Output Format

For each test case, output on a new line, whether the rain is `LIGHT`,` MODERATE`, or `HEAVY`.

You may print each character in lowercase or uppercase. For example, `LIGHT`, `light`, `Light`, and `liGHT`, are all identical.

---

## Constraints

- $1 \leq T \leq 20$
- $1 \leq X \leq 20$

---

## Examples

**Example 1**

**Input**

```text
4
1
20
3
7
```

**Output**

```text
LIGHT
HEAVY
MODERATE
HEAVY
```

**Explanation**

**Test case $1$:** The rate of precipitation is less than $3$. Thus, the rain is `LIGHT`.

**Test case $2$:** The rate of precipitation is greater than equal to $7$. Thus, the rain is `HEAVY`.

**Test case $3$:** The rate of precipitation is greater than equal to $3$ and less than $7$. Thus, the rain is `MODERATE`.

**Test case $4$:** The rate of precipitation is greater than equal to $7$. Thus, the rain is `HEAVY`.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1
```

**Output for this case**

```text
LIGHT
```



#### Test case 2

**Input for this case**

```text
20
```

**Output for this case**

```text
HEAVY
```



#### Test case 3

**Input for this case**

```text
3
```

**Output for this case**

```text
MODERATE
```



#### Test case 4

**Input for this case**

```text
7
```

**Output for this case**

```text
HEAVY
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/RAINFALL1)

[Contest: Division 1](https://www.codechef.com/START69A/problems/RAINFALL1)

[Contest: Division 2](https://www.codechef.com/START69B/problems/RAINFALL1)

[Contest: Division 3](https://www.codechef.com/START69C/problems/RAINFALL1)

[Contest: Division 4](https://www.codechef.com/START69D/problems/RAINFALL1)

***Author:*** [notsoloud](https://www.codechef.com/users/notsoloud)

***Testers:*** [iceknight1093](https://www.codechef.com/users/IceKnight1093), [mexomerf](https://www.codechef.com/users/mexomerf)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

328

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Given the amount of rain received in a day, X, decide whether the rainfall was `LIGHT`, `MODERATE`, or `HEAVY`.

#
[](#explanation-5)EXPLANATION:

Simply implement the checks mentioned in the statement and print the appropriate answer.

- If X \lt 3, the answer is `LIGHT`

- If 3 \leq X \lt 7, the answer is `MODERATE`

- If 7 \leq X, the answer is `HEAVY`

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(1) per testcase.

#
[](#code-7)CODE:

Code (Python)
``for _ in range(int(input())):
    x = int(input())
    print('Light' if x < 3 else ('Moderate' if x < 7 else 'Heavy'))
``

</details>
