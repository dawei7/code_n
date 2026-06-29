# Max Binary

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MAX_BIN |
| Difficulty Rating | 1143 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [MAX_BIN](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/MAX_BIN) |

---

## Problem Statement

Chef has a **binary** strings $S$ of length $N$, and an integer $K$.
Hitesh wants to **maximize** the *decimal representation* of $S$ using $K$ operations of the following type:
- Type $1$: Insert $0$ at any position in the string.
- Type $2$: Change any $0$ to $1$.

Help Hitesh find the modified string with maximum possible decimal representation after performing **at most** $K$ operations.

Note that the *decimal representation* of a binary string refers to the numeric value it represents when converted to the decimal number system. For instance, the decimal representation of $101$ will be $5$ $(2^2 + 2^0)$, and that of $000110$ will be $6$ $(2^2 +2^1)$

---

## Input Format

- First line will contain $T$, number of test cases. Then the test cases follow.
- The first line of each test case contains two integers $N$ and $K$.
- The second line contains the string $S$.

---

## Output Format

For each test case, output on a new line, the modified string with maximum possible decimal representation after performing **at most** $K$ operations.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 10^6$
- $1 \leq K \leq 10^6$
- $S$ consists of $0$ and $1$ only.
- The sum of $N$ and $K$ over all test cases won't exceed $5\cdot 10^6$.

---

## Examples

**Example 1**

**Input**

```text
4
4 2
1101
6 3
001110
5 4
00110
3 1
000
```

**Output**

```text
110100
10111000
10110000
100
```

**Explanation**

**Test case $1$:** We are allowed to perform two operations. We can perform both operations of type $1$ to obtain $110100$, having decimal value $52$.

**Test case $2$:** We are allowed to perform three operations. We can perform two operations of type $1$ to obtain $00111000$, and one operation of type $2$ to obtain $10111000$, having decimal value $184$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4 2
1101
```

**Output for this case**

```text
110100
```



#### Test case 2

**Input for this case**

```text
6 3
001110
```

**Output for this case**

```text
10111000
```



#### Test case 3

**Input for this case**

```text
5 4
00110
```

**Output for this case**

```text
10110000
```



#### Test case 4

**Input for this case**

```text
3 1
000
```

**Output for this case**

```text
100
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/MAX_BIN)

[Contest: Division 1](https://www.codechef.com/START84A/problems/MAX_BIN)

[Contest: Division 2](https://www.codechef.com/START84B/problems/MAX_BIN)

[Contest: Division 3](https://www.codechef.com/START84C/problems/MAX_BIN)

[Contest: Division 4](https://www.codechef.com/START84D/problems/MAX_BIN)

***Author:*** [hjindal](https://www.codechef.com/users/hjindal)

***Tester:*** [abhidot](https://www.codechef.com/users/abhidot)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

1143

#
[](#prerequisites-3)PREREQUISITES:

Greedy

#
[](#problem-4)PROBLEM:

Given a binary string S, you can perform the following operations on it:

- Change a 0 to a 1

- Insert a 0 anywhere in the string

Find the maximum possible integer that can be formed after at most K operations.

#
[](#explanation-5)EXPLANATION:

Let X be the decimal value of the string.

Let’s see how the given operations affect the value of X.

- Suppose we change bit i from 0 to 1. This increases the value of X by 2^i.

- Suppose we insert a 0 after bit i. This doesn’t change anything about bits 0, 1, 2, \ldots, i-1, but shifts bits i, i+1, \ldots to the left by one step, i.e, multiplies their values by 2.

So, if Y is the total value of bits \geq Y, X will increase by exactly Y.

From this, it’s easy to see that whenever we insert a 0, it’s always optimal to do so at the end of the string, since it directly multiplies the value of X by 2.

So, we only need to decide when to insert a 0 and when to change a 0 into a 1.

In fact, this can be done greedily!

- If the leftmost character of S is 1, then insert a 0 at the end of S

- Otherwise, change the leftmost character of S to 1.

Each operation is easily performed in \mathcal{O}(1), so the final string can be found in \mathcal{O}(N+K).

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N + K) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    s, k = input().split()
    k = int(k)
    s = list(s)
    if s[0] == '0':
        s[0] = '1'
        k -= 1
    s += ['0']*k
    print(''.join(s))
``

</details>
