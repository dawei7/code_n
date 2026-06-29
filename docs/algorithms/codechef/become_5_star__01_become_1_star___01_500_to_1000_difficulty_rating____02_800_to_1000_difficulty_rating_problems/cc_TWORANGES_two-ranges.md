# Two Ranges

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TWORANGES |
| Difficulty Rating | 918 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 800 to 1000 difficulty rating problems |
| Official Link | [TWORANGES](https://www.codechef.com/practice/course/logical-problems/DIFF1000/problems/TWORANGES) |

---

## Problem Statement

Chef has two ranges $[A, B]$ and $[C, D]$. Chef needs to find the number of integers that belong to **at least** one of the ranges.

Note: A range $[P, Q]$ contains **all** the integers $\{P, P+1, P+2, \dots, Q-1, Q\}$.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single line containing $4$ integers $A, B, C,$ and $D$, as mentioned in the statement.

---

## Output Format

For each test case, output on a new line, the number of integers that belong to at least one of the ranges.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq A \leq B \leq 8$
- $1 \leq C \leq D \leq 8$

---

## Examples

**Example 1**

**Input**

```text
4
1 3 5 5
3 8 2 5
1 8 4 6
5 5 5 5
```

**Output**

```text
4
7
8
1
```

**Explanation**

**Test case $1$:** There are $4$ integers that belong to at least one of the ranges. These are $1, 2, 3,$ and $5$.

**Test case $2$:** There are $7$ integers that belong to at least one of the ranges. These are $2, 3, 4, 5, 6, 7,$ and $8$.

**Test case $3$:** There are $8$ integers that belong to at least one of the ranges. These are $1, 2, 3, 4, 5, 6, 7,$ and $8$.

**Test case $4$:** There is only $1$ integer that belong to at least one of the ranges. That integer is $5$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 3 5 5
```

**Output for this case**

```text
4
```



#### Test case 2

**Input for this case**

```text
3 8 2 5
```

**Output for this case**

```text
7
```



#### Test case 3

**Input for this case**

```text
1 8 4 6
```

**Output for this case**

```text
8
```



#### Test case 4

**Input for this case**

```text
5 5 5 5
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/TWORANGES)

[Contest: Division 1](https://www.codechef.com/START75A/problems/TWORANGES)

[Contest: Division 2](https://www.codechef.com/START75B/problems/TWORANGES)

[Contest: Division 3](https://www.codechef.com/START75C/problems/TWORANGES)

[Contest: Division 4](https://www.codechef.com/START75D/problems/TWORANGES)

***Author:*** [utkarsh_25dec](https://www.codechef.com/users/utkarsh_25dec)

***Testers:*** [iceknight1093](https://www.codechef.com/users/iceknight1093), [rivalq](https://www.codechef.com/users/rivalq)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Given two ranges [A, B] and [C, D]; count the number of integers contained in their union.

#
[](#explanation-5)EXPLANATION:

Notice that the bounds on the ranges are quite small; between 1 and 8.

This means the union of the ranges is also a subset of \{1, 2, 3, 4, 5, 6, 7,  8\}.

So, for each integer from 1 to 8, check whether it belongs to one of the ranges.

That is, for each 1 \leq x \leq 8, check at least one of

-
A \leq x \leq B; or

- C \leq x \leq D

is true.

The number of x satisfying this condition is the answer.

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(1) per testcase.

#
[](#code-7)CODE:

Code (Python)
``for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    ans = 0
    for i in range(1, 9):
        if a <= i <= b or c <= i <= d: ans += 1
    print(ans)
``

</details>
