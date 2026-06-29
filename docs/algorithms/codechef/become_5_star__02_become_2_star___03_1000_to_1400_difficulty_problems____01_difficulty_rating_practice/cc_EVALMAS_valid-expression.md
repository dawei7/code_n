# Valid Expression

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | EVALMAS |
| Difficulty Rating | 1354 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [EVALMAS](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/EVALMAS) |

---

## Problem Statement

The correct way of evaluating an expression with $*, +,$ and $-$ is, first multiplication, then addition, and then subtraction. For example, the expression $2+3*7-5 = 2+21-5 = 23-5 = 18$.

You are given integers $N$ and $X$. Your task is to generate a string $S$ of length $N$ consisting **only** of $*, +,$ and $-$ such that when these $N$ operators are placed in order between $(N+1)$ **ones**, the result of the expression becomes $X$.
For example, if $S =$ `++-*-`, the resulting expression is $1+1+1-1*1-1$, which is then evaluated based on the rules above.

If multiple such strings exist, **print any of them**. If no such string exists, print $-1$ instead.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two space-separated integers $N$ and $X$ — the number of characters in the string and the result of expression after appending $(N+1)$ ones between all operators.

---

## Output Format

For each test case, output on a new line a string $S$ of length $N$ consisting **only** of $*, +,$ and $-$ that satisfies the given condition.

If multiple such strings exist, **print any of them**. If no such string exists, print $-1$ instead.

---

## Constraints

- $1 \leq T \leq 2000$
- $1 \leq N \leq 10^5$
- $-10^5 \leq X \leq 10^5$
- The sum of $N$ over all test cases won't exceed $2\cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
3 4
2 -5
3 1
```

**Output**

```text
+++
-1
*+-
```

**Explanation**

**Test case $1$:** A possible string satisfying the condition is `+++`. The corresponding expression is $1+1+1+1 = 4$ which is equal to $X$.

**Test case $2$:** It can be proven that no such string with length $N=2$ exists such that the corresponding expression evaluates to $-5$.

**Test case $3$:** A possible string satisfying the condition is `*+-`. The corresponding expression is $1*1+1-1 = 1+1-1 = 2-1 = 1$ which is equal to $X$.
Note that there are other valid strings, such as `+*-` and `-*+`. Any valid string will be accepted as output.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3 4
```

**Output for this case**

```text
+++
```



#### Test case 2

**Input for this case**

```text
2 -5
```

**Output for this case**

```text
-1
```



#### Test case 3

**Input for this case**

```text
3 1
```

**Output for this case**

```text
*+-
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/EVALMAS)

[Contest: Division 1](https://www.codechef.com/START78A/problems/EVALMAS)

[Contest: Division 2](https://www.codechef.com/START78B/problems/EVALMAS)

[Contest: Division 3](https://www.codechef.com/START78C/problems/EVALMAS)

[Contest: Division 4](https://www.codechef.com/START78D/problems/EVALMAS)

***Author:*** [notsoloud](https://www.codechef.com/users/notsoloud)

***Testers:*** [tabr](https://www.codechef.com/users/tabr), [yash_daga](https://www.codechef.com/users/yash_daga)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Given N and X, construct a string of length N using the characters `+`, `-`, `*` such that upon evaluation with N+1 ones, the result is X.

Multiplication is performed first, addition second, and subtraction last.

#
[](#explanation-5)EXPLANATION:

Let’s think about the maximum and minimum values we can achieve.

Clearly, since there are no parentheses,

- The maximum is 1+1+1+\ldots + 1 = N+1

- The minimum is 1-1-1-\ldots - 1 = 1-N

So, if X \gt N+1 or X \lt 1-N, the answer is immediately -1.

Let’s solve for the remaining numbers.

Starting with 1+1+\ldots + 1, notice that replacing one `+` with a `*` essentially allows us to ‘combine’ two ones into a single one, thereby reducing the sum by 1.

For example,

- 1+1+1+1 = 4

- 1+1+1*1 = 3

- 1+1*1*1 = 2

- 1*1*1*1 = 1

Notice that this allows to create every X between 1 and N+1, by using X-1 occurrences of `+` and N-X occurrences of `*`.

A similar logic applies to the non-positive numbers, where we can start with 1-1-1-\ldots -1, and replace a `-` with a `*` to increase the sum by 1. For example,

- 1-1-1-1 = -2

- 1-1-1*1 = -1

- 1-1*1*1 = 0

In particular, -X can be obtained using X+1 occurrences of `-` and N-X-1 occurrences of `*`.

This means we can obtain every X in the range [1-N, N+1], and so we’re done.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    n, x = map(int, input().split())
    if x > 0:
        if x > n+1: print(-1)
        else: print('*'*(n-x+1) + '+'*(x-1))
    else:
        x = -x
        if x > n-1: print(-1)
        else: print('-'*(1+x) + '*'*(n-1-x))
``

</details>
