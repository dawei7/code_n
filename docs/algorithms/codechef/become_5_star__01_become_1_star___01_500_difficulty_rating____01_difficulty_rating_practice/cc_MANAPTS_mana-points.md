# Mana Points

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MANAPTS |
| Difficulty Rating | 327 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [MANAPTS](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/MANAPTS) |

---

## Problem Statement

Chef is playing a mobile game. In the game, Chef's character *Chefario* can perform special attacks. However, one special attack costs $X$ mana points to Chefario.

If Chefario currently has $Y$ mana points, determine the **maximum** number of special attacks he can perform.

---

## Input Format

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first and only line of each test case contains two space-separated integers $X$ and $Y$ — the cost of one special attack and the number of mana points Chefario has initially.

---

## Output Format

For each test case, output the maximum number of special attacks Chefario can perform.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \le X \le 100$
- $1 \le Y \le 1000$

---

## Examples

**Example 1**

**Input**

```text
3
10 30
6 41
50 2
```

**Output**

```text
3
6
0
```

**Explanation**

**Test case $1$:** Chefario can perform a maximum of $3$ special attacks which will cost him $30$ mana points.

**Test case $2$:** Chefario can perform a maximum of $6$ special attacks which will cost him $36$ mana points. Note that Chefario can not perform $7$ special attacks as these will cost him $42$ mana points while he has only $41$ mana points.

**Test case $3$:** Chefario will not be able to perform any special attacks in this case.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
10 30
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
6 41
```

**Output for this case**

```text
6
```



#### Test case 3

**Input for this case**

```text
50 2
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/MANAPTS)

[Contest: Division 1](https://www.codechef.com/START74A/problems/MANAPTS)

[Contest: Division 2](https://www.codechef.com/START74B/problems/MANAPTS)

[Contest: Division 3](https://www.codechef.com/START74C/problems/MANAPTS)

[Contest: Division 4](https://www.codechef.com/START74D/problems/MANAPTS)

***Author:*** [jeevanjyot](https://www.codechef.com/users/jeevanjyot)

***Testers:*** [nishant403](https://www.codechef.com/users/nishant403), [satyam_343](https://www.codechef.com/users/satyam_343)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chefario has Y mana, and using a special move costs X mana. How many special moves can Chefario use?

#
[](#explanation-5)EXPLANATION:

The number of special moves that can be used is exactly

\left\lfloor \frac{Y}{X} \right\rfloor

where \left\lfloor a \right\rfloor denotes the largest integer that doesn’t exceed a, i.e, the [floor](https://en.wikipedia.org/wiki/Floor_and_ceiling_functions) function.

This can be computed using `y/x` in C++ and Java, and `y//x` in Python.

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(1) per testcase.

#
[](#code-7)CODE:

Code (Python)
``for _ in range(int(input())):
    x, y = map(int, input().split())
    print(y//x)
``

</details>
