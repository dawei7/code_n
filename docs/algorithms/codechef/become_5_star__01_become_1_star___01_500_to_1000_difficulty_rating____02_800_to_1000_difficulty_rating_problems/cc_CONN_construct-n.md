# Construct N

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CONN |
| Difficulty Rating | 860 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 800 to 1000 difficulty rating problems |
| Official Link | [CONN](https://www.codechef.com/practice/course/logical-problems/DIFF1000/problems/CONN) |

---

## Problem Statement

You are given an integer $N$. Find if it is possible to represent $N$ as the sum of several(possibly zero) $2$'s and several(possibly zero) $7$'s.

Formally, find if there exist two integers $X, Y \ (X, Y \ge 0)$ such that $2 \cdot X + 7\cdot Y = N$.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single line containing an integer $N$.

---

## Output Format

For each test case, print on a new line `YES` if it is possible to represent $N$ as the sum of several(possibly zero) $2$'s and several(possibly zero) $7$'s and `NO` otherwise.

You may print each character of the string in either uppercase or lowercase (for example, the strings `yEs`, `yes`, `Yes`, and `YES` will all be treated as identical).

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 10^8$

---

## Examples

**Example 1**

**Input**

```text
4
2
5
7
11
```

**Output**

```text
YES
NO
YES
YES
```

**Explanation**

**Test case $1$:** $2 \cdot 1 + 7\cdot 0 = 2$.

**Test case $2$:** It is impossible to express $5$ as a sum of several $2$'s and $7$'s.

**Test case $3$:** $2 \cdot 0 + 7\cdot 1 = 7$.

**Test case $4$:** $2 \cdot 2 + 7\cdot 1 = 11$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
5
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
7
```

**Output for this case**

```text
YES
```



#### Test case 4

**Input for this case**

```text
11
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

[Contest](https://www.codechef.com/START47/)

[Practice](https://www.codechef.com/problems/CONN)

**Setter:** [soumyadeep_21](https://www.codechef.com/users/soumyadeep_21)([https://www.codechef.com/users/abhi_inav](https://www.codechef.com/users/abhi_inav))

**Testers:** [inov_360](https://www.codechef.com/users/inov_360), [mexomerf](https://www.codechef.com/users/mexomerf)

**Editorialist:** [hrishik85](https://www.codechef.com/users/hrishik85)

#
[](#difficulty-2)DIFFICULTY:

860

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Given an integer N, we have to output if

-
N can be represented as  N = 2 \times X + 7 \times Y

- where X, Y \geq 0

#
[](#explanation-5)EXPLANATION:

If you write out an example sequence of numbers [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] you realise that the only numbers which cannot be represented in the format required are [1, 3, 5].

For N \geq 7, all numbers can be represented in the format above.

#
[](#time-complexity-6)TIME COMPLEXITY:

Time complexity is O(1).

#
[](#solution-7)SOLUTION:

Editorialist's Solution
``t=int(input())
for _ in range(t):
    N=int(input())
    if N>=7:
        print('YES')
    else:
        if N%2==0:
            print('YES')
        else:
            print('NO')
``

</details>
