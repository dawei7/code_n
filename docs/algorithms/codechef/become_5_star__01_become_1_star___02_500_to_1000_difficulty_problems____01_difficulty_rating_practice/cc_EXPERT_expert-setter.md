# Expert Setter

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | EXPERT |
| Difficulty Rating | 561 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [EXPERT](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/EXPERT) |

---

## Problem Statement

A problem setter is called an *expert* if **at least** $50 \%$ of their problems are approved by Chef.

Munchy submitted $X$ problems for approval. If $Y$ problems out of those were approved, find whether Munchy is an *expert* or not.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a two space-separated integers $X$ and $Y$ - the number of problems submitted and the number of problems that were approved by Chef.

---

## Output Format

For each test case, output on a new line `YES`, if Munchy is an *expert*. Otherwise, print `NO`.

The output is case-insensitive. Thus, the strings `YES`, `yes`, `yeS`, and `Yes` are all considered the same.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq Y \le X \leq 10^6$

---

## Examples

**Example 1**

**Input**

```text
4
5 3
1 1
4 1
2 1
```

**Output**

```text
YES
YES
NO
YES
```

**Explanation**

**Test case $1$:** We are given that $3$ out of $5$ problems were approved. Thus, $60 \%$ of the problems were approved. Since at least $50 \%$ of the problems were approved, Munchy is an *expert*.

**Test case $2$:** We are given that $1$ out of $1$ problems were approved. Thus, $100 \%$ of the problems were approved. Since at least $50 \%$ of the problems were approved, Munchy is an *expert*.

**Test case $3$:** We are given that $1$ out of $4$ problems were approved. Thus, $25 \%$ of the problems were approved. Since at least $50 \%$ of the problems were not approved, Munchy is not an *expert*.

**Test case $4$:** We are given that $1$ out of $2$ problems were approved. Thus, $50 \%$ of the problems were approved. Since at least $50 \%$ of the problems were approved, Munchy is an *expert*.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 3
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
1 1
```

**Output for this case**

```text
YES
```



#### Test case 3

**Input for this case**

```text
4 1
```

**Output for this case**

```text
NO
```



#### Test case 4

**Input for this case**

```text
2 1
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

[Practice](https://www.codechef.com/problems/EXPERT)

[Contest: Division 1](https://www.codechef.com/START60A/problems/EXPERT)

[Contest: Division 2](https://www.codechef.com/START60B/problems/EXPERT)

[Contest: Division 3](https://www.codechef.com/START60C/problems/EXPERT)

[Contest: Division 4](https://www.codechef.com/START60D/problems/EXPERT)

***Author:*** [Kanhaiya Mohan](https://www.codechef.com/users/notsoloud)

***Tester:*** [Tejas Pandey](https://www.codechef.com/users/tejas10p)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

561

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

A problemsetter has proposed X problems and Y out of them were approved. Is Y at least 50\% of X?

#
[](#explanation-5)EXPLANATION:

It is enough to directly check the condition: for Y to be at least 50\% of X, Y must satisfy the inequality 2Y \geq X.

So,

- The answer is “Yes” if 2Y \geq X

- The answer is “No” otherwise

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    x, y = map(int, input().split())
    print('Yes' if 2*y >= x else 'No')
``

</details>
