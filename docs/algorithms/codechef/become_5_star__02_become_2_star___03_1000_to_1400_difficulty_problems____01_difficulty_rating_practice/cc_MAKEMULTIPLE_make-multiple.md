# Make Multiple

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MAKEMULTIPLE |
| Difficulty Rating | 1163 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [MAKEMULTIPLE](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/MAKEMULTIPLE) |

---

## Problem Statement

Chef has two integers $A$ and $B$ $(A \leq B)$.

Chef can choose any **non-negative** integer $X$ and add them to both $A$ and $B$. Find whether it is possible to make $A$ a [divisor](https://en.wikipedia.org/wiki/Divisor) of $B$.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two integers $A$ and $B$.

---

## Output Format

For each test case, output `YES` if it is possible to make $A$ a factor of $B$, `NO` otherwise.

You can print each character of the string in uppercase or lowercase. For example, the strings `Yes`, `YES`, `yes`, and `yEs`, are all considered identical.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq A \leq B \leq 10^9$

---

## Examples

**Example 1**

**Input**

```text
3
3 6
4 14
9 10
```

**Output**

```text
YES
YES
NO
```

**Explanation**

**Test case $1$:** We can choose $X = 0$ and add them to $3$ and $6$. Thus, $3$ is a factor of $6$.

**Test case $2$:** We can choose $X = 1$ and add them to $4$ and $14$. Thus, $4+1 = 5$ is a factor of $14+1 = 15$.

**Test case $3$:** There is no possible value of $X$ to add such that $A$ becomes a factor of $B$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3 6
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
4 14
```

**Output for this case**

```text
YES
```



#### Test case 3

**Input for this case**

```text
9 10
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

[Practice](https://www.codechef.com/problems/MAKEMULTIPLE)

[Contest: Division 1](https://www.codechef.com/START62A/problems/MAKEMULTIPLE)

[Contest: Division 2](https://www.codechef.com/START62B/problems/MAKEMULTIPLE)

[Contest: Division 3](https://www.codechef.com/START62C/problems/MAKEMULTIPLE)

[Contest: Division 4](https://www.codechef.com/START62D/problems/MAKEMULTIPLE)

***Author:*** [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_25dec)

***Testers:*** [Nishank Suresh](https://www.codechef.com/users/iceknight1093), [Takuki Kurokawa](https://www.codechef.com/users/tabr)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

1163

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Given two integers A and B, is it possible to add a non-negative integer K to both of them such that A+K is a divisor of B+K?

#
[](#explanation-5)EXPLANATION:

First, if A = B, then the answer is obviously “Yes”.

Otherwise, note that no matter which K we choose, the difference between A and B remains constant.

Let d = B - A. A valid K exists if and only if A \leq d.

Proof

If A \leq d, then choose K = d - A.

This makes A = d and B = 2d, and of course A is now a factor of B.

Conversely, suppose A \gt d. Suppose, for some K, A+K is a factor of B+K. Then, there exists an x \geq 1 such that:

x\cdot (A+K) = B+K = A+d+K \implies (x-1)\cdot (A+K) = d

But A \gt d, so A+K \gt d. This means a valid only exists in the case when d = 0, when we can choose x = 1.

However, we assumed A \neq B, which implies d \neq 0, so this case cannot happen.

This completes the proof.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    a, b = map(int, input().split())
    d = b - a
    print('Yes' if d == 0 or a <= d else 'No')
``

</details>
