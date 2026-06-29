# Lcm hates Gcd

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | LCM_GCD |
| Difficulty Rating | 1369 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [LCM_GCD](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/LCM_GCD) |

---

## Problem Statement

Chef has two integers $A$ and $B$.
Chef wants to find the **minimum** value of $\texttt{lcm}(A, X) - \texttt{gcd}(B, X)$ where $X$ is any positive integer.

Help him determine this value.

Note: $\texttt{gcd}(P, Q)$ denotes the [greatest common divisor](https://en.wikipedia.org/wiki/Greatest_common_divisor) of $P$ and $Q$ and $\texttt{lcm}(P, Q)$ denotes the [least common multiple](https://en.wikipedia.org/wiki/Least_common_multiple) of $P$ and $Q$.

---

## Input Format

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first and only line of each test case contains two space-separated integers $A$ and $B$ — the integers mentioned in the statement.

---

## Output Format

For each test case, output the minimum value of $\texttt{lcm}(A, X) - \texttt{gcd}(B, X)$.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \le A, B \le 10^9$

---

## Examples

**Example 1**

**Input**

```text
3
12 15
5 50
9 11
```

**Output**

```text
9
0
8
```

**Explanation**

**Test case $1$:** For $X = 6$: $\texttt{lcm}(12, 6) - \texttt{gcd}(15, 6) = 12 - 3 = 9$ which is the minimum value required.

**Test case $2$:** For $X = 50$: $\texttt{lcm}(5, 50) - \texttt{gcd}(50, 50) = 50 - 50 = 0$ which is the minimum value required.

**Test case $3$:** For $X = 1$: $\texttt{lcm}(9, 1) - \texttt{gcd}(11, 1) = 9 - 1 = 8$ which is the minimum value required.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
12 15
```

**Output for this case**

```text
9
```



#### Test case 2

**Input for this case**

```text
5 50
```

**Output for this case**

```text
0
```



#### Test case 3

**Input for this case**

```text
9 11
```

**Output for this case**

```text
8
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/LCM_GCD)

[Contest: Division 1](https://www.codechef.com/START74A/problems/LCM_GCD)

[Contest: Division 2](https://www.codechef.com/START74B/problems/LCM_GCD)

[Contest: Division 3](https://www.codechef.com/START74C/problems/LCM_GCD)

[Contest: Division 4](https://www.codechef.com/START74D/problems/LCM_GCD)

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

You are given integers A and B. Find the smallest possible value of \text{lcm}(A, X) - \gcd(B, X) across all positive integers X.

#
[](#explanation-5)EXPLANATION:

The answer is probably guessable by looking at the sample tests and/or working out a few small examples.

Short answer

The answer is simply

A - \gcd(A, B)

Long answer

I’ll focus a bit on how one can derive this without guessing.

Our expression is \text{lcm}(A, X) - \gcd(B, X).

In particular, the first part of that expression is always a multiple of A.

Let’s fix the value of this lcm: suppose we choose X such that \text{lcm}(A, X) = k\cdot A.

Notice that this means that X is a factor of k\cdot A.

Our objective is now to *maximize* \gcd(B, X), since that’s what would make the difference as small as possible.

For \gcd(B, X) to be as large as possible, X should contain as many prime factors in common with B as possible.

Along with the constraint that X is a factor of k\cdot A, this tells us that the best choice of X is k\cdot A itself; choosing a strict factor isn’t going to help us increase the gcd.

Ok, so now we have k\cdot A - \gcd(B, k\cdot A).

What value of k minimizes this?

Intuitively, k = 1 seems good; after all, the second part is a factor of B so will always be \leq B no matter how large k is; while the first part keeps increasing without bound.

k = 1 gives us A - \gcd(A, B), which if you notice is the expression given in the “short answer” above.

Let’s try to prove that this is optimal.

Proof

First, notice that for any k\geq 1, we have \gcd(B, k\cdot A) \leq \gcd(k\cdot B, k\cdot A); since k\cdot B is a multiple of B.

But it’s also true that \gcd(k\cdot B, k\cdot A) = k\cdot\gcd(A, B).

So, we have \gcd(B, k\cdot A) \leq k\cdot \gcd(A, B).

This means that

k\cdot A - \gcd(B, k\cdot A) \geq k\cdot A - k\cdot\gcd(A, B) \\
k\cdot A - \gcd(B, k\cdot A) \geq k\cdot(A - \gcd(A, B)) \\
k\cdot A - \gcd(B, k\cdot A) \geq A - \gcd(A, B)

which is exactly what we set out to prove!

All that remains is computing the answer quickly, which requires us to compute \gcd(A, B) quickly.

This can be done in \mathcal{O}(\log\min(A, B)) using the [Euclidean algorithm](https://cp-algorithms.com/algebra/euclid-algorithm.html).

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(\log\min(A, B)) per testcase.

#
[](#code-7)CODE:

Code (Python)
``from math import gcd
for _ in range(int(input())):
    a, b = map(int, input().split())
    print(a - gcd(a, b))
``

</details>
