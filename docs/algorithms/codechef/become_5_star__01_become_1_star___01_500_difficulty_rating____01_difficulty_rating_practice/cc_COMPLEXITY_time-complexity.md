# Time Complexity

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | COMPLEXITY |
| Difficulty Rating | 364 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [COMPLEXITY](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/COMPLEXITY) |

---

## Problem Statement

A sorting algorithm $A$ is said to have more time complexity than a sorting algorithm $B$ if it uses more number of comparisons for sorting the same array than algorithm $B$.

Given that algorithm $A$ uses $X$ comparisons to sort an array and algorithm $B$ uses $Y$ comparisons to sort the same array, find whether algorithm $A$ has more time complexity.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two space-separated integers $X$ and $Y$ — the number of comparisons used by algorithms $A$ and $B$ to sort the array respectively.

---

## Output Format

For each test case, output on a new line, `YES`, if the algorithm $A$ has more time complexity than $B$ and `NO` otherwise.

You may print each character of the string in uppercase or lowercase (for example, the strings `YES`, `yEs`, `yes`, and `yeS` will all be treated as identical).

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq X, Y \leq 100$

---

## Examples

**Example 1**

**Input**

```text
4
9 9
15 7
10 19
21 20
```

**Output**

```text
NO
YES
NO
YES
```

**Explanation**

**Test case $1$:** The number of comparisons used by algorithm $A$ is $9$ and that used by $B$ is also $9$. Since the number of comparisons used by $A$ is not more than that of $B$, $A$ does not have more time complexity than $B$.

**Test case $2$:** The number of comparisons used by algorithm $A$ is $15$ and that used by $B$ is $7$. Since the number of comparisons used by $A$ is more than that of $B$, $A$ does have more time complexity than $B$.

**Test case $3$:** The number of comparisons used by algorithm $A$ is $10$ and that used by $B$ is $19$. Since the number of comparisons used by $A$ is not more than that of $B$, $A$ does not have more time complexity than $B$.

**Test case $4$:** The number of comparisons used by algorithm $A$ is $21$ and that used by $B$ is $20$. Since the number of comparisons used by $A$ is more than that of $B$, $A$ does have more time complexity than $B$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
9 9
```

**Output for this case**

```text
NO
```



#### Test case 2

**Input for this case**

```text
15 7
```

**Output for this case**

```text
YES
```



#### Test case 3

**Input for this case**

```text
10 19
```

**Output for this case**

```text
NO
```



#### Test case 4

**Input for this case**

```text
21 20
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

[Practice](https://www.codechef.com/problems/COMPLEXITY)

[Contest: Division 1](https://www.codechef.com/NOV221A/problems/COMPLEXITY)

[Contest: Division 2](https://www.codechef.com/NOV221B/problems/COMPLEXITY)

[Contest: Division 3](https://www.codechef.com/NOV221C/problems/COMPLEXITY)

[Contest: Division 4](https://www.codechef.com/NOV221D/problems/COMPLEXITY)

***Author:*** [Kanhaiya Mohan](https://www.codechef.com/users/notsoloud)

***Testers:*** [Takuki Kurokawa](https://www.codechef.com/users/tabr), [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_25dec)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

364

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Sorting algorithm A uses X comparisons and B uses Y comparisons to sort an array. Does A have more time complexity?

#
[](#explanation-5)EXPLANATION:

According to the statement, the answer is “Yes” if X \gt Y and “No” otherwise.

This can be checked using an `if` condition.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    x, y = map(int, input().split())
    print('Yes' if x > y else 'No')
``

</details>
