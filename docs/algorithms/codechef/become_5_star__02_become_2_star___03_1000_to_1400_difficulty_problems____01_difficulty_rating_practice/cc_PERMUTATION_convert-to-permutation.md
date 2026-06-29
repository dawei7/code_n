# Convert to permutation

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PERMUTATION |
| Difficulty Rating | 1197 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [PERMUTATION](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/PERMUTATION) |

---

## Problem Statement

You are given an array $A$ of size $N$. In one operation, you can:
- Choose an index $i$ $(1\le i \le N)$ and increase $A_i$ by $1$.

Find the **minimum** number of operations required to convert the array $A$ into a *permutation* of size $N$. If it is impossible to do so, print $-1$.

Note that a *permutation* of size $N$ contains each element from $1$ to $N$ exactly once.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains the integer $N$ — the size of the array.
    - The next line contains $N$ space-separated integers, the elements of the array $A$.

---

## Output Format

For each test case, output on a new line, the **minimum** number of operations required to convert the array $A$ into a *permutation* of size $N$.
If it is impossible to do so, print $-1$.

---

## Constraints

- $1 \leq T \leq 500$
- $1 \leq N \leq 1000$
- $0 \leq A_i \leq 1000$

---

## Examples

**Example 1**

**Input**

```text
4
4
3 1 1 2
3
0 3 3
3
3 2 1
3
2 0 1
```

**Output**

```text
3
-1
0
3
```

**Explanation**

**Test case $1$:** We can convert the array $A$ into a permutation using $3$ operations:
- Operation $1$: Choose $i = 3$ and increase $A_i$ by $1$. Thus, the array becomes $A = [3, 1, 2, 2]$.
- Operation $2$: Choose $i = 3$ and increase $A_i$ by $1$. Thus, the array becomes $A = [3, 1, 3, 2]$.
- Operation $3$: Choose $i = 3$ and increase $A_i$ by $1$. Thus, the array becomes $A = [3, 1, 4, 2]$.

It can be shown that this is the minimum number of operations required to convert $A$ into a permutation.

**Test case $2$:** The given array cannot be converted into a permutation using any number of operations.

**Test case $3$:** The given array is already a permutation. Thus, we require $0$ operations.

**Test case $4$:** We can convert the array $A$ into a permutation using $3$ operations:
- Operation $1$: Choose $i = 1$ and increase $A_i$ by $1$. Thus, the array becomes $A = [3, 0, 1]$.
- Operation $2$: Choose $i = 2$ and increase $A_i$ by $1$. Thus, the array becomes $A = [3, 1, 1]$.
- Operation $3$: Choose $i = 3$ and increase $A_i$ by $1$. Thus, the array becomes $A = [3, 1, 2]$.

It can be shown that this is the minimum number of operations required to convert $A$ into a permutation.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
3 1 1 2
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
3
0 3 3
```

**Output for this case**

```text
-1
```



#### Test case 3

**Input for this case**

```text
3
3 2 1
```

**Output for this case**

```text
0
```



#### Test case 4

**Input for this case**

```text
3
2 0 1
```

**Output for this case**

```text
3
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/PERMUTATION)

[Contest: Division 1](https://www.codechef.com/START69A/problems/PERMUTATION)

[Contest: Division 2](https://www.codechef.com/START69B/problems/PERMUTATION)

[Contest: Division 3](https://www.codechef.com/START69C/problems/PERMUTATION)

[Contest: Division 4](https://www.codechef.com/START69D/problems/PERMUTATION)

***Authors:*** [notsoloud](https://www.codechef.com/users/notsoloud)

***Testers:*** [iceknight1093](https://www.codechef.com/users/IceKnight1093), [mexomerf](https://www.codechef.com/users/mexomerf)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

1197

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

You have an array A. In one move, you can increase some A_i by 1.

Find the minimum cost to make A into a permutation of [1, 2, \ldots, N] or claim that this is impossible.

#
[](#explanation-5)EXPLANATION:

Ideally, we’d like to turn the smallest element of A into 1, the second smallest into 2, \ldots, the largest into N.

So let’s do exactly this!

Sort the array A, so that A_1 \leq A_2 \leq \ldots \leq A_N.

Now, we want to turn A_i into i, which needs i - A_i moves.

If A_i \gt i for any index i, then the answer is -1 since we can’t turn A_i into i, we aren’t allowed to decrease elements.

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(N) per testcase.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    ans = sum(i+1 - a[i] for i in range(n))
    for i in range(n):
        if a[i] > i+1: ans = -1
    print(ans)
``

</details>
