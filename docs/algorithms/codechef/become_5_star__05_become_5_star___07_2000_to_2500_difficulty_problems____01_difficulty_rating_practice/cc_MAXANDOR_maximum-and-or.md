# Maximum And Or

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MAXANDOR |
| Difficulty Rating | 2028 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [MAXANDOR](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/MAXANDOR) |

---

## Problem Statement

Chef has been recently introduced to bitwise operations.

Chefina defines a function $F(P,Q,R) = (R$ $|$ $P) - (Q$ $\&$ $P)$
where $|$ represents the [bitwise or](https://en.wikipedia.org/wiki/Bitwise_operation#OR) and $\&$ represents the [bitwise and](https://en.wikipedia.org/wiki/Bitwise_operation#AND) operator.

Chef has three non-negative integers $A,B,$ and $C$.
Chef has to count the number of integers $X$, such that:
- $0 \leq X \lt 2^C;$
- $F(X,A,B)$ has the **maximum** possible value among all values of $X$.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single line containing three space-separated integers $A,B,C-$ as defined in the statement.

---

## Output Format

For each test case, output on a new line, the count of $X$ such that $F(X,A,B)$ is maximum possible.

---

## Constraints

- $1 \leq T \leq 2 \cdot 10^5$
- $0 \leq C \leq 30$
- $0 \leq A,B < 2^{C}$

---

## Examples

**Example 1**

**Input**

```text
3
1 2 3
0 0 2
87 986 15
```

**Output**

```text
4
1
64
```

**Explanation**

**Test case $1$:** There are $4$ possible values of $X$ which give maximum value for $F(X, A, B)$. These values are $4,5,6,7$.
For all these values, $F(X,A,B)$ is $5$.

**Test case $2$:** The only possible value of $X$ which gives maximum value for $F(X, A, B)$ is $3$.
For $X = 3$:
- $0\le X \lt 2^2$
- $F(3, 0, 0) = (0$ $|$ $3) - (0$ $\&$ $3) = 3$

It can be shown that $F(X, 0, 0)$ cannot have a value greater than $3$ for $0\le X \lt 2^2$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 2 3
```

**Output for this case**

```text
4
```



#### Test case 2

**Input for this case**

```text
0 0 2
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
87 986 15
```

**Output for this case**

```text
64
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/MAXANDOR)

[Contest: Division 1](https://www.codechef.com/START88A/problems/MAXANDOR)

[Contest: Division 2](https://www.codechef.com/START88B/problems/MAXANDOR)

[Contest: Division 3](https://www.codechef.com/START88C/problems/MAXANDOR)

[Contest: Division 4](https://www.codechef.com/START88D/problems/MAXANDOR)

***Author:*** [yash5507](https://www.codechef.com/users/yash5507)

***Tester:*** [jay_1048576](https://www.codechef.com/users/jay_1048576)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

2028

#
[](#prerequisites-3)PREREQUISITES:

Familiarity with bitwise operations

#
[](#problem-4)PROBLEM:

Let F(x, y, z) = (x\mid y) - (x\ \& \ z).

Given A, B, C, find the number of integers 0 \leq x \lt 2^C such that F(x, A, B) is maximum.

#
[](#explanation-5)EXPLANATION:

Almost everything in this problem is a bitwise operation, except the subtraction in F(x, y, z).

However, notice that (x\mid y) will contain all the set bits of x, while (x \ \& \ z) cannot contain any bits that aren’t set in x.

So, (x\ \& \ z) is a *submask* of (x\mid y), and this means the subtraction operation is really just bitwise XOR.

That is, we can rewrite the function as F(x, y, z) = (x\mid y) \oplus (x\ \& \ z).

Now that everything we’re dealing with is bitwise operation, it helps to look at what’s going on bit-by-bit.

Let’s fix a bit k and see what happens.

Let x_k denote the value of the k-th bit of x (which is either 0 or 1). Similarly define A_k, B_k, F_k(x, A, B).

We already know A_k and B_k, our aim is to find out what values x_k can possibly take.

We have F_k(x, A, B) = (x_k\mid A_k) \oplus (x_k\ \& \ B_k), and we’d like to maximize F_k(x, A, B).

There are 4 cases depending on their values:

-
A_k = B_k = 1

Here, (x_k \mid A_k) = 1, and (x_k \ \& \ B_k) = x_k.

So, F_k(x, A, B) =1 \oplus x_k, which is maximized when x_k = 0.

-
A_k = B_k = 0

Here, (x_k \mid A_k)  = x_k, and (x_k \ \& \ B_k) = 0.

So, F_k(x, A, B) = x_k \oplus 0, which is maximized when x_k = 1.

-
A_k = 1 and B_k = 0

Here, F_k(x, A, B) = 1\oplus 0 = 1, and is independent of x_k. So, we can choose x_k to be either 0 or 1

-
A_k = 0 and B_k = 1

Here, F_k(x, A, B) = x_k\oplus x_k = 0, once again we can choose x_k freely.

Putting the above together:

- If A_k = B_k, x_k is fixed and we have no choice.

- If A_k \neq B_k, x_k can be chosen freely.

So, the answer is simply 2^d, where d is the number of bits where A and B differ in their binary representations.

d can be computed by iterating over each bit independently; or you can notice that it’s just the number of set bits in (A\oplus B) for an \mathcal{O}(1) solution.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(C) or \mathcal{O}(1) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    a, b, c = map(int, input().split())
    dif = bin(a ^ b).count('1')
    print(2 ** dif)
``

</details>
