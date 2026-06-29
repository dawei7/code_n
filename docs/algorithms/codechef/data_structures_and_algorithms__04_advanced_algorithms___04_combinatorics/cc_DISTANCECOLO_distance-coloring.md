# Distance Coloring

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DISTANCECOLO |
| Difficulty Rating | 1513 |
| Difficulty Band | Combinatorics |
| Path | Data Structures and Algorithms |
| Lesson | Conceptual Problems |
| Official Link | [DISTANCECOLO](https://www.codechef.com/learn/course/combinatorics/COMBI05/problems/DISTANCECOLO) |

---

## Problem Statement

You have $N$ stones in a row, numbered from $1$ to $N$. You also have $K$ different colors with you.

We know that the number of different ways of coloring these $N$ stones with these $K$ colors is $K^N$. But you now add an extra condition:
- If $|j - i| < K$, then Stone $i$ and Stone $j$ cannot have the same color.

In other words, you cannot color two stones with the same color if they are $\lt K$ distance apart.

Find the number of different ways of coloring the stones with this extra condition. Since the answer might be large, output it modulo $10^9 + 7$.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The only line of each test case contains two space-separated integers $N$ and $K$ — the number of stones and the number of colors that you have, respectively.

---

## Output Format

For each test case, output on a new line the number of different ways of coloring, modulo $10^9 + 7$.

---

## Constraints

- $1 \leq T \leq 10000$
- $1 \leq N \leq 100$
- $1 \leq K \leq 100$

---

## Examples

**Example 1**

**Input**

```text
4
1 1
1 2
2 1
2 2
```

**Output**

```text
1
2
1
2
```

**Explanation**

If there are $K$ colors, we will denote the colors as $C_1, C_2, \ldots, C_K$.

**Testcase 1:** $N = 1$, and $K = 1$.\
So we need to find the number of ways of coloring $1$ stone, using the colors $\{C_1\}$, and ensuring that no two stones which are at a distance of $< 1$ apart have the same color.

The only way to do so is by coloring Stone $1$ with $C_1$. So the answer is $1$.

**Testcase 2:** $N = 1$, and $K = 2$.\
So we need to find the number of ways of coloring $1$ stone, using the colors $\{C_1, C_2\}$, and ensuring that no two stones which are at a distance of $< 2$ apart have the same color.

The two ways to do so are by coloring Stone $1$ with either $C_1$ or $C_2$. So the answer is $2$.

**Testcase 3:** $N = 2$, and $K = 1$.\
So we need to find the number of ways of coloring $2$ stones, using the colors $\{C_1\}$, and ensuring that no two stones which are at a distance of $< 1$ apart have the same color.

The only way to do so is by coloring both Stones with $C_1$. So the answer is $1$.

**Testcase 4:** $N = 2$, and $K = 2$.\
So we need to find the number of ways of coloring $2$ stones, using the colors $\{C_1, C_2\}$, and ensuring that no two stones which are at a distance of $< 2$ apart have the same color.

The two ways to do so are:
- coloring Stone $1$ with $C_1$ and Stone $2$ with $C_2$
- coloring Stone $1$ with $C_2$ and Stone $2$ with $C_1$

Note that you cannot color both Stones with the same color, since $2 - 1 < K$.\
So, the answer is $2$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 1
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
1 2
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
2 1
```

**Output for this case**

```text
1
```



#### Test case 4

**Input for this case**

```text
2 2
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/DISTANCECOLO)

[Contest: Division 1](https://www.codechef.com/START92A/problems/DISTANCECOLO)

[Contest: Division 2](https://www.codechef.com/START92B/problems/DISTANCECOLO)

[Contest: Division 3](https://www.codechef.com/START92C/problems/DISTANCECOLO)

[Contest: Division 4](https://www.codechef.com/START92D/problems/DISTANCECOLO)

***Tester & Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

1513

#
[](#prerequisites-3)PREREQUISITES:

Basic math

#
[](#problem-4)PROBLEM:

There are N stones and K colors. Each stone must be colored with one of the K colors.

However, any two stones with the same color should have a distance of at least K between them.

How many ways exist to color the stones?

#
[](#explanation-5)EXPLANATION:

Let’s try to color the stones one at a time, from 1 to N.

- Stone 1 can be colored in any of the K colors, there are no restrictions yet.

- Stone 2 has K-1 options, since it can’t be the same color as 1.

- Stone 3 has K-2 options, it can’t be the same color as the previous two.

\vdots

- Stone K-1 has 2 options.

- Stone K has 1 option, since it can’t be any of the previous K-1 colors (which are all distinct).

- Stone K+1 has only one option: it can’t take the color of any of stones 2, 3, \ldots, K; but it can take the color of stone 1.

- Similarly, stone K+2 *must* have the same color as stone 2, and so on.

In general, if i \gt K then stone i will have exactly one option: have the same color as stone i-K.

Multiply the choices for each stone to obtain the final answer.

In particular, you might notice that:

- If K \leq N, the answer is K! (we multiply each of 2, 3, \ldots, K exactly once; everything else is 1)

- If K \gt N, the answer is K\times (K-1) \times \ldots \times (K-N+1) = \frac{K!}{(K-N)!}

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(K) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``mod = 10**9 + 7
for _ in range(int(input())):
    n, k = map(int, input().split())
    ans = 1
    while n > 0 and k > 0:
        ans *= k
        ans %= mod
        n -= 1
        k -= 1
    print(ans)
``

</details>
