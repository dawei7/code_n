# Masterchef finals

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TOP10 |
| Difficulty Rating | 255 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [TOP10](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/TOP10) |

---

## Problem Statement

Chef has been working hard to compete in MasterChef.
He is ranked $X$ out of all contestants. However, only $10$ contestants would be selected for the finals.

Check whether Chef made it to the top $10$ or not?

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of one integers $X$ — the current rank of Chef.

---

## Output Format

For each test case, output on a new line, `YES`, if Chef made it to the top $10$ and `NO` otherwise.

Each character of the output may be printed in either uppercase or lowercase. That is, the strings `NO`, `no`, `nO`, and `No` will be treated as equivalent.

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
15
10
1
50
```

**Output**

```text
NO
YES
YES
NO
```

**Explanation**

**Test case $1$:** Chef's rank is $15$ which is greater than $10$. Thus, Chef did not make it to the top $10$.

**Test case $2$:** Chef's rank is $10$ which is equal to $10$. Thus, Chef made it to the top $10$.

**Test case $3$:** Chef made it to the top $10$, as his rank is $1$.

**Test case $4$:** Chef did not make it to the top $10$ as his rank is $50$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
15
```

**Output for this case**

```text
NO
```



#### Test case 2

**Input for this case**

```text
10
```

**Output for this case**

```text
YES
```



#### Test case 3

**Input for this case**

```text
1
```

**Output for this case**

```text
YES
```



#### Test case 4

**Input for this case**

```text
50
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

[Practice](https://www.codechef.com/problems/TOP10)

[Contest: Division 1](https://www.codechef.com/START88A/problems/TOP10)

[Contest: Division 2](https://www.codechef.com/START88B/problems/TOP10)

[Contest: Division 3](https://www.codechef.com/START88C/problems/TOP10)

[Contest: Division 4](https://www.codechef.com/START88D/problems/TOP10)

***Author:*** [notsoloud](https://www.codechef.com/users/notsoloud)

***Tester:*** [jay_1048576](https://www.codechef.com/users/jay_1048576)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

255

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

The top 10 contestants qualify to the finals of MasterChef, and Chef’s rank is X.

Will he qualify?

#
[](#explanation-5)EXPLANATION:

As mentioned in the statement, the answer is `Yes` if X \leq 10 and `No` otherwise.

This can be checked using an `if` condition.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    x = int(input())
    print('Yes' if x <= 10 else 'No')
``

</details>
