# Instagram

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | INSTAGRAM |
| Difficulty Rating | 408 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [INSTAGRAM](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/INSTAGRAM) |

---

## Problem Statement

Chef categorises an instagram account as *spam*, if, the *following* count of the account is more than $10$ times the count of *followers*.

Given the *following* and *follower* count of an account as $X$ and $Y$ respectively, find whether it is a *spam* account.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two space-separated integers $X$ and $Y$ — the *following* and *follower* count of an account, respectively.

---

## Output Format

For each test case, output on a new line, `YES`, if the account is *spam* and `NO` otherwise.

You may print each character of the string in uppercase or lowercase. For example, the strings `YES`, `yes`, `Yes` and `yES` are identical.

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
1 10
10 1
11 1
97 7
```

**Output**

```text
NO
NO
YES
YES
```

**Explanation**

**Test case $1$:** The following count is $1$ while the follower count is $10$. Since the following count is not more than $10$ times the follower count, the account is not spam.

**Test case $2$:** The following count is $10$ while the follower count is $1$. Since the following count is not **more** than $10$ times the follower count, the account is not spam.

**Test case $3$:** The following count is $11$ while the follower count is $1$. Since the following count is more than $10$ times the follower count, the account is spam.

**Test case $4$:** The following count is $97$ while the follower count is $7$. Since the following count is more than $10$ times the follower count, the account is spam.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 10
```

**Output for this case**

```text
NO
```



#### Test case 2

**Input for this case**

```text
10 1
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
11 1
```

**Output for this case**

```text
YES
```



#### Test case 4

**Input for this case**

```text
97 7
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

[Practice](https://www.codechef.com/problems/INSTAGRAM)

[Contest: Division 1](https://www.codechef.com/START71A/problems/INSTAGRAM)

[Contest: Division 2](https://www.codechef.com/START71B/problems/INSTAGRAM)

[Contest: Division 3](https://www.codechef.com/START71C/problems/INSTAGRAM)

[Contest: Division 4](https://www.codechef.com/START71D/problems/INSTAGRAM)

***Author:*** [notsoloud](https://www.codechef.com/users/notsoloud)

***Testers:*** [iceknight1093](https://www.codechef.com/users/IceKnight1093), [rivalq](https://www.codechef.com/users/rivalq)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

408

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

An Instagram account is considered spam if it follows at least 10 times more accounts than it has followers.

Given X and Y, the following and follower count of an account, decide whether it is a spam account.

#
[](#explanation-5)EXPLANATION:

The problem statement states that the given account is spam if and only if X \gt 10\cdot Y

So, simply check this using an `if` condition:

- The answer is `Yes` if X \gt 10\cdot Y

- The answer is `No` otherwise

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(1) per testcase.

#
[](#code-7)CODE:

Code (Python)
``for _ in range(int(input())):
    x, y = map(int, input().split())
    print('Yes' if x > 10*y else 'No')
``

</details>
